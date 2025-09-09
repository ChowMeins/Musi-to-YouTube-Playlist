# Musi to YouTube Playlist

A Python script that converts playlists from the Musi mobile app to YouTube playlists. This tool allows you to migrate your music playlists from Musi directly to your YouTube account.

## Overview

The script extracts song information from a Musi playlist URL and automatically creates a corresponding playlist on YouTube using the YouTube Data API v3. Songs are searched and added to your YouTube account, preserving the original playlist structure.

## Requirements

### Prerequisites
- Python 3.x
- Google Cloud Console account
- YouTube account
- Musi playlist URL

### Python Dependencies
- google-auth
- google-auth-oauthlib
- google-auth-httplib2
- google-api-python-client
- requests
- beautifulsoup4

## Setup Instructions

### Step 1: Install Dependencies
```bash
pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client requests beautifulsoup4
```

### Step 2: Google API Configuration
1. Visit the [Google Cloud Console](https://console.cloud.google.com/welcome)
2. Create a new project or select an existing one
3. Enable the YouTube Data API v3 for your project
4. Go to "Credentials" and create credentials:
   - Create an OAuth 2.0 Client ID
   - Download the JSON file
5. Rename the downloaded file to `client_secrets.json`
6. Place the file in the project directory

### Step 3: OAuth Setup
- Configure OAuth consent screen in Google Cloud Console
- Add your email to test users if using testing mode
- Set authorized redirect URIs if required

## Usage

### Basic Usage
1. **Get your Musi playlist URL**
   - Open Musi app on your mobile device
   - Navigate to the playlist you want to convert
   - Copy the playlist URL

2. **Configure the script**
   - Open the Python script
   - Update the `playlist_url` variable with your Musi playlist URL
   - Ensure `client_secrets.json` is in the correct location

3. **Run the script**
   ```bash
   python musi_to_youtube.py
   ```

4. **Authentication**
   - The script will open a browser window for Google authentication
   - Sign in to your Google account
   - Grant permissions for YouTube access

5. **Verify results**
   - Check your YouTube account for the newly created playlist
   - Review that all songs were successfully added

## How It Works

### Process Overview
1. **Playlist Parsing**: Extracts song titles and artists from the Musi playlist URL
2. **YouTube Authentication**: Authenticates with YouTube API using OAuth 2.0
3. **Playlist Creation**: Creates a new playlist on your YouTube account
4. **Song Search**: Searches YouTube for each song from the Musi playlist
5. **Song Addition**: Adds found songs to the newly created YouTube playlist

### Error Handling
- Songs that cannot be found on YouTube are logged for manual review
- Authentication errors provide clear instructions for resolution
- Network issues are handled with appropriate retry mechanisms

## Configuration

### File Structure
```
Musi-to-YouTube-Playlist/
├── musi_to_youtube.py      # Main script file
├── client_secrets.json     # Google API credentials (you provide)
└── README.md              # This file
```

### Script Variables
- `playlist_url`: Your Musi playlist URL
- `client_secrets_file`: Path to your Google API credentials file (default: "client_secrets.json")
- `playlist_title`: Name for the YouTube playlist (extracted from Musi or custom)

## Limitations

### API Limitations
- Subject to YouTube Data API v3 quotas and rate limits
- Daily quota restrictions may limit large playlist conversions

### Matching Accuracy
- Song matching depends on title and artist information accuracy
- Some songs may not be available on YouTube
- Alternative versions or covers might be selected instead of original tracks

### Musi App Dependencies
- Requires valid Musi playlist URLs
- Changes to Musi's website structure may affect functionality

## Privacy and Security

### Data Handling
- No personal data is stored permanently by the script
- Authentication tokens are handled securely through Google's OAuth flow
- Playlist data is only used for the conversion process

### Permissions
- Script requires YouTube account access for playlist creation and modification
- Only necessary permissions are requested through OAuth flow

## Technical Details

### Supported Formats
- Musi playlist URLs from the mobile application
- Public and private playlists (with appropriate access)

### Output Format
- Creates standard YouTube playlists
- Preserves original song order when possible
- Maintains playlist metadata where available
