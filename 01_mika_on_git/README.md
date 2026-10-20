# 01 – Mikä Git on?

## Tavoite

Tässä osassa tutustut Gitiin ja ymmärrät, miksi sitä käytetään ohjelmistokehityksessä.

Opit:
- mikä Git on
- mitä versionhallinta tarkoittaa
- miksi ohjelman eri versioita kannattaa tallentaa
- miten Git auttaa seuraamaan muutoksia

Et tarvitse aiempaa kokemusta Gitistä. Tässä osassa tutustut aiheeseen ilman Git-komentoja.

## 1. Mikä Git on?

Git on versionhallintajärjestelmä. Sen avulla voit tallentaa projektin muutoksia ja tarkastella aikaisempia versioita.

Kuvitellaan, että kehität Pythonilla pientä seikkailupeliä.

Aluksi ohjelma tulostaa:

```python
print("Tervetuloa seikkailuun!")
```

Myöhemmin lisäät peliin pelaajan nimen:

```python
pelaaja = input("Mikä on nimesi? ")

print(f"Tervetuloa seikkailuun, {pelaaja}!")
```

Seuraavaksi lisäät terveyspisteet, inventaarion ja vihollisia.

Ohjelma muuttuu jatkuvasti. Jos teet vahingossa virheen tai haluat tarkistaa, millainen ohjelma oli aikaisemmin, versionhallinnasta on hyötyä.

Git auttaa pitämään muutokset järjestyksessä ja seuraamaan projektin kehitystä.

## 2. Mitä tapahtuu ilman versionhallintaa?

Voisit tallentaa ohjelmasta useita kopioita:

```text
seikkailupeli.py
seikkailupeli_uusi.py
seikkailupeli_uusi2.py
seikkailupeli_valmis.py
seikkailupeli_valmis_oikeasti.py
```

Tämä toimii hetken, mutta pian voi olla vaikea tietää, mikä tiedosto on uusin ja mitä missäkin versiossa muuttui.

Git ratkaisee tätä ongelmaa tallentamalla muutokset samaan projektiin hallitusti. Sinun ei tarvitse luoda jokaisesta versiosta erillistä tiedostoa.

## 3. Mitä versionhallinta tarkoittaa?

Versionhallinnassa projektin muutokset tallennetaan erillisinä versioina eli committeina.

Voit ajatella committia projektin tallennuspisteenä.

Esimerkiksi:

| Versio | Muutos |
|---|---|
| 1 | Seikkailupeli tulostaa tervetuloviestin. |
| 2 | Pelaaja voi antaa nimensä. |
| 3 | Pelaajalle lisätään terveyspisteet. |
| 4 | Peliin lisätään ensimmäinen vihollinen. |

Kun tallennat muutoksia Gitiin, voit myöhemmin tarkastella, mitä muuttui ja milloin muutos tallennettiin.

Commit ei ole sama asia kuin tavallinen tiedoston tallentaminen. Tallennat ensin tiedoston normaalisti editorissa ja teet sen jälkeen Gitillä erillisen tallennuksen osaksi projektin historiaa.

Opit commitien tekemisen tarkemmin osassa 3.

## 4. Kokeile: tutki ohjelmaa

Tässä kurssissa käytät pientä seikkailupeliä esimerkkinä Gitin toimintaperiaatteista.

Tutki seuraavaa Python-ohjelmaa:

```python
pelaaja = input("Mikä on nimesi? ")
terveys = 100

print(f"Tervetuloa seikkailuun, {pelaaja}!")
print(f"Terveytesi on {terveys}.")
```

Suorita ohjelma ja mieti:

- Mitä ohjelma tekee?
- Mitkä tiedot voivat muuttua pelin kehittyessä?
- Mitä haluaisit tehdä, jos uusi muutos rikkoisi ohjelman?

Sinun ei tarvitse osata Git-komentoja vielä. Tässä vaiheessa tärkeintä on ymmärtää, miksi muutosten tallentaminen ja aikaisempien versioiden tarkastelu ovat hyödyllisiä.

## 5. Muuta ohjelmaa

Lisää ohjelman loppuun uusi tulostusrivi:

```python
print("Edessäsi on synkkä metsä.")
```

Suorita ohjelma uudelleen.

Nyt olet muuttanut ohjelmaa. Kuvittele, että haluaisit myöhemmin selvittää, mitä lisäsit tai palauttaa ohjelman aikaisempaan versioon.

Gitillä voit tallentaa muutoksen osaksi projektin historiaa ja myöhemmin tarkastella muutosten eroja.

Tässä vaiheessa et vielä tallenna muutoksia Gitiin. Harjoittelet vasta ymmärtämään, miksi muutosten seuraamisesta on hyötyä.

## 6. Riko ja korjaa

Etsi ohjelmasta tämä rivi:

```python
terveys = 100
```

Muuta se seuraavaksi:

```python
terveys = "paljon"
```

Suorita ohjelma.

Ohjelma toimii edelleen, koska Python sallii tekstin tallentamisen muuttujaan. Muuttuja ei kuitenkaan enää sisällä lukua, jota voisi käyttää tavalliseen terveyspisteiden laskemiseen.

Esimerkiksi myöhemmin pelissä voisi olla tällainen rivi:

```python
terveys = terveys - 10
```

Jos `terveys` sisältää tekstiä eikä lukua, tämä laskutoimitus aiheuttaa virheen.

Korjaa muuttuja takaisin alkuperäiseen muotoonsa:

```python
terveys = 100
```

Suorita ohjelma uudelleen ja varmista, että se toimii odotetusti.

Tämä harjoitus havainnollistaa, miten pienikin muutos voi vaikuttaa ohjelman toimintaan.

Git ei estä virheiden tekemistä. Se auttaa seuraamaan muutoksia ja tarkastelemaan projektin historiaa. Varsinainen ohjelman toimivuus pitää silti testata.

## 7. Tarkista, mitä opit

Vastaa omin sanoin seuraaviin kysymyksiin:

1. Mikä Git on?
2. Mitä versionhallinta tarkoittaa?
3. Miksi useiden tiedostokopioiden tekeminen voi olla hankalaa?
4. Mitä commit tarkoittaa?
5. Estääkö Git virheiden tekemisen?

### Vastaukset tarkistettavaksi

1. Git on versionhallintajärjestelmä, jolla seurataan projektin muutoksia.
2. Versionhallinta tarkoittaa tiedostojen muutosten ja eri versioiden hallintaa.
3. Kopioista voi olla vaikea tunnistaa oikeaa versiota ja muutosten eroja.
4. Commit on Gitin tallentama kokonaisuus projektin muutoksia eli tallennuspiste.
5. Ei. Git auttaa seuraamaan ja hallitsemaan muutoksia, mutta ohjelman toimivuus pitää silti tarkistaa.

## 8. Osa on valmis, kun…

- [ ] Osaat selittää omin sanoin, mikä Git on.
- [ ] Ymmärrät, miksi muutoksia tallennetaan versioiksi.
- [ ] Tiedät, mitä commit tarkoittaa.
- [ ] Ymmärrät, miksi useiden tiedostokopioiden ylläpitäminen voi olla hankalaa.
- [ ] Ymmärrät, ettei Git korvaa tavallista tiedostojen tallentamista eikä ohjelman testaamista.

---

## Seuraavaksi

[Seuraava osa: 02 – Mikä on Git-repository?](../02_repository/)

[← Kurssin etusivulle](../README.md)