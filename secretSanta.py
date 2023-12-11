import random


def main():
    #open text file and read lines
    tx = open("secretSanta.txt", 'r')
    finishedMaps = ""
    #opfile = open("opfile.txt", 'w')
    lns = tx.readlines()
    names = []
    mails = []

    #add all names in txt file to a name list, add all emails in txt file to an email list
    for ln in lns:
        names.append(ln[0:ln.find(':')].rstrip())
        mails.append(ln[ln.find(':')+1: len(ln)].rstrip())

    mappedNames = []
    mappedMails = []
    i = len(names)
    #for every sender, give a random receiver that doesn't already have a sender 
    while i > 0:
        sender = random.randint(0,len(names)-1)
        receiver = random.randint(0,len(names)-1)
        #check if the sender isnt mapped to self and sender doesnt already have a recipient and recipient isnt already mapped to a sender
        if sender != receiver and sender not in mappedMails and receiver not in mappedNames:
            finishedMaps = finishedMaps + (f" {len(names)-i+1}. {mails[sender]} sends gift to: {names[receiver]} \n")
            #remove the sender and receiver mapped from the list
            mappedNames.append(receiver)
            mappedMails.append(sender)
            i = i-1
        #reset the algorithm until each gmail is mapped to someone thats not themself
        else:
            finishedMaps = ""
            i = len(names)
            mappedNames = []
            mappedMails = []
    print(finishedMaps)



main()
