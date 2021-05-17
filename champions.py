import requests
import json
from random import choice
from patch import getLastPatch
from region import setRegion

#Create a list of all champions of the last released patch
#with their respective names in the user's language
userRegion = setRegion()
lastPatch = getLastPatch()
url = f'http://ddragon.leagueoflegends.com/cdn/{lastPatch}/data/{userRegion}/champion.json'
response = requests.get(url)
champion = json.loads(response.text)
data = champion['data']
nameslst = list(data)

#Return random champion if user is using en_US,
#else, get the champion's name in the user's language
#as there are champions with different names in certain regions
def getRandomChamp():
    randomChamp = choice(nameslst)
    if userRegion == 'en_US':
        return randomChamp
    else:
        champKey = data.get(randomChamp)
        champName = champKey['name']
        return champName
