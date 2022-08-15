import tweet
import calculateur
import time

if __name__=='__main__':
    print("Lancement")
    api=tweet.auth()
    print("Authentifié")
    while True:
        mention=tweet.get_mentions(api)
        #mention=tweet.check_list(mention)
        print([m.text for m in mention])
        for tw in mention:
            print(tw.text)
            (quant,mult)=calculateur.find_t_co2(tw.text)
            if quant==None or mult==None or quant=="":
                print("ERREUR")
            else:
                quant=calculateur.reformat_number(quant)
                texte=calculateur.calc_equiv(quant,mult)
                print(texte)
                tweet.publicate_response(api,"@"+(tw.user).screen_name+" "+texte,tw.id)
                print("Publié")
        print("Waiting... "+str(time.time()))
        time.sleep(60)