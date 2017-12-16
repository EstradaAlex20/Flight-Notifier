# Flight-Notifier
This is a script that I wrote that will pull information from an email about cheap flights and send me a text message with the most important information.

I made this program in such a way that it sends out a text to 2 different phone numbers. You can change this to just a single phone number by erasing the second send function for each type of flights. I haven't done this, as the program suits my needs this way.

You need to have a couple libraries installed for this to run properly. 
A list of the libraries I use:
OS
Schedule
Time
email
sys
imaplib
re
urllib(specifically urllib.request, urllib.parse, and urllib.error)
json
and from twilio.rest import Client

I might come back and refactor this code and eliminate some redundencies, but right now it is just a simple tool that works fine. For example, I could pull all of the information I need using re, but I have imported json because I planned on using it to format the emails.

if you stumble upon this somehow and have some questions you should email me at estrada.alex20@gmail.com and I will answer them!

