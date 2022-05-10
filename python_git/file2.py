#this code will show that if a user put their demand and then he got a fake message then this code will show that if that message was a spam then it will identigy that and then tell that this is fake otherwise safe.

entry = input("Enter Your Recommendation : ")
spam = ("this is a spam")
nospam = ("your Message is not a spam it means that is safe message")
normal = ("normal messages")
def spams():
    if entry == ("Earn Money For Free"):
        print(spam)
    if entry == ("Win 1 million pounds"):
        print(spam)
    if entry == ("Win Apple Earpods"):
        print(spam)
    if entry == ("kill"):
        print(spam)
    else:
        print(nospam)
spams()

#this code worked sussessully 