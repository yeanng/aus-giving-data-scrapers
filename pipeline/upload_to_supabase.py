
import requests

SUPABASE_URL = "https://fswalnobzhvwobrypxzq.supabase.co"
SUPABASE_API_KEY = "your-anon-or-service-key"

def upload_grant(data):
    headers = {
        "apikey": SUPABASE_API_KEY,
        "Authorization": f"Bearer {SUPABASE_API_KEY}",
        "Content-Type": "application/json"
    }
    res = requests.post(
        f"{SUPABASE_URL}/rest/v1/grants",
        json=data,
        headers=headers
    )
    print(res.status_code, res.text)

if __name__ == "__main__":
    upload_grant({
        "recipient": "Test Org",
        "amount": 100000,
        "year": 2024,
        "description": "Demo upload from script"
    })
