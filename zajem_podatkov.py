
import requests
import re
import os
import sys
import csv

###############################################################################
# Najprej definirajmo nekaj pomožnih orodij za pridobivanje podatkov s spleta.
###############################################################################

# URL
#url tabela : 
shoes_table_url = 'https://runrepeat.com/ranking/rankings-of-running-shoes'
shoes_frontpage_url = 'https://runrepeat.com/ranking/rankings-of-running-shoes'
# mapa, v katero bomo shranili podatke
shoe_directory= 'shoes_data'
# ime datoteke v katero bomo shranili glavno stran
frontpage_filename = 'frontpage.html'
# ime CSV datoteke v katero bomo shranili podatke
csv_filename = 'shoes_data.csv'
url = shoes_frontpage_url

link = 'https://runrepeat.com/ranking/rankings-of-running-shoes?id%20=%20icon-ranking-grid-selected'

# mapa, v katero bomo shranili podatke
mapa_= 'shoes_data_grid'
# ime datoteke v katero bomo shranili glavno stran
ime_datoteke_ = 'page1_grid.html'


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
    
download_url_to_string(url)

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

# Definirajte funkcijo, ki prenese glavno stran in jo shrani v datoteko.


def save_frontpageurl(url, ime_datoteke, vsili_prenost = False):
    '''Save "cats_frontpage_url" to the file
    "cat_directory"/"frontpage_filename"'''
    try:
        # del kode, ki morda sproži napako
        r = requests.get(url)
    except requests.exceptions.ConnectionError:
            # koda, ki se izvede pri napaki
        # dovolj je če izpišemo opozorilo in prekinemo izvajanje funkcije
        print('stran ne obstaja!')
    else:
        with open(ime_datoteke, 'w', encoding='utf-8') as datoteka:
            datoteka.write(r.text)
            print('shranjeno!')
            


        
###############################################################################
# Po pridobitvi podatkov jih želimo obdelati.
###############################################################################


def read_file_to_string(directory,filename):
    path = os.path.join(directory, filename)
    with open(path, encoding='utf-8') as datoteka:
        return datoteka.read()
        

# Definirajte funkcijo, ki sprejme niz, ki predstavlja vsebino spletne strani,
# in ga razdeli na dele, kjer vsak del predstavlja en oglas. To storite s
# pomočjo regularnih izrazov, ki označujejo začetek in konec posameznega
# oglasa. Funkcija naj vrne seznam nizov.


def page_to_ads(TODO):
    vzorec = re.compile()
    '''Split "page" to a list of advertisement blocks.'''
    return TODO
# Definirajte funkcijo, ki sprejme niz, ki predstavlja oglas, in izlušči
# podatke o imenu, ceni in opisu v oglasu.


def get_dict_from_ad_block(TODO):
    '''Build a dictionary containing the name, description and price
    of an ad block.'''
    return TODO

# Definirajte funkcijo, ki sprejme ime in lokacijo datoteke, ki vsebuje
# besedilo spletne strani, in vrne seznam slovarjev, ki vsebujejo podatke o
# vseh oglasih strani.


def ads_from_file(TODO):
    '''Parse the ads in filename/directory into a dictionary list.'''
    return TODO

###############################################################################
# Obdelane podatke želimo sedaj shraniti.
###############################################################################


def write_csv(fieldnames, rows, directory, filename):
    '''Write a CSV file to directory/filename. The fieldnames must be a list of
    strings, the rows a list of dictionaries each mapping a fieldname to a
    cell-value.'''
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, filename)
    with open(path, 'w') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)
    return None

# Definirajte funkcijo, ki sprejme neprazen seznam slovarjev, ki predstavljajo
# podatke iz oglasa mačke, in zapiše vse podatke v csv datoteko. Imena za
# stolpce [fieldnames] pridobite iz slovarjev.


def write_cat_ads_to_csv(TODO):
    return TODO


