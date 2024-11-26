from googleapiclient.discovery import build
from youtube_transcript_api import YouTubeTranscriptApi
from google.cloud import language_v1
import os
# API Keys and Credentials
YOUTUBE_API_KEY = os.getenv("YT_DATA_API")
FACT_CHECK_API_KEY = os.getenv("YT_DATA_API")
language_client = language_v1.LanguageServiceClient()

# Fetch captions for a YouTube video
def fetch_captions(video_id):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        # Combine captions into chunks of 5 sentences for more context
        combined_text = []
        chunk = []
        for i, item in enumerate(transcript):
            chunk.append(item['text'])
            if (i + 1) % 5 == 0:  # Every 5 sentences, combine into one block
                combined_text.append({"text": " ".join(chunk), "start": item["start"]})
                chunk = []
        # Add any remaining chunk
        if chunk:
            combined_text.append({"text": " ".join(chunk), "start": transcript[-1]["start"]})
        return combined_text
    except Exception as e:
        return [{"text": f"Error fetching captions: {e}", "start": 0}]


# Extract factual claims using Google Natural Language API
def extract_claims(transcript, chunk_size=3):
    all_claims = []
    chunk = []

    for idx, item in enumerate(transcript):
        chunk.append(item["text"])

        # Group captions into chunks of specified size
        if (idx + 1) % chunk_size == 0 or idx == len(transcript) - 1:
            combined_text = " ".join(chunk)
            chunk = []  # Reset for the next chunk

            # Analyze the combined chunk
            document = language_v1.Document(content=combined_text, type_=language_v1.Document.Type.PLAIN_TEXT)
            response = language_client.analyze_entities(document=document)

            # Process entities
            for entity in response.entities:
                if entity.salience > 0.1:  # Filter by relevance
                    verified_results = verify_claims(entity.name)

                    for result in verified_results:
                        if result.get("language", "en") == "en":  # Only  English results
                            all_claims.append({
                                "claim": f"Excerpt: {entity.name}",  # Focus only on the claim
                                "full_context": combined_text,  #provide the larger context
                                "timestamp": item["start"],  # Use the last item's timestamp
                                "verification": result.get("review", "Unverified"),
                                "source": result.get("source", "#")
                            })

    return all_claims

def deduplicate_claims(claims):
    unique_claims = {}
    for claim in claims:
        key = claim["claim"]
        if key not in unique_claims:
            unique_claims[key] = claim
    return list(unique_claims.values())


# Verify claims using Fact Check API
def verify_claims(claim):
    fact_check_service = build("factchecktools", "v1alpha1", developerKey=FACT_CHECK_API_KEY)
    request = fact_check_service.claims().search(query=claim)
    response = request.execute()

    # Filter fact-checking results to include only English responses
    verification_results = []
    for result in response.get("claims", []):
        language = result.get("textLanguage", "en")
        if language == "en":
            verification_results.append({
                "claim": result.get("text", "No text available"),
                "claimant": result.get("claimant", "Unknown"),
                "review": result.get("claimReview", [{}])[0].get("textualRating", "Unverified"),
                "source": result.get("claimReview", [{}])[0].get("url", "#")
            })
    return verification_results

def calculate_credibility(claims):
    verified = len([c for c in claims if c.get("verification") == "Verified"])
    disputed = len([c for c in claims if c.get("verification") == "Disputed"])
    total = len(claims)

    if total == 0:
        return "No Claims"

    score = (verified - disputed) / total
    if score > 0.7:
        return "Mostly Accurate"
    elif score > 0.3:
        return "Mixed Claims"
    else:
        return "Mostly Disputed"

