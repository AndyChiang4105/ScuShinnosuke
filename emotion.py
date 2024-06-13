import requests
import json
from pprint import pprint

def main():
        
    url = "https://aip.baidubce.com/rpc/2.0/nlp/v1/sentiment_classify?access_token=24.04851c1c215f7605de1502f9f95ca113.2592000.1720877890.282335-82084981"
    
    payload = json.dumps({
        "text":"我今天太伤心了，因为我摔了一跤，呜呜呜 "
    })
    print(payload)
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)
        
if __name__ == '__main__':
    main()
