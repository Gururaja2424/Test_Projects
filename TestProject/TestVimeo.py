import vimeo
import requests
import base64

msg = "hello world"
print(msg)


def getVimeoConnection():
    print("method start")
    client = vimeo.VimeoClient(
        token='{0917e101a5077730d19879701b617430}',
        key='{b51bb022d75e0a18d861a9bf0f3486d1ff78d298}',  #client_id
        secret='{Em2+J1sgk//bOoReyLSdY1fcoY7UHSMyJlBxOHEc82oTLiNPEdHCPtXR0v8crb4RhQGQQP11kjISrKEiMxZy/zhZtEUWC/W481qikowptkeXJQQRbwk3C0VpZE4ndcF6}'
    )

    #response = client.get("https://api.vimeo.com/oauth/authorize/client") 
    response = client.get("https://api.vimeo.com/onteder")
    
    #assert response.status_code == 200
    
    print(response.json())
   
    print("method end")
    
        
    return response

result = getVimeoConnection()
print(result)

def liveStream():
    
    # api-endpoint 
    URL = "https://api.vimeo.com/me"
    
    Authorization = 'bearer {0917e101a5077730d19879701b617430}'
    
    # defining a parameters to be sent to the API 
    headers = {'Authorization': Authorization, 'Accept': 'application/vnd.vimeo.*+json;version=3.4'}
    
    # sending get request and saving the response as response object 
    req = requests.get(URL, headers=headers)
    
    # extracting data in json format 
    data = req.json() 
    return data

def authorization():
    
    # api-endpoint 
    URL = "https://api.vimeo.com/oauth/authorize/client"

    client_id = "b51bb022d75e0a18d861a9bf0f3486d1ff78d298"
    client_secret = "Em2+J1sgk//bOoReyLSdY1fcoY7UHSMyJlBxOHEc82oTLiNPEdHCPtXR0v8crb4RhQGQQP11kjISrKEiMxZy/zhZtEUWC/W481qikowptkeXJQQRbwk3C0VpZE4ndcF6"
    encodedData = base64.b64encode(bytes(f"{client_id}:{client_secret}", "ISO-8859-1")).decode("ascii")
    authorization_header_string = f"Authorization: Basic {encodedData}"
    
    # defining a parameters to be sent to the API 
    headers = {'Authorization': authorization_header_string, 'Content-Type': 'application/json', 'Accept': 'application/vnd.vimeo.*+json;version=3.4'}
    
    # sending get request and saving the response as response object 
    req = requests.get(URL, headers=headers)
    
    # extracting data in json format 
    data = req.json() 
    return data


result1 = authorization()
print(result1)





