import tweepy

def authentication():
    # Authenticate to Twitter
    try:
        auth = tweepy.OAuthHandler("gvoDtfDn73wd8ooFamZV0fGe7", "CbH12mjG59wYvuOYdO4OM08MGkKr4Z81gu5mEEDT2IirUEJRp3")
        auth.set_access_token("2489524002-sIXDsaE8F5tdJVL6XX8Ovj645QmGhNyTJdYv8v0","PX8z5y1auwU69RFfvPbYgeGfHYcLrIqPJigfdlGVQJlB8")
       # api = tweepy.API(auth)
        api = tweepy.API(auth, wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
        api.verify_credentials()
        print("Authentication OK")
        #api = tweepy.API(auth, wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
        
    except:
        print("Error during authentication")
        
    return api

# Authenticate to Twitter
#auth = tweepy.OAuthHandler("CONSUMER_KEY", "CONSUMER_SECRET")
#auth.set_access_token("ACCESS_TOKEN", "ACCESS_TOKEN_SECRET")

def make_ordinal(n):
    '''
    Convert an integer into its ordinal representation::

        make_ordinal(0)   => '0th'
        make_ordinal(3)   => '3rd'
        make_ordinal(122) => '122nd'
        make_ordinal(213) => '213th'
    '''
    n = int(n)
    suffix = ['th', 'st', 'nd', 'rd', 'th'][min(n % 10, 4)]
    if 11 <= (n % 100) <= 13:
        suffix = 'th'
    return str(n) + suffix

def tweet_message(name,age,twitterid):
    api1=authentication()
    print("in tweet message")
    user = api1.me()
    print('Name: ' + user.name)
    print('Friends: ' + str(user.friends_count))
    imagePath = "HBD.jpg"
    #status = "Hi! Dummy1 Birthday Wishes message from Python script"
    ordinalage=make_ordinal(age)
    msg = "Happy {} Birthday {} .. Many Many Happy Returns of the day {}".format(ordinalage ,name,twitterid)
    print(msg)
    #Send the tweet.
    api1.update_with_media(imagePath, msg)
    print("tweet sent")

if __name__=="__main__": 
    tweet_message("Cassie","32","@kgkrishna555")