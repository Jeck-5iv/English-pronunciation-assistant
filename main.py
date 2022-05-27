from db_creation.db_creation import create_db
from db_search import find_video_fragments


def print_video_fragments(fragments_array):
    for fragment in fragments_array:
        print(fragment['url'])
        print(fragment['phrase'])
        print()


def get_fragments(text):
    create_db()
    return find_video_fragments(text)
