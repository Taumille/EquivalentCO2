def beautiful_int(i):
    s=str(i)
    s_beau=""
    # 12 000 000 = a 3 3 ou a=2
    a=len(s)%3
    for k in range(a):
        s_beau+=s[k]
    if a!=0:
        s_beau+=" "
    i=a
    while i<len(s):
        for _ in range(3):
            s_beau+=s[i]
            i+=1
        s_beau+=' '
    return s_beau[:-1]