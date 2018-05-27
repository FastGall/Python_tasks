import xlrd, xlwt
import matplotlib.pyplot as plt
#Open xls
print("print xls-file name")
name_xls = str(input())
rb = xlrd.open_workbook(name_xls,formatting_info=True)

#active page
sheet = rb.sheet_by_index(0)

day_list = []
index_day = []
index_day.append(1)
day_list.append(sheet.row_values(2)[0])
for i in range(sheet.nrows):
    if((sheet.row_values(i)[0] not in day_list) and sheet.row_values(i)[0] != 'Date'):
        index_day.append(i)
        day_list.append(sheet.row_values(i)[0])
index_day.append(sheet.nrows)

j = 0
k = 1
n = index_day[j]
m = index_day[k]

x = []
labels = []

city = [[] for i in range(len(day_list))]
city_values = [[] for i in range(len(day_list))]
countries = [[] for i in range(len(day_list))]
gender = [[] for i in range(len(day_list))]
age = [[] for i in range(len(day_list))]

while(1):
    for i in range(n,m):
        if(sheet.row_values(i)[1] == 'cities'):
            city[j].append(sheet.row_values(i)[2])
            city_values[j].append(int(sheet.row_values(i)[4]))
            if(sheet.row_values(i)[2] not in labels):
                labels.append(sheet.row_values(i)[2])
                x.append(int(sheet.row_values(i)[4]))
            else:
                for z in range(len(labels)):
                    if(labels[z] == sheet.row_values(i)[2]):
                        x[z] = int(x[z]) + int(sheet.row_values(i)[4])
        if(sheet.row_values(i)[1] == 'countries'):
            countries[j].append(sheet.row_values(i)[2])
        if(sheet.row_values(i)[1] == 'gender_age'):
            gender[j].append(sheet.row_values(i)[2])
            age[j].append(sheet.row_values(i)[3])
    if(m == sheet.nrows):
        break
    j += 1
    k += 1
    n = index_day[j]
    m = index_day[k]

"""
for i in range(len(day_list)):
    print("|", *day_list[i], " ", *city[i]," - ",*city_values[i] , *countries[i], 
    *gender[i], *age[i],"|\n")
"""


plt.figure(figsize=(15,10))

explode = [0 for i in range(len(labels))]

plt.subplot(aspect=True)
plt.pie(x, labels = labels, explode = explode, autopct = '%.2f%%', shadow=False);
plt.title("City statistic")

plt.show()
        
        
