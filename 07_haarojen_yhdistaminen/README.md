# 07 – Haarojen yhdistäminen

## Tavoite

Edellisessä osassa loit uuden haaran ja teit siinä muutoksia seikkailupeliin. Nyt opit yhdistämään haaran muutokset takaisin `main`-haaraan.

Gitissä haarojen yhdistämistä kutsutaan nimellä *merge*.

Opit:
- miksi haaroja yhdistetään
- miten tarkistat nykyisen haaran
- miten yhdistät toisen haaran nykyiseen haaraan
- miten tarkistat yhdistämisen tuloksen
- mitä yhdistämiskonflikti tarkoittaa

## 1. Tarkista haarat

Avaa terminaali seikkailupeliprojektisi kansiossa ja suorita:

```bash
git branch
git status
```

Jos teit edellisen osan harjoitukset, sinulla voi olla esimerkiksi nämä haarat:

```text
* pelaajan-terveys
  main
  uusi-polku
```

Tähdellä merkitty haara on nykyinen haarasi. Haarojen nimet ja järjestys voivat omassa projektissasi olla erilaisia.

Ennen yhdistämistä varmista, että:
- olet seikkailupeliprojektin repositoryssa
- työpuu on puhdas eli keskeneräisiä muutoksia ei ole
- tiedät, minkä haaran haluat yhdistää ja mihin haaraan

Jos työpuussa on keskeneräisiä muutoksia, tarkista ne ja tallenna ne tarvittaessa commitilla ennen jatkamista.

## 2. Vaihda haaraan, johon haluat yhdistää muutokset

Tässä osassa yhdistät `uusi-polku`-haaran muutokset `main`-haaraan.

Vaihda ensin päähaaraan:

```bash
git switch main
```

Tarkista, että olet oikeassa haarassa:

```bash
git branch
git status
```

Nyt `main`-haaran pitäisi olla merkitty tähdellä ja työpuun pitäisi olla puhdas.

**Muista:** `git merge` yhdistää nimetyn haaran muutokset siihen haaraan, jossa olet komennon suoritushetkellä.

## 3. Yhdistä haara

Suorita:

```bash
git merge uusi-polku
```

Git yrittää yhdistää `uusi-polku`-haaran muutokset nykyiseen `main`-haaraan.

Jos `main`-haaraan ei ole tehty yhdistämisen jälkeen uusia committeja, Git voi siirtää `main`-haaran osoittamaan suoraan samaan committiin kuin `uusi-polku`. Tätä kutsutaan *fast-forward*-yhdistämiseksi.

Jos molempiin haaroihin on tehty uusia committeja, Git voi luoda yhdistämiscommitin. Jos samassa tiedostossa on ristiriitaisia muutoksia, yhdistäminen voi vaatia konfliktin ratkaisemista.

## 4. Tarkista yhdistämisen tulos

Tarkista ensin repositoryn tila:

```bash
git status
```

Tarkastele sitten commit-historiaa:

```bash
git log --oneline --graph --all
```

Komento näyttää commitit ja haarojen historian graafisessa muodossa.

Avaa `main.py` ja tarkista, että sivupolun ominaisuus on mukana `main`-haaran versiossa.

Voit myös suorittaa ohjelman ja varmistaa, että se toimii odotetusti.

Kun yhdistäminen on onnistunut, `main` sisältää `uusi-polku`-haaran muutokset. Alkuperäinen `uusi-polku`-haara säilyy edelleen olemassa, vaikka sen muutokset on yhdistetty.

## 5. Mitä jos Git ilmoittaa konfliktista?

Yhdistämiskonflikti tarkoittaa, ettei Git pysty automaattisesti päättämään, miten ristiriitaiset muutokset pitäisi yhdistää.

Konfliktitilanteessa:

1. Suorita `git status` ja tarkista, mitkä tiedostot ovat konfliktissa.
2. Avaa konfliktissa oleva tiedosto.
3. Etsi Gitin lisäämät konfliktimerkinnät.
4. Muokkaa tiedostoa niin, että siihen jää haluttu lopputulos.
5. Poista konfliktimerkinnät ja tallenna tiedosto.
6. Lisää ratkaistu tiedosto staging-alueelle ja viimeistele yhdistäminen Gitin ilmoittamalla tavalla.

Konfliktimerkinnät voivat näyttää esimerkiksi tältä:

```text
<<<<<<< HEAD
Nykyisen haaran versio
=======
Yhdistettävän haaran versio
>>>>>>> uusi-polku
```

`HEAD` viittaa tässä nykyisen haaran versioon. Konfliktin ratkaisun jälkeen tiedostoon pitää jäädä varsinainen sisältö, ei konfliktimerkintöjä.

Tässä osassa sinun ei tarvitse aiheuttaa konfliktia tarkoituksella. Seuraavassa konfliktien käsittelyyn keskittyvässä osassa harjoittelet konfliktin ratkaisemista vaihe vaiheelta.

## 6. Kokeile itse

Tee harjoitus omassa seikkailupeliprojektissasi.

1. Vaihda `main`-haaraan:

   ```bash
   git switch main
   ```

2. Tarkista, että työpuu on puhdas:

   ```bash
   git status
   ```

3. Luo uusi haara ja siirry siihen:

   ```bash
   git switch -c metsan-aarre
   ```

4. Lisää `main.py`-tiedoston loppuun tulostusrivi:

   ```python
   print("Löydät metsästä vanhan aarteen.")
   ```

5. Tallenna tiedosto ja tarkista muutokset:

   ```bash
   git status
   git diff
   ```

6. Tallenna muutos commitilla:

   ```bash
   git add main.py
   git commit -m "Lisää metsän aarre"
   ```

7. Vaihda takaisin `main`-haaraan:

   ```bash
   git switch main
   ```

8. Tarkista `main.py`. Uuden aarteen tulostusrivin pitäisi puuttua, koska muutosta ei ole vielä yhdistetty.

9. Yhdistä haara:

   ```bash
   git merge metsan-aarre
   ```

10. Tarkista `main.py`, repositoryn tila ja commit-historia:

    ```bash
    git status
    git log --oneline --graph --all
    ```

Varmista lopuksi, että aarteen tulostusrivi on mukana `main`-haarassa.

## 7. Tarkista, mitä opit

Vastaa omin sanoin:

1. Mitä haaran yhdistäminen tarkoittaa?
2. Miksi pitää vaihtaa ensin siihen haaraan, johon haluaa yhdistää muutokset?
3. Mitä komento `git merge uusi-polku` tekee, kun olet `main`-haarassa?
4. Mitä *fast-forward*-yhdistäminen tarkoittaa?
5. Mitä yhdistämiskonflikti tarkoittaa?
6. Millä komennolla voit tarkastella haarojen historiaa graafisesti?

**Vastaukset tarkistettavaksi**

1. Yhdistäminen tuo toisen haaran muutokset nykyiseen haaraan.
2. Koska `git merge` yhdistää muutokset aktiiviseen haaraan.
3. Se yrittää yhdistää `uusi-polku`-haaran muutokset `main`-haaraan.
4. Git siirtää nykyisen haaran osoittamaan suoraan yhdistettävän haaran uudempaan committiin, kun historia sallii sen.
5. Git ei pysty automaattisesti ratkaisemaan ristiriitaisia muutoksia.
6. `git log --oneline --graph --all`.

## 8. Osa on valmis, kun…

- [ ] Ymmärrät, mitä haaran yhdistäminen tarkoittaa.
- [ ] Osaat vaihtaa siihen haaraan, johon haluat yhdistää muutokset.
- [ ] Osaat yhdistää haaran komennolla `git merge haaran-nimi`.
- [ ] Ymmärrät, että Git voi yhdistää muutokset automaattisesti tai ilmoittaa yhdistämiskonfliktista.
- [ ] Osaat tarkastella haarojen historiaa komennolla `git log --oneline --graph --all`.
- [ ] Osaat tarkistaa, että yhdistetyt muutokset näkyvät oikeassa haarassa.

## Seuraavaksi

[Seuraava osa: 08 – Etärepositorio](../08_etarepositorio/)

[← Edellinen osa: 06 – Haarautuminen ja branchit](../06_haarautuminen/)

[← Kurssin etusivulle](../README.md)