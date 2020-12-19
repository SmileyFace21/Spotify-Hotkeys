import ssl, smtplib
class SendMail:

    def __init__(self, sender_email, password):
        self.sender_email = sender_email
        self.password = password
        self.port = 465


    def send_mail(self, receiving_email, subject=None, body=None, message = None):
        if message is None:
            message = "Subject:" + subject + "\n" + body

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", self.port, context=context) as server:
            server.login(self.sender_email, self.password)
            sender_email = self.sender_email
            server.sendmail(sender_email, receiving_email, message)

