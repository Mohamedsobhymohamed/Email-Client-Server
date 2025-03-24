import tkinter as tk
from tkinter import filedialog, messagebox
from send_email import dispatch_email
from receive_email import receive_email

file_selection = None

def select_file():
    global file_selection
    file_selection = filedialog.askopenfilename()
    if file_selection:
        messagebox.showinfo("File Chosen", f"Attached: {file_selection}")

def launch_ui():
    app_window = tk.Tk()
    app_window.title("Email Manager")
    app_window.geometry("450x500")
    app_window.configure(bg="#1c1c1c")
    
    text_color = "white"
    button_color = "black"
    button_text = "white"
    
    tk.Label(app_window, text="Sender Email:", fg=text_color, bg="#1c1c1c").pack(pady=(10,0))
    sender_field = tk.Entry(app_window, width=50)
    sender_field.pack()
    
    tk.Label(app_window, text="Password:", fg=text_color, bg="#1c1c1c").pack()
    pass_field = tk.Entry(app_window, width=50, show="*")
    pass_field.pack()
    
    tk.Label(app_window, text="Recipient Email:", fg=text_color, bg="#1c1c1c").pack()
    recipient_field = tk.Entry(app_window, width=50)
    recipient_field.pack()
    
    tk.Label(app_window, text="Subject:", fg=text_color, bg="#1c1c1c").pack()
    subject_field = tk.Entry(app_window, width=50)
    subject_field.pack()
    
    tk.Label(app_window, text="Message:", fg=text_color, bg="#1c1c1c").pack()
    message_field = tk.Text(app_window, height=5, width=50, bg="#2e2e2e", fg="white")
    message_field.pack()
    
    attach_btn = tk.Button(app_window, text="📎 Attach File", bg=button_color, fg=button_text, command=select_file)
    attach_btn.pack(pady=5)
    
    def email_dispatch():
        email_sender = sender_field.get()
        email_pass = pass_field.get()
        email_recipient = recipient_field.get()
        email_subject = subject_field.get()
        email_body = message_field.get("1.0", tk.END)
        
        if not email_sender or not email_pass or not email_recipient:
            messagebox.showerror("Error", "All fields must be filled!")
            return
        
        dispatch_email(email_sender, email_pass, email_recipient, email_subject, email_body, file_selection)

    send_btn = tk.Button(app_window, text="📧 Send Email", bg=button_color, fg=button_text, command=email_dispatch)
    send_btn.pack(pady=5)
    
    inbox_btn = tk.Button(app_window, text="📥 Check Inbox", bg=button_color, fg=button_text, command=lambda: receive_email(
        sender_field.get(), pass_field.get()
    ))
    inbox_btn.pack(pady=5)
    
    app_window.mainloop()

if __name__ == "__main__":
    launch_ui()
