from flask import Flask, render_template, request
from api_helpers import fetch_captions, extract_claims, verify_claims, calculate_credibility, deduplicate_claims

app = Flask(__name__)

@app.route('/')
def home():
    video_id = request.args.get('v', '')
    captions = claims = credibility = None

    if video_id:
        # Fetch captions
        captions = fetch_captions(video_id)
        if isinstance(captions, str):  # If captions is an error message
            return render_template('index.html', video_id=video_id, captions=captions, claims=claims, credibility=credibility)

        # Extract claims and deduplicate
        raw_claims = extract_claims(captions)
        claims = deduplicate_claims(raw_claims)

        # Calculate credibility
        credibility = calculate_credibility(claims)

    return render_template('index.html', video_id=video_id, captions=captions, claims=claims, credibility=credibility)

if __name__ == "__main__":
    app.run(debug=True)
