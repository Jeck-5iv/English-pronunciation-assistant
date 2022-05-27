from urllib.request import urlopen
from urllib.error import HTTPError
import json
from tqdm import tqdm


def parse_video_subtitles(videoId, con, cur, lang):
    try:
        ted_url = urlopen(f'https://www.ted.com/talks/subtitles/id/{videoId}/lang/{lang}')
    except HTTPError as er:
        return None

    ted_json = ted_url.read().decode('utf8')
    ted_list = json.loads(ted_json)

    rows = []
    for indict in ted_list['captions']:
        rows.append([
            videoId,
            indict['duration'],
            indict['content'],
            indict['startOfParagraph'],
            indict['startTime']])

    cur.executemany("insert into subtitles values (?, ?, ?, ?, ?)", rows)
    # save changes
    con.commit()


def fill_db(con, cur, lang, videos_count):
    for videoId in tqdm(range(1, 1 + videos_count)):
        parse_video_subtitles(videoId, con, cur, lang)
