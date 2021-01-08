
'''This is a simple program to scrape paytm mall and save the data of chocolates of page-1 only in HTML'''



from bs4 import BeautifulSoup
import requests

r=requests.get('https://paytmmall.com/shop/search?q=chocolates&from=organic&child_site_id=6&site_id=2&category=101449&page=1&latitude=32.1820774&longitude=76.3448772')
html_content=r.content
soup=BeautifulSoup(html_content,'html.parser')



boiler='''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chocalate Data From Paytm Mall</title>
</head>
<style>th,td{border: 1px solid red;}
th{background-color: green;}</style>
<body>
    <h1 style="text-align: center;">Data Scraped from Paytm Mall</h1>
   <table style="border: 2px rgba(228, 195, 9, 0.836) solid;">
       <tr>
           <th>Product </th><th>Name</th><th>Price</th>
        </tr>'''
f=open('scraped_data.html','a+')
f.write(boiler+'\n')


products_all_block=soup.find('div',class_='_3RA-')
product_lines=products_all_block.find_all('div',class_='_1fje')
for product_line in product_lines:
    products=product_line.find_all('div',class_='_2i1r')
    for prod in products:
        prod_name=prod.div.a['title']
        prod_img=prod.div.a.find('div',class_='_3nWP').img['src']
        prod_price=prod.div.a.find('div',class_='_1kMS').span.text
        prod_url='https://paytmmall.com'+prod.div.a['href']
        tr_adder=f'''<tr>
            <td><img src="{prod_img}" alt="{prod_name}" width="154" height="123"></td>
            <td><a href="{prod_url}" target="_blank">{prod_name}</a> </td>
            <td>Rs {prod_price}</td>
        </tr> '''
        f.write(tr_adder+'\n')
closer='''   </table>
</body>
</html>'''
f.write(closer)
f.close()
       
