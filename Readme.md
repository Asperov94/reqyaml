# reqyml

## Features
- Request as code
- Send requests using yaml

## Requirements
- certifi==2022.6.15
- charset-normalizer==2.1.0
- idna==3.3
- PyYAML==6.0
- requests==2.28.1
- urllib3==1.26.10


## How to use
install Requirements.
``` 
pip3 install -r requirements.txt
``` 



### Using file config:  

| Keys | values | meaning |
| ------ | ------ | ------ |
| url | http://example.com | url | 
| method |  get, post, put, delete (default=get) | Method for request |
| payload | pyload  | payload for post request, param for get request |
| return | json, text (default= json) | return forman response |
| verify | True, False (default= True) | Ignore SSL Cert | 
| print_response | True, False (default= False) | print reponse(HEADERS, BODY/PAYLOAD) |
| print_requests | True, False (default= False) | print request |




example config.yaml:
``` 
example_get:
  method: get
  print_response: True
  print_requests: True
  verify: False
  url: https://google.com
  payload: ""
  return: json
example_post:
  method: post
  url: https: https://google.com
  payload: { "key":"value"}
  return: json
  verify: False
```