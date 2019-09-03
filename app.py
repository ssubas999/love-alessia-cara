# app.py

#importing necessary libraries
import flask, random, os, requests, json, requests_oauthlib

app = flask.Flask(__name__)

@app.route('/')
def index():
    
    # Twitter API using requests_oauthlib(OAuth1)
    # Twitter API url abstracted for screen_name = 'alessiacara' that will get 20 tweets in response
    url = "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=alessiacara&exclude_replies=true&count=20"
    # Submitting Consumer API keys and Access token & access token secret
    oauth = requests_oauthlib.OAuth1(
        "API_key",
        "API_secret_key",
        "Access_token",
        "Access_token_secret"
        )
        
    response = requests.get(url, auth = oauth)
    json_body1 = response.json()
    # Using pyton's json library to make it more readable (in commented line below)
    # print(json.dumps(json_body1, indent = 2))
    
    # Digging through the JSON object in order to abstract tweets(tweets_list) and followers count(fc)
    tweets_list = []
    for content in json_body1:
        tweet = content["text"]
        tweets_list.append(tweet)
    fc = json_body1[0]["user"]["followers_count"]
    random_num0 = random.randint(0,(len(tweets_list)-1))
    rt = tweets_list[random_num0]
    
    # Genius API using Bearer autorization
    # Genious API url abstracted by artist id (394321), sorted by popularity and will get 20 responses per load
    url = "https://api.genius.com/artists/394321/songs?sort=popularity&page=1&per_page=20"
    my_headers = {"Authorization": "Bearer Bxi5CY7701gxpWiHC32WaItkXKU2Auk0v2p5K30rVEvOFfvq9xMg61Ig1mR_xnSQ"}
    response = requests.get(url, headers = my_headers)
    # Using pyton's json library to make it more readable | .json() will return the response as json formatted string (more like a combination of lists and dictionary)
    # The u- prefix just means(when you print json data) that you have a Unicode string. When you really use the string, it won't appear in your data.
    # print(json.dumps(json_body2, indent = 2))
    json_body2 = response.json()
    
    # Digging through JSON object
    img_url_list = []
    album_title_list =  []
    lyrics_url_list = []
    for inside_songs in json_body2['response']['songs']:
        
        # Abstracting list of song_art_image_url
        img_url = inside_songs['song_art_image_url']
        img_url_list.append(img_url)
        
        # Abstracting list of title_with_featured
        album_title = inside_songs['title_with_featured']
        album_title_list.append(album_title)
        
        # Abstracting list of url
        lyrics_url = inside_songs['url']
        lyrics_url_list.append(lyrics_url)
        
    # Choosing a random song out of 20 songs.
    random_num2 = random.randint(0,(len(album_title_list)-1))
    ra = album_title_list[random_num2]
    riu = img_url_list[random_num2]
    rlu = lyrics_url_list[random_num2]
    
    print("hello world")
    return flask.render_template("index.html", random_tweet = rt, random_album = ra, random_image_url = riu, random_lyrics_url = rlu, followers_count = fc)


app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0'),
    debug= True
    )