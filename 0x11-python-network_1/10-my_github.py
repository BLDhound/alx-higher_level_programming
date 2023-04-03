import requests
import sys

# Get GitHub username and personal access token from command line arguments
username = sys.argv[1]
password = sys.argv[2]

# Set up the API endpoint and headers
url = "https://api.github.com/user"
headers = {"Accept": "application/vnd.github.v3+json"}

# Make the API request with basic authentication
response = requests.get(url, headers=headers, auth=(username, password))

# Check if the request was successful
if response.status_code == 200:
    # Extract the user id from the response JSON
    user_id = response.json()["id"]
    print("Your GitHub user id is:", user_id)
else:
    # Print an error message if the request failed
    print("Failed to retrieve GitHub user id. Status code:", response.status_code)
