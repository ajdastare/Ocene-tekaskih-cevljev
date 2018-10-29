import re

#datoteko odperemo kot niz
with open('shoes_data_grid') as datoteka: 
    with open('page1_grid.html') as datoteka2:
        vsebina = datoteka2.read()
i = 0
vzorec = r'<span class="text-ellipsis" itemprop="name">(.*?)</span>'

for ujemanje in re.finditer(vzorec,vsebina):
    print(ujemanje.group(1))
    i +=1
print(i)

with open('podatki3.csv','w') as csv:
    print('model', file = csv)
    for ujemanje in re.finditer(vzorec,vsebina, re.DOTALL):
        print(''ujemanje.group(1), file = csv)
