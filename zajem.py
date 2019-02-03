import csv
import json
import os
import re
import sys
import pandas


import requests


url = 'https://runrepeat.com/ranking/rankings-of-running-shoes'

shoe_directory= 'shoes'
frontpage_filename = 'shoes_1.html'
csv_filename = 'shoes_data.csv'


def pripravi_imenik(ime_datoteke):
    '''Če še ne obstaja, pripravi prazen imenik za dano datoteko.'''
    imenik = os.path.dirname(ime_datoteke)
    if imenik:
        os.makedirs(imenik, exist_ok=True)


def shrani_spletno_stran(url, ime_datoteke, vsili_prenos=False):
    '''Vsebino strani na danem naslovu shrani v datoteko z danim imenom.'''
    try:
        print('Shranjujem {} ...'.format(url), end='')
        sys.stdout.flush()
        if os.path.isfile(ime_datoteke) and not vsili_prenos:
            print('shranjeno že od prej!')
            return
        r = requests.get(url)
    except requests.exceptions.ConnectionError:
        print('stran ne obstaja!')
    else:
        pripravi_imenik(ime_datoteke)
        with open(ime_datoteke, 'w', encoding='utf-8') as datoteka:
            datoteka.write(r.text)
            print('shranjeno!')


def vsebina_datoteke(ime_datoteke):
    '''Vrne niz z vsebino datoteke z danim imenom.'''
    with open(ime_datoteke, encoding='utf-8') as datoteka:
        return datoteka.read()


def zapisi_csv(slovarji, imena_polj, ime_datoteke):
    '''Iz seznama slovarjev ustvari CSV datoteko z glavo.'''
    pripravi_imenik(ime_datoteke)
    with open(ime_datoteke, 'w', encoding='utf-8') as csv_datoteka:
        writer = csv.DictWriter(csv_datoteka, fieldnames=imena_polj)
        writer.writeheader()
        for slovar in slovarji:
            writer.writerow(slovar)


def zapisi_json(objekt, ime_datoteke):
    '''Iz danega objekta ustvari JSON datoteko.'''
    pripravi_imenik(ime_datoteke)
    with open(ime_datoteke, 'w', encoding='utf-8') as json_datoteka:
        json.dump(objekt, json_datoteka, indent=4, ensure_ascii=False)
# s tem vzorcem bom našla linke posameznih modelov
vzorec1 = re.compile(r'<a href="(?P<link>.*?)".*?target="_self">')
# na vsakem linku za model bom zajela podatke:
vzorec2 = re.compile(
    r'<h1 class="p-name main-shoe-title"><span>(?P<model>.*?)</span></h1>.*?'
    r'<h3 id="user_reviews" class="text-left my_rating_title">User ratings</h3>\n.*?<p>(?P<ocena>.*?) / 5 based on (?P<stevilo_ocen>.*?) ratings</p>.*?'
    r'<span class="offer_list_price">(?P<cena>.*?)</span>.*?'
    r'<div id="terrain-description" class="hide"><h4>(?P<teren>.*?)</h4>.*?'
    r'<div><span class="rank-text">Top  1% overall</span></div>\n.*?<div><span class="top-list">Best running shoes</span></div>\n.*?\n.*?\n.*?\n.*?\n.*?\n.*?\n.*?\n.*?\n.*?\n.*?<div><span class="rank-text">Top  1% (?P<znamka>.*?)</span></div>\n.*?<div><span class="top-list">Best (?P<znamka_drugic>.*?) running shoes</span></div>'

)


def nalozi_strani():
    for i in range(0, 33):
        url = ('https://runrepeat.com/ranking/rankings-of-running-shoes?page={}').format(i)
        shrani_spletno_stran(url, 'zajeti-podatki/stran-{}.html'.format(i))
    print('Shranjeno')

#zajela bom vse strani različnih modelov, na straneh je link ki navigira do strani posameznega modela

podatki_filmov = []
def ujemanje_linki(vzorec):
    for i in range(1, 33):
        vsebina = vsebina_datoteke('zajeti-podatki/stran-{}.html'.format(i))
        for ujemanje_modela in vzorec.finditer(vsebina):
            podatki_filmov.append(ujemanje_modela.group(1))
    return podatki_filmov

# vsak link do modela, bom shranila v mapo modeli - tu so podatki posameznega modela

def zapisi_stran(podatki):
    for i in range(0,len(podatki)):
        shrani_spletno_stran(podatki[i],'modeli/model-{}.html'.format(i))
    print('Done')


#regularni izraz, ki bo nasel ceno modela
vzorec_cena = re.compile(r'<span class="offer_list_price">(?P<cena>.*?)</span>', flags=re.DOTALL)
#izraz, ki bo nasel teren
vzorec_teren = re.compile(r'<div id="terrain-description" class="hide"><h4>(?P<teren>.*?)</h4>')
#izraz, ki najde znamko
# znamka= re.compile(r'<div><span class="rank-text">Top  1% overall</span></div>\n.*?<div><span class="top-list">Best running shoes</span></div>\n.*?\n.*?\n.*?\n.*?\n.*?\n.*?\n.*?\n.*?\n.*?\n.*?<div><span class="rank-text">Top  1% (?P<znamka>.*?)</span></div>\n.*?<div><span class="top-list">Best (?P<znamka_drugic>.*?) running shoes</span></div>')
#izraz, ki najde ime modela 
ime_modela = re.compile(r'<h1 class="p-name main-shoe-title"><span>(?P<model>.*?)</span></h1>')
#izraz, ki najde oceno modela in stevilo ozen
ocena_in_st = re.compile(r'<h3 id="user_reviews" class="text-left my_rating_title">User ratings</h3>\n.*?<p>(?P<ocena>.*?) / 5 based on (?P<stevilo_ocen>.*?) ratings</p>.*?',
    flags=re.DOTALL
    )


znamka_preko_linka = re.compile(r'<img src="(?P<karkoli>.*?)" alt="(?P<znamka>.*?) brand logo">')

podatki57 = {}
vsebina2 = vsebina_datoteke('modeli/model-957.html')
for ujemanje3 in ocena_in_st.finditer(vsebina2):
    test = ujemanje3.groupdict(1)
    test2 = test['ocena']
    podatki57['neki']  = test2

    
def izloci_podatke_modela(vsebina):
    podatki = {}
    for ujemanje3 in znamka_preko_linka.finditer(vsebina):
        test3 = ujemanje3.groupdict(1)
        del test3['karkoli']
        podatki['znamka'] = str(test3['znamka'])
    
    for ujemanje4 in ime_modela.finditer(vsebina):
        test4 = ujemanje4.groupdict(1)
        podatki['model'] = str(test4['model'])
    
    for ujemanje2 in vzorec_teren.finditer(vsebina):
        test2 = ujemanje2.groupdict(1)
        podatki['teren'] = str(test2['teren'])
    
    ujemanje1 = vzorec_cena.search(vsebina)
    if ujemanje1:
        podatki['cena'] = int(str(ujemanje1['cena']).strip('€'))
    else:
        podatki['cena'] = None
    
    ujemanje5 = ocena_in_st.search(vsebina)
    if ujemanje5:
        podatki['ocena'] = str(ujemanje5['ocena'])
        podatki['stevilo ocen'] = str(ujemanje5['stevilo_ocen'])
            # test5 = ujemanje5.groupdict(1)
            # podatki['ocena'] = float(test5['ocena'])
            # podatki['stevilo ocen'] = int(test5['stevilo_ocen'])
    else:
        podatki['ocena']= None
        podatki['stevilo ocen'] = None
    
    return podatki



podatki_modelov_skupaj = []
def zapisi_modele():
    for i in range(0, 959):
        vsebina_modela = vsebina_datoteke('modeli/model-{}.html'.format(i))
        podatki_modelov_skupaj.append(izloci_podatke_modela(vsebina_modela))

zapisi_json(podatki_modelov_skupaj, 'obdelani-podatki/vsi-modeli.json')
zapisi_csv(podatki_modelov_skupaj, ['znamka', 'model', 'teren', 'cena','ocena', 'stevilo ocen'],'obdelani-podatki/vsi-modeli.csv')


