# Input magic
print("print day value")
days = int(input())
print("print exam value")
exam = int(input())

koef_mass = [[] for i in range(exam)]

print("print s[i],d[i],c[i]. 1,3,1 - example")
for i in range(exam):
    koef_mass[i] = eval(input())

#Calculate

if(days < exam):
    print("-1")
    exit()

calendar = [0 for i in range(days)]

i = 1
need_days = 0
k = 0
while(i != exam + 1):
    if((koef_mass[k][0] + koef_mass[k][2]) <= koef_mass[k][1]):
        calendar[koef_mass[k][1] - 1] = exam + 1
        need_days = koef_mass[k][2]
        for j in range(koef_mass[k][1]):
            if(need_days == 0):
                    break
            if(calendar[j] == 0):
                calendar[j] = i
                need_days = need_days - 1
        if(need_days != 0):
            print(-1)
            exit()
    else:
        print(-1)    
        exit()
    i+=1
    k+=1
            
print(calendar) 