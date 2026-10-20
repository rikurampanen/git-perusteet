# 09 – Yhdistämiskonfliktit

## Mikä on yhdistämiskonflikti?

Git pystyy usein yhdistämään eri haaroissa tehdyt muutokset automaattisesti. Jos kaksi haaraa muuttaa samaa tiedoston kohtaa eri tavalla, Git ei välttämättä pysty päättelemään, kumpi muutos pitäisi säilyttää.

Tällöin syntyy **yhdistämiskonflikti** (*merge conflict*).

Konflikti ei tarkoita, että Git olisi rikkonut ohjelman. Se tarkoittaa, että sinun täytyy päättää, miltä yhdistetyn koodin pitäisi näyttää.

Tässä osassa opit:

- miten yhdistämiskonflikti syntyy
- miten tunnistat konfliktin
- miten ratkaiset konfliktin muokkaamalla tiedostoa
- miten merkitset konfliktin ratkaistuksi
- miten viimeistelet yhdistämisen commitilla.

## 1. Tarkista lähtötilanne

Avaa terminaali kurssilla käyttämässäsi `seikkailupeli`-repositoriossa. Tarkista nykyinen tilanne:

```bash
git status
git branch
```

Tässä harjoituksessa käytetään kahta haaraa:

- `main`
- `konflikti-harjoitus`

Ennen aloittamista varmista, että:

- `main`-haara on olemassa
- työskentelytilasi on puhdas eli sinulla ei ole tallentamattomia muutoksia
- et ole keskeneräisen yhdistämisen tai konfliktin tilassa
- haaraa `konflikti-harjoitus` ei ole jo olemassa.

Jos sinulla on keskeneräisiä muutoksia, tallenna ne tarvittaessa commitiksi ennen harjoitusta. Älä poista aiempia muutoksia vain harjoituksen aloittamiseksi.

Jos `konflikti-harjoitus` on jo olemassa aiemman yrityksen jäljiltä, tarkista ensin haarat ja niiden tila. Älä luo samaa haaraa uudelleen.

## 2. Muuta tiedostoa `main`-haarassa

Vaihda päähaaraan:

```bash
git switch main
```

Avaa `main.py` ja etsi rivi:

```python
print("Edessäsi on synkkä metsä.")
```

Muuta se seuraavaksi:

```python
print("Edessäsi on sumuinen metsä.")
```

Tallenna tiedosto ja tee commit:

```bash
git add main.py
git commit -m "Muuta metsän kuvausta"
```

Nyt muutos on tallennettu `main`-haaraan.

Jos Git ilmoittaa, ettei mitään ole commitattavana, tarkista tiedoston sisältö ja `git status`. Rivi saattaa olla jo muuttunut tai muutos on voitu tallentaa aiemmin.

## 3. Luo toinen haara ja tee ristiriitainen muutos

Luo uusi haara nykyisestä tilanteesta:

```bash
git switch -c konflikti-harjoitus
```

Avaa `main.py` ja muuta sama rivi toiseen muotoon:

```python
print("Edessäsi on pimeä metsä.")
```

Tallenna tiedosto ja tee commit:

```bash
git add main.py
git commit -m "Muuta metsän kuvausta toisessa haarassa"
```

Nyt molemmat haarat ovat lähteneet samasta tilanteesta, mutta niihin on tallennettu erilainen muutos samaan riviin.

- `main`-haarassa lukee, että metsä on sumuinen.
- `konflikti-harjoitus`-haarassa lukee, että metsä on pimeä.

Git ei voi tietää, kumpi kuvaus sinun pitäisi valita.

## 4. Aiheuta konflikti

Vaihda takaisin `main`-haaraan:

```bash
git switch main
```

Yritä yhdistää toinen haara:

```bash
git merge konflikti-harjoitus
```

Git ilmoittaa yhdistämiskonfliktista, koska molemmat haarat ovat muuttaneet samaa riviä eri tavalla.

Tarkista tilanne:

```bash
git status
```

Git kertoo, missä tiedostossa konflikti on. Tässä harjoituksessa ristiriita on `main.py`-tiedostossa.

**Tärkeää:** Älä yritä aloittaa uutta yhdistämistä. Ratkaise ensin käynnissä oleva konflikti.

## 5. Ratkaise konflikti

Avaa `main.py`. Ristiriitainen kohta voi näyttää tältä:

```text
<<<<<<< HEAD
print("Edessäsi on sumuinen metsä.")
=======
print("Edessäsi on pimeä metsä.")
>>>>>>> konflikti-harjoitus
```

Merkinnät tarkoittavat:

- `<<<<<<< HEAD` aloittaa nykyisen haaran version. Tässä se on `main`-haaran versio.
- `=======` erottaa kaksi versiota toisistaan.
- `>>>>>>> konflikti-harjoitus` päättää yhdistettävästä haarasta tulevan version.

Sinun tehtäväsi on päättää, miltä lopullisen tiedoston pitää näyttää. Voit valita jommankumman version tai kirjoittaa kokonaan uuden.

Esimerkiksi voit yhdistää kuvaukset näin:

```python
print("Edessäsi on sumuinen ja pimeä metsä.")
```

Poista kaikki konfliktimerkinnät ja jätä tiedostoon vain haluamasi lopullinen Python-koodi. Tallenna tiedosto.

Konfliktimerkinnät eivät ole Python-koodia. Jos ne jäävät tiedostoon, ohjelma ei toimi oikein.

## 6. Merkitse konflikti ratkaistuksi

Kun olet muokannut tiedoston ja tallentanut sen, lisää ratkaistu tiedosto staging-alueelle:

```bash
git add main.py
```

Tarkista tilanne:

```bash
git status
```

Git tunnistaa konfliktin ratkaistuksi, kun olet ilmoittanut siitä lisäämällä tiedoston staging-alueelle. Tarkista silti, että kaikki konfliktit on ratkaistu.

Viimeistele yhdistäminen commitilla:

```bash
git commit -m "Ratkaise metsän kuvausta koskeva konflikti"
```

Tarkastele historiaa:

```bash
git log --oneline --graph --all
```

Yhdistäminen on nyt valmis. Git on tallentanut historian, jossa molempien haarojen muutokset on käsitelty ja konfliktin lopputulos on valittu.

## 7. Testaa ohjelma

Suorita ohjelma:

```bash
python main.py
```

Tarkista, että ohjelma toimii ja metsän kuvaus on sellainen kuin päätit.

Voit myös tarkistaa, ettei tiedostossa ole jäljellä konfliktimerkintöjä:

- `<<<<<<<`
- `=======`
- `>>>>>>>`

Jos käytät eri Python-komentoa omassa ympäristössäsi, suorita ohjelma samalla tavalla kuin kurssin aiemmissa osissa.

## 8. Kokeile itse

Harjoittele konfliktin ratkaisemista uudelleen toisella rivillä.

Tässä harjoituksessa muutetaan aarretta koskevaa tulostetta. Jos `main.py` sisältää jo sopivan aarteen kuvauksen, voit käyttää sitä. Muussa tapauksessa lisää ensin sopiva tulosterivi `main`-haaraan ja tee siitä commit ennen harjoituksen aloittamista.

1. Varmista, että työskentelytilasi on puhdas ja olet `main`-haarassa.
2. Luo uusi haara:

   ```bash
   git switch -c aarre-konflikti
   ```

3. Muuta aarretta koskevaa tulosteriviä eri tavalla tässä haarassa ja tee commit.
4. Vaihda `main`-haaraan.
5. Muuta samaa tulosteriviä eri tavalla `main`-haarassa ja tee commit.
6. Yhdistä toinen haara:

   ```bash
   git merge aarre-konflikti
   ```

7. Ratkaise syntynyt konflikti, lisää tiedosto staging-alueelle ja viimeistele yhdistäminen commitilla.
8. Suorita ohjelma ja tarkista lopputulos.

**Pohdi:** Miten päätit, mikä teksti säilytetään? Voisiko molempien haarojen muutoksia hyödyntää lopullisessa versiossa?

Jos `aarre-konflikti` on jo olemassa aiemmasta harjoituksesta, älä yritä luoda sitä uudelleen samalla nimellä. Tarkista ensin haarat ja käytä tarvittaessa uutta nimeä.

## Osa on valmis, kun…

- [ ] Ymmärrät, miksi yhdistämiskonflikti syntyy.
- [ ] Osaat tunnistaa konfliktimerkinnät tiedostosta.
- [ ] Osaat muokata tiedoston haluttuun lopputulokseen ja poistaa konfliktimerkinnät.
- [ ] Osaat merkitä ratkaistun tiedoston komennolla `git add`.
- [ ] Ymmärrät, miten yhdistäminen viimeistellään komennolla `git commit`.
- [ ] Osaat testata ohjelman konfliktin ratkaisemisen jälkeen.

## Seuraavaksi

[Seuraava osa: 10 – Git-työnkulku](../10_git-tyonkulku/)

[← Edellinen osa: 08 – Etärepositorio](../08_etarepositorio/)

[← Kurssin etusivulle](../README.md)