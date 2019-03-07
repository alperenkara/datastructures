# 

def harfKaristirma(str1,str2):
    # str2 de harflere eris
    # her bir harfi kontrol et
    # st1 in icindeki harfler var mi

    for i in str2:
        if i not in str1:
            return False 
    return True

print(harfKaristirma("alperen","asdsd"))
