import imaplib
import email
from plyer import notification
from tkinter import messagebox

IMAP_SERVER = "imap.gmail.com"

def receive_email(email_user, password):
    try:
        mail = imaplib.IMAP4_SSL(IMAP_SERVER)
        mail.login(email_user, password)
        mail.select("inbox")

        # Fetch the latest email
        result, data = mail.search(None, "ALL")
        mail_ids = data[0].split()
        latest_email_id = mail_ids[-1] if mail_ids else None

        if latest_email_id:
            result, message_data = mail.fetch(latest_email_id, "(RFC822)")
            raw_email = message_data[0][1]
            msg = email.message_from_bytes(raw_email)

            subject = msg["subject"]
            from_email = msg["from"]
            body = ""

            # Extract email content
            if msg.is_multipart():
                for part in msg.walk():
                    content_type = part.get_content_type()
                    content_disposition = str(part.get("Content-Disposition"))

                    if content_type == "text/plain" and "attachment" not in content_disposition:
                        body = part.get_payload(decode=True).decode()
                        break  # Prefer plain text over HTML
                    elif content_type == "text/html" and not body:  
                        body = part.get_payload(decode=True).decode()  
            else:
                body = msg.get_payload(decode=True).decode()

            # **PRINT email details to console**
            print("\n=== LATEST EMAIL RECEIVED ===")
            print(f"From: {from_email}")
            print(f"Subject: {subject}")
            print("Body:\n" + ("-" * 40))
            print(body)
            print("-" * 40)

            # Show notification
            notification.notify(
                title=f"New Email from {from_email}",
                message=f"Subject: {subject}\n{body[:50]}...",
                timeout=10
            )

            messagebox.showinfo("Latest Email", f"From: {from_email}\nSubject: {subject}\n\n{body}")

        else:
            print("\nNo new emails found.")
            messagebox.showinfo("Info", "No new emails found.")

        mail.logout()
    except Exception as e:
        print(f"Error: {e}")
        messagebox.showerror("Error", f"Failed to fetch email: {e}")
