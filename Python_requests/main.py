import requests

data_petstore ={"petid":"7"}
response = requests.get("https://petstore.swagger.io/v2/pet/7",
  json=data_petstore)
print (response.text)