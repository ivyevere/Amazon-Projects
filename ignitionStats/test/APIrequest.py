import requests

# api_url = "https://jsonplaceholder.typicode.com/todos/1"
# response = requests.get(api_url)
# response.json()
# print(response.status_code)

api_url = "https://jsonplaceholder.typicode.com/todos"
todo = {"userId": 1, "title": "Logged", "completed": False}
response = requests.post(api_url, json=todo)
response.json()
print(response.status_code)

RSC = response.status_code

x = 0
if RSC > 300:
    print(response.status_code + "Missing_Parameter")
if RSC > 200 and RSC < 300:
    print(str(response.status_code) + " is a success")
print("Failure code: " + str(x))