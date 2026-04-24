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
