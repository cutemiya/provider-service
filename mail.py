from smtp import *

from base import login, email_password


def new_mail() -> SMTP:
    smtp_obj = SMTP('smtp.gmail.com', 587)
    smtp_obj.starttls()

    smtp_obj.login(login, email_password)

    return smtp_obj


def close(smtp: SMTP):
    smtp.quit()


def send_message(smtp: SMTP, mail: str, message: str):
    msg = f"""From: info@it.huba.ru
    To: user@example.com\n
    {message}
    """
    smtp.sendmail(login, mail, msg)
