# Python Flight Notifier

This is a small program I wrote in python that helps me keep track of cheap flights because I like to travel. I signed up for an email list that will send out cheap flights a couple times a day, however their emails are often full of extra junk about other stuff they want you to sign up for. Also it is annoying to setup notifications for just these types of emails. So this program is aimed at those two problems. It will check if I have recieved an email from this email list and then parse the emails and pull out only the important information and then send it to my phone as a text message.

## Getting Started

The way this project is meant to be used is to update the credentials file with all of your information, and then run the call flights program in the background. You will need to make a twillio account, and sign up for the email list (https://scottscheapflights.com/), in order to take full advantage of this program. 

### Prerequisites

What libraries you will be using if you run this program.

```
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
```

## Running the tests

If you have the credentials file filled out with your correct information from twillio, you can test the program by running the flightNotifier.py file. If you have an unread email from scott's cheap flights you should recieve a text message. Feel free to email me at Estrada.alex20@gmail.com personally if you run into issues with this. 

## Built With

* [Twilio](https://www.twilio.com/) - Mobile Python API

## Authors

* **Alex Estrada** - *Initial work* - [EstradaAlex20 Github](https://github.com/EstradaAlex20)
Note: I am a junior in a my Digital Simulation and Game Design bachelors program currently. As such, I am very interested in being a better programmer, so if you are looking at this project, or any of my other projects and see any mistakes or bad programming practices, let me know!(Estrada.alex20@gmail.com) I'd love to hear from anyone who is looking at this.

## Acknowledgments

* Thanks to Scott's cheap flights for doing all the heavy lifting as far as finding the cheap flights!
