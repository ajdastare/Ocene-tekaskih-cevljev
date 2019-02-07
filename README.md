# Ocene-tekaskih-cevljev

Analizirala bom 912 tekaških čevljev glede na ocene uporabnikov, ceno in proizvajalca.
https://runrepeat.com/ranking/rankings-of-running-shoes


Za vsak model tekaškega čevlja bom zajela:
* ime modela
* ime proizvajalca - znamka
* ceno
* oceno
* število glasov
* tip podlage

Delovne hipoteze:
* Ali obstaja povezava med najbolje ocenjenimi modeli tekaških čevljev in višjo ceno?
* Ali obstaja povezava me najbolje ocenjenimi modeli in znamko? 
* Katere znamke čevljev so najbolj ocenjene in kateri modeli? 
****

1. Faza : Zajem in čiščenje podatkov

Zajela sem 10 strani na zgoraj omenjeni strani, koda je v zajem.py.
Ko sem zajela te strani, sem skupaj zajela vsak link na tej strani ki vodi do posameznega modela. Podatke iz teh strani sem shranila v datoteko 'modeli'. Za vsak model sem torej zajela podatke in jih shranila v svojo html datoteko 'model-{}.html'.
Zajeti in očiščeni podatki so v datoteki 'obdelani podatki' v obliki csv in json. 

2. Faza : Analiza podatkov
Analizo podatkov sem napisala v jupyer notebook 'Analiza-koncano.ipynb', kjer so zapisani tudi končni sklepi. 
