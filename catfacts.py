#!/usr/bin/python

#This program sends a random cat fact to a list of numbers from a json file.  For usage and more information, look in the README
import os
import sys
import json
import random
import time
from bandwidth_sdk import Client
from bandwidth_sdk import Message
from bandwidth_sdk import models

#Sends the message to the given number
#param number is the current number being sent to, obtained from the json file
def sendMessage(number):
		global cFacts
		currentMessage = Message.send(
    			sender='+14242747426', 		#my number
    			receiver=number,		#the number being sent to
    			text=random.choice(cFacts),	#a randomly selected fact from the list
    			tag='cat fact',			#a tag to describe the message
			receipt_requested='all')	#request a delivery receipt
		
		#time.sleep(3)				#this and the following line are for testing
		#print Message.get(currentMessage.id)



if (len(sys.argv) == 1):											#if no input filename, use the default list of cat facts
	cFacts = ["Mature cats with no health problems are in deep sleep 15 percent of their lives.",
		"If your cat pushes his face against your head, it is a sign of acceptance and affection.",
		"Many cats cannot properly digest cow's milk. Milk and milk products give them diarrhea.",
		"A cat has approximately 60 to 80 million olfactory cells.",
		"Cat's urine glows under a black light."]							#default cat fact list
elif (len(sys.argv)== 2):											#if there is a json file specified for cats facts
	with open(sys.argv[1]) as data_file:
		data = json.load(data_file)
	cFacts = data["facts"]											#set cFacts list to be the facts from that file
else:														#incorrect usage, see README
	print "incorrect usage, see README"
	exit();
with open("numbers.json") as number_file:									#open the list of numbers
	numList = json.load(number_file)
for number in numList:												#go through the list of numbers
	sendMessage(number)											#calls method to send a fact to that number
	time.sleep(3)												#wait for 3 seconds to send the next
