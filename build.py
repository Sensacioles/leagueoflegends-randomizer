import requests
import json
from random import choice
from champions import lastPatch,userRegion

url = f'http://ddragon.leagueoflegends.com/cdn/{lastPatch}/data/{userRegion}/item.json'
response = requests.get(url)
item = json.loads(response.text)
data = item['data']

#Return random boot except the base ones
def getRandomBoot():
    bootlst = []
    for id in data:
        boot = data[id]
        if 'Boots' in boot['tags']:
            if boot.get('depth') == 2:
                bootlst.append(boot['name'])
    return choice(bootlst)

#Return random mythic item except Ornn's upgraded ones
def getRandomMythic():
    mythiclst = []
    for id in data: 
        mythic = data[id]
        if '<rarityMythic>' in mythic['description']:
            if mythic.get('requiredAlly') != 'Ornn':
                mythiclst.append(mythic['name'])
    return choice(mythiclst)

#Return random legendary item except support gold-based ones and Mejai
def getRandomLegendary():
    legendarylst = []
    for id in data:
        legendary = data[id]
        if '<rarityLegendary>' not in legendary['description']:
            if legendary.get('depth') == 3:
                legendarylst.append(legendary['name'])
    return choice(legendarylst)

#Return full random build
def getRandomBuild():
    buildlst = []
    buildlst.append(getRandomMythic())
    for slotIndex in range(1,5,1):
        buildlst.append(getRandomLegendary())
    buildlst.append(getRandomBoot())
    return buildlst
