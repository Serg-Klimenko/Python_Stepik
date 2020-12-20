# 3.5.2
# В этой задаче вам необходимо воспользоваться API сайта artsy.net
# API проекта Artsy предоставляет информацию о некоторых деятелях искусства, их работах, выставках.
# В рамках данной задачи вам понадобятся сведения о деятелях искусства (назовем их, условно,
# художники).
# Вам даны идентификаторы художников в базе Artsy.
# Для каждого идентификатора получите информацию о имени художника и годе рождения.
# Выведите имена художников в порядке неубывания года рождения. В случае если у художников
# одинаковый год рождения, выведите их имена в лексикографическом порядке.
# Работа с API Artsy
import requests
import json

client_id = 'b76f622aed499ee50888'
client_secret = 'fe66c4757f724c085b7cf14605dc106a'

# инициируем запрос на получение токена
r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })
# разбираем ответ сервера
j = json.loads(r.text)
# достаем токен
token = j["token"]
# создаем заголовок, содержащий наш токен
headers = {"X-Xapp-Token": token}
artists = {}
with open("dataset_3_5_2.txt", "r") as inf:
    for artist_id in inf:
        # инициируем запрос с заголовком
        res = requests.get(f"https://api.artsy.net/api/artists/{artist_id.strip()}",
                           headers=headers)
        # разбираем ответ сервера
        data = res.json()
        artists[data["sortable_name"]] = data["birthday"]
sorted_artists = sorted(artists.items(), key=lambda kv: kv[1])
for artist in sorted_artists:
    print(artist[0])


