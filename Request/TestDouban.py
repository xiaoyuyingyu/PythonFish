import requests
from bs4 import BeautifulSoup

#请求网页,lxml是解析器
resp = requests.get('https://book.douban.com/top250?start=0')
soup = BeautifulSoup(resp.text,'lxml')


#书名
alldiv = soup.find_all('div', class_='pl2')
names = [a.find('a')['title'] for a in alldiv]
#print(names)




#作者

allp = soup.find_all('p', class_='pl')
authors = [p.get_text() for p in allp]
#print(authors)


#分数
starspan = soup.find_all('span', class_='rating_nums')
scores = [s.get_text() for s in starspan]
#print(scores)



#简介
sumspan = soup.find_all('span', class_='inq')
sums = [i.get_text() for i in sumspan]
#print(sums)

filename = '豆瓣图书Top250.txt'
f = open(filename, 'w', encoding='utf-8')


for name, author, score, sum in zip(names, authors, scores, sums):
    name = '书名：' + str(name) + '\n'
    author = '作者：' + str(author) + '\n'
    score = '评分：' + str(score) + '\n'
    sum = '简介：' + str(sum) + '\n'
    data = name + author + score + sum
    # 保存数据
    f.writelines(data + '==============888========='+'\n')

print('保存成功')


# 文件名

filename = '豆瓣图书Top250.txt'
# 保存文件操作
#with open(filename, 'w', encoding='utf-8') as f:
    # 保存数据
#f = open(filename, 'w', encoding='utf-8')
#f.writelines(data + '==============888========='+'\n' )

