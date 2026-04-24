import asyncio
import websockets
import threading
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from cryptography.fernet import Fernet

# ================= SERVER =================
SERVER_URL = "ws://127.0.0.1:8765"  # CHANGE THIS TO VPS/IP

# ================= ENCRYPTION =================
# Generate once and share SAME key with all users
KEY = Fernet.generate_key()
cipher = Fernet(KEY)

print("SHARE THIS KEY WITH FRIENDS:")
print(KEY.decode())

def encrypt(msg):
    return cipher.encrypt(msg.encode()).decode()

def decrypt(msg):
    return cipher.decrypt(msg.encode()).decode()

# ================= NETWORK =================
ws = None
loop = None

async def send_msg_async(msg):
    global ws
    await ws.send(encrypt(msg))

def send_msg():
    msg = entry.get()
    entry.delete(0, "end")

    if loop:
        asyncio.run_coroutine_threadsafe(send_msg_async(msg), loop)

async def receiver():
    global ws

    async with websockets.connect(SERVER_URL) as websocket:
        ws = websocket
        chat.insert("end", "[CONNECTED]\n")

        while True:
            msg = await websocket.recv()
            chat.insert("end", f"Friend: {decrypt(msg)}\n")
            chat.see("end")

def start_loop():
    global loop
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(receiver())

# ================= UI =================
app = tk.Tk()
app.title("🌐 ANOM CHAT ONLINE ENCRYPTED")
app.geometry("600x500")
app.configure(bg="black")

chat = ScrolledText(app, bg="black", fg="lime")
chat.pack(fill="both", expand=True)

bottom = tk.Frame(app, bg="black")
bottom.pack(fill="x")

entry = tk.Entry(bottom)
entry.pack(side="left", fill="x", expand=True, padx=5, pady=5)

tk.Button(bottom, text="Send", command=send_msg).pack(side="left")

tk.Label(app, text="Set SERVER_URL in code", fg="orange", bg="black").pack()

threading.Thread(target=start_loop, daemon=True).start()

app.mainloop()
