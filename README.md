Project1

Alessia Cara's fan-page created by Subas Subedi

This program is a very simple fan-page of Alessia Cara (my favorite female singer). Primary goal of this project is to use the information (data) retrieved using Twitter REST API and Genius API and present in the form of a web-app. It will display random quote (tweet), song and song image everytime we refresh the page fetched via Twitter and Genius APIs therefore, two users accessing this webapp at the same time are very likely to get different content.

Built With:
-	Python
-	Flask
-	Add-on libraries (os, requests, json, requests_oauthlib)
-	Deployed via Heroku (https://www.heroku.com/)

Alessia Cara:
Alessia Caracciolo professionally known as Alessia Cara is a Canadian singer, songwriter and instrumentalist. After making several acoustic covers on YouTube and SoundCloud at her young age, she released her first debut single in 2015 (Here) which was a massive hit all over the world.

I searched for her tweets using her secreen_name and limiting the response to 20 per load.
screenname (twitter.com): ‘alessiacara’

Similarly, I searched for her songs using her artist_id and limiting the responses to 20 per load and sorted by popularity.
artist_id (genius.com): ‘394321’

Known Problems:
I do not have any known problems regarding the functionalities of this project yet. I will document in this section when I find any issues.
However, I had some issues while working on the project that I fixed later. Some are,
-	At the beginning, I couldn’t make the ‘requests_oauthlib’ working and was stuck on the project for a while. In the meanwhile, I also    tried to use Tweepy (python wrapper library for Twitter API) but didn’t have much flexibility. Finally, I knew about json format and    figured out how to dig through twitter responses.

-	Moreover, while working with the response from APIs in json format ‘u’ prefix confused me a lot. Also, tried to remove by using         ‘lstring(‘u’)’ but didn’t work. Finally, I googled and found out that ‘u’ just means that data has Unicode string which doesn’t         include on data.

-	After deploying the app on Heroku, I didn’t want to expose API keys in public therefore configured via config vars through Heroko       dashboard. I didn’t know the right way to use those variables back in my ‘app.py’ file. There was no way to check for errors before     deploying the page therefore, I had to push every try to the repo.
