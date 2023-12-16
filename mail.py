import smtplib

from base import login, email_password


def new_mail() -> smtplib.SMTP:
    smtp_obj = smtplib.SMTP('smtp.gmail.com', 587)
    smtp_obj.starttls()

    smtp_obj.login(login, email_password)

    return smtp_obj


def close(smtp: smtplib.SMTP):
    smtp.quit()


def send_message(smtp: smtplib.SMTP, mail: str, message: str):
    msg = f"""From: info@it.huba.ru
    To: user@example.com\n
    {message}
    """
    smtp.sendmail(login, mail, msg)
