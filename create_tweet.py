import tweepy
auth = tweepy.OAuthHandler("gvoDtfDn73wd8ooFamZV0fGe7", "CbH12mjG59wYvuOYdO4OM08MGkKr4Z81gu5mEEDT2IirUEJRp3")
auth.set_access_token("2489524002-sIXDsaE8F5tdJVL6XX8Ovj645QmGhNyTJdYv8v0","PX8z5y1auwU69RFfvPbYgeGfHYcLrIqPJigfdlGVQJlB8")
api = tweepy.API(auth)
api.verify_credentials()
print("Authentication OK")