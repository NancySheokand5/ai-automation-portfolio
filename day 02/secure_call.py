import os 
import requests
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("API_KEY")
if not api_key:
    print("API_KEY not found in .env file")
    exit()
headers = {"Authorization": f"Bearer {api_key}"}
response = requests.get("https://httpbin.org/bearer", headers=headers, timeout=10)
print(response.status_code)
print(response.json())