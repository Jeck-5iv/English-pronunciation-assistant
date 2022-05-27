import sqlite3
import config

DB_NAME = config.DB_NAME
TABLE_NAME = config.TABLE_NAME
VIDEO_PART_DURATION = config.VIDEO_PART_DURATION


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


CON = sqlite3.connect(DB_NAME, check_same_thread=False)
CON.row_factory = dict_factory
CUR = CON.cursor()


def find_usage(text: str):
    CUR.execute(
        f"""
        SELECT * FROM {TABLE_NAME}
        WHERE content like '%{text}%';
        """
    )
    usages_dict = CUR.fetchall()
    return usages_dict


def gen_ref_by_usage_dict(usage_dict):
    id = usage_dict['videoId']
    start_time = max(0, usage_dict['startTime'] - VIDEO_PART_DURATION // 2)
    return f'https://www.ted.com/talks/{id}#t-{start_time}'


def find_video_fragments(text: str):
    array_of_usage_dicts = find_usage(text)
    if len(array_of_usage_dicts) == 0:
        print('No results found, increase VIDEOS_COUNT in config.py')
    else:
        fragments = dict()
        for usage_dict in array_of_usage_dicts:
            phrase = usage_dict['content']
            url = gen_ref_by_usage_dict(usage_dict)
            fragments[phrase] = url
        return fragments


