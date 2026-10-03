import os
import requests
from dotenv import load_dotenv
load_dotenv()
apikey = os.getenv("API_KEY")
url = "https://httpbin.org/status/500"
lead = {
    "name" : "John Doe",
    "phone" :"9876543210",
    "interest": "2BHK apartment",
    "source": "website_form",
}
headers = {"Authorization": f"Bearer {apikey}",
           "Content-Type": "application/json",}
try:
    response = requests.post(url, headers=headers, json=lead, timeout=10)
    response.raise_for_status()
    print("Lead sent successfully:", response.status_code)
    print("Server Response:", response.json()["json"])
except requests.exceptions.Timeout:
    print("Server too slow.pls try again later")
except requests.exceptions.HTTPError as e:
    print("Server returned an error:", e)
except requests.exceptions.RequestException as e:
    print("Network problem:", e)