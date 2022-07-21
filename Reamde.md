# reqyml

## Features
- Request as code
- Send requests using yaml

## Requirements
- requests==
- yaml==


## How to use
install Requirements.
``` 
pip3 install -r requirements.txt
``` 



### Using file config:  

| Keys | values | meaning |
| ------ | ------ | ------ |
| url |  | http://example.com| url | 
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
  url: https://icmoex.sbermock.sigma.sbrf.ru/app/currencyfix
  payload: ""
  return: json
example_post:
  method: post
  url: https://icmoex.sbermock.sigma.sbrf.ru/app/prices
  payload: ""
  return: json
  verify: False
```




(c)Mateshev Evgenii