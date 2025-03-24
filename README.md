# Email Client Application

## Overview
This is a simple Python-based Email Client that allows users to send and receive emails using a GUI interface built with Tkinter. The application supports sending emails with attachments and retrieving the latest emails from an inbox. It utilizes the `smtplib` library for sending emails and `imaplib` for receiving emails. The project consists of three main scripts:

- **send_email.py** – Handles the email sending functionality using SMTP.
- **receive_email.py** – Fetches the latest emails from an inbox using IMAP.
- **email_client_gui.py** – Provides a graphical user interface (GUI) for interacting with the email functionalities.

## Features
- 📧 **Send Emails:** Send messages to any recipient via SMTP authentication.
- 📎 **Attach Files:** Allows users to attach files to emails before sending.
- 📥 **Receive Emails:** Retrieves and displays the latest received email.
- 🔐 **Secure Authentication:** Uses TLS encryption for email transmission.
- 🖥 **User-Friendly GUI:** Built with Tkinter for ease of use.

## Requirements
Ensure you have Python installed (preferably 3.x). Install the required dependencies using:

```sh
pip install plyer
```
(Note: `tkinter` is built into Python, so no need to install it separately.)

## Project Structure
```
📂 EmailClient
│── send_email.py        # Handles email sending via SMTP
│── receive_email.py     # Fetches latest emails via IMAP
│── email_client_gui.py  # GUI interface using Tkinter
│── README.md            # Project documentation
```

## Usage
### Running the Application
Run the following command in your terminal or command prompt:
```sh
python email_client_gui.py
```

### Sending an Email
1. Open the application.
2. Enter your **Sender Email** and **Password**.
3. Enter the **Recipient Email**, **Subject**, and **Message**.
4. (Optional) Click **Attach File** to include an attachment.
5. Click **Send Email** to dispatch the email.

### Checking Inbox
1. Click **Check Inbox** after logging in.
2. The latest email will be displayed in a popup window.
3. A system notification will also alert you to new emails.

## Error Handling
- If authentication fails, ensure you use the correct credentials.
- If using Gmail, enable **Less Secure Apps** or generate an **App Password**.
- Ensure an active internet connection to prevent SMTP connection errors.

## Future Enhancements
- 📬 **Support for Multiple Email Accounts**.
- 📄 **Rich Text Formatting** for email body.
- 📂 **Support for Multiple Attachments**.
- 🔔 **Real-time Email Notifications**.

## Contributing
Feel free to fork this repository, suggest improvements, or report issues. Contributions are welcome!

## License
This project is open-source under the MIT License.

