from datetime import *
import os, random, subprocess

helloIntent = ['hi', 'hello', 'namaste', 'bonjour']
timeIntent = ['what\'s the time', 'time please', 'tell me the current time']
dateIntent = ['what\'s the date today', 'date please', 'tell me today\'s date']
musicIntent = ['play a song', 'play some song for me', 'play a random song']

while True:

    message = input( "Enter your message: " )

    if message in helloIntent:
        print('hello')
    elif message == 'how are you' or message == 'how you doin?':
        print('i am great, what about you?')
    elif message == 'i am also fine':
        print('sounds good')
    elif message in timeIntent:
        now = datetime.now( )
        print(now.strftime( '%a %d %b %Y %H:%M:%S %p' ))
    elif message in dateIntent:
        today = date.today( )
        print(f"{today.day}/{today.month}/{today.year}" )
    elif message in musicIntent:
        os.chdir('/Users/anmolrajarora/Documents/python' )
        songs = os.listdir( )
        song = random.choice( songs )
        subprocess.call( [ 'open' , song ] )
    elif message == 'bye':
        print('Bye!')
        break
    else:
        print('I don\'t understand :( ')
        