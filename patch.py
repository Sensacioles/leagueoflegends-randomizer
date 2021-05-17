import requests
import json

#Create a list of all versions(patches)
response = requests.get('https://ddragon.leagueoflegends.com/api/versions.json')
versions = json.loads(response.text)
patchlst = list(versions)

#Returns last released patch
def getLastPatch():
    return patchlst[0]
