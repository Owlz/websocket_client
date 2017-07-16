# Python >= 3.5!
This requires Python >= 3.5

# Overview
Just a silly script for quickly interacting with websockets in python. It's synchronous, and for the moment re-creates the socket each time. So it's not really useful in production, but if you need a quick shell without a headache it should do fine.

# Install
It's python package installable:

```bash
pip install .
```

# Running

## Command-line shell
It exposes a command-line shell to connect:

```bash
$ websocket_client
Enter full url (i.e.: ws://<ip>/path): ws://82.202.226.240/feed
> {"method":"help"}
{"result": "check\ngenerate\nhelp\noperations\nreconnect", "method": "help", "status": "ok"}
> 
```

## Python lib
The core is obviously the python library itself.

```python
> from websocket_client import websocket
> ws = websocket("ws://82.202.226.240/feed")
> ws.send('{"method":"help"}')
'{"result": "check\\ngenerate\\nhelp\\noperations\\nreconnect", "method": "help", "status": "ok"}'
```
