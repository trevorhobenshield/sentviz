from math import floor
from pathlib import Path

import pandas as pd
from tqdm import tqdm
from youtube_transcript_api import YouTubeTranscriptApi

# get video ids for each video
urls = Path('urls.txt').read_text().split()
video_ids = [u.split('&')[0].split('?v=')[1] for u in urls]

# ensure all video ids were extracted
assert len(urls) == len(video_ids)

# get transcript and timestamp-url for each transcript segment
data = []
for v in tqdm(video_ids):
    data.extend([{'url': f'https://www.youtube.com/watch?v={v}&t={floor(t["start"] - 1)}',
                  'text': t['text']} for t in YouTubeTranscriptApi.get_transcript(v)])
df = pd.json_normalize(data)
df.to_parquet('transcript.parquet')
