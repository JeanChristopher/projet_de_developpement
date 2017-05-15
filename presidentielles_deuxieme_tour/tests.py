# -*- coding: utf-8 -*-
from neo4j.v1 import GraphDatabase, basic_auth

driver = GraphDatabase.driver("bolt://localhost:7687", auth=basic_auth("neo4j", "pa9uKai@ch"))
session = driver.session()

#ouverture du fichier texte contenant les tweets
with open("D:\PROJET_DE_DEVELOPPEMENT\Tweets_candidats_officiels_10.txt", "r") as fichier_tweets:
    donnees = fichier_tweets.readlines()
    for ligne in donnees:
        print(ligne)
        # enregistrement du contenu du fichier dans un dictionnaire
        dict = eval(ligne)
        # connexion à la base de données
        #session.run(
         # "CREATE (a:BD_Tweets_2 {emeteur: {emeteur}, texte: {texte}, coord: {coord}, nbres_retweet: {nbres_retweet}, lieu: {lieu}})",
         #             {"emeteur": dict['user']['screen_name'], "texte": dict['text'], "coord": dict['coordinates'],
         #              "nbres_retweet": dict['retweet_count'], "lieu": dict['user']['location']})
        session.run(
                         "CREATE (a:BD_emetteur_2 {emetteur: {emetteur}})", {"emetteur": dict['user']['screen_name']})
        # session.run(
        #              "CREATE (a:BD_lieu_1 {lieu: {lieu}, emetteur: {emetteur}})", {"lieu": dict['user']['location'],
        #              "emetteur": dict['user']['screen_name']})

session.close()
