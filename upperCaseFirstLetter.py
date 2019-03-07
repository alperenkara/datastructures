# input = i like coding
# output = I Like Coding
import string
def makeUpperLetter(str):
    return print(string.capwords(str))

makeUpperLetter("i like coding")

def basharfBuyuk(string):
    # split
    kelimeler = string.split(" ")
    # make capitalize 
    for i in range(0,len(kelimeler)):
        kelimeler[i] = kelimeler[i][0].upper()+kelimeler[i][1:]
    # merge and return
    # take list object and put into string variable
    return print(" ".join(kelimeler))

basharfBuyuk("ali mehmet huseyin")

# "some text in here".title()