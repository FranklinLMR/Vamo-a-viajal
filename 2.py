import requests

url = "https://visa-requirement.p.rapidapi.com/v2/visa/check"

headers = {
    "X-RapidAPI-Key": "8242cdfc05msh1a619c121b65abep1ca282jsna243e38d77d8",
    "X-RapidAPI-Host": "visa-requirement.p.rapidapi.com",
    "Content-Type": "application/json",
}

payload = {
    "passport": "DO",
    "destination": Visacode,  # e.g. "US"
}

r = requests.post(url, json=payload, headers=headers)
print("Status:", r.status_code)
print("Text:", r.text)
