
from youtube_transcript_api import YouTubeTranscriptApi
try:
    transcript = YouTubeTranscriptApi.get_transcript('W4EwfEU8CGA')
    full_text = "\n".join([f"{t:.2f}s: {text}" for t, text in transcript])
    with open('/home/ubuntu/high-performance-system-optimization/knowledge-base/video-masterclass/1M_RPS_Masterclass.md', 'w', encoding='utf-8') as f:
        f.write('# 1M RPS Masterclass Full Transcript\n\n' + full_text)
    print('SUCCESS')
except Exception as e:
    print(f'ERROR: {e}')
