#this is sree branch im making changes



'''import requests
import xml.etree.ElementTree as ET

# Set the API endpoint URL and search parameters
url = "https://pub.orcid.org/v3.0/search"
headers = {"Accept": "application/vnd.orcid+xml", "Authorization": "Bearer 3ab0419a-37a6-4686-bf2b-e3fc9c87439d"}
params = {"q": "affiliation-org-name:\"indian institute of technology hyderabad\""}

# Send the API request and retrieve the response
response = requests.get(url, headers=headers, params=params)

# Parse the response using ElementTree
root = ET.fromstring(response.content)

# Extract the URIs from the search results
uris = [uri_elem.text for uri_elem in root.findall(".//common:uri", namespaces={"common": "http://www.orcid.org/ns/common"})]

# Print the URIs
for uri in uris:
    print(uri)
'''
'''
import requests

# set the API endpoint URL
url = 'https://orcid.org/oauth/token'

# set the parameters for the API request
data = {
    'client_id': 'APP-1P905D70XI2V3EJE',
    'client_secret': '28651eb1-a118-4b81-b601-ba5ee4243822',
    'grant_type': 'client_credentials',
    'scope': '/read-public'
}

# set the headers for the API request
headers = {
    'Accept': 'application/json'
}

# make the API request
response = requests.post(url, data=data, headers=headers)
print(response)

# check the response status code
if response.status_code == 200:
    # extract the access token from the response data
    access_token = response.json()['access_token']
    print('Access token:', access_token)
else:
    # print an error message if the request was not successful
    print('Error:', response.status_code, response.json())
'''