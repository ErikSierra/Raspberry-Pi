import requests
import json

api_url = "http://<pi-hole-IP-address>/admin/api.php"
api_key = "<your-API-key>"

# Get statistics for the last 24 hours
params = {'auth': api_key, 'overTime': 24}

# Send the API request
response = requests.get(api_url, params=params)

# Parse the API response data
response_data = json.loads(response.text)

# Print the total number of blocked domains in the last 24 hours
print("Total Blocked Domains (Last 24 Hours):", response_data['ads_blocked_today'])
