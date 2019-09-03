# app.py
import flask, random, os, tweepy, requests, json, requests_oauthlib

app = flask.Flask(__name__)

@app.route('/')  
def index():
    
    # Twitter API using requests_oauthlib
    url = "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=alessiacara&exclude_replies=true&count=20"
    oauth = requests_oauthlib.OAuth1(
        "M0V2et56cbWEztaGyng2sRs0v",
        "95tvu7fmfyHMidMLjfVQjsMizuAnLnG00iHoERj88PIfoYq8Fx",
        "1469370974-X5gqdeacJvTLZL4D9KYRjIsWm4jOoxqeLX2VaxI",
        "ZOAnVOjmckToiA7jtWP7zag5wjsAv1IRC8bb4OiHfuM2Q"
        )
    response = requests.get(url, auth = oauth)
    json_body1 = response.json()
    # Using pyton's json library to make it more readable (in commented line below)
    # print(json.dumps(json_body1, indent = 2))
    
    
    tweets_list = []
    for content in json_body1:
        tweet = content["text"]
        tweets_list.append(tweet)
    fc = json_body1[0]["user"]["followers_count"]
    print(fc)
    random_num0 = random.randint(0,(len(tweets_list)-1))
    rt = tweets_list[random_num0]
    
    
    '''
    #Alternative way of extracting information via Twitter API using wrapper library- Tweepy
    
    # It will download the home timeline tweets using tweepy
    auth = tweepy.OAuthHandler("API key", "API secret key")
    auth.set_access_token("Access token", "Access token secret")

    api = tweepy.API(auth)

    user_tweets = api.user_timeline(screen_name = 'alessiacara', count = 10)
    tweet_list = []
    for tweet in user_tweets:
        tweet_list.append(tweet.text)
    random_num1 = random.randint(0,9)
    rt = tweet_list[random_num1]
    '''
    
    #Genius api
    url = "https://api.genius.com/artists/394321/songs?sort=popularity&page=1&per_page=20"
    my_headers = {"Authorization": "Bearer Bxi5CY7701gxpWiHC32WaItkXKU2Auk0v2p5K30rVEvOFfvq9xMg61Ig1mR_xnSQ"}
    response = requests.get(url, headers = my_headers)
    # .json() will return the response as json formatted string (more like a combination of lists and dictionary)
    json_body2 = response.json()
    # The u- prefix just means(when you print json data) that you have a Unicode string. When you really use the string, it won't appear in your data.
    # Using pyton's json library to make it more readable
    # print(json.dumps(json_body2, indent = 2))
    
    # Creating list of image urls.
    img_url_list = []
    album_title_list =  []
    lyrics_url_list = []
    for inside_songs in json_body2['response']['songs']:
        img_url = inside_songs['song_art_image_url']
        img_url_list.append(img_url)
        
        album_title = inside_songs['title_with_featured']
        album_title_list.append(album_title)
        
        lyrics_url = inside_songs['url']
        lyrics_url_list.append(lyrics_url)

    random_num2 = random.randint(0,(len(album_title_list)-1))
    ra = album_title_list[random_num2]
    riu = img_url_list[random_num2]
    rlu = lyrics_url_list[random_num2]

    return flask.render_template("index.html", random_tweet = rt, random_album = ra, random_image_url = riu, random_lyrics_url = rlu, followers_count = fc)


app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0'),
    debug= True
    )