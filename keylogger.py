import tkinter as tk
from datetime import datetime

LOG_FILE = "key_log.txt"

def log_key(event):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Handle special keys
    if event.keysym == "space":
        key = "SPACE"
    elif event.keysym == "Return":
        key = "ENTER"
    elif event.keysym == "BackSpace":
        key = "BACKSPACE"
    else:
        key = event.char if event.char else event.keysym

    with open(LOG_FILE, "a") as file:
        file.write(f"[{timestamp}] {key}\n")

def clear_log():
    open(LOG_FILE, "w").close()
    status_label.config(text="Log cleared!")

# GUI setup
root = tk.Tk()
root.title("Educational Key Logger")
root.geometry("400x250")

info = tk.Label(
    root,
    text="⚠ Logs keys typed ONLY in this window\nEducational use only",
    fg="red"
)
info.pack(pady=10)

entry = tk.Entry(root, width=40)
entry.pack(pady=10)
entry.bind("<KeyPress>", log_key)

clear_btn = tk.Button(root, text="Clear Log File", command=clear_log)
clear_btn.pack(pady=10)

status_label = tk.Label(root, text="")
status_label.pack()

root.mainloop()
