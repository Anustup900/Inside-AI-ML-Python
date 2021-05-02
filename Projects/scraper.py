import requests 
import bs4

from bs4 import BeautifulSoup


url = 'https://finance.yahoo.com/quote/AMZN?p=AMZN&.tsrc=fin-srch'


#new_url = 'https://coronabeds.jantasamvad.org/'

page = requests.get(url)

bs_soup = BeautifulSoup(page.content, "html.parser")

amazon_price = bs_soup.find_all('div', {'class' : 'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').get_text()
# > siome radom < 
print(amazon_price)




# bs_table = soup.find("table", {"weaeathe"})
bs_table_column = bs_table.findAll('td')