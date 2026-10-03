import requests
url = "https://httpbin.org/bearer"
r1 = requests.get(url, timeout=10)
print("Without token:", r1.status_code)
headers = {"Authorization": "Bearer my-test-token-123"}
r2 = requests.get(url, headers=headers, timeout=10)
print("With token:", r2.status_code)
print(r2.json())