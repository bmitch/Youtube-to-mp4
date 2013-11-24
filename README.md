##Overview
Git source: https://github.com/bmitch/Youtube-to-mp4

This Python script is uses a JSON file containing a list of YouTube URLs posted to a Facebook group.

The URLs in the file are looped through and a MP4 of the YouTube video is then downloaded via [youtube-dl](http://rg3.github.io/youtube-dl/).


## Steps to Accomplish
1. Use FaceBook Graph API to obtain list of YouTube URLs.
2. Parse resulting JSON and loop through each YouTube URL.
3. For each YouTube URL use [youtube-dl](http://rg3.github.io/youtube-dl/) to download the MP4.



## Step 1 - Using FaceBook Graph API
Obtain your Facebook API key:
http://www.mytechshout.com/how-to-get-facebook-api-key.html

Obtain your Facebook group id by navigating to your Facebook group and grabbing the number in the URL after /groups/

For example, https://www.facebook.com/groups/1234/ would be group number 1234.

Navigate to the [Graph API explorer](https://developers.facebook.com/tools/explorer/).

In the input next to the "GET" button enter your group number followed by a query string to obtain a list of all the links posted. Use the image below for reference:
{<1>}![](/content/images/2013/Nov/Capture_PNG.png)

This will return a list of YouTube links posted to your group.

Copy and save this content to a folder where you will run your Python script from.

## Step 2 - Loop through each YouTube URL.

The following code will loop through each YouTube link in file and output the YouTube URL.

<script src="https://gist.github.com/bmitch/7630154.js"></script>

## Step 3 - Use youtube-dl to Download MP4.
Download and install [youtube-dl](http://rg3.github.io/youtube-dl/).

Update your script to use youtube-dl to download as MP4:
<script src="https://gist.github.com/bmitch/7630288.js"></script>

## Notes
You can access the source here:
https://github.com/bmitch/Youtube-to-mp4
