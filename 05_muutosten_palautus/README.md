# 05 – Muutosten palautus

## Tavoite

Tässä osassa opit toimimaan, kun teet seikkailupeliin vahingossa muutoksen tai haluat perua keskeneräisen työn.

Opit:
- miten palautat tiedoston viimeisimmän commitin mukaiseen sisältöön
- miten poistat muutoksen staging-alueelta
- miten tarkastelet muutoksia ennen palauttamista
- miksi jo tallennettujen commitien käsittely vaatii erityistä huolellisuutta

## 1. Mitä jos teet virheen?

Edellisissä osissa olet muuttanut seikkailupelin ohjelmakoodia ja tallentanut muutoksia committeihin.

Kuvitellaan, että ohjelman terveyspisteet ovat olleet 100:

```python
terveys = 100
```

Muutat arvoksi 10:

```python
terveys = 10
```

Tarkoituksesi oli ehkä kokeilla jotakin, mutta nyt haluat palata aiempaan tilanteeseen.

Jos muutos on vain työpuussa eikä sitä ole valmisteltu staging-alueelle, Git voi palauttaa tiedoston viimeisimmän commitin mukaiseen sisältöön.

Ennen palauttamista tarkista kuitenkin aina, mitä olet muuttamassa. Palauttaminen voi hävittää myös sellaisia muutoksia, jotka haluaisit säilyttää.

## 2. Tarkista tilanne ennen palauttamista

Suorita:

```bash
git status
```

Katso, mitkä tiedostot ovat muuttuneet.

Tutki seuraavaksi muutosten sisältö:

```bash
git diff
```

Näet työpuun muutokset, joita ei ole valmisteltu staging-alueelle.

Tämä vaihe on tärkeä: ennen palauttamista sinun pitää tietää, mitä muutoksia tiedostossa on ja haluatko todella hävittää ne.

**Tärkeä sääntö:** älä suorita palautuskomentoa ennen kuin olet tarkistanut tilanteen ja ymmärrät, mitä komento tekee.

## 3. Palauta työpuun muutos

Tässä harjoituksessa palautat tiedoston viimeisimmän commitin mukaiseen sisältöön.

Muuta `main.py`-tiedostossa terveyspisteet arvoon 10:

```python
terveys = 10
```

Tallenna tiedosto editorissa. Varmista, että muutos ei ole staging-alueella eikä sitä ole tallennettu commitiksi.

Tarkista tilanne:

```bash
git status
git diff
```

Suorita sitten:

```bash
git restore main.py
```

Komento palauttaa `main.py`-tiedoston viimeisimmän commitin mukaiseen sisältöön.

Jos viimeisimmässä commitissa terveyspisteet olivat 100, ne palaavat arvoon 100.

Tarkista tulos:

```bash
git status
```

Jos tiedostossa ei ollut muita muutoksia, työpuu on nyt puhdas.

**Varoitus:** `git restore main.py` voi hävittää kaikki tiedoston työpuussa olevat keskeneräiset muutokset, ei vain viimeisintä muokkausta. Tarkista muutokset aina ennen palauttamista.

## 4. Poista muutos staging-alueelta

Mitä jos olet jo käyttänyt `git add` -komentoa mutta et haluakaan sisällyttää muutosta seuraavaan committiin?

Muuta ensin `main.py`-tiedoston terveyspisteet esimerkiksi arvoon 75:

```python
terveys = 75
```

Tallenna tiedosto ja lisää muutos staging-alueelle:

```bash
git add main.py
```

Tarkista tilanne:

```bash
git status
git diff --staged
```

Nyt muutos on valmisteltu seuraavaan committiin.

Jos haluat poistaa muutoksen staging-alueelta mutta säilyttää sen tiedostossa, suorita:

```bash
git restore --staged main.py
```

Tarkista tilanne uudelleen:

```bash
git status
git diff
```

Muutos on edelleen tiedostossa, mutta sitä ei ole enää valmisteltu seuraavaan committiin.

Muista näiden komentojen ero:

- `git restore --staged main.py` poistaa muutoksen staging-alueelta mutta säilyttää tiedostossa olevat muutokset.
- `git restore main.py` palauttaa tiedoston sisällön viimeisimmän commitin mukaiseen tilaan ja voi hävittää työpuun keskeneräiset muutokset.

**Huomaa:** tässä harjoituksessa älä suorita `git restore main.py` -komentoa, koska tarkoitus on säilyttää tiedostossa oleva muutos.

## 5. Harjoittele turvallisesti

Kokeile seuraavia vaiheita seikkailupeliprojektissasi.

### Vaihe A: Tee muutos

Muuta terveyspisteet:

```python
terveys = 75
```

Tallenna tiedosto ja suorita:

```bash
git status
git diff
```

Tutki, mitä Git näyttää.

### Vaihe B: Palauta muutos

Jos haluat hävittää kokeilun ja palata viimeisimpään committiin, suorita:

```bash
git restore main.py
```

Tarkista:

```bash
git status
```

Avaa tiedosto ja varmista, että terveyspisteet ovat palautuneet viimeisimmän commitin mukaiseen arvoon.

### Vaihe C: Kokeile staging-aluetta

Tee tiedostoon uusi muutos:

```python
terveys = 50
```

Tallenna ja suorita:

```bash
git add main.py
git status
git diff --staged
```

Poista muutos staging-alueelta:

```bash
git restore --staged main.py
```

Tarkista uudelleen:

```bash
git status
git diff
```

Muutos on edelleen tiedostossa, mutta se ei ole enää valmisteltuna seuraavaan committiin.

Jos haluat lopuksi palauttaa tiedoston viimeisimpään committiin, tarkista ensin `git diff` ja suorita vasta sitten:

```bash
git restore main.py
```

## 6. Entä jos muutos on jo tallennettu commitiksi?

Jos olet jo tehnyt commitin, tilanne on erilainen.

Commit kuuluu Gitin historiaan. Sitä ei pidä käsitellä samalla tavalla kuin keskeneräistä tiedostomuutosta.

Yksi myöhemmin opeteltava tapa on `git revert`, joka luo uuden commitin kumoamaan aiemman commitin muutokset.

Tässä vaiheessa sinun ei tarvitse suorittaa sitä. Riittää, että ymmärrät eron keskeneräisen muutoksen ja jo tallennetun commitin välillä.

**Älä käytä `git reset --hard` -komentoa tämän harjoituksen yhteydessä.** Se voi hävittää tekemäsi muutokset, eikä sitä tarvita tässä osassa.

## 7. Riko ja korjaa

Lisää `main.py`-tiedoston loppuun:

```python
print("Tämä viesti oli vahinko.")
```

Tallenna tiedosto.

Tarkista ensin:

```bash
git status
git diff
```

Jos haluat perua lisäyksen ja se on vain työpuussa, suorita:

```bash
git restore main.py
```

Avaa tiedosto uudelleen ja varmista, että vahingossa lisätty rivi on poistunut.

**Pohdi:** miksi on tärkeää tarkistaa muutokset ennen palauttamista?

**Vastaus:** palautus voi hävittää kaikki kyseisessä tiedostossa olevat työpuun keskeneräiset muutokset, ei pelkästään viimeisintä lisäystä.

## 8. Muista nämä kolme tilannetta

| Tilanne | Komento tai toimintatapa | Vaikutus |
|---|---|---|
| Muutos on vain työpuussa | `git restore main.py` | Palauttaa tiedoston viimeisimpään committiin ja voi hävittää työpuun muutokset |
| Muutos on staging-alueella | `git restore --staged main.py` | Poistaa muutoksen staging-alueelta mutta säilyttää sen tiedostossa |
| Muutos on jo commitissa | Tutki tilanne; myöhemmin `git revert` | Aiemman commitin vaikutus voidaan kumota uudella commitilla |

Komennot toimivat tässä tiedostokohtaisesti, koska niissä annetaan tiedoston nimi. Älä suorita palautusta ennen kuin ymmärrät, mitä muutoksia se koskee.

## 9. Tarkista, mitä opit

Vastaa omin sanoin:

1. Mitä `git restore main.py` tekee?
2. Mitä `git restore --staged main.py` tekee?
3. Häviävätkö tiedoston muutokset, kun poistat ne staging-alueelta?
4. Miksi `git status` ja `git diff` kannattaa suorittaa ennen palautusta?
5. Miksi jo commitattua muutosta käsitellään eri tavalla kuin keskeneräistä muutosta?

**Vastaukset tarkistettavaksi**

1. `git restore main.py` palauttaa tiedoston viimeisimmän commitin mukaiseen sisältöön ja voi hävittää työpuun keskeneräiset muutokset.
2. `git restore --staged main.py` poistaa muutoksen staging-alueelta.
3. Eivät. Muutos jää tiedostoon, jos sitä ei erikseen palauteta.
4. Niiden avulla näet, mitä olet muuttamassa ja mitä voit menettää.
5. Commit on osa projektin historiaa. Sen vaikutus kannattaa kumota hallitusti, esimerkiksi myöhemmin opeteltavalla `git revert` -komennolla.

## 10. Osa on valmis, kun…

- [ ] Osaat tarkistaa muutokset ennen niiden palauttamista.
- [ ] Ymmärrät, miten työpuun muutos palautetaan.
- [ ] Osaat poistaa muutoksen staging-alueelta.
- [ ] Ymmärrät näiden kahden komennon eron.
- [ ] Tiedät, ettei jo tallennettua committia pidä käsitellä kuin keskeneräistä muutosta.

## Seuraavaksi

[Seuraava osa: 06 – Haarautuminen](../06_haarautuminen/)

[← Edellinen osa: 04 – Muutosten tarkastelu](../04_muutosten_tarkastelu/)

[← Kurssin etusivulle](../README.md)