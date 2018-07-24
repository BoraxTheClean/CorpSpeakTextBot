from random import randint
from globals import *
import os
import boto3
PHONE_NUMBERS = os.environ['PHONE_NUMBERS'].split(',')


def handler(event, context):
    text = make_text()
    send_text(text)


def make_text():
    return get_word(adv) + " " + get_word(verbs) + " " + get_word(adj) + " " + get_word(nouns)


def get_word(lis):
    return lis[randint(0, len(lis) - 1)]


def send_text(text):
    client = boto3.client('sns')
    print(text)
    for NUMBER in PHONE_NUMBERS:
        client.publish(PhoneNumber=NUMBER, Message=text)
