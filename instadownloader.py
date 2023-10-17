def insta(link):
	import requests
	import json
	url = "https://instagram-downloader-download-instagram-videos-stories.p.rapidapi.com/index"
	querystring = {"url":link}
	headers = {
		"X-RapidAPI-Key": "c160d7f5bbmsh7a5316eecf4786fp13a953jsn210f143381f9",
		"X-RapidAPI-Host": "instagram-downloader-download-instagram-videos-stories.p.rapidapi.com"
	}
	response = requests.request("GET", url, headers=headers, params=querystring)
	rest = json.loads(response.text)
	data = {}
	if rest['Type']=='Post-Video':
		data['media'] = rest['media']
		data['type'] ='video'
	elif rest['Type'] =='Carousel':
		data['media'] = rest['media']
		data['type'] ='carousel'
	elif rest['Type'] == 'Post-Image':
		data['media'] = rest['media']
		data['type'] ='image'
	else:
		data['type'] ='error'
	return data