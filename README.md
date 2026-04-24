# ANOM-CHAT-ONLINE-Encrypted-Messenger-

Anom Chat is a lightweight Python-based real-time messaging application that allows users to communicate over the internet using a WebSocket relay server. Messages are protected using Fernet AES encryption, ensuring that chat content is not readable in transit.

The project is designed as a learning tool for:

networking (client/server communication)
real-time messaging systems
basic cryptography implementation
GUI development in Python


💬 What it does
Enables real-time chat between multiple users over the internet
Uses a central WebSocket server to relay messages
Encrypts all messages before sending
Decrypts messages only on the client side
Provides a simple desktop GUI for chatting
🔐 Encryption

Anom Chat uses Fernet symmetric encryption (AES-based):

A shared secret key is generated using cryptography.fernet
Each message is encrypted before being sent
The server only forwards encrypted data (cannot read messages)
Clients decrypt messages locally using the same key

This ensures message privacy during transmission.

🌍 Architecture
Client (GUI app) → encrypts and sends messages
WebSocket Server → relays messages between users
Other Clients → receive and decrypt messages
⚠️ Disclaimer

This project is intended for educational purposes only.
It demonstrates concepts in:

socket programming
real-time communication
symmetric encryption

It is not a production-grade secure messaging system.

If you want, I can also:

make it a short one-line GitHub description
or 
write a professional README with badges + screenshots section + install guide



▶️ How to Use
1. Install requirements

On both server and client machines:

pip install websockets cryptography
2. Start the server (host machine / VPS)

Run the server first:

python server.py

You should see:

[SERVER] ws://0.0.0.0:8765 running
3. Get the server IP

If hosting on a VPS or another PC, find its IP:

curl ifconfig.me

or:

ip a
4. Configure the client

Open client.py and update:

SERVER_URL = "ws://YOUR_SERVER_IP:8765"

Example:

ws://203.0.113.10:8765
5. Run the client

On each user’s device:

python client.py
6. Share encryption key

When the client starts, it generates a key like:

SHARE THIS KEY WITH FRIENDS:
G3mX1x7q8V0k2PpQzYtR8c1nVx9Jd2aBcD3EfGhIjKl=

⚠️ All users must use the same key for messages to decrypt correctly.

7. Start chatting
Type message in the box
Click Send
Messages appear instantly for all connected users
💬 Summary
Run server
Set server IP in client
Run client
Share encryption key
Chat securely over internet
