import smtplib
from email.message import EmailMessage


def send_email(receiver, message, **kwargs):
    """Arguements:\n
        1. receiver [str] -> Receiver's email address\n
        2. message [str] -> Message to be sent\n
        **kwargs:\n
        \t Email [str] -> Sender's email *(can be left blank if default email address is to be used)\n
        \t Password [str] -> Sender's email's password *(can be left blank if default email address is to be used)\n"""
    msg = EmailMessage()
    msg.set_content(message)
    msg["Subject"] = "Wish from a loved once"
    msg["To"] = receiver
    email = kwargs.get("Email", None)
    password = kwargs.get("Password", None)

    if email == None and password == None:
        email = "your_email"
        password = "your_password"
    msg["From"] = email

    # print(email)
    # print(password)

    server = smtplib.SMTP("smtp.gmail.com", port=587)
    server.starttls()
    server.login(email, password)
    server.send_message(msg)
    server.quit()
