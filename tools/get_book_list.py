# 我读完的书单放到自己blog里了，
# 爬下来进行一些分析
# 为什么自己爬自己写的东西啊？
# 因为水平有限
import requests
from bs4 import BeautifulSoup

url = 'http://www.guofei.site/{year}/01/01/Book-List-{year}.html'
# url = 'http://127.0.0.1:4006/{year}/01/01/Book-List-{year}.html'


def get_one_year_books(year):
    one_year_books = []
    r = requests.get(url.format(year=year))
    soup = BeautifulSoup(r.text, 'lxml')
    book_list_year = soup.find_all(name='div', attrs={'class': 'col-md-12'})
    for book in book_list_year:
        book_detail = book.table.tbody.tr.find_all(name='td')
        one_year_books.append([book_detail[1].string, book_detail[3].string])
    return one_year_books


years = [2013, 2014, 2015, 2016, 2017, 2018, 2019]
all_books = []
for year in years:
    all_books.extend(get_one_year_books(year))

#%%
all_books_md=''

for year in years:
    tmp_one_year_books=get_one_year_books(year)
    all_books_md+='- {year}年（共读完{count_book}本）'.\
        format(year=year,count_book=len(tmp_one_year_books))+'\n'
    for book in tmp_one_year_books:
        all_books_md+='    - '+book[0]+'\t'+book[1]+'\n'

print(all_books_md)

#%%
# 分析最近的读书情况
import pandas as pd
import datetime
import numpy as np
import matplotlib.pyplot as plt

pd_all_books=pd.DataFrame(all_books,columns=['book','date'])
pd_all_books=pd_all_books.transform({'book':lambda x:x,'date':lambda x:datetime.datetime.strptime(x,'%Y年%m月%d日')})
pd_all_books=pd_all_books.sort_values(by='date',ascending=True)


pd_all_books['book_count']=1
pd_all_books=pd_all_books.loc[pd_all_books.date>datetime.datetime(year=2013,month=1,day=1),:]
plt.plot(pd_all_books.date,np.cumsum(pd_all_books.book_count),'.')
plt.show()
#%%

pd_rolling=pd_all_books.loc[:,['date','book_count']].set_index('date').resample('D').sum().rolling(window=120).sum()
pd_rolling=pd_rolling/120
pd_rolling.plot()

plt.show()
