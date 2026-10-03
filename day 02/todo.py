import requests
url = "https://jsonplaceholder.typicode.com/todos"
response = requests.get(url, timeout=10)
if response.status_code == 200:
    todos = response.json()
    completed =0
    for todo in todos:
        if todo["completed"]:
            completed += 1
    print("Number of completed todos:", completed)
else :
    print("Something went wrong:", response.status_code)
