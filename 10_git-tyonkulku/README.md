# 10 – Git-työnkulku ja yhteenveto

## Miten Git toimii käytännössä?

Tällä kurssilla olet tutustunut Gitin peruskäsitteisiin ja harjoitellut niiden avulla seikkailupelin kehittämistä.

Olet oppinut tallentamaan muutoksia, tarkastelemaan historiaa, palauttamaan tiedostoja, luomaan haaroja, yhdistämään muutoksia, ratkaisemaan yhdistämiskonflikteja ja käyttämään GitHubia.

Tässä osassa yhdistät nämä taidot yhdeksi käytännölliseksi työnkuluksi.

Tässä osassa opit:

- tarkistamaan projektin tilan ennen muutoksia
- tekemään ja testaamaan muutoksia hallitusti
- tallentamaan järkeviä committeja
- kehittämään uutta ominaisuutta omassa haarassa
- yhdistämään haaroja ja lähettämään muutoksia GitHubiin
- valitsemaan tilanteeseen sopivan Git-komennon.

## 1. Tarkista projektin tila

Avaa terminaali kurssilla käyttämässäsi `seikkailupeli`-repositoriossa. Aloita tarkistamalla, missä repositoriossa ja haarassa työskentelet.

```bash
git status
git branch
```

`git status` kertoo, onko tiedostoissa muutoksia ja onko niitä lisätty staging-alueelle.

`git branch` näyttää paikalliset haarat. Nykyisen haaran edessä on tähti (`*`).

Tarkista myös viimeisimmät commitit:

```bash
git log --oneline -5
```

Komento näyttää enintään viisi viimeisintä committia.

Ennen uuden työn aloittamista varmista, että ymmärrät nykyisen tilanteen. Jos sinulla on keskeneräisiä muutoksia, päätä, haluatko jatkaa niiden työstämistä vai tallentaa ne commitiksi. Älä hävitä muutoksia vain siksi, että haluat aloittaa uuden tehtävän.

## 2. Hae etämuutokset tarvittaessa

Jos repositoriosi on yhdistetty GitHubiin ja muut ovat voineet tehdä muutoksia samaan haaraan, hae uusimmat muutokset ennen työskentelyä.

Tarkista ensin tilanne:

```bash
git status
```

Jos työskentelytilasi on kunnossa ja nykyisellä haaralla on etäseuranta määritettynä, voit suorittaa:

```bash
git pull
```

Komento hakee muutoksia etärepositoriosta ja integroi ne nykyiseen haaraan. Jos paikalliset ja etämuutokset ovat ristiriidassa, saatat joutua ratkaisemaan yhdistämiskonfliktin.

Jos haluat ensin hakea tiedot yhdistämättä niitä automaattisesti, käytä:

```bash
git fetch
```

Voit sen jälkeen tarkastella historiaa ja päättää, miten haluat käsitellä etärepositoriossa olevia muutoksia.

Jos repositoriota ei ole yhdistetty etärepositorioon, tätä vaihetta ei tarvitse tehdä.

## 3. Kehitä uutta ominaisuutta omassa haarassa

Uutta ominaisuutta kannattaa kehittää omassa haarassa. Näin voit tehdä muutoksia erillään päähaarasta ja yhdistää ne vasta, kun olet valmis.

Varmista ensin, että olet `main`-haarassa ja työskentelytilasi on puhdas:

```bash
git switch main
git status
```

Luo uusi haara:

```bash
git switch -c uusi-ominaisuus
```

Korvaa `uusi-ominaisuus` kuvaavalla nimellä, jos haluat nimetä haaran toisin. Tässä osassa käytämme lopputehtävässä haaraa `aarrearkku`.

Avaa seikkailupelin `main.py` ja lisää uusi ominaisuus. Voit esimerkiksi kysyä pelaajalta, haluaako hän tutkia metsästä löytyvää sivupolkua.

Lisää ohjelmaan:

```python
vastaus = input("Tutkitko salaperäisen sivupolun? (kyllä/ei) ")

if vastaus.lower() == "kyllä":
    print("Löydät polun päästä vanhan arkun.")
else:
    print("Jatkat matkaasi metsän läpi.")
```

Jos ohjelmassasi on jo vastaava toiminto, voit siirtyä suoraan seuraavaan vaiheeseen tai kehittää sitä edelleen.

Tallenna tiedosto ja suorita ohjelma:

```bash
python main.py
```

Kokeile molempia vastausvaihtoehtoja. Varmista, että ohjelma toimii ennen muutoksen tallentamista Gitiin.

## 4. Tarkastele muutoksia

Ennen muutosten lisäämistä staging-alueelle tarkista, mitä tiedostoissa on muuttunut.

```bash
git status
git diff
```

`git diff` näyttää työskentelyalueen muutokset suhteessa staging-alueeseen. Se ei siis näytä suoraan kaikkia muutoksia viimeisimpään committiin verrattuna.

Jos haluat nähdä, mitä muutoksia olet jo lisännyt staging-alueelle, käytä:

```bash
git diff --staged
```

