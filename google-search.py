## Refer this URL https://developers.google.com/custom-search/v1/reference/rest/v1/cse/list

from keys import google_secret_key, google_search_cx
import requests
import json

cx = google_search_cx

# Set the API key and the query string
api_key = google_secret_key
query = "ferrari"

# Set the base URL for the API
base_url = "https://content-customsearch.googleapis.com/customsearch/v1"

data = {
    'q': query,
    'cx': google_search_cx,
    'key': google_secret_key
}

# Construct the full URL with the query and API key
url = base_url + "?q=" + query + "&key=" + api_key

# Send the request to the API and store the response
results = requests.get(base_url, params=data)

titles = []
links = []
snippets = []

for i in results.json()['items']:
    titles.append(i['title'])
    links.append(i['link'])
    snippets.append(i['snippet'])

print(titles)
print(links)
print(snippets)
