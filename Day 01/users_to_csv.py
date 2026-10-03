import requests
import csv

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url, timeout=10)

if response.status_code != 200:
    print("Something went wrong:", response.status_code)
    exit()

users = response.json()

rows = []

for user in users:
    row = {
        "name": user["name"],
        "email": user["email"],
        "city": user["address"]["city"],
    }

    rows.append(row)

    print(
        row["name"],
        "|",
        row["email"],
        "|",
        row["city"]
    )

with open("users.csv", "w", newline="", encoding="utf-8") as f:

    writer = csv.DictWriter(
        f,
        fieldnames=["name", "email", "city"]
    )

    writer.writeheader()
    writer.writerows(rows)

print("Saved", len(rows), "users to users.csv")