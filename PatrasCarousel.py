import urllib
import json
import urllib.request
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def json_parsing():
    access_token = 'YOUR-ACCESS-TOKEN'
    instagram_url = 'https://api.instagram.com/v1/media/search?access_token='+access_token+'&lat=38.2248929&lng=21.7253226&distance=5000'
    instagram_response = urllib.request.urlopen(instagram_url)
    instagram_data = json.loads(instagram_response.read().decode('utf-8'))
    filter = []
    images = []
    username = []
    for i in range(len(instagram_data["data"])):
        filter.append(instagram_data["data"][i]["filter"])
        images.append(instagram_data["data"][i]['images']['standard_resolution']['url'])
        username.append(instagram_data["data"][i]['user']['username'])
    return render_template("index.html",filter=filter ,i=i, images=images, username=username)

if __name__ == '__main__':
    app.run()
