import pandas as pd
people = pd.read_excel('C:/Users/Administrator/Desktop/People.xlsx',header=1)
# print(people.shape)
# print(people.columns)
# print(people.head(3))
# print('===================')
# print(people.tail(1))
# print(people.columns)
# people.to_excel('C:/Users/Administrator/Desktop/output2.xlsx')
s1 = pd.Series([1,2,3],index=['1','2','3'],name='Apple')
s2 = pd.Series([10,20,30],index=['1','2','3'],name='Banana')
s3 = pd.Series([100,200,300],index=['4','6','11111'],name='Cup')
df = pd.DataFrame({s1.name:s1,s2.name:s2,s3.name:s3}) # dict 形式添加到dataframe中去
# df.to_excel('C:/Users/Administrator/Desktop/output2.xlsx')
df = pd.DataFrame([s1,s2,s3])# list形式，添加到dataframe中去

print(df.index)