from flask import Flask, render_template, request
from api_helpers import process_transcript

app = Flask(__name__)

@app.route('/')
def home():
    video_id = request.args.get('video_id', '')
    results = {"claims": [], "error": None}

    if video_id:
        results = process_transcript(video_id)

    return render_template(
        'index.html',
        video_id=video_id,
        claims=results.get("claims", []),
        error=results.get("error")
    )

if __name__ == "__main__":
    app.run(debug=True)
