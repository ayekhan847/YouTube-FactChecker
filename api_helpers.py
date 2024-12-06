import os
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound
from google.cloud import language_v1

#initializing the Google Cloud Language API client
language_client = language_v1.LanguageServiceClient()


def fetch_transcript(video_id):
    try:
        #getting the transcript from YouTube Video
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return transcript  # Returns a list of {text, start, duration}
    except TranscriptsDisabled:
        return {"error": "Transcripts are disabled for this video."}
    except NoTranscriptFound:
        return {"error": "No transcript was found for this video."}
    except Exception as e:
        return {"error": str(e)}


def analyze_transcript(transcript, salience_threshold=0.15):
    claims = []

    for segment in transcript:
        text = segment["text"]
        timestamp = segment["start"]

        #prepare the document for Google Cloud NLP
        document = language_v1.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT)

        try:
            # Using the google natural language to analyze the entities
            response = language_client.analyze_entities(document=document)

            # filtering each entity with the name, type, and salience
            relevant_entities = [
                {
                    "entity_name": entity.name,
                    "entity_type": language_v1.Entity.Type(entity.type_).name,
                    "salience": entity.salience
                }
                for entity in response.entities
                if entity.salience >= salience_threshold and entity.type_ != language_v1.Entity.Type.NUMBER
            ]

            #going to append the claim only if important entities are found
            if relevant_entities:
                claims.append({
                    "claim_text": text,
                    "timestamp": timestamp,
                    "entities": relevant_entities
                })

        except Exception as e:
            claims.append({"error": f"Entity analysis failed: {str(e)}"})

    return claims


def process_transcript(video_id):
    #first save transcript by fetching it
    transcript = fetch_transcript(video_id)

    # For errors
    if isinstance(transcript, dict) and "error" in transcript:
        return transcript

    #analyze the transcript
    claims = analyze_transcript(transcript)
    return {"claims": claims}
