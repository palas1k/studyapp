import pickle
import os, platform, logging
import pandas as excelfile
import datetime




f1 = excelfile.read_excel('studytime.xlsx')
while True:
    InsertTime = input("Введите время потраченое на учебу \n или 'sum' чтобы узнать сколько времени всего прошло: ")
    if InsertTime== 'sum':
#        print((f1.sum()//60) +'часов'+' '+(f1.sum()%60)+'минут')
        print(f1.sum())
        exit()
    else :
        try:
            int(InsertTime)
            break
        except:
            print('Надо ввести цифру')

f = excelfile.DataFrame.append(f1, {'Дата': datetime.date.today(),'Время учебы': InsertTime}, ignore_index=True)
with excelfile.ExcelWriter('studytime.xlsx', mode='w') as writer:
    f.to_excel(writer, index=False, )
#f1 = excelfile.read_excel('studytime.xlsx')
#print(f1.sum())


