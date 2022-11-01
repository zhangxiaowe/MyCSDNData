import datetime
import requests
import bs4

url = 'https://blog.csdn.net/qq_34035956'
headers = { 
    'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36(KHTHL, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
}

# test start
headers0 = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36(KHTHL, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
}
headers1 = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
}

url0 = 'https://blog.csdn.net/qq_34035956?type=blog'
html_file0 = requests.get(url0, headers=headers0)
obj_soup0 = bs4.BeautifulSoup(html_file0.text, 'lxml')
for link in obj_soup0.find_all('a'):  # 遍历网页中所有的超链接（a标签）
    value0 = "{}".format(link.get('href'))
    if value0.find('category_') != -1:
        html_file1 = requests.get(value0, headers=headers0)
        obj_soup1 = bs4.BeautifulSoup(html_file1.text, 'lxml')
        for link1 in obj_soup1.find_all('a'):
            value1 = "{}".format(link1.get('href'))
            if value1.find('qq_34035956/article') != -1 & value1.find("comments") == -1:
                requests.get(value1, headers=headers0)
#                 requests.get(value1, headers=headers1)
        
# test end

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
