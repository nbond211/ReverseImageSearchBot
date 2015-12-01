import sbi
import tweepy, time, sys
import simplejson
import urllib2
import cStringIO
from PIL import Image

# Link this bot to the Twitter Account: ReverseImageBot
CONSUMER_KEY = 'BBHHlXvwewlsNRZEow66eMZvb'
CONSUMER_SECRET = '0pGusVtbzhypjPK9OvgnLNlsWSHPB2ZSwL392dw6y8O4Jqlxxk'
ACCESS_KEY = '4331937375-zLFSiWpbSQZN9MwsfrwhqlezLCp5GmcYjs1zV8j'
ACCESS_SECRET = 'xdNQ302s3FSWXFJMyedkrmrkjieFWGKQ0UR0jLrmjfJT5'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

# Download Tweets from account ReverseImageBot
tweets = api.user_timeline('ReverseImageBot')
# Get most recent Tweet
mostRecent = tweets[0]

# Find the word generated previously by the bot
# (to use in the new image title)
contents = str(mostRecent.text)
index = 0

for x in range(0, len(contents)):
    if (contents[x] == " "):
        index = x

prevWord = contents[0 : index]

# Find photo in Tweet
for media in mostRecent.entities.get("media",[{}]):
    #checks if there is any media-entity
    if media.get("type",None) == "photo":
        # checks if the entity is of the type "photo"
        imgUrl = media["media_url"]
        # save to file etc.

# Use Google Image Reverse Search to generate word from image
result = sbi.search_by(url=imgUrl)


fetcher = urllib2.build_opener()
# Remove spaces in phrase generated from image
searchTerm = result.best_guess.replace(" ", "")
startIndex = 0
# Search for phrase in Google Images
searchUrl = "http://ajax.googleapis.com/ajax/services/search/images?v=1.0&q=" + searchTerm + "&start=" + str(startIndex)
f = fetcher.open(searchUrl)
deserialized_output = simplejson.load(f)

imageUrl = deserialized_output['responseData']['results'][0]['unescapedUrl']
# Image previously Tweeted by bot
file = cStringIO.StringIO(urllib2.urlopen(imageUrl).read())
img = Image.open(file)

# New image downloaded by bot
file2  = cStringIO.StringIO(urllib2.urlopen(imgUrl).read())
img2 = Image.open(file2)


### Combine Images ###
sameSize = img2.resize(img.size)

background = img.convert("RGB")
sameSize = sameSize.convert("RGB")

new_img = Image.blend(background, sameSize, 0.5)
new_img.save("new.jpg")

# Update status with merged image
api.update_with_media("new.jpg", prevWord + " " + result.best_guess)