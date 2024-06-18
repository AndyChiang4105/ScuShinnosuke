import requests
import json
from pprint import pprint

def main():
        
    url = "https://aip.baidubce.com/rpc/2.0/nlp/v1/sentiment_classify?access_token="
    
    payload = json.dumps({
        "text":"我今天太伤心了，因为我摔了一跤，呜呜呜 " #input text用json存
    })
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)
        
if __name__ == '__main__':
    main()
