#!/usr/bin/python
# -*- coding: utf-8 -*-

from time import time
from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/user/account
# twilio settings
account_sid = "AC7f346d6709e1a16127d78d51e491f6de"#account id
auth_token = "f894f65a625fcd6f58957caa999c8dfa"#authentication token 
client = Client(account_sid, auth_token)
force = 0 
delay = 3600
timestamp = 0


def check_message(message):
    """makes sure the message is below 160 characters"""
    if len(message) >= 155:
        message = message[0:152] + '...'
    return message


def send_sms(location, vacant_seat):
    """sends an SMS using Twilio to number specified with message"""
    if force or (int(time()) - timestamp) > delay:
        #import TwilioRestClient
        from twilio.rest import TwilioRestClient
        body_message = "The current location is  " + \
            str(location) + "\n vacant seats is " + str(vacant_seat)
    body_message = check_message(body_message.strip())
    print body_message
    message = client.messages.create(
        "+917996620470", body=str(body_message), from_="+19472224104",)
    if message.status != "failed":
        print "SMS send successfully"
        return True
    else:
        print "failed to send sms"
        return False
