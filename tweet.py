import tweepy
import numpy as np


def auth():
    liste_token=np.load("private/tokens.npy")
    API_KEY = liste_token[0]
    API_SECRET = liste_token[1]
    BEARER_TOKEN = liste_token[2]
    ACCESS_TOKEN = liste_token[3]
    ACCESS_SECRET = liste_token[4]

    auth=tweepy.OAuthHandler(consumer_key=API_KEY,consumer_secret=API_SECRET)
    auth.set_access_token(key=ACCESS_TOKEN,secret=ACCESS_SECRET)
    api=tweepy.API(auth, wait_on_rate_limit=True)
    print("API created")
    return api

def get_mentions(api):
    mentions=api.mentions_timeline()
    return mentions

def check_list(list_mentions):
    listProcessed=np.load("save/processed.npy")
    curseur=0

    while curseur<len(list_mentions):
        if list_mentions[curseur].id in listProcessed:
            list_mentions.pop(curseur)
        else:
            curseur+=1
    return list_mentions

def publicate_response(api,text,id):
    liste_mention=np.load("save/processed.npy")
    api.update_status(text,in_reply_to_status_id=id)
    liste_mention=np.append(liste_mention,id)
    print("Liste mention :"+str(liste_mention))
    print("Add : "+str(id))
    np.save("save/processed.npy",liste_mention)

if __name__=='__main__':
    auth()