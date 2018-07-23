from bs4 import BeautifulSoup
import requests
from xlsxwriter import Workbook

workbook = Workbook('Smart_Watches.xlsx')

worksheet = workbook.add_worksheet()

worksheet.write(0,0,'Title')
worksheet.write(0,1,'Price')
worksheet.write(0,2,'image1')
worksheet.write(0,3,'image2')
worksheet.write(0,4,'image3')
worksheet.write(0,5,'image4')
worksheet.write(0,6,'color')
worksheet.write(0,7,'Description')
worksheet.write(0,8,'URL')

mylink = []
my_url = []
p=1
while p<=2:
	page = requests.get("https://www.crov.com/category/smart-watches_qGVCveDYhPbL_" + str(p) + ".html")
	soup = BeautifulSoup(page.text, 'html.parser')

	items = soup.find_all('a',{'class': 'products-link'})
	for item in items:
		product = item["href"]
		mylink.append(product)
	p +=p
for i in mylink:
	page_data = requests.get(i)
	page_soup = BeautifulSoup(page_data.text, 'html.parser')

	try:
		color_variations = page_soup.find('div',{'class': 'prod-select for-pc J-prodSelect'}).find_all('a')
		for data in color_variations:
			url = data["href"]
			my_url.append(url)
	except:
		my_url.append(i)

row=1
for x in my_url:
	mypage = requests.get(x)
	mysoup = BeautifulSoup(mypage.text, 'html.parser')

	try:
		title = mysoup.find('h1',{'class': 'prod-name'}).span.text.strip()
		#print(title)
		worksheet.write(row,0,title)
	except:
		pass		
	try:
		price = mysoup.find('span',{'class': 'J-price'}).text.strip().replace('US$','')
		#print(price)
		worksheet.write(row,1,price)
	except:
		pass		
	try:
		image1_raw = mysoup.find("ul", {"class": "thumb-list J-slider-controls"}).find_next("li").div.div.img["src"].replace('pd4','pd')
		image1 = "https:" + image1_raw
		#print(image1)
		worksheet.write(row,2,image1)	
	except:
		pass		
	try:
		image2_raw = mysoup.find("ul", {"class": "thumb-list J-slider-controls"}).find_next("li").find_next("li").div.div.img["src"].replace('pd4','pd')
		image2 = "https:" + image2_raw
		#print(image2_raw)
		worksheet.write(row,3,image2)	
	except:
		pass		
	try:
		image3_raw = mysoup.find("ul", {"class": "thumb-list J-slider-controls"}).find_next("li").find_next("li").find_next("li").div.div.img["src"].replace('pd4','pd')
		image3 = "https:" + image3_raw
		#print(image3)	
		worksheet.write(row,4,image3)
	except:
		pass		
	try:
		image4_raw = mysoup.find("ul", {"class": "thumb-list J-slider-controls"}).find_next("li").find_next("li").find_next("li").find_next("li").div.div.img["src"].replace('pd4','pd')
		image4 = "https:" + image4_raw
		#print(image4)
		worksheet.write(row,5,image4)
	except:
		pass		
	try:
		color = mysoup.find('div', {'class': 'attr-inner'}).text.strip()
		#print(color)
		worksheet.write(row,6,color)
	except:
		pass		
	try:
		Description = mysoup.find("div", {"class":"detail-p rich-text J-richTextBox"}).p.text
		#print(Description)
		worksheet.write(row,7,Description)
	except:
		pass		
	
	worksheet.write(row,8,x)
	row = row+1
workbook.close()

	