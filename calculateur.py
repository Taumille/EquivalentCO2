import utils

def reformat_number(s):
    s_format=""
    s=s.replace(",",".")
    if s[0]!=".":
        s_format+=s[0]
    for k in range(1,len(s)-1):
        s_format+=s[k]
    if s[-1]!=".":
        s_format+=s[-1]
    try:
        n=float(s_format)
    except ValueError:
        n=None
    return n
def find_t_co2(s):
    set_number=['0','1','2','3','4','5','6','7','8','9','0',',','.']
    number=""
    curseur_dernier_chiffre=0

    if "@" in s:
        while '@' in s:
            i = s.index("@")
            k=i
            while s[k]!=" " and k<len(s)-1:
                k+=1
            s=s[:i]+s[k:]
            print('New s :'+s)
    if "CO2" in s or "CO²" in s or "co2" in s:
        c=0
        while s[c:c+3]!="CO2" and s[c:c+3]!="CO²" and s[c:c+3]!="co2":
            while c<len(s) and not(s[c] in set_number) and s[c:c+3]!="CO2" and s[c:c+3]!="CO²" and s[c:c+3]!="co2":
                c+=1
            if c<len(s) and s[c:c+3]!="CO2" and s[c:c+3]!="CO²" and s[c:c+3]!="co2" and s[c] in set_number:
                number=""
            while c<len(s) and s[c:c+3]!="CO2" and s[c:c+3]!="CO²" and s[c:c+3]!="co2" and s[c] in set_number:
                number+=s[c]
                curseur_dernier_chiffre=c
                c+=1

            if s[c:c+3]=="CO2" or s[c:c+3]=="CO²" or s[c:c+3]=="co2":
                print("unité :"+s[curseur_dernier_chiffre:c])
                if "kg" in s[curseur_dernier_chiffre:c]:
                    return (number,1)
                elif "tonne" in s[curseur_dernier_chiffre:c]:
                    return (number,3)
                elif "t" in s[curseur_dernier_chiffre:c]:
                    return (number,3)
                elif "g" in s[curseur_dernier_chiffre:c]:
                    return (number,-3)
    else:
        print("Echec")
        return (None,None)
def calc_equiv(quantity,multiple,mail=True,ampoule=True,wifi=True,clim=True):
    text="Bonjour,\n"+str(quantity)
    if multiple==3:
        text+=" tonnes"
        quantity=quantity*1000
    elif multiple==1:
        text += " kg"
    elif multiple==-3:
        text += " g"
        quantity=quantity/1000
    text+=" de CO2 représentent :"
    if mail:
        # Un email avec pièce joint = 50 g CO2
        text+="\n   \U0001F4E8 "+utils.beautiful_int(int(quantity/0.05))+" emails avec une pièce jointe rigolote"
    if ampoule:
        # 60 gC02/Kwh
        # 0.009 kwh/h ampoule led
        # 0.54 gCO2/h
        if int(quantity / (0.54*10**-3))>8760:
            text += "\n   \U0001F4A1 " + utils.beautiful_int(int(quantity / (0.54*10**-3) / 8760)) + " années où une ampoule LED resterait allumée"
        else:
            text += "\n   \U0001F4A1 " + utils.beautiful_int(int(quantity / (0.54*10**-3))) + "h où une ampoule LED resterait allumée"

    if wifi:
        # 250kwh/an = 28.53wh/h
        # 0.06 kgCO2/wh
        # 0.002103049kgCO2/h
        if int(quantity / 0.002103049)>8760:
            text += "\n   \U0001F4E1 " + utils.beautiful_int(int(quantity / 0.002103049 / 8760)) + " années sans couper le wifi"
        else:
            text += "\n   \U0001F4E1 " + utils.beautiful_int(int(quantity / 0.002103049 )) + "h sans couper le wifi"
    return text


if __name__=='__main__':
    calc_equiv(123,3)