import requests
import json

#Couldn't complete it, but I tried this

reqUrl = "https://empresas.yachay.lat/includes/api.php"

headersList = {
 "Accept": "*/*",
 "identifier": "gTxMO3VojXzm6g8vTk6rWt1wjAt5BMdE",
 "secret": "dUA5kAV2aJC2xkHDKTrnrNLHECrjxhGG",
 "Content-Type": "application/json" 
}
documentType="DNI"
documentNumber=12365445
payload = json.dumps({
    "action":"AddClient",
    "accesskey": "AccesoTemporal$2022$RCP",
    "firstname" : "John1",
    "lastname" : "Doe1",
    "email" : "john1.doe1@example.com",
    "address1" : "1243 Main Street",
    "city":"Lima",
    "state":"Peru",
    "postcode" : "00202",
    "country":"US",
    "phonenumber":"586724951",
    "customfields":f"{documentType} :{documentNumber}"
    })

response = requests.request("POST", reqUrl, data=payload,  headers=headersList)
print(response.text)