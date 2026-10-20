# 03 – Ensimmäinen commit

## Tavoite

Tässä osassa tallennat seikkailupeliprojektisi ensimmäisen version Gitiin.

Opit:
- mitä Gitin seuranta tarkoittaa
- mitä `git add` tekee
- mitä `git commit` tekee
- miten tarkistat valmistellut muutokset
- miten tarkastelet commit-historiaa
- miten kirjoitat kuvaavan commit-viestin

## 1. Missä tilanteessa olemme?

Edellisessä osassa loit `seikkailupeli`-kansioon Git-repositoryn komennolla:

```bash
git init
```

Sen jälkeen tarkistit tilanteen:

```bash
git status
```

Git tunnisti `main.py`-tiedoston, mutta sitä ei ollut vielä lisätty staging-alueelle eikä tallennettu committiin.

Nyt jatkat samassa harjoitusprojektissa. Älä luo uutta repositorya äläkä suorita `git init` -komentoa uudelleen.

Varmista, että olet `seikkailupeli`-kansiossa ja että `main.py` sisältää edellisen osan ohjelman.

## 2. Mitä commit tarkoittaa?

Commit on Gitin tallentama kokonaisuus projektin muutoksia.

Voit ajatella committia projektin tallennuspisteenä, jonka sisältöä voit myöhemmin tarkastella.

Seikkailupelisi ensimmäinen commit sisältää ohjelman, joka kysyy pelaajan nimen ja tulostaa tervetuloviestin sekä terveyspisteet.

Myöhemmin voit tehdä uusia committeja, kun lisäät peliin esimerkiksi uusia tapahtumia, haarautuvia polkuja tai vihollisia.

Hyvä commit sisältää loogisen kokonaisuuden. Sen viestistä pitäisi pystyä päättelemään, mitä muutettiin.

Muista, että tavallinen tiedoston tallentaminen ja Git-commit ovat eri asioita. Tallennat ensin tiedoston editorissa ja sen jälkeen valmistelet ja tallennat muutokset Gitillä.

## 3. Lisää tiedosto staging-alueelle

Varmista ensin, että olet projektikansiossa ja että `main.py` sisältää edellisen osan ohjelman.

Suorita:

```bash
git add main.py
```

Komento lisää tiedoston senhetkiset muutokset Gitin staging-alueelle eli valmisteltavaksi seuraavaan committiin.

Staging-alueella voit valita, mitkä muutokset sisällytetään seuraavaan committiin.

Tärkeä ero: `git add` ei vielä tee committia. Se valmistelee muutokset tallennettaviksi.

## 4. Tarkista tilanne

Suorita:

```bash
git status
```

Nyt `main.py` näkyy tavallisesti valmisteltuna muutoksena. Git käyttää usein ilmaisua `Changes to be committed`.

Tämä tarkoittaa, että tiedoston muutokset on valittu seuraavaan committiin.

Työnkulku on nyt seuraava:

1. Tiedosto on projektikansiossa.
2. `git add` valmistelee muutokset staging-alueelle.
3. `git commit` tallentaa valmistellut muutokset repositoryn historiaan.

## 5. Tee ensimmäinen commit

Suorita:

```bash
git commit -m "Lisää seikkailupelin aloitus"
```

Komento tallentaa staging-alueella olevat muutokset commitiksi ja liittää niihin viestin.

Komennon osat:

- `git commit` luo commitin.
- `-m` tarkoittaa, että annat commit-viestin suoraan komennossa.
- `"Lisää seikkailupelin aloitus"` kertoo, mitä commit sisältää.

Git voi ilmoittaa, ettei käyttäjän nimeä tai sähköpostiosoitetta ole määritetty. Jos näin käy, määritä omat tietosi Gitin ilmoituksen mukaisesti ja suorita commit uudelleen.

## 6. Tarkista tallennettu versio

Suorita:

```bash
git status
```

Jos kaikki muutokset on tallennettu eikä muita muutoksia ole, Git ilmoittaa tavallisesti, että työpuu on puhdas (`working tree clean`).

Tarkastele seuraavaksi commit-historiaa:

```bash
git log --oneline
```

Näet tekemäsi commitin lyhyenä rivinä. Rivillä näkyvät commitin tunniste ja viesti.

Nyt projektillasi on ensimmäinen commit.

## 7. Kokeile: tee toinen commit

Avaa `main.py` ja lisää ohjelman loppuun:

```python
print("Matkasi alkaa nyt.")
```

Tallenna tiedosto editorissa.

Tarkista tilanne:

```bash
git status
```

Git ilmoittaa, että tiedostoa on muutettu. Uusi muutos ei ole vielä mukana aikaisemmassa commitissa.

Valmistele muutos:

```bash
git add main.py
```

Tarkista tilanne uudelleen:

```bash
git status
```

Tee sitten uusi commit:

```bash
git commit -m "Lisää pelin aloitusteksti"
```

Tarkastele historiaa:

```bash
git log --oneline
```

Nyt historiassa pitäisi näkyä kaksi committia.

Huomaa, että aikaisempi commit säilyy ennallaan. Uusi commit tallentaa uuden version projektistasi.

**Tärkeää:** jos muokkaat tiedostoa `git add` -komennon jälkeen, uudet muutokset eivät automaattisesti siirry staging-alueelle. Sinun pitää suorittaa `git add` uudelleen, jos haluat sisällyttää myös ne seuraavaan committiin.

## 8. Riko ja korjaa: miksi commit ei aina onnistu?

Kokeile suorittaa commit ilman uusia valmisteltuja muutoksia:

```bash
git commit -m "Ei uusia muutoksia"
```

Git ilmoittaa tavallisesti, ettei uusia muutoksia ole tallennettavaksi.

Tämä on normaalia. Git ei luo uutta committia vain siksi, että suoritat komennon.

Tee nyt `main.py`-tiedostoon uusi tulostusrivi:

```python
print("Metsän polku haarautuu kahteen suuntaan.")
```

Tallenna tiedosto ja suorita:

```bash
git status
```

Valmistele muutos ja tarkista tilanne:

```bash
git add main.py
git status
```

Tee lopuksi commit:

```bash
git commit -m "Lisää kuvaus metsän polusta"
```

Tarkista historia:

```bash
git log --oneline
```

Nyt historiassa pitäisi näkyä kolme committia.

Tämä harjoitus havainnollistaa, että commit syntyy valmistelluista muutoksista eikä pelkästä komennon suorittamisesta.

## 9. Tarkista, mitä opit

Vastaa omin sanoin:

1. Mitä `git add` tekee?
2. Mitä `git commit` tekee?
3. Miksi `git add` ja `git commit` ovat eri komentoja?
4. Mitä `git status` auttaa selvittämään?
5. Miten näet commit-historian?
6. Miksi `git add` pitää suorittaa uudelleen, jos tiedostoa muokataan sen jälkeen?

### Vastaukset tarkistettavaksi

1. `git add` valmistelee tiedoston muutokset seuraavaan committiin.
2. `git commit` tallentaa staging-alueella olevat muutokset repositoryn historiaan.
3. `git add` valitsee tallennettavat muutokset, kun taas `git commit` tallentaa valmistellut muutokset.
4. `git status` näyttää esimerkiksi muuttuneet, valmistellut ja seuraamattomat tiedostot.
5. Komennolla `git log --oneline`.
6. Koska `git add` valmistelee vain komennon suoritushetkellä staging-alueelle lisätyt muutokset. Myöhemmät muokkaukset pitää lisätä erikseen.

## 10. Osa on valmis, kun…

- [ ] Osaat lisätä tiedoston staging-alueelle komennolla `git add`.
- [ ] Osaat tehdä commitin komennolla `git commit`.
- [ ] Osaat kirjoittaa commitille kuvaavan viestin.
- [ ] Osaat tarkistaa tilanteen komennolla `git status`.
- [ ] Osaat tarkastella historiaa komennolla `git log --oneline`.
- [ ] Ymmärrät staging-alueen ja commitin eron.
- [ ] Ymmärrät, että uusi commit tallentaa uudet muutokset ja säilyttää aiemman historian.

---

## Seuraavaksi

[Seuraava osa: 04 – Muutosten tarkastelu](../04_muutosten_tarkastelu/)

[← Edellinen osa: 02 – Mikä on Git-repository?](../02_repository/)

[← Kurssin etusivulle](../README.md)