import tweepy
auth = tweepy.OAuthHandler("")
auth.set_access_token("")
api = tweepy.API(auth)
api.verify_credentials()
print("Authentication OK")
