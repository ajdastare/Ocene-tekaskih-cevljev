# Ocene-tekaskih-cevljev

Analizirala bom 912 tekaških čevljev glede na ocene uporabnikov, ceno in proizvajalca.
https://runrepeat.com/ranking/rankings-of-running-shoes


Za vsak model tekaškega čevlja bom zajela:
* ime modela
* ime proizvajalca - znamka
* ceno
* oceno
* število glasov

Delovne hipoteze:
* Ali obstaja povezava med najbolje ocenjenimi modeli tekaških čevljev in višjo ceno?
* Ali obstaja povezava me najbolje ocenjenimi modeli in znamko? 
* Katere znamke čevljev so najbolj ocenjene in kateri modeli? 
****

Zajem podatkov

Zajela sem 10 strani na zgoraj omenjeni strani, koda je v zajem.py . 
Zajeti podatki so v csv obliki vsi-cevlji.csv. 
Podatke sem razdelila po imenu modela tekaškega čevlja, oceni in številu vseh ocen. Cene in imena proizvajalca nisem zajela, saj teh dveh podatkov v html zapisu pod vsakim modelom na strani ni. 
