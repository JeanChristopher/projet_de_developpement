from tweepy import*
import codecs

from configparser import ConfigParser

# création d'une classe héritant de la classe tweepy.streamlistener
consumer_key = "8EMTDCf5LYnWtRnz8gNzcrGMh"
consumer_secret_key = "3QbSGxjhohQIBY8MFexww8TqErN7DSBx6CR1eHjzKhEUBFkXPK"
access_token = "425874978-CBCceEOl3AfihjGCNm3ris9hSqCUINTdmxb3lRCF"
access_token_secret_key =  "025nNTWbIF5FZDJmNFsqE3Cvr5eWeaOqbvYP3Yg1cHB0W"


class tweets_temps_reel(StreamListener):
    def on_status(self, status):
        print(status.text)

    def on_error(self, status):
        print("ERROR")
        print(status)

    def on_data(self, data):
        base_tweets = codecs.open("D:\PROJET_DE_DEVELOPPEMENT\Tweets_candidats_officiels_10.json", "a", "utf8")
        base_tweets.writelines(data)
        base_tweets.close()
        print(data)

    def on_connect(self):
        # Called initially to connect to the Streaming API
        print("Vous êtes connecté à l'API.")

if __name__ == '__main__':

    t = tweets_temps_reel()
    auth = OAuthHandler(consumer_key, consumer_secret_key)
    auth.set_access_token(access_token, access_token_secret_key)

    flow = Stream(auth, t)

    flow.filter(track=["#Marine2017", "#Macron", "#macron2017", "#EmmanuelMacron", "#EmmanuelMacron2017"])