# Alessia Cara's Fan Created Fan-Page

Page can be accessed [here](https://lovealessiacara.herokuapp.com/).

This is a very simple fan-page of Alessia Cara (my favorite female singer). Primary goal of this page is to use the information (data) retrieved using Twitter REST API and Genius API and present in the form of a web-app. It will display random quote (tweet), song and song image everytime we refresh the page fetched via Twitter and Genius APIs therefore, two users accessing this webapp at the same time are very likely to get different content.


### Built With:

-   Python
-	Flask
-	Deployed via [Heroku](https://www.heroku.com/)



### API Endpoint:

I searched for her tweets using her secreen_name and limiting the response to 20 per load.
*screenname* (twitter.com): ‘alessiacara’

Similarly, I searched for her songs using her artist_id and limiting the responses to 20 per load and sorted by popularity.
*artist_id* (genius.com): ‘394321’



### Known Problems:

I do not have any known problems regarding the functionalities of this page yet. I will document in this section when I find any issues.