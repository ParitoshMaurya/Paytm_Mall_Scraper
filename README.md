# Paytm Mall Scraper
In this project, I have scraped the data of chocolates from PayTM Mall. I have scraped the 1st page only `https://paytmmall.com/shop/search?q=chocolates&from=organic&child_site_id=6&site_id=2&category=101449&page=1&latitude=32.1820774&longitude=76.3448772` and created a html file `scraped_data.html` which will show the scraped data in table format.


## Requirements

### BeautifulSoup

Beautiful Soup is a Python package for parsing HTML and XML documents. It creates a parse tree for parsed pages that can be used to extract data from HTML, which is useful for web scraping. If you're using Linux based OS, you can install BeautifulSoup using following command in terminal.

Here, pip is a package-management system used to install and manage software packages written in Python.

```
sudo apt-get update && sudo apt-get install python3-pip
pip3 install beautifulsoup4
```

### Requests Library

Requests is an Apache2 Licensed HTTP library, written in Python. Requests will allow you to send HTTP/1.1 requests using Python.
You can install requests library using following code in your terminal in Linux.

`pip3 install requests`

After finishing installation process above, you can run the tasks, using `python3 paytmmall.py` and you will get an HTML file `scraped_data.html` in which scraped data is stored.
