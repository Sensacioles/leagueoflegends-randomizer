from champions import getRandomChamp
from lane import getRandomLane
from build import getRandomBuild

output = f'''\nChampion: {getRandomChamp()}
Lane: {getRandomLane()}
Build: {getRandomBuild()}
'''
print(output)