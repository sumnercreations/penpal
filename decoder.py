def decode(message):
    alpha_dict={'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9,'k':10,'l':11,'m':12,'n':13,'o':14,'p':15,'q':16,'r':17,'s':18,'t':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25}
    alpha_num={0:'a',1:'b',2:'c',3:'d',4:'e',5:'f',6:'g',7:'h',8:'i',9:'j',10:'k',11:'l',12:'m',13:'n',14:'o',15:'p',16:'q',17:'r',18:'s',19:'t',20:'u',21:'v',22:'w',23:'x',24:'y',25:'z'}
    alphaset=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    # keyword is the first word in the message
    keywordList = message.split()
    keyword = keywordList[0]
    print(keyword)
    key = len(keyword)
    # remove the keyword from the message
    keywordList.pop(0)
    # make the list a string using join()
    message = ' '.join(keywordList)
    decoded = ''
    for letter in message:
        if letter.lower() in alphaset:
            x=alpha_dict[letter.lower()]
            decode = alpha_num[(x - key) % 26]
            if letter.isupper():
                decoded += decode.upper()
            else:
                decoded+=decode
        else:
            decoded+=letter
    return decoded