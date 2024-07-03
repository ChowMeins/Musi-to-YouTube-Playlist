This is a python script that converts a Musi Playlist (mobile app) to a YouTube Playlist

In order for this script to work, you will need:
- The Client Secrets File
- Musi Playlist URL

In order to get the Client Secrets File follow the following steps:
1.) Visit the site https://console.cloud.google.com/welcome
2.) Create a new product
3.) Create an API Key and OAuth ID and generate the .json file
4.) Move the .json file to the project directory and rename it "client_secrets.json" (or change variable name in the script)
5.) Insert the Musi Playlist URL in the variable 'playlist_url'
6.) Run the script and check to see if the playlist has been generated
