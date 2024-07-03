from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from google_auth_oauthlib.flow import InstalledAppFlow
import googleapiclient.discovery
import googleapiclient.errors

# Documentation for YouTube API
# https://developers.google.com/youtube/v3/docs]
 
# YouTube API information
SCOPES = ["https://www.googleapis.com/auth/youtube.force-ssl"]
API_SERVICE_NAME = "youtube"
API_VERSION = "v3"
CLIENT_SECRETS_FILE = "client_secrets.json" # Add .json file to directory

# Obtain user credentials
flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
credentials = flow.run_local_server()
youtube = googleapiclient.discovery.build(API_SERVICE_NAME, API_VERSION, credentials=credentials)

# Create request body for creating the YouTube Playlist
request_body = {
    "snippet": {
        "title": "Musi Playlist",
        "description": "A playlist created with the YouTube API",
        "defaultLanguage": "en"
    },
    "status": {
        "privacyStatus": "private"
    }
}
request = youtube.playlists().insert(
    part = "snippet, status",
    body = request_body
)
response = request.execute()
playlist_id = str(response['id'])

# Setup headless Chrome
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)

# INSERT MUSI PLAYLIST URL HERE
playlist_url = ''
# Load the webpage
driver.get(playlist_url)

# Wait for the JavaScript to load the content (if necessary)
driver.implicitly_wait(10)  # Waits for 10 seconds

# Get the page source and pass it to BeautifulSoup
html_content = driver.page_source
soup = BeautifulSoup(html_content, 'html5lib')

# Close the WebDriver
driver.quit()

# Use BeautifulSoup to parse the content and insert the youtube ID's into the playlist
playlist_content = soup.find_all('a', class_='track')
for element in playlist_content:
    youtube_id = str(element.get('href')[-11:])

    request_body = {
        "snippet": {
            "playlistId": playlist_id,
            "resourceId": {
                "kind": "youtube#video",
                "videoId": youtube_id
            }
        }
    }
    request = youtube.playlistItems().insert(
        part="snippet",
        body=request_body
    )
    response = request.execute()

print("Conversion Completed!")