Tarkastele muutoksia rauhassa. Tarkoituksena on varmistaa, että seuraavaan committiin päätyvät juuri ne muutokset, jotka haluat tallentaa.

## 5. Lisää ja tallenna muutos

Lisää `main.py` staging-alueelle:

```bash
git add main.py
```

Tarkista seuraavaan committiin valmistellut muutokset:

```bash
git diff --staged
```

Tallenna muutos commitilla:

```bash
git commit -m "Lisää valinta salaperäiselle sivupolulle"
```

Hyvä commit-viesti kertoo lyhyesti, mitä muuttui.

Tarkista lopuksi:

```bash
git status
git log --oneline -5
```

Kun kaikki muutokset on tallennettu eikä staging-alueella tai työskentelyalueella ole keskeneräisiä muutoksia, `git status` ilmoittaa yleensä, että työpuu on puhdas.

Muista, että commit tallentaa muutoksen paikalliseen Git-historiaan. Se ei vielä itsessään lähetä muutosta GitHubiin.

## 6. Yhdistä haara päähaaraan

Kun uusi ominaisuus on valmis ja testattu, voit yhdistää sen `main`-haaraan.

Vaihda ensin päähaaraan:

```bash
git switch main
```

Yhdistä ominaisuushaara:

```bash
git merge uusi-ominaisuus
```

Korvaa `uusi-ominaisuus` sen haaran nimellä, jossa teit muutokset.

Tarkista yhdistämisen jälkeen:

```bash
git status
git log --oneline --graph --all
```

Suorita myös ohjelma ja varmista, että uusi ominaisuus toimii `main`-haarassa.

Jos yhdistäminen aiheuttaa konfliktin, ratkaise se ennen kuin jatkat. Jos haluat säilyttää ominaisuushaaran myöhempää käyttöä varten, sitä ei tarvitse poistaa yhdistämisen jälkeen.

## 7. Lähetä muutokset GitHubiin

Jos repositoriosi on yhdistetty GitHubiin ja nykyisellä haaralla on etäseuranta määritettynä, voit lähettää commitit komennolla:

```bash
git push
```

Jos olet yhdistänyt ominaisuushaaran `main`-haaraan ja haluat julkaista yhdistetyn tuloksen, vaihda ensin `main`-haaraan ja lähetä se:

```bash
git switch main
git push
```

Jos `main`-haaralla ei ole seurantasuhdetta määritettynä, voit tarvittaessa käyttää:

```bash
git push -u origin main
```

Tämä edellyttää, että etärepositorio on määritetty nimellä `origin` ja että sinulla on oikeus lähettää siihen muutoksia.

Avaa lopuksi repositorio GitHubissa ja tarkista, että haluamasi commitit näkyvät siellä.

## 8. Mitä jos jokin menee pieleen?

Gitissä on erilaisia komentoja eri tilanteisiin. Valitse komento sen mukaan, missä vaiheessa muutoksesi ovat.

| Tilanne | Komento | Vaikutus |
|---|---|---|
| Haluat nähdä työskentelyalueen muutokset | `git diff` | Näyttää muutokset, joita ei ole lisätty staging-alueelle. |
| Haluat nähdä staging-alueen muutokset | `git diff --staged` | Näyttää seuraavaan committiin valmistellut muutokset. |
| Haluat palauttaa tiedoston keskeneräiset muutokset | `git restore main.py` | Palauttaa tiedoston staging-alueen sisältöön ja voi hävittää tekemäsi muokkaukset. |
| Haluat poistaa tiedoston staging-alueelta | `git restore --staged main.py` | Poistaa tiedoston staging-alueelta mutta säilyttää sen työskentelyalueen muutokset. |
| Haluat tarkastella aiempia committeja | `git log --oneline` | Näyttää commit-historian. |
| Haluat hakea etämuutokset ja integroida ne | `git pull` | Hakee muutoksia ja integroi ne nykyiseen haaraan. |
| Haluat lähettää commitit GitHubiin | `git push` | Lähettää committeja etärepositorioon, jos yhteys ja seurantasuhde on määritetty. |

**Varoitus:** `git restore main.py` voi hävittää tiedoston keskeneräiset muutokset, joita ei ole tallennettu committiin. Tarkista ensin `git status` ja `git diff`. Jos haluat säilyttää keskeneräisen työn, tallenna se turvallisesti ennen palauttamista.

Jos haluat perua jo tehdyn commitin vaikutukset, tutustu komentoon `git revert`. Se luo uuden commitin, joka kumoaa aiemman muutoksen. Älä käytä historian muuttamiseen tarkoitettuja komentoja ymmärtämättä niiden vaikutuksia.

Jos yhdistäminen epäonnistuu tai syntyy konflikti, älä aloita uusia yhdistämisiä sokkona. Tarkista ensin `git status` ja selvitä, missä vaiheessa Gitin toiminto on.

## 9. Lopputehtävä: kehitä seikkailupeliä

Nyt käytät koko kurssin aikana oppimiasi taitoja yhdessä tehtävässä.

### Tehtävän tavoite

Lisää peliin toiminto, jossa pelaaja voi tutkia metsästä löytyvän arkun ja päättää, avaako hän sen.

