import socket
import threading
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from cryptography.fernet import Fernet
import os

# ================= KEY HANDLING (FIXED) =================
KEY_FILE = "anom.key"

def load_or_create_key():
    if os.path.exists(KEY_FILE):
        with open(KEY_FILE, "rb") as f:
            return f.read()
    else:
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as f:
            f.write(key)
        return key

SECRET_KEY = load_or_create_key()
cipher = Fernet(SECRET_KEY)

# ================= NETWORK =================
HOST = "0.0.0.0"
PORT = 5050

sock = None
conn = None

# ================= ENCRYPT / DECRYPT =================
def encrypt(msg):
    return cipher.encrypt(msg.encode())

def decrypt(msg):
    return cipher.decrypt(msg).decode()

# ================= LOG =================
def log(msg):
    chat.insert("end", msg + "\n")
    chat.see("end")

# ================= SERVER =================
def start_server():
    global sock, conn

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((HOST, PORT))
        sock.listen(1)

        log("[SERVER] Waiting for connection...")

        conn, addr = sock.accept()
        log(f"[CONNECTED] {addr}")

        threading.Thread(target=receive_loop, daemon=True).start()

    except Exception as e:
        log(f"[SERVER ERROR] {e}")

# ================= CONNECT =================
def connect():
    global sock, conn

    ip = ip_entry.get()

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((ip, PORT))

        conn = sock
        log(f"[CONNECTED] {ip}")

        threading.Thread(target=receive_loop, daemon=True).start()

    except Exception as e:
        log(f"[CONNECT ERROR] {e}")

# ================= RECEIVE =================
def receive_loop():
    global conn

    while True:
        try:
            data = conn.recv(4096)
            if not data:
                break

            msg = decrypt(data)
            log(f"Friend: {msg}")

        except:
            break

# ================= SEND =================
def send():
    global conn

    msg = msg_entry.get()

    if not conn:
        log("[ERROR] Not connected")
        return

    try:
        conn.send(encrypt(msg))
        log(f"You: {msg}")
        msg_entry.delete(0, "end")

    except Exception as e:
        log(f"[SEND ERROR] {e}")

# ================= UI =================
app = tk.Tk()
app.title("🧅 ANOM CHAT ENCRYPTED v2")
app.geometry("700x500")
app.configure(bg="black")

chat = ScrolledText(app, bg="black", fg="lime", font=("Consolas", 10))
chat.pack(fill="both", expand=True)

bottom = tk.Frame(app, bg="black")
bottom.pack(fill="x")

msg_entry = tk.Entry(bottom)
msg_entry.pack(side="left", fill="x", expand=True, padx=5, pady=5)

tk.Button(bottom, text="Send", command=send).pack(side="left")

ip_entry = tk.Entry(app)
ip_entry.insert(0, "192.168.1.1")
ip_entry.pack(fill="x")

tk.Button(app, text="Start Server", command=start_server).pack(fill="x")
tk.Button(app, text="Connect", command=connect).pack(fill="x")

# show key info (so both users can match it)
log(f"[KEY LOADED] {SECRET_KEY.decode()}")

log("[SYSTEM] ANOM CHAT READY")

app.mainloop()
