import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from tkinter import messagebox

# SMTP Configuration
MAIL_SERVER = "smtp.gmail.com"
MAIL_PORT = 587

def dispatch_email(user_email, user_pass, recipient, mail_subject, mail_body, attachment_path=None):
    try:
        mail_message = MIMEMultipart()
        mail_message['From'] = user_email
        mail_message['To'] = recipient
        mail_message['Subject'] = mail_subject
        mail_message.attach(MIMEText(mail_body, 'plain'))

        if attachment_path and os.path.exists(attachment_path):
            try:
                file_title = os.path.basename(attachment_path)
                with open(attachment_path, "rb") as file_obj:
                    attachment_part = MIMEBase("application", "octet-stream")
                    attachment_part.set_payload(file_obj.read())
                    encoders.encode_base64(attachment_part)
                    attachment_part.add_header("Content-Disposition", f"attachment; filename={file_title}")
                    mail_message.attach(attachment_part)
            except Exception as err:
                messagebox.showerror("Attachment Error", f"Could not attach file: {err}")
                return

        smtp_server = smtplib.SMTP(MAIL_SERVER, MAIL_PORT)
        smtp_server.starttls()
        smtp_server.login(user_email, user_pass)
        smtp_server.sendmail(user_email, recipient, mail_message.as_string())
        smtp_server.quit()

        messagebox.showinfo("Success", "Email sent successfully with attachment!" if attachment_path else "Email sent successfully!")

    except smtplib.SMTPAuthenticationError:
        messagebox.showerror("Authentication Issue", "Invalid email or password. Use an App Password if using Gmail.")
    except smtplib.SMTPConnectError:
        messagebox.showerror("Connection Issue", "Unable to reach the SMTP server. Check your internet connection.")
    except smtplib.SMTPException as err:
        messagebox.showerror("SMTP Error", f"Email sending failed: {err}")
    except Exception as err:
        messagebox.showerror("Error", f"Unexpected problem: {err}")
