import requests

channelid = ""
token = ""

def cli_msg(token, channelid, msg):
    api = f"https://discord.com/api/v10/channels/{channelid}/messages"
    headers = {
        'Authorization': f'{token}',
        'Content-Type': 'application/json'
    }
    
    data = {
        'content': msg
    }
    
    r = requests.post(api, headers=headers, json=data)
    
    if r.status_code == 200:
        print(f"Succesfully Sent: {msg}")
    else:
        print(f"Error while sending message: {msg}")
        
if __name__ == "__main__":
    print("Discord CLI by github.com/r0ck450\n")
    while True:
        msg = input("> ")
        cli_msg(token, channelid, msg)
