import tkinter as tk
from tkinter import scrolledtext
import socket
import threading

# ----------------------------
# Scan logic (SAFE + FAST)
# ----------------------------
def scan_ports():
    output.delete(1.0, tk.END)

    target = entry.get().strip()
    if not target:
        output.insert(tk.END, "Enter a target (example: 127.0.0.1)\n")
        return

    output.insert(tk.END, f"Scanning: {target}\n\n")

    def worker():
        try:
            ip = socket.gethostbyname(target)
        except:
            output.insert(tk.END, "Invalid host\n")
            return

        for port in range(1, 1025):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.1)

            try:
                result = sock.connect_ex((ip, port))
                if result == 0:
                    output.insert(tk.END, f"[OPEN] Port {port}\n")
                    output.see(tk.END)
            except:
                pass
            finally:
                sock.close()

        output.insert(tk.END, "\nDone.\n")

    threading.Thread(target=worker, daemon=True).start()


# ----------------------------
# UI
# ----------------------------
root = tk.Tk()
root.title("ChatGPT's Port Scanner 0.1")
root.geometry("600x400")
root.configure(bg="black")

title = tk.Label(
    root,
    text="ChatGPT's Port Scanner 0.1",
    fg="blue",
    bg="black",
    font=("Consolas", 16, "bold")
)
title.pack(pady=10)

entry = tk.Entry(
    root,
    width=40,
    fg="blue",
    bg="black",
    insertbackground="blue"
)
entry.insert(0, "127.0.0.1")
entry.pack(pady=5)

btn = tk.Button(
    root,
    text="SCAN",
    command=scan_ports,
    fg="blue",
    bg="black",
    activebackground="blue",
    activeforeground="black",
    relief="flat",
    font=("Consolas", 12, "bold")
)
btn.pack(pady=10)

output = scrolledtext.ScrolledText(
    root,
    width=70,
    height=15,
    fg="blue",
    bg="black",
    insertbackground="blue"
)
output.pack(pady=10)

root.mainloop()