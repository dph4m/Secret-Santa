import random
import smtplib
from email.message import EmailMessage

#open text file and read lines
def main():
    tx = open("secretSanta.txt", 'r')
    lns = tx.readlines()
    names = []
    mails = []

    #add all names in txt file to a name list, add all emails in txt file to an email list
    for ln in lns:
        names.append(ln[0:ln.find(':')])
        mails.append(ln[ln.find(':')+1: len(ln)])
#for every sender, give a random receiver that doesn't already have a sender 
    while len(names) > 0:
        sender = random.randint(0,len(names)-1)
        receiver = random.randint(0,len(names)-1)
        #random until sender isnt themself and the list isnt empty
        while receiver == sender and len(names) > 1:
            receiver = random.randint(0,len(names)-1)
        print(f"{mails[sender]} sends gift to: {names[receiver]} \n")
        #remove the sender and receiver mapped from the list
        mails.pop(sender)
        names.pop(receiver)


main()