import requests
from datetime import datetime

class InstaScraper() :
    def __init__(self, url) :
        self.url = url
    
    def dataRequest(self) :
        header = {'User-agent' : 'Sid'}
        res = requests.get(f'{self.url}?__a=1', headers = header)


        return res.json()

    def parsedFinalData(self) :
        data = self.dataRequest()
        self.Description = data['graphql']['shortcode_media']['edge_media_to_caption']['edges'][0]['node']['text']
        self.Date = datetime.fromtimestamp(data['graphql']['shortcode_media']['taken_at_timestamp']).strftime("%m/%d/%Y, %H:%M:%S")
        self.Likes = data['graphql']['shortcode_media']['edge_media_preview_like']['count']
        self.Username = data['graphql']['shortcode_media']['owner']['full_name']
        self.PostCount = data['graphql']['shortcode_media']['owner']['edge_owner_to_timeline_media']['count']
        self.Followers = data['graphql']['shortcode_media']['owner']['edge_followed_by']['count']
        self.Type = data['graphql']['shortcode_media']['__typename']

        return self.__dict__

