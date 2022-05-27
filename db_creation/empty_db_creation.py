def check_db_not_exists(cur):
    cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cur.fetchall()
    return not tables or 'subtitles' not in tables[0]


def create_empty_db(con, cur):
    if check_db_not_exists(cur):
        cur.execute(
            """
            CREATE TABLE subtitles
            (videoId integer, duration integer, content text, startOfParagraph integer, startTime integer)
            """)
    con.commit()