### Työvaiheet

1. Tarkista repositorion tila:

   ```bash
   git status
   ```

2. Varmista, että olet `main`-haarassa ja työskentelytilasi on puhdas. Luo uusi haara:

   ```bash
   git switch main
   git switch -c aarrearkku
   ```

3. Avaa `main.py` ja lisää ohjelman loppuun seuraava koodi. Jos vastaava toiminto on jo olemassa, muokkaa nykyistä koodia sen sijaan, että lisäisit saman toiminnon kahdesti.

   ```python
   vastaus = input("Tutkitko salaperäisen sivupolun? (kyllä/ei) ")

   if vastaus.lower() == "kyllä":
       print("Löydät polun päästä vanhan arkun.")
       avaa_arkku = input("Avataanko arkku? (kyllä/ei) ")

       if avaa_arkku.lower() == "kyllä":
           print("Arkun sisältä löytyy kultakolikoita!")
       else:
           print("Jätät arkun paikoilleen ja jatkat matkaa.")
   else:
       print("Jatkat matkaasi metsän läpi.")
   ```

4. Tallenna tiedosto ja suorita ohjelma:

   ```bash
   python main.py
   ```

5. Testaa vähintään nämä tilanteet:
   - pelaaja tutkii sivupolun ja avaa arkun
   - pelaaja tutkii sivupolun mutta ei avaa arkkua
   - pelaaja ei tutki sivupolkua.

6. Tarkastele muutoksia:

   ```bash
   git status
   git diff
   ```

7. Lisää muutokset staging-alueelle ja tarkista ne:

   ```bash
   git add main.py
   git diff --staged
   ```

8. Tallenna muutos commitilla:

   ```bash
   git commit -m "Lisää aarrearkun tutkiminen"
   ```

9. Vaihda `main`-haaraan ja yhdistä ominaisuus:

   ```bash
   git switch main
   git merge aarrearkku
   ```

10. Tarkista ohjelma ja commit-historia:

    ```bash
    python main.py
    git status
    git log --oneline --graph --all
    ```

11. Jos repositoriosi on yhdistetty GitHubiin, lähetä yhdistetyt muutokset:

    ```bash
    git push
    ```

    Jos `main`-haaralla ei ole etäseurantaa määritettynä, käytä tarvittaessa komentoa `git push -u origin main`.

### Onnistumisen ehdot

Tehtävä on valmis, kun:

- [ ] uusi ominaisuus toimii
- [ ] kaikki kolme testitilannetta on kokeiltu
- [ ] muutos on tallennettu commitilla
- [ ] ominaisuushaara on yhdistetty `main`-haaraan
- [ ] Gitin työskentelytila on kunnossa
- [ ] muutokset näkyvät GitHubissa, jos käytät etärepositoriota.

## 10. Kurssin yhteenveto

Tämän kurssin jälkeen sinun pitäisi ymmärtää seuraavat asiat:

- **Git** tallentaa projektin muutoksia ja niiden historiaa.
- **Repository** sisältää projektin versionhallinnan tiedot.
- **Commit** tallentaa muutoksia osaksi Git-historiaa.
- `git status` ja `git diff` auttavat tarkastelemaan keskeneräistä työtä.
- `git add` lisää muutoksia staging-alueelle ennen committia.
- `git restore` auttaa palauttamaan tiedoston muutoksia, mutta voi myös hävittää niitä.
- **Branch** mahdollistaa erillisen kehityslinjan.
- `git merge` yhdistää haarojen muutoksia.
- **Yhdistämiskonflikti** vaatii päätöksen siitä, miltä lopullisen koodin pitää näyttää.
- `git fetch` hakee tietoja etärepositoriosta, kun taas `git pull` hakee ja integroi muutoksia.
- `git push` lähettää committeja etärepositorioon.
- **GitHub** auttaa säilyttämään ja jakamaan repositorioita sekä tekemään yhteistyötä.

## Lopuksi

Git ei ole vain työkalu koodin tallentamiseen. Se auttaa kokeilemaan uusia asioita, seuraamaan muutoksia, palautumaan virheistä ja työskentelemään yhdessä muiden kanssa.

Hyvä perusrutiini on yksinkertainen:

1. Tarkista tila.
2. Tee pieni muutos.
3. Testaa se.
4. Tarkastele muutoksia.
5. Tallenna toimiva kokonaisuus commitilla.
6. Yhdistä haara, kun ominaisuus on valmis.
7. Lähetä muutokset etärepositorioon, kun se on tarpeen.

Mitä enemmän käytät Gitiä oikeissa projekteissa, sitä luonnollisemmaksi tämä työnkulku muuttuu.

## Kurssin päättyessä

Olet harjoitellut Gitin perustoimintoja käytännössä. Seuraava askel on käyttää niitä omissa ohjelmointiprojekteissasi: tee pieniä muutoksia, tallenna ne selkeisiin committeihin ja tarkastele historiaa aina tarvittaessa.

[← Edellinen osa: 09 – Yhdistämiskonfliktit](../09_yhdistamiskonfliktit/)

[← Kurssin etusivulle](../README.md)