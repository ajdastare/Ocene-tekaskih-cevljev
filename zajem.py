import re
import csv
import requests

link = 'https://runrepeat.com/ranking/rankings-of-running-shoes'
# mapa, v katero bomo shranili podatke
shoe_directory= 'shoes'
# ime datoteke v katero bomo shranili glavno stran
frontpage_filename = 'shoes_1.html'
# ime CSV datoteke v katero bomo shranili podatke
csv_filename = 'shoes_data.csv'

def download_url_to_string(url):
    '''This function takes a URL as argument and tries to download it
    using requests. Upon success, it returns the page contents as string.'''
    try:
        # del kode, ki morda sproži napako
        r = requests.get(url)
    except requests.exceptions.ConnectionError:
            # koda, ki se izvede pri napaki
        # dovolj je če izpišemo opozorilo in prekinemo izvajanje funkcije
        return print('stran ne obstaja!')
    # nadaljujemo s kodo če ni prišlo do napake
    return r.text
    
test = download_url_to_string(link)

#vrne kot string shrnajeno v text
#save_string_to file pa shrani v text v file 

def save_string_to_file(text, directory, filename):
    '''Write "text" to the file "filename" located in directory "directory",
    creating "directory" if necessary. If "directory" is the empty string, use
    the current directory.'''
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, filename)
    with open(path, 'w', encoding='utf-8') as file_out:
        file_out.write(text)
    return None


with open('shoes') as mapa: 
    with open('shoes_1.html') as datoteka2:
        vsebina = datoteka2.read()

def vsebina_datoteke(ime_datoteke):
    with open(ime_datoteke, encoding = 'utf-8') as datoteka: 
        return datoteka.read()
def pripravi_imenik(ime_datoteke):
    '''Če še ne obstaja, pripravi prazen imenik za dano datoteko.'''
    imenik = os.path.dirname(ime_datoteke)
    if imenik:
        os.makedirs(imenik, exist_ok=True)

vzorec = r'<span class="text-ellipsis" itemprop="name">(?P<ime>.*?)</span>'
vzorec2 = r'<div class="hidden-xs hidden-sm count-reviews">(?P<stevilo>.*?)</div>'
#ocena in št.review
vzorec3 =r'title="">(?P<ocena>.*?)</div>.*?<div class="hidden-xs hidden-sm count-reviews">(?P<stevilo>.*?)</div>'
#Ocena
vzorec4 = r'title="">(?P<ocena>.*?)</div>'

#ime, ocena, št.review
celotni_vzorec = re.compile(r'<span class="text-ellipsis" itemprop="name">(?P<ime>.*?)</span>.*?'
    r'(\n.*?){27}'
    r'title="">(?P<ocena>\d{2})</div>(\n.*?)<div class="hidden-xs hidden-sm count-reviews">(?P<review>\d*?) reviews</div>',re.DOTALL
    )

#SLEDNJE JE ZAKODIRANO, SAJ JE SAMO POSTOPEK KI SEM GA UPORABILA, DA SEM PRIŠLA DO PRAVILNEGA REGULARNEGA IZRAZA ZA celotni_vzorec
# i = 0
# # vrne imena
# for ujemanje in re.finditer(vzorec,vsebina):
#     print(ujemanje.group(1))
#     i +=1
# print(i)
# i = 0
# # št. review
# for ujemanje in re.finditer(vzorec2,vsebina):
#     print(ujemanje.group(1))
#     i += 1
# print(i)
# i = 0
# #povprecna ocena
# for ujemanje in re.finditer(vzorec4,vsebina):
#     print(ujemanje.group(1))
#     i +=1
# print(i) 
# i = 0


for ujemanje in re.finditer(celotni_vzorec,vsebina):
    print(ujemanje.groupdict())
    i += 1
    print(i)
print(i)

#za prvo stran, naredi 'data_page1.csv in v datoteko napiše ime, oceno in review
with open('data_page1.csv', 'w') as datoteka:
    writer = csv.DictWriter(datoteka,['ime', 'ocena','review'])
    writer.writeheader()
    for ujemanje in celotni_vzorec.finditer(vsebina):
        writer.writerow(ujemanje.groupdict())


def zapisi_csv(slovarji, imena_polj, ime_datoteke):
    '''Iz seznama slovarjev ustvari CSV datoteko z glavo.'''
    pripravi_imenik(ime_datoteke)
    with open(ime_datoteke, 'w', encoding='utf-8') as csv_datoteka:
        writer = csv.DictWriter(csv_datoteka, fieldnames=imena_polj)
        writer.writeheader()
        for slovar in slovarji:
            writer.writerow(slovar)




https://runrepeat.com/ranking/rankings-of-running-shoes?page=2

#Zajela bom 10 strani tako da bo skupaj 300 modelov cevljev

for i in range(1, 11):
    url = ('https://runrepeat.com/ranking/rankings-of-running-shoes?page={}').format(i)
    test = download_url_to_string(url)
    save_string_to_file(test,'zajeti_podatki','shoes-{}.html'.format(i))


podatki_cevljev = []

for i in range(1, 11):
    vsebina = vsebina_datoteke(
        'zajeti_podatki/shoes-{}.html'.format(i))
    for ujemanje in celotni_vzorec.finditer(vsebina):
        podatki_cevljev.append(ujemanje.groupdict())

zapisi_csv(podatki_cevljev,['ime', 'ocena','review'], 'obdelani-podatki/vsi-cevlji.csv')
