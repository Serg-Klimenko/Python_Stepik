# 3.3.2 http-запросы, html-страницы и requests
# На вход подается ссылка на HTML файл.
# Вам необходимо скачать этот файл, затем найти в нем все ссылки вида <a ... href="..." ... >
# и вывести список сайтов, на которые есть ссылка.
# Сайтом в данной задаче будем называть имя домена вместе с именами поддоменов. То есть, это
# последовательность символов, которая следует сразу после символов протокола, если он есть,
# до символов порта или пути, если они есть, за исключением случаев с относительными ссылками вида
# <a href="../some_path/index.html">.
# Сайты следует выводить в алфавитном порядке.
import re
import requests

#url = input()
res = requests.get('http://pastebin.com/raw/7543p0ns')
text = (' <a href="www.ttttttt.com"/>1</a>\n'
        '<a href="ftp://mail.ru/distib" >1</a>\n'
        '<a href="../skip_relative_links">1</a>\n'
        '<a href="https://www.stepic.org/media/attachments/lesson/24472/sample1.html">1</a>\n'
        '<a href="http://stepic.org/media/attachments/lesson/24472/sample1.html">1</a>\n'
        '<a href="https://www.testt.com/resource/">1</a>\n'
        '<a href="https://mobile.testt.com/app-news.html?utm_medium=ref&utm_campaign=footer_mainpage#"/>1</a>\n'
        '<a href="http://www.cnews.ru/cgi-bin/redirect.cgi?http://gift.cnews.ru">\n'
        '<a title=test download="http://test.com"; href="test.com" class="my test" style=>\n'
        '<a href=\'http://neerc.ifmo-2.ru:1345\'>\n'
        '<a href="http://www.cnews1.ru/cgi-bin/redirect.cgi?http://gift.cnews.ru">\n'
        '<a href="http://turbo.ru/">Turbo.ru</a>\n'
        '<a href="http://drinktime.ru">DrinkTime.ru</a>\n'
        '<a href="http://www.memori.ru/link/" class="nav_memori" '
        'onclick="location.href=\'http://memori.ru/link/?sm=1&u_data[url]=\'+encodeURIComponent('
        'document.location.href)+\'&u_data[name]=\'+encodeURIComponent(\'РосБизнесКонсалтинг\');return false;" '
        'title="в мемори">в мемори</a>\n '
        '<a href="http://www.liveinternet.ru/click" target=_blank><img '
        'src="http://pics.rbc.ru/img/ver99/counter_liveinternet.gif" border=0 width=31 height=31 '
        'title="liveinternet.ru"></a>\n '
        '<a href="http://this-site.com/"></a>\n')
urls = re.findall(r'(?:<a.*href[\s=]*["\']\w*:\/\/)(\w[-_.\w\d]+\.\w*)', text)
for url in sorted(set(urls)):
    print(url)
