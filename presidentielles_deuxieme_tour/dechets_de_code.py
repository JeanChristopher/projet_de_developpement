
# insertion de différentes informations contenues dans le dictionnaire des hashtags dans
    #if dict["retweet_count"] < 1:

# for hashtag in dict['entities']['hashtags']:
    # # si un hashtag déja récupéré est dans la liste, la ligne n'est pas récupérée
    #         if hashtag["text"] not in dict['entities']['hashtags'][0]["text"]:
    #             session.run(
    #             "CREATE (a:BD_Hashtag_2 {texte: {texte} , emetteur: {emetteur}})", {"texte": hashtag["text"],
    #             "emetteur": dict['user']['screen_name']})
                # on met en relation le noeud du hashtag avec celui du tweet
            # session.run(
            #         "")

# """
# CREATE (t1:Tweet {emeteur: 'Titi', texte: 'Blablabla bla bla bla', lieu: 'ENSG'}) CREATE (h:Hashtag {valeur:'Macron'}) MATCH (t:Tweet {emeteur:'Titi'}),(h:Hashtag {valeur:'Macron'}) CREATE (t)-[:TAG]->(h)
# """