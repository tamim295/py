import requests
from bs4 import BeautifulSoup

# Send a GET request to the website
url = "https://www.youtube.com/watch?v=-kotvsCL-Cw&ab_channel=OnnoRokomPathshala"
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Create a BeautifulSoup object to parse the HTML content
    soup = BeautifulSoup(response.content, "html.parser")

    # Find and extract specific elements from the HTML
    title = soup.title.text
    paragraph = soup.find("p")

    # Check if the paragraph element exists before accessing its text
    if paragraph:
        paragraph_text = paragraph.text
    else:
        paragraph_text = "No paragraph found"

    # Print the extracted data
    print("Title:", title)
    print("Paragraph:", paragraph_text)
else:
    print("Request failed with status code:", response.status_code)