import requests


data_petstore ={ "id": 7,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "python",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"}
response = requests.post("https://petstore.swagger.io/v2/pet",
  json=data_petstore)
print (response.text)



data_petstore ={ "id": 7,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "qa",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"}
response = requests.put("https://petstore.swagger.io/v2/pet",
  json=data_petstore)
print (response.text)



response = requests.get("https://petstore.swagger.io/v2/pet/7",
  json=data_petstore)
print (response.text)