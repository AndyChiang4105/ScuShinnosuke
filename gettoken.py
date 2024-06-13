import requests
import json


def main():
        
    url = "https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=shnTSjhAbQV0IfyCBYvqCh8U&client_secret=lcbum7qjnBbmlFTR4cGoQ1sSCMaPC15D"
    
    payload = ""
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    
    response = requests.request("POST", url, headers=headers, data=payload)
    
    print(response.text)
    

if __name__ == '__main__':
    main()