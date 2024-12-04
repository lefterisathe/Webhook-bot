import requests
import tkinter as tk
from tkinter import messagebox


# Function to send a message to the webhook
def send_message():
    webhook_url = webhook_entry.get()  # Get the webhook URL
    message_content = message_text.get("1.0", tk.END).strip()  # Get the message content

    if not webhook_url or not message_content:
        messagebox.showwarning("Missing Information", "Please fill in both the Webhook URL and the Message.")
        return

    data = {
        "content": message_content,  # The message to send
        "username": bot_name_entry.get() or "NiggerBot",  # Optional bot name
    }

    try:
        response = requests.post(webhook_url, json=data)
        if response.status_code == 204:
            messagebox.showinfo("Success", "Message sent successfully!")
        else:
            messagebox.showerror("Error", f"Failed to send message: {response.status_code}\n{response.text}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")


# Create the main GUI window
root = tk.Tk()
root.title("Discord Webhook Sender")
root.geometry("400x300")

# Add a label and entry for the webhook URL
tk.Label(root, text="Webhook URL:").pack(anchor="w", padx=10, pady=5)
webhook_entry = tk.Entry(root, width=50)
webhook_entry.pack(padx=10, pady=5)

# Add a label and entry for the bot name
tk.Label(root, text="Bot Name (optional):").pack(anchor="w", padx=10, pady=5)
bot_name_entry = tk.Entry(root, width=50)
bot_name_entry.pack(padx=10, pady=5)

# Add a label and text box for the message
tk.Label(root, text="Message:").pack(anchor="w", padx=10, pady=5)
message_text = tk.Text(root, height=5, width=50)
message_text.pack(padx=10, pady=5)

# Add a button to send the message
send_button = tk.Button(root, text="Send Message", command=send_message)
send_button.pack(pady=10)

# Run the GUI application
root.mainloop()
