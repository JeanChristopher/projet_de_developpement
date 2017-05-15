# -*- coding: utf-8 -*-


from tweepy import *
from neo4j.v1 import GraphDatabase, basic_auth


# création d'une classe héritant de la classe tweepy.streamlistener
consumer_key = "8EMTDCf5LYnWtRnz8gNzcrGMh"
consumer_secret_key = "3QbSGxjhohQIBY8MFexww8TqErN7DSBx6CR1eHjzKhEUBFkXPK"
access_token = "425874978-CBCceEOl3AfihjGCNm3ris9hSqCUINTdmxb3lRCF"
access_token_secret_key = "025nNTWbIF5FZDJmNFsqE3Cvr5eWeaOqbvYP3Yg1cHB0W"


class tweets_temps_reel(StreamListener):
    def on_status(self, status):
        print(status.text)

    def on_error(self, status):
        print("ERROR")
        print(status)

    def on_data(self, data):
        # Ecriture de data dans le fichier texte
        # base_tweets = codecs.open("D:\dossiers_Pycharm\Tweets_candidats_officiels.txt", "a", "utf8")
        # base_tweets.writelines(data)
        # base_tweets.close()
        # print(data)
        # eliminer d'un text tout les caractères non encodé en ascii
        # def remove_non_ascii_1(text):
        # return ''.join(i for i in text if ord(i)<128)
        # Insertion de data dans neo4j
        # remove_non_ascii_1(data)
        try:
            data = data.replace('false', 'False')
            data = data.replace('true', 'True')
            data = data.replace('null', 'None')
            data = data.encode('utf-8', 'surrogatepass')


        except UnicodeEncodeError:
            print("ce texte ne peut être encodé")

        dict = eval(data)

        # insertion de différentes informations contenues dans le dictionnaire des hashtags dans
        if dict["retweet_count"] < 1:
            session.run(
                "CREATE (a:BD_Tweets {emeteur: {emeteur}, texte: {texte}, coord: {coord}, nbres_retweet: {nbres_retweet}, lieu: {lieu}})",
                {"emeteur": dict['user']['screen_name'], "texte": dict['text'], "coord": dict['coordinates'],
                 "nbres_retweet": dict['retweet_count'], "lieu": dict['user']['location']})
            for hashtag in dict['entities']['hashtags']:
                # si un hashtag déja récupéré est dans la liste, la ligne n'est pas récupérée
                if hashtag["text"] not in dict['entities']['hashtags'][0]["text"]:
                    session.run(
                        "CREATE (a:BD_Hashtag_2 {texte: {texte} , emetteur: {emetteur}})", {"texte": hashtag["text"],
                        "emetteur": dict['user']['screen_name']})
                # on met en relation le noeud du hashtag avec celui du tweet
                session.run(
                    "")
                session.run(
                    "CREATE (a:BD_emetteur {emetteur: {emetteur}})", {"emetteur": dict['user']["screen_name"]})

            session.run(
                "CREATE (a:BD_lieu_1 {lieu: {lieu}, emetteur: {emetteur}})", {"lieu": dict['user']['location'],
                 "emetteur": dict['user']['screen_name']})
            """
            MATCH(t: Tweet {emeteur: 'Titi'}), (h: Hashtag{valeur: 'Macron'}) CREATE(t) - [: TAG]->(h)
            """
        print(data)

# """
# CREATE (t1:BD_emetteur {emeteur: 'Titi', texte: 'Blablabla bla bla bla', lieu: 'ENSG'})
#
# CREATE (h:Hashtag {valeur:'Macron'})

