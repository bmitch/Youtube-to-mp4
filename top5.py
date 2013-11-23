import json
import os

json_data = open("top5.json").read()
data = json.loads(json_data)
data = data["feed"]
data = data['data']

print data[1]['link']

for (i, item) in enumerate(data):
	if 'link' in data[i]:
		print " " + str(i) + " " + data[i]['link']
		print str(i) + "/" + str(len(data))
		os.system("youtube-dl " + data[i]['link'])
		os.system("sudo mv *.mp4 /mnt/videos/youtubemp4s")