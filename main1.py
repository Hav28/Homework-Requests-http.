import requests
import re
import operator

def test_request():
    url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json'
    response = requests.get(url)
    list = response.json()

    name = "Hulk, Captain America, Thanos"
    list_name = re.split(", ", name)
    name.split(",")
    heroes = {}
    for name in list_name:
        for id in list:
            if id['name'] == name:
                heroes[id['name']] = id['powerstats']['intelligence']

    best_super_heroes = {v:k for k, v in heroes.items()}
    sorted_super_heroes = sorted(heroes.items(), key=operator.itemgetter(1))
    list_super_heroes = dict(sorted_super_heroes)
    sorted_super_heroes_1 = {v: k for k, v in list_super_heroes.items()}
    max_intelligence = max(sorted_super_heroes_1)

    print(f'Самый умный супергерой: {sorted_super_heroes_1[max_intelligence]}, у него интеллект = {max_intelligence}')


if __name__ == '__main__':
    test_request()


