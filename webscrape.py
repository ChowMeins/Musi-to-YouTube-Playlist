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
flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES) # This is part of the google-auth-oauthlib library. It is used to handle the OAuth 2.0 flow for desktop or command-line applications.
credentials = flow.run_local_server() # This method starts a local web server to handle the OAuth authorization process.
youtube = googleapiclient.discovery.build(API_SERVICE_NAME, API_VERSION, credentials=credentials) # This function creates a service object for interacting with a specific Google API.

# Create request body for creating the YouTube Playlist
# https://developers.google.com/youtube/v3/docs/playlists/insert 
request_body = {
    "snippet": {
        "title": "Musi Playlist",
        "description": "A playlist created with the YouTube API from Musi.",
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
soup = BeautifulSoup(html_content, 'html.parser')

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

print("Conversion Completed! Exiting Program...")