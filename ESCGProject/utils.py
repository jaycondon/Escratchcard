from ESCGProject import app

#from ESCGProject.database import db_session, init_db
from ESCGProject.models import Card, Card_Detail, User

import random

import os

def getImages(isWinner,no_of_cards):
	imagelist = []
	finallist = []
	for f in os.listdir("ESCGProject/static/images"):
		imagelist.append(f)
		print(f)
	i = 0
	if isWinner==False:
		while(i < no_of_cards):
			image = imagelist[random.randrange(0, len(imagelist), 1)]
			if finallist.count(image)==2:
				pass
			else:
				finallist.append(image)
				i = i + 1
		print(finallist)
		return finallist
	else:
		win_image = imagelist[random.randrange(0, len(imagelist), 1)]
		i = 0
		while i < no_of_cards:
			if i < 3:
				finallist.append(win_image)
				i = i + 1
			else:
				image = imagelist[random.randrange(0, len(imagelist), 1)]
				if image == win_image:
					pass
				else:
					finallist.append(image)
					i = i + 1
		random.shuffle(finallist)
		print(finallist)
		return finallist
