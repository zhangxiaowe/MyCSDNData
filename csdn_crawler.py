import datetime
import requests
import bs4

url = 'https://blog.csdn.net/qq_34035956'
headers = { 
    'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36(KHTHL, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
}

-- test start
requests.get('https://blog.csdn.net/qq_34035956/article/details/127485638', headers=headers)
requests.get('https://blog.csdn.net/qq_34035956/article/details/127622414', headers=headers)
requests.get('https://blog.csdn.net/qq_34035956/article/details/106072568', headers=headers)
requests.get('https://blog.csdn.net/qq_34035956/article/details/127623802', headers=headers)
requests.get('https://blog.csdn.net/qq_34035956/article/details/104053265', headers=headers)
requests.get('https://blog.csdn.net/qq_34035956/article/details/109255357', headers=headers)
requests.get('https://blog.csdn.net/qq_34035956/article/details/104036671', headers=headers)
requests.get('https://blog.csdn.net/qq_34035956/article/details/118550011', headers=headers)

headers1 = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
}
html_file = requests.get('https://blog.csdn.net/qq_34035956?type=blog', headers=headers1)
obj_soup = bs4.BeautifulSoup(html_file.text, 'lxml')
result = []
for link in obj_soup.find_all('a'):  # 遍历网页中所有的超链接（a标签）
    result.append("{}".format(link.get('href')))

for link in result:
    if link.find('category_') != -1:
        requests.get(link, headers=headers1)
        
-- test end

html_file = requests.get(url, headers=headers)
obj_soup = bs4.BeautifulSoup(html_file.text, 'lxml')

result = []
names = obj_soup.select('div .user-profile-statistics-name')
numbers = obj_soup.select('div .user-profile-statistics-num')
for i in range(len(numbers)):
  result.append("{}: {}".format(names[i].text, numbers[i].text))

now_time = datetime.datetime.now()
year = now_time.year
month = now_time.month
day = now_time.day

output = "\n{}_{}_{}\t {}".format(year, month, day, result)
with open("./csdndata/csdn_data.txt", mode="a") as f:
  f.write(output)
