import typing

import psycopg2

from base import dbname, user, password, host, port

conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)


def run_migrate() -> typing.NoReturn:
    with conn:
        with conn.cursor() as cursor:
            cursor.execute('''
            create table if not exists TgChat (
                id serial primary key,
                title text,
                chat_id int not null
            )
            ''')


def insert_one(title: str, chat_id: int) -> typing.NoReturn:
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(f"insert into TgChat(title, chat_id) value ('{title}', {chat_id})")


def get_all_chat_ids() -> typing.List[int]:
    with conn:
        with conn.cursor() as cursor:
            cursor.execute("select chat_id from TgChat")
            return [i[0] for i in cursor.fetchall()]
