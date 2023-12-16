import typing

import psycopg2

from base import dbname, user, password, host, port

conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)


def insert_one(company_id: int, chat_id: int) -> typing.NoReturn:
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(f"insert into tgchat(company_id, chat_id) value ('{company_id}', {chat_id})")


def get_all_chat_ids(company_id: int) -> typing.List[int]:
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(f"select chat_id from tgchat where company_id={company_id}")
            return [i[0] for i in cursor.fetchall()]


def get_all_emails(email: str) -> typing.List[str]:
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(f'select c.id from "CompanyDetails" c join "Account" A on A.id = c.account_id where email =' + f"'{email}'")
            company_id = cursor.fetchone()[0]

            cursor.execute(f'select A.email from "_CompanyDetailsToUserDetails" cdud join "UserDetails" UD on UD.id = cdud."B" join "Account" A on A.id = UD.account_id where cdud."A" = {company_id}')
            return [i[0] for i in cursor.fetchall()]
