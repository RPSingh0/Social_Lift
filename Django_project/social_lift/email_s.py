if __name__ != "__main__":
    import smtplib
    from email.message import EmailMessage

    def send_email(receiver, message, **kwargs):
        msg = EmailMessage()
        msg.set_content(message)
        msg["Subject"] = "Wish from a loved once"
        msg["To"] = receiver
        email = kwargs.get("Email", None)
        password = kwargs.get("Password", None)

        if email == None and password == None:
            email = "anonymous.it.iter@gmail.com"
            password = "cxxfzbjjollbcjiz"
        msg["From"] = email

        print(email)
        print(password)

        server = smtplib.SMTP("smtp.gmail.com", port=587)
        server.starttls()
        server.login(email, password)
        server.send_message(msg)
        server.quit()
