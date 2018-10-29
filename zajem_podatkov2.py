import csv
import json
import os
import re
import sys

import requests

# URL
url_ = 'https://runrepeat.com/ranking/rankings-of-running-shoes'
# mapa, v katero bomo shranili podatke
mapa_= 'shoes_data2'
# ime datoteke v katero bomo shranili glavno stran
ime_datoteke_ = 'frontpage.html'
# ime CSV datoteke v katero bomo shranili podatke
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



for i in range(1, 3):
    url = ('https://runrepeat.com/ranking/rankings-of-running-shoes'
        
            '?page={}'
    ).format(i)
    shrani_spletno_stran(url, 'page-{}.html'.format(i))
podatki_filmov = []


or i in range(1, 3):
    vsebina = vsebina_datoteke(
        'page-{}.html'.format(i))
    for ujemanje_filma in vzorec.finditer(vsebina):
        podatki_filmov.append(izloci_podatke_filma(ujemanje_filma))
zapisi_json(podatki_filmov, 'obdelani-podatki/vsi-filmi.json')
zapisi_csv(podatki_filmov, ['id', 'naslov', 'dolzina', 'leto',
                            'ocena', 'opis'], 'obdelani-podatki/vsi-filmi.csv')