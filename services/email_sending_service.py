from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
import smtplib
import ssl
from datetime import date

class EmailSendingService:

    SMTP_SERVER = "smtp.gmail.com"
    PORT = 587  # For starttls

    SENDER_EMAIL = "yousaf559@gmail.com" # TODO: replace with your email address
    
    PASSWORD = 'dojljzdpakurrxlt'  # TODO: replace with your 16-digit-character password 

    # assuming these two values are from your analysis
    SCORE = 0.86
    TODAY_DATE = date.today()

    @classmethod
    def send_suggestion(cls, title, description):
        receiver_email = ["yousafzafar_98@live.com"] # TODO: replace with your recipients
        msg = MIMEMultipart()
        msg["Subject"] = 'Report Suggestion ' + title
        msg["From"] = EmailSendingService.SENDER_EMAIL
        msg['To'] = ", ".join(receiver_email)

        ## Plain text
        text = description

        body_text = MIMEText(text, 'plain')  # 
        msg.attach(body_text)  # attaching the text body into msg
        context = ssl.create_default_context()
        # Try to log in to server and send email
        server = smtplib.SMTP(EmailSendingService.SMTP_SERVER, EmailSendingService.PORT)
        server.ehlo()  # check connection
        server.starttls(context=context)  # Secure the connection
        server.ehlo()  # check connection
        server.login(EmailSendingService.SENDER_EMAIL, EmailSendingService.PASSWORD)

        # Send email here
        server.sendmail(EmailSendingService.SENDER_EMAIL, receiver_email, msg.as_string())

    @classmethod
    def alert_admin(cls):
        receiver_email = ["yousafzafar_98@live.com"] # TODO: replace with your recipients
        msg = MIMEMultipart()
        msg["Subject"] = "Login Attempted On {}".format(EmailSendingService.TODAY_DATE)
        msg["From"] = EmailSendingService.SENDER_EMAIL
        msg['To'] = ", ".join(receiver_email)

        ## Plain text
        text = """\
        This is to inform you that a login was attempted from your account. If this was you, please ignore this message."""

        body_text = MIMEText(text, 'plain')  # 
        msg.attach(body_text)  # attaching the text body into msg

        html = """\
        <html>
        <body>
            <p>Hi,<br>
            <br>
            This is to inform the training job has been completed. The AUC for the job on {} is {} <br>
            Thank you. <br>
            </p>
        </body>
        </html>
        """

        body_html = MIMEText(html.format(EmailSendingService.TODAY_DATE, EmailSendingService.SCORE), 'html')  # parse values into html text
        msg.attach(body_html)  # attaching the text body into msg

        context = ssl.create_default_context()
        # Try to log in to server and send email
        server = smtplib.SMTP(EmailSendingService.SMTP_SERVER, EmailSendingService.PORT)
        server.ehlo()  # check connection
        server.starttls(context=context)  # Secure the connection
        server.ehlo()  # check connection
        server.login(EmailSendingService.SENDER_EMAIL, EmailSendingService.PASSWORD)

        # Send email here
        server.sendmail(EmailSendingService.SENDER_EMAIL, receiver_email, msg.as_string())