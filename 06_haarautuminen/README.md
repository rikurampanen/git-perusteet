# 06 – Haarautuminen ja branchit

## Tavoite

Tässä osassa opit käyttämään Git-haaroja seikkailupeliprojektissasi. Haarojen avulla voit kehittää uutta ominaisuutta erillään päähaaran versiosta.

Opit:
- mitä Git-haara tarkoittaa
- miten olemassa olevat haarat listataan
- miten uusi haara luodaan
- miten haarasta toiseen vaihdetaan
- miten muutos tallennetaan commitilla uuteen haaraan
- miten haarojen välisiä eroja tarkastellaan

## 1. Tarkista nykyinen tilanne

Avaa terminaali seikkailupeliprojektisi kansiossa ja suorita:

```bash
git status
git branch
```

Komento `git status` näyttää repositoryn tilanteen. Komento `git branch` näyttää paikalliset haarat. Nykyisen haaran edessä on tähti.

Esimerkiksi:

```text
* main
```

Tämä tarkoittaa, että olet `main`-haarassa.

Ennen harjoitusta varmista, että:
- olet seikkailupeliprojektin kansiossa
- nykyinen haara on `main`
- työpuu on puhdas eli keskeneräisiä muutoksia ei ole

Jos `git status` näyttää keskeneräisiä muutoksia, tarkista ne ennen jatkamista. Älä vaihda haaraa ennen kuin ymmärrät, mitä muutoksille tapahtuu.

## 2. Mitä Git-haara tarkoittaa?

Git-haara eli *branch* on projektin historiasta jatkuva kehityslinja.

Kuvitellaan, että seikkailupeli toimii jo hyvin. Haluat lisätä peliin uuden ominaisuuden, mutta et halua tehdä sitä suoraan päähaaraan. Voit luoda uuden haaran, kehittää ominaisuutta siellä ja päättää myöhemmin, yhdistätkö sen päähaaraan.

Git-repositoriossa päähaaran nimi on usein `main`.

Haara ei ole kokonaan erillinen kopio projektista. Haarat viittaavat eri kohtiin Gitin historiassa, ja tiedostojen sisältö muuttuu sen mukaan, missä haarassa olet ja mitä committeja siihen kuuluu.

## 3. Luo uusi haara

Luo seikkailupelin uutta ominaisuutta varten haara nimeltä `uusi-polku`:

```bash
git switch -c uusi-polku
```

Komento luo uuden haaran ja vaihtaa siihen samalla.

Tarkista tilanne:

```bash
git branch
```

Tuloste voi näyttää tältä:

```text
  main
* uusi-polku
```

Olet nyt `uusi-polku`-haarassa. Seuraavaksi teet muutoksia tässä haarassa.

Jos Git-versiosi ei tue komentoa `git switch`, voit käyttää vastaavaa vanhempaa komentoa:

```bash
git checkout -b uusi-polku
```

## 4. Tee muutos pelin koodiin

Avaa projektin `main.py` ja lisää ohjelman loppuun uusi tulostusrivi:

```python
print("Löydät metsästä salaperäisen sivupolun.")
```

Tallenna tiedosto ja suorita ohjelma. Tarkista, että uusi teksti näkyy tulosteessa.

Tarkastele sitten muutoksia:

```bash
git status
git diff
```

Git näyttää, että `main.py` on muuttunut ja että uusi rivi on työpuussa.

Muutos on tässä vaiheessa vain tiedostossa. Se ei vielä kuulu haaran historiaan, koska et ole tehnyt siitä committia.

## 5. Tallenna muutos uuteen haaraan

Lisää tiedosto staging-alueelle ja tee commit:

```bash
git add main.py
git commit -m "Lisää uusi polku seikkailuun"
```

Tarkista tilanne:

```bash
git status
git log --oneline
```

Uusi commit kuuluu nyt `uusi-polku`-haaran historiaan.

Voit tarkastella myös haarojen nimiä:

```bash
git branch
```

Muista: `git add` ja `git commit` toimivat nykyisen repositoryn ja aktiivisen haaran tilanteen mukaan. Commit tallentaa valmistellut muutokset nykyiseen historiaan.

## 6. Vaihda takaisin päähaaraan

Vaihda takaisin `main`-haaraan:

```bash
git switch main
```

Avaa `main.py` ja tarkista sen sisältö. Uuden sivupolun tulostusrivin pitäisi puuttua, koska teit muutoksen vain `uusi-polku`-haarassa.

Tarkista myös historia:

```bash
git log --oneline
```

Uusi commit ei näy `main`-haaran historiassa, koska et ole yhdistänyt haaroja.

Tämä on haarojen tärkeä ominaisuus: yhden haaran commitit eivät automaattisesti siirry toiseen haaraan.

## 7. Palaa uuteen haaraan

Vaihda takaisin:

```bash
git switch uusi-polku
```

Avaa `main.py` uudelleen. Sivupolun tulostusrivin pitäisi olla jälleen mukana.

Tarkista aktiivinen haara ja historia:

```bash
git branch
git log --oneline
```

Olet nyt palannut haaraan, johon tallensit uuden ominaisuuden.

Haaran vaihtaminen ei itsessään luo uutta committia eikä yhdistä haaroja. Se vaihtaa siihen projektin versioon, jota kyseinen haara edustaa.

## 8. Kokeile itse

Tee uusi harjoitus erillisellä haaralla.

1. Vaihda `main`-haaraan: `git switch main`.
2. Varmista komennolla `git status`, että työpuu on puhdas.
3. Luo uusi haara ja vaihda siihen: `git switch -c pelaajan-terveys`.
4. Lisää `main.py`-tiedostoon uusi tulostusrivi, esimerkiksi:

   ```python
   print(f"Pelaajan terveys on {terveys}.")
   ```

5. Tallenna tiedosto ja tarkista muutokset komennoilla `git status` ja `git diff`.
6. Tee commit:

   ```bash
   git add main.py
   git commit -m "Lisää pelaajan terveyden tulostus"
   ```

7. Vaihda takaisin `main`-haaraan ja tarkista, näkyykö uusi rivi siellä.
8. Vaihda takaisin `pelaajan-terveys`-haaraan ja tarkista tiedoston sisältö.

Älä vielä yhdistä haaroja. Seuraavassa osassa opit yhdistämään haaroja eli tekemään *mergen*.

## 9. Tarkista, mitä opit

Vastaa omin sanoin:

1. Mitä Git-haara tarkoittaa?
2. Millä komennolla näet olemassa olevat haarat?
3. Miten luot uuden haaran ja siirryt siihen samalla?
4. Mitä tapahtuu, kun vaihdat takaisin `main`-haaraan?
5. Miksi uuden haaran commit ei automaattisesti näy `main`-haaran historiassa?
6. Miksi uuden ominaisuuden kehittäminen omassa haarassa voi olla hyödyllistä?

**Vastaukset tarkistettavaksi**

1. Haara on projektin historiasta jatkuva kehityslinja.
2. `git branch`.
3. `git switch -c haaran-nimi`.
4. Git vaihtaa `main`-haaran sisältöön ja historiaan.
5. Haarojen historiat ovat erilliset, kunnes niitä yhdistetään tai muutokset siirtyvät haarasta toiseen muulla tavalla.
6. Uutta ominaisuutta voi kehittää erillään päähaarasta, jolloin keskeneräinen työ ei suoraan muuta päähaaran versiota.

## 10. Osa on valmis, kun…

- [ ] Osaat näyttää olemassa olevat haarat komennolla `git branch`.
- [ ] Osaat luoda uuden haaran ja siirtyä siihen komennolla `git switch -c nimi`.
- [ ] Osaat vaihtaa olemassa olevaan haaraan komennolla `git switch nimi`.
- [ ] Osaat tallentaa muutoksen commitilla aktiiviseen haaraan.
- [ ] Osaat tarkistaa, miten tiedoston sisältö eroaa eri haaroissa.
- [ ] Ymmärrät, miksi haaroja käytetään uusien ominaisuuksien kehittämiseen erillään päähaarasta.

## Seuraavaksi

[Seuraava osa: 07 – Haarojen yhdistäminen](../07_haarojen_yhdistaminen/)

[← Edellinen osa: 05 – Muutosten palautus](../05_muutosten_palautus/)

[← Kurssin etusivulle](../README.md)