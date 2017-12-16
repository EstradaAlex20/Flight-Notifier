## This program is used to parse and then notify me when a cheap flight is
## available. I get my cheap flights from https://scottscheapflights.com/
## He sends about 4 emails a day, but I wanted to reformat them and send them
## directly to my phone, so that's what this script does.


import email
import sys
import imaplib
import re
import urllib.request, urllib.parse, urllib.error
import json
from twilio.rest import Client


cred_file = open("credentials.txt", "r")
username = cred_file.readline().split()[2]
password = cred_file.readline().split()[2]
twilio_account_sid = cred_file.readline().split()[2]
twilio_auth_token = cred_file.readline().split()[2]
send_to = cred_file.readline().split()[2]
send_from = cred_file.readline().split()[2]
send_from2 = cred_file.readline().split()[2]
cred_file.close()


#########################################################
#This block checks if you have a new email and if you do
#it puts the text into a string, and a list of strings.
#########################################################

mail = imaplib.IMAP4_SSL("imap.gmail.com")
mail.login(username, password)
mail.select("flights")
result, data = mail.uid('search', None, "UNSEEN")
if not data[0].split():
    sys.exit()

most_recent = data[0].split()[-1]
result2, email_data = mail.uid('fetch', most_recent, '(RFC822)')
raw_email = email_data[0][1].decode("utf-8")
email_message=email.message_from_string(raw_email)

for part in email_message.walk():
    if part.get_content_type()=='text/plain':
       email_text = part.get_payload()
       partsplit = part.get_payload().split()

#########################################################
#########################################################




#########################################################
#This function will return a string depending on what type
#of flight you recieve. This deals with the fact that each
#email isn't formatted the same
#########################################################

def typeofflight(wordlist):
    count1 = 0
    count2 = 0
    for part in wordlist:
        #print(part)
        if "PRICES" in part:
            return "Roundtrip"
        elif "TO:" in part:
            for part in wordlist:
                count1+=1
                #print("count1", count1, part)
                if "TO:" in part:
                    break
            for part in wordlist:
                count2+=1
                #print("count2", count2, part)
                if "FROM:" in part:
                    break
            if count2-count1 >= 5:
                return "MoreThanOneDestination"
            else:
                return "OneDestination"

#########################################################
#########################################################




#########################################################
#This function deals with the flights that have one destination
#and one to multiple starting points. It also sends a text
#to the phone number with a condensed form of the information
#########################################################

def OneDestination(wordlist):
    #do some stuff
    to_count = 0
    from_count = 0
    how_count = 0
    destination_city = ""
    temp_price_list = []
    all_words_combined = ""
    city_list = []
    for part in wordlist:
        to_count+=1
        if "TO:" in part:
            break
    for part in wordlist:
        from_count+=1
        if "FROM:" in part:
            break
    for part in wordlist:
        how_count+=1
        if "WHEN" in part:
            break
        
    for part in wordlist[to_count:from_count-1]:
        if "(" in part:
            break
        else:
            destination_city = destination_city + part + " "

            
    for part in wordlist[from_count:how_count]:
        price = re.findall(r'\$\d+',part)
        temp_price_list.append(price)
        
    pricelist = [x for x in temp_price_list if x != []]
    pricelist = [''.join(x) for x in pricelist]

    for part in wordlist[from_count:how_count]:
        all_words_combined = all_words_combined + part

    city_list = re.findall(r'[A-Z].*?\)', all_words_combined)

    flights = dict(zip(city_list, pricelist))
    print(destination_city)
    for i in flights:
        print(i, flights[i])

    client = Client(twilio_account_sid, twilio_auth_token)

    client.messages.create(
        to=send_to,
        from_=send_from,
        body= "\nFlight Notifier: \nTo: " + destination_city + "\nFrom:\n" + str(flights)
    )

    client.messages.create(
        to=send_from2,
        from_=send_from,
        body= "\nFlight Notifier: \nTo: " + destination_city + "\nFrom:\n" + str(flights)
    )

#########################################################
#########################################################



#########################################################
#This function deals with flights that have multiple roundtrip
#flights in the email. It also sends a text to the phone
#number provided in the cred_file.
#########################################################
        
def RoundTrip(wordlist):
    destinations = []
    destinations2 = []
    Text_string = "Flight Notifier:\nYou have Roundtrip flights between:\n"
    fromcities = re.findall(r'[A-Za-z ]+\([A-Z]+\)\:', email_text)
    destinationcitiesFIRST = re.findall(r'\:\s*(?:[A-Za-z ]+\([A-Z]+\)\s\-\s.+\s*)+', email_text)
    for i in destinationcitiesFIRST:
        destinations.append(i.replace("\n", ""))
    for j in destinations:
        destinations2.append(re.findall(r'[A-Z][A-Za-z ]+\([A-Z]+\)\s.\s\$[0-9]+',j))
    print(fromcities)
    print(destinations2)


    for i in range(len(fromcities)):
        Text_string = Text_string + fromcities[i] + " and\n" + '\n'.join(destinations2[i])+ "\n\n"

    client = Client(twilio_account_sid, twilio_auth_token)

    client.messages.create(
        to=send_to,
        from_=send_from,
        body=Text_string
    )

    client.messages.create(
        to=send_from2,
        from_=send_from,
        body= Text_string
    )

#########################################################
#########################################################

if typeofflight(partsplit) == "Roundtrip":
    RoundTrip(partsplit)
elif typeofflight(partsplit) == "MoreThanOneDestination":
    #do some stuff
    print("multiple places")
elif typeofflight(partsplit) == "OneDestination":
    OneDestination(partsplit)    
            








