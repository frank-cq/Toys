# sudo apt install python-lxml,python-requests

from lxml import html
import requests

urlPrefix = 'https://book.douban.com/subject/'
candidateBookNums = []
candidateBookNums.append('3633461')

selectedBooks = {}
# i = 1

while candidateBookNums:

	bookNum = candidateBookNums.pop(0)
	bookUrl = urlPrefix + str(bookNum)

	# 获取网页
	page = requests.get(bookUrl)

	# 将网页格式化为树型
	tree = html.fromstring(page.text)

	# 书籍名称
	bookName = tree.xpath('//title/text()')
	# 平均分
	rating_num = tree.xpath('//strong[@property="v:average"]/text()')[0]
	# 评分人数
	rating_people = tree.xpath('//a/span[@property="v:votes"]/text()')[0]

	if rating_num < 8 or rating_people < 800:
		continue

	stars = tree.xpath('//span[@class="rating_per"]/text()')
	# 5星评价比例
	stars5 = stars[0]
	# 4星评价比例
	stars4 = stars[1]
	# 3星评价比例
	stars3 = stars[2]
	# 2星评价比例
	stars2 = stars[3]
	# 1星评价比例
	stars1 = stars[4]
	# 豆瓣读书中指向其他书的链接
	links = tree.xpath('//div[@class="content clearfix"]/dl/dd/a/@href')

	# 去掉空白符，如回车、换行、空格、缩进
	bookName = bookName[0].strip()

	# 整理豆瓣上书籍的评分信息
	book = {
		'name':bookName,
		'score':rating_num,
		'rating_people':rating_people,
		'stars5':stars5,
		'stars4':stars4,
		'stars3':stars3,
		'stars2':stars2,
		'stars1':stars1,   
	}
	selectedBooks[bookNum] = book
	print bookName,book

	for j in links:
		bookNum = j.split('/')[-2]
		if bookNum not in selectedBooks.keys() and bookNum not in candidateBookNums:
			candidateBookNums.append(bookNum)

	# i += 1
	# if i > 100:
	# 	break

print selectedBooks
