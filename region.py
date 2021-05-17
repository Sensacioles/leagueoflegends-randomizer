import requests
import json

#Displays the list of all available languages
response = requests.get('https://ddragon.leagueoflegends.com/cdn/languages.json')
regions = json.loads(response.text)
index = 0
for index in range(index,len(regions),3):
    print(f'{index} = {regions[index]}    {index+1} = {regions[index+1]}    {index+2} = {regions[index+2]}')

#Set language to the input from the user
def setRegion():
    userRegion = int(input('Choose your language/region: '))
    return regions[userRegion]