"""

        # for row in base_tweets:
        #     from_node = row.split('\t')[0].strip()
        #     to_node = row.split('\t')[1].strip()
        #     graph_db.create(
        #     node(name=from_node),
        #     node(name=to_node))

    def on_connect(self):
        # Called initially to connect to the Streaming API
        print("Vous êtes connecté à l'API.")
#{"created_at":"Thu Apr 20 13:56:53 +0000 2017","id":855057685846388736,"id_str":"855057685846388736","text":"RT @melmez1: #parlonsprojet  La v\u00e9rit\u00e9 sur M\u00e9lenchon \u00e0 lire !  #NotreRepublique https:\/\/t.co\/tVBfywXoym tous avec @jlm_2017 #Hamon #Fillon\u2026","source":"\u003ca href=\"http:\/\/twitter.com\" rel=\"nofollow\"\u003eTwitter Web Client\u003c\/a\u003e","truncated":false,"in_reply_to_status_id":null,"in_reply_to_status_id_str":null,"in_reply_to_user_id":null,"in_reply_to_user_id_str":null,"in_reply_to_screen_name":null,"user":{"id":580904021,"id_str":"580904021","name":"P A N","screen_name":"PAdNP","location":null,"url":null,"description":"Vid\u00e9aste.","protected":false,"verified":false,"followers_count":553,"friends_count":1339,"listed_count":36,"favourites_count":9537,"statuses_count":11969,"created_at":"Tue May 15 13:46:42 +0000 2012","utc_offset":7200,"time_zone":"Paris","geo_enabled":false,"lang":"fr","contributors_enabled":false,"is_translator":false,"profile_background_color":"26B0BF","profile_background_image_url":"http:\/\/pbs.twimg.com\/profile_background_images\/836451397\/fd811fd7f878370e1c383edf3e25fb65.jpeg","profile_background_image_url_https":"https:\/\/pbs.twimg.com\/profile_background_images\/836451397\/fd811fd7f878370e1c383edf3e25fb65.jpeg","profile_background_tile":true,"profile_link_color":"000000","profile_sidebar_border_color":"FFFFFF","profile_sidebar_fill_color":"DDEEF6","profile_text_color":"333333","profile_use_background_image":true,"profile_image_url":"http:\/\/pbs.twimg.com\/profile_images\/832240993596489729\/rKrtBAlk_normal.jpg","profile_image_url_https":"https:\/\/pbs.twimg.com\/profile_images\/832240993596489729\/rKrtBAlk_normal.jpg","profile_banner_url":"https:\/\/pbs.twimg.com\/profile_banners\/580904021\/1488716348","default_profile":false,"default_profile_image":false,"following":null,"follow_request_sent":null,"notifications":null},"geo":null,"coordinates":null,"place":null,"contributors":null,"retweeted_status":{"created_at":"Thu Apr 20 09:34:58 +0000 2017","id":854991775064367104,"id_str":"854991775064367104","text":"#parlonsprojet  La v\u00e9rit\u00e9 sur M\u00e9lenchon \u00e0 lire !  #NotreRepublique https:\/\/t.co\/tVBfywXoym tous avec @jlm_2017 #Hamon #Fillon #macron","source":"\u003ca href=\"http:\/\/www.twitter.com\" rel=\"nofollow\"\u003eTwitter for Windows Phone\u003c\/a\u003e","truncated":false,"in_reply_to_status_id":null,"in_reply_to_status_id_str":null,"in_reply_to_user_id":null,"in_reply_to_user_id_str":null,"in_reply_to_screen_name":null,"user":{"id":2840105417,"id_str":"2840105417","name":"mel mez","screen_name":"melmez1","location":"bordeaux","url":null,"description":null,"protected":false,"verified":false,"followers_count":526,"friends_count":639,"listed_count":240,"favourites_count":2050,"statuses_count":64249,"created_at":"Tue Oct 21 14:51:02 +0000 2014","utc_offset":-25200,"time_zone":"Pacific Time (US & Canada)","geo_enabled":false,"lang":"fr","contributors_enabled":false,"is_translator":false,"profile_background_color":"C0DEED","profile_background_image_url":"http:\/\/abs.twimg.com\/images\/themes\/theme1\/bg.png","profile_background_image_url_https":"https:\/\/abs.twimg.com\/images\/themes\/theme1\/bg.png","profile_background_tile":false,"profile_link_color":"1DA1F2","profile_sidebar_border_color":"C0DEED","profile_sidebar_fill_color":"DDEEF6","profile_text_color":"333333","profile_use_background_image":true,"profile_image_url":"http:\/\/pbs.twimg.com\/profile_images\/852795433382313987\/O7gdGkxt_normal.jpg","profile_image_url_https":"https:\/\/pbs.twimg.com\/profile_images\/852795433382313987\/O7gdGkxt_normal.jpg","profile_banner_url":"https:\/\/pbs.twimg.com\/profile_banners\/2840105417\/1470050047","default_profile":true,"default_profile_image":false,"following":null,"follow_request_sent":null,"notifications":null},"geo":null,"coordinates":null,"place":null,"contributors":null,"is_quote_status":false,"retweet_count":15,"favorite_count":17,"entities":{"hashtags":[{"text":"parlonsprojet","indices":[0,14]},{"text":"NotreRepublique","indices":[50,66]},{"text":"Hamon","indices":[111,117]},{"text":"Fillon","indices":[118,125]},{"text":"macron","indices":[126,133]}],"urls":[],"user_mentions":[{"screen_name":"jlm_2017","name":"JLM 2017","id":4897361049,"id_str":"4897361049","indices":[101,110]}],"symbols":[],"media":[{"id":854748080385781760,"id_str":"854748080385781760","indices":[67,90],"media_url":"http:\/\/pbs.twimg.com\/media\/C9ys2bfXcAARa6C.jpg","media_url_https":"https:\/\/pbs.twimg.com\/media\/C9ys2bfXcAARa6C.jpg","url":"https:\/\/t.co\/tVBfywXoym","display_url":"pic.twitter.com\/tVBfywXoym","expanded_url":"https:\/\/twitter.com\/ramoht\/status\/854748099876716544\/photo\/1","type":"photo","sizes":{"large":{"w":1440,"h":1699,"resize":"fit"},"thumb":{"w":150,"h":150,"resize":"crop"},"small":{"w":576,"h":680,"resize":"fit"},"medium":{"w":1017,"h":1200,"resize":"fit"}},"source_status_id":854748099876716544,"source_status_id_str":"854748099876716544","source_user_id":740486882593808384,"source_user_id_str":"740486882593808384"}]},"extended_entities":{"media":[{"id":854748080385781760,"id_str":"854748080385781760","indices":[67,90],"media_url":"http:\/\/pbs.twimg.com\/media\/C9ys2bfXcAARa6C.jpg","media_url_https":"https:\/\/pbs.twimg.com\/media\/C9ys2bfXcAARa6C.jpg","url":"https:\/\/t.co\/tVBfywXoym","display_url":"pic.twitter.com\/tVBfywXoym","expanded_url":"https:\/\/twitter.com\/ramoht\/status\/854748099876716544\/photo\/1","type":"photo","sizes":{"large":{"w":1440,"h":1699,"resize":"fit"},"thumb":{"w":150,"h":150,"resize":"crop"},"small":{"w":576,"h":680,"resize":"fit"},"medium":{"w":1017,"h":1200,"resize":"fit"}},"source_status_id":854748099876716544,"source_status_id_str":"854748099876716544","source_user_id":740486882593808384,"source_user_id_str":"740486882593808384"}]},"favorited":false,"retweeted":false,"possibly_sensitive":false,"filter_level":"low","lang":"fr"},"is_quote_status":false,"retweet_count":0,"favorite_count":0,"entities":{"hashtags":{"[text":"parlonsprojet","indices":[13,27]},{"text":"NotreRepublique","indices":[63,79]},{"text":"Hamon","indices":[124,130]},{"text":"Fillon","indices":[131,138]}],"urls":[],"user_mentions":[{"screen_name":"melmez1","name":"mel mez","id":2840105417,"id_str":"2840105417","indices":[3,11]},{"screen_name":"jlm_2017","name":"JLM 2017","id":4897361049,"id_str":"4897361049","indices":[114,123]}],"symbols":[],"media":[{"id":854748080385781760,"id_str":"854748080385781760","indices":[80,103],"media_url":"http:\/\/pbs.twimg.com\/media\/C9ys2bfXcAARa6C.jpg","media_url_https":"https:\/\/pbs.twimg.com\/media\/C9ys2bfXcAARa6C.jpg","url":"https:\/\/t.co\/tVBfywXoym","display_url":"pic.twitter.com\/tVBfywXoym","expanded_url":"https:\/\/twitter.com\/ramoht\/status\/854748099876716544\/photo\/1","type":"photo","sizes":{"large":{"w":1440,"h":1699,"resize":"fit"},"thumb":{"w":150,"h":150,"resize":"crop"},"small":{"w":576,"h":680,"resize":"fit"},"medium":{"w":1017,"h":1200,"resize":"fit"}},"source_status_id":854748099876716544,"source_status_id_str":"854748099876716544","source_user_id":740486882593808384,"source_user_id_str":"740486882593808384"}]},"extended_entities":{"media":[{"id":854748080385781760,"id_str":"854748080385781760","indices":[80,103],"media_url":"http:\/\/pbs.twimg.com\/media\/C9ys2bfXcAARa6C.jpg","media_url_https":"https:\/\/pbs.twimg.com\/media\/C9ys2bfXcAARa6C.jpg","url":"https:\/\/t.co\/tVBfywXoym","display_url":"pic.twitter.com\/tVBfywXoym","expanded_url":"https:\/\/twitter.com\/ramoht\/status\/854748099876716544\/photo\/1","type":"photo","sizes":{"large":{"w":1440,"h":1699,"resize":"fit"},"thumb":{"w":150,"h":150,"resize":"crop"},"small":{"w":576,"h":680,"resize":"fit"},"medium":{"w":1017,"h":1200,"resize":"fit"}},"source_status_id":854748099876716544,"source_status_id_str":"854748099876716544","source_user_id":740486882593808384,"source_user_id_str":"740486882593808384"}]},"favorited":false,"retweeted":false,"possibly_sensitive":false,"filter_level":"low","lang":"fr","timestamp_ms":"1492696613166"}


if __name__ == '__main__':
    driver = GraphDatabase.driver("bolt://localhost:7687", auth=basic_auth("neo4j", "pa9uKai@ch"))
    session = driver.session()

    t = tweets_temps_reel()
    auth = OAuthHandler(consumer_key, consumer_secret_key)
    auth.set_access_token(access_token, access_token_secret_key)

    flow = Stream(auth, t)

    flow.filter(
        track=["#Marine2017", "#Macron", "#macron2017", "#EmmanuelMacron", "#EmmanuelMacron2017"])

    session.close()
