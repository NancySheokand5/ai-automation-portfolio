# Day 1: API to CSV

## Problem
Copying data from a web service into a spreadsheet by hand is slow and error-prone.

## Solution
A Python script that calls a REST API, reads the JSON response, and exports selected fields to a CSV file.

## What it does
1. Sends a `GET` request to `https://jsonplaceholder.typicode.com/users`
2. Checks the status code and stops with a message if it isn't `200`
3. Reads nested JSON (`user["address"]["city"]`)
4. Prints each user's name, email and city
5. Saves the 10 users to `users.csv`

## Tools
Python, `requests`, `csv`, JSON

## How to run
```bash
pip install requests
python users_to_csv.py
```

## Screenshots
![Terminal output](screenshots/day01_output.png)
![CSV file](screenshots/day01_csv.png)

## What I learned
- How HTTP requests and responses work (GET, status codes)
- How to read JSON, including nested objects and lists
- Why automation scripts need `timeout` and status-code checks

## Business use
The same pattern applies to pulling leads, orders or invoices from any service into a sheet for reporting.