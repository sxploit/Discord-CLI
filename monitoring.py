import requests

channelid = ""
token = ""

def monitor_msgs(token, channelid, last_message=None):
    api = f"https://discord.com/api/v10/channels/{channelid}/messages"
    headers = {
        'Authorization': f'{token}',
        'Content-Type': 'application/json'
    }
    
    params = {
        'limit': 1
    }
    
    if last_message:
        params['after'] = last_message
        
    r = requests.get(api, headers=headers, params=params)
    
    if r.status_code == 200:
        msgs = r.json()
        if msgs:
            return msgs[0]
    else:
        print(f"Error While Getting New Messages from {channelid}")
    return None

if __name__ == "__main__":
    last_messages = None
    print("Discord CLI by github.com/r0ck450\n")
    while True:
        msg = monitor_msgs(token, channelid, last_messages)
        if msg:
            print(f"{msg['author']['username']}: {msg['content']}")
            last_messages = msg['id']
