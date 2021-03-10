def twitter_api():
    access_token = config.get('twitter_credentials', 'access_token')
    access_token_secret = config.get('twitter_credentials', 'access_token_secret')
    consumer_key = config.get('twitter_credentials', 'consumer_key')
    consumer_secret = config.get('twitter_credentials', 'consumer_secret')

    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = API(auth)
    return api

def tweet_image(url, message):
    api = twitter_api()
    filename = 'HBD.jpg'
    request = requests.get(url, stream=True)
    if request.status_code == 200:
        with open(filename, 'wb') as image:
            for chunk in request:
                image.write(chunk)

        api.update_with_media(filename, status=message)
        os.remove(filename)
    else:
        print("Unable to download image")


url = "http://animalia-life.com/data_images/bird/bird1.jpg"
message = "Nice one"
tweet_image(url, message)