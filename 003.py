import pandas as pd
from datetime import date,timedelta

def add_month(d,md):
    yd = md // 12 # 对年份整除，逢12加1
    m = d.month + md % 12 # 对月份取余；此处每月份加1
    if m != 12: # 考虑到初始给定的月份不一定为1月时，需要进行条件判断，使得月份不大于12
        yd += m // 12
        m = m%12
    return date(d.year + yd,m,d.day)

books = pd.read_excel('C:/Users/Administrator/Desktop/Books (1).xlsx',skiprows=3,usecols='C:F',index_col=None,dtype={'ID':str,'InStore':str,'Date':str})# skiprows 忽略读取前三行，usecols选择C列到F列，dtype强制转换类型为str
date_start = date(2021,12,4)

# print(books.index)
for i in books.index:
    books.at[i,'ID'] = i + 1
    # books['ID'].at[i] = i + 1
    books.at[i,'InStore'] = 'Yes' if i % 2 == 0 else 'No'
    # books['Date'].at[i] = date_start + timedelta(days=i)# 加日期，步进为1
    # books['Date'].at[i] = date(date_start.year + i,date_start.month ,date_start.day)
    books.at[i,'Date'] = add_month(date_start,i)

print(books)
books.set_index('ID',inplace=True)
books.to_excel('C:/Users/Administrator/Desktop/date_change.xlsx')
# print(books['ID']) # float64
# print(type(books['ID'])) # Series 类型