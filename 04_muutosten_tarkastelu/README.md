# 04 – Muutosten tarkastelu

## Tavoite

Tässä osassa opit tutkimaan seikkailupeliprojektin muutoksia ennen niiden tallentamista Gitiin.

Opit:
- miten tarkistat projektin tilan
- miten näet, mitä tiedostossa on muuttunut
- miten tarkastelet staging-alueelle valmisteltuja muutoksia
- miten tarkastelet aiempia committeja
- miksi muutokset kannattaa tarkistaa ennen committia

## 1. Miksi muutoksia pitää tarkastella?

Edellisessä osassa teit ensimmäiset commitit seikkailupeliisi.

Ohjelma kehittyy vähitellen. Lisäät uusia ominaisuuksia, muutat tekstejä ja korjaat virheitä. Aina ei kuitenkaan ole helppo muistaa, mitä kaikkea muutit.

Esimerkiksi olet voinut muuttaa pelaajan terveyspisteitä ja samalla muokata tervetuloviestiä. Ennen tallennusta haluat tarkistaa, että muutokset ovat sellaisia kuin tarkoitit.

Git tarjoaa tähän työkaluja. Niiden avulla voit tarkistaa muutokset ennen committia ja tutkia, mitä aiemmissa tallennuspisteissä muuttui.

## 2. Tee muutoksia ohjelmaan

Varmista, että olet seikkailupeliprojektin kansiossa ja että `main.py` sisältää edellisessä osassa tehdyn ohjelman.

Muuta terveyspisteiden arvoa:

```python
terveys = 80
```

Aiemmin arvo oli `100`.

Etsi ohjelmasta myös metsää kuvaava tulostusrivi ja muuta se seuraavaksi:

```python
print("Edessäsi on vanha ja salaperäinen metsä.")
```

Tallenna tiedosto editorissa.

Et ole vielä tehnyt uutta committia. Tiedostoon tekemäsi muutokset eivät ole mukana aiemmassa commitissa, joten Gitin historia sisältää edelleen vanhan version.

## 3. Tarkista projektin tila

Suorita:

```bash
git status
```

Git ilmoittaa, että `main.py`-tiedostoa on muutettu.

On tärkeää erottaa toisistaan kolme asiaa:

- **Tiedoston tallentaminen:** tallennat muutokset editorissa.
- **Muutosten valmistelu:** lisäät haluamasi muutokset staging-alueelle komennolla `git add`.
- **Commitin tekeminen:** tallennat valmistellut muutokset Gitin historiaan komennolla `git commit`.

Tiedoston tallentaminen editorissa ei siis automaattisesti tee committia.

## 4. Katso, mitä muuttui

Suorita:

```bash
git diff
```

Komento näyttää työpuussa olevat muutokset, joita ei ole valmisteltu staging-alueelle.

Tulosteessa voi näkyä esimerkiksi:

```diff
- terveys = 100
+ terveys = 80
```

Miinusmerkillä (`-`) alkava rivi kuvaa poistuvaa sisältöä ja plusmerkillä (`+`) alkava rivi lisättyä sisältöä.

Myös muuttamasi tulostusteksti näkyy tulosteessa.

Tämä on hyödyllistä, koska sinun ei tarvitse muistaa kaikkia muutoksia ulkoa. Git näyttää erot puolestasi.

**Muista:** `git diff` ei näytä staging-alueelle jo valmisteltuja muutoksia. Se vertaa työpuuta staging-alueeseen.

## 5. Tarkastele valmisteltuja muutoksia

Lisää muutokset staging-alueelle:

```bash
git add main.py
```

Suorita sitten:

```bash
git status
```

`main.py` näkyy nyt valmisteltuna muutoksena.

Kokeile seuraavaksi:

```bash
git diff
```

Jos et ole tehnyt tiedostoon uusia muutoksia `git add` -komennon jälkeen, tuloste ei näytä juuri valmisteltuja muutoksia.

Tämä johtuu siitä, että tavallinen `git diff` vertaa työpuuta staging-alueeseen.

Jos haluat tarkastella staging-alueelle valmisteltuja muutoksia, käytä:

```bash
git diff --staged
```

Komento näyttää valmistellut muutokset suhteessa viimeisimpään committiin. Näet siis, mitä seuraava commit sisältäisi.

Näiden komentojen ero on tärkeä:

- `git diff` näyttää valmistelun jälkeiset, vielä staging-alueelle lisäämättömät muutokset.
- `git diff --staged` näyttää staging-alueelle valmistellut muutokset.

Voit käyttää molempia komentoja ennen committia varmistaaksesi, että olet tallentamassa juuri haluamasi muutokset.

## 6. Tarkastele commit-historiaa

Aiemmissa osissa käytit komentoa:

```bash
git log --oneline
```

Se näyttää commitit tiiviissä muodossa. Jokaisella rivillä näkyvät commitin lyhyt tunniste ja viesti.

Jos haluat tarkastella viimeisimmän commitin tietoja ja siihen tallennettuja muutoksia, suorita:

```bash
git show
```

Voit myös tarkastella tiettyä committia antamalla sen tunnisteen:

```bash
git show COMMIT_TUNNISTE
```

Korvaa `COMMIT_TUNNISTE` todellisella tunnisteella, jonka näet `git log --oneline` -komennon tulosteessa. Älä kirjoita esimerkin tekstiä sellaisenaan.

Huomaa ero:
- `git log --oneline` näyttää commit-historian tiiviisti.
- `git show` näyttää yksittäisen commitin tiedot ja siihen liittyvät muutokset.

## 7. Kokeile itse

Tee seuraavat vaiheet seikkailupeliprojektissasi:

1. Muuta `main.py`-tiedoston terveyspisteitä.
2. Tallenna tiedosto editorissa.
3. Suorita `git status`.
4. Suorita `git diff` ja tutki tulostetta.
5. Lisää tiedosto staging-alueelle komennolla `git add main.py`.
6. Suorita `git diff` uudelleen.
7. Suorita `git diff --staged` ja tutki valmisteltuja muutoksia.
8. Tarkastele commit-historiaa komennolla `git log --oneline`.

**Pohdi:** Miksi muutokset kannattaa tarkistaa ennen niiden tallentamista commitiksi?

**Vastaus:** Tarkistamalla voit huomata vahingossa tehdyt muutokset, virheet tai keskeneräiset muutokset ennen kuin tallennat ne osaksi projektin historiaa.

## 8. Riko ja korjaa

Tässä harjoituksessa kokeilet muutoksen lisäämistä ja poistamista.

Lisää `main.py`-tiedoston loppuun ylimääräinen tulostusrivi:

```python
print("Tämä on vain kokeilu.")
```

Tallenna tiedosto ja suorita:

```bash
git diff
```

Etsi tulosteesta lisäämäsi rivi.

Poista sitten kyseinen rivi tiedostosta ja tallenna tiedosto uudelleen.

Suorita:

```bash
git diff
```

Jos lisäämäsi rivi oli ainoa työpuun muutos eikä sitä ollut valmisteltu staging-alueelle, rivi ei enää näy diff-tulosteessa.

Tässä harjoituksessa poistit kokeilurivin itse editorissa. Et käyttänyt Git-komentoa palauttamaan tiedostoa.

Jos olet jo käyttänyt `git add` -komentoa, staging-alueella voi edelleen olla aiemmin valmisteltu versio muutoksesta. Tarkista silloin molemmat näkymät:

```bash
git diff
git diff --staged
```

Ne voivat näyttää eri tilanteita, koska ne vertaavat eri sisältöjä.

## 9. Tarkista, mitä opit

Vastaa omin sanoin:

1. Mitä `git status` kertoo?
2. Mitä `git diff` näyttää?
3. Miten `git diff --staged` eroaa tavallisesta `git diff` -komennosta?
4. Millä komennolla tarkastelet commit-historiaa?
5. Millä komennolla tarkastelet viimeisimmän commitin sisältöä ja muutoksia?
6. Miksi muutokset kannattaa tarkistaa ennen committia?

**Vastaukset tarkistettavaksi**

1. `git status` näyttää repositoryn tilan ja tiedostojen muutosten tilanteen.
2. `git diff` näyttää työpuun muutokset, joita ei ole valmisteltu staging-alueelle.
3. `git diff --staged` näyttää staging-alueelle valmistellut muutokset suhteessa viimeisimpään committiin.
4. `git log --oneline`.
5. `git show`.
6. Tarkistus auttaa löytämään vahingossa tehdyt tai keskeneräiset muutokset ennen niiden tallentamista.

## 10. Osa on valmis, kun…

- [ ] Osaat tarkistaa repositoryn tilan komennolla `git status`.
- [ ] Osaat tarkastella työpuun muutoksia komennolla `git diff`.
- [ ] Ymmärrät tavallisen `git diff` -komennon ja `git diff --staged` -komennon eron.
- [ ] Osaat tarkastella commit-historiaa komennolla `git log --oneline`.
- [ ] Osaat tarkastella commitin sisältöä komennolla `git show`.
- [ ] Ymmärrät, miksi muutokset kannattaa tarkistaa ennen committia.

## Seuraavaksi

[Seuraava osa: 05 – Muutosten palautus](../05_muutosten_palautus/)

[← Edellinen osa: 03 – Ensimmäinen commit](../03_ensimmainen_commit/)

[← Kurssin etusivulle](../README.md)