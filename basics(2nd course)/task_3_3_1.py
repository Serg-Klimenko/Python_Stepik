# 3.3.1 http-запросы, html-страницы и request
# Рассмотрим два HTML-документа A и B.
# Из A можно перейти в B за один переход, если в A есть ссылка на B, т. е. внутри A есть
# тег <a href="B">, возможно с дополнительными параметрами внутри тега.
# Из A можно перейти в B за два перехода если существует такой документ C, что из A в C можно
# перейти за один переход и из C в B можно перейти за один переход.
# Вашей программе на вход подаются две строки, содержащие url двух документов A и B.
# Выведите Yes, если из A в B можно перейти за два перехода, иначе выведите No.
# Обратите внимание на то, что не все ссылки внутри HTML документа могут вести на существующие
# HTML документы.
# https://stepic.org/media/attachments/lesson/24472/sample0.html
# https://stepic.org/media/attachments/lesson/24472/sample2.html
import requests
import re

url_a = input()
url_b = input()
res = requests.get(url_a)
result = 'No'
urls_from_c = re.findall(r'(?:<a href=")(.+)(?:">)', res.text)
for url in urls_from_c:
    tmp_res = requests.get(url)
    if tmp_res.status_code == 200 and url_b in tmp_res.text:
        result = 'Yes'
        break
print(result)
