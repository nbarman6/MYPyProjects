import requests

str =input("ENTER YOUR NAME (I WILL TELL YOUR GENDER) : ")
url=f"https://api.genderize.io?name=" + str
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(f"NAME: {data['name']}")
    print(f"GENDER: {data['gender']}")
else:
    print("FAILED TO RETRIEVE DATA")