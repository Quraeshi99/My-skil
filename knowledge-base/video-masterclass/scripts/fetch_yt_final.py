
from youtube_transcript_api import YouTubeTranscriptApi

video_id = 'W4EwfEU8CGA'
try:
    api = YouTubeTranscriptApi()
    # The skill.view showed that result is a list of FetchedTranscriptSnippet objects
    # These objects have attributes .text, .start, .duration
    result = api.fetch(video_id)
    
    with open('full_transcript.txt', 'w', encoding='utf-8') as f:
        for seg in result:
            f.write(f"[{seg.start}] {seg.text}\n")
    print("Successfully saved transcript to full_transcript.txt")
except Exception as e:
    print(f"Error: {e}")
