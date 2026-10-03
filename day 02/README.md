# Day 2: Secure Lead Sender

## Problem
Leads must be sent to a CRM securely, without exposing credentials in code, and the script must not crash when the server fails.

## Solution
A Python script that POSTs lead data as JSON with a Bearer token loaded from a `.env` file, with timeout and error handling.

## Files
| File | Purpose |
|---|---|
| `params_demo.py` | Query parameters (`?userId=1`) using `params=` |
| `auth_demo.py` | Compared a request with and without a Bearer token (401 vs 200) |
| `secure_call.py` | Loaded the API key from `.env` and made an authenticated GET |
| `lead_sender.py` | POSTed a lead as JSON with auth headers and `try/except` |

## Security
- The API key lives in `.env`, which is listed in `.gitignore` and never uploaded
- `.env.example` shows the format: `API_KEY=your_key_here`

## How to run
```bash
pip install requests python-dotenv
# create a .env file with: API_KEY=your_key_here
python lead_sender.py
```

## Error handling tested
| Test URL | Result |
|---|---|
| `https://httpbin.org/post` | 200, lead echoed back |
| `https://httpbin.org/status/401` | 401 Unauthorized, caught by `HTTPError` block |
| `https://httpbin.org/status/500` | 500 Server Error, caught by `HTTPError` block |
| `https://httpbin.org/bearer` with POST | 405 Method Not Allowed (wrong method for the endpoint) |

The script printed a clear message and exited normally in every failure case.

## Screenshots
![Success](screenshots/day02_success.png)
![401 and 500 tests](screenshots/day02_errors.png)

## What I learned
- Query parameters vs headers vs JSON body
- API keys must be kept out of code and out of GitHub
- 401 (bad credentials), 404 (wrong URL), 405 (wrong method), 500 (server problem)
- `try/except` with `raise_for_status()` keeps automations from crashing

## Business use
Every AI or CRM integration sends structured data with authentication. This script is the base pattern.