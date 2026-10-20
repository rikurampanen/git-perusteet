# 08 – Etärepositorio ja GitHub

## Mitä etärepositorio tarkoittaa?

Tähän asti olet tehnyt muutoksia Git-repositorion paikalliseen versioon omalla koneellasi. Voit myös tallentaa repositoriosta etäversion esimerkiksi GitHubiin.

**Paikallinen repositorio** on omalla koneellasi. **Etärepositorio** on toisessa paikassa, kuten GitHubissa, oleva repositorio, johon voit lähettää committeja ja josta voit hakea muiden tekemiä muutoksia.

GitHub on Git-repositorioiden säilyttämiseen ja jakamiseen tarkoitettu verkkopalvelu. Git ja GitHub eivät ole sama asia: Git hallitsee projektin versiohistoriaa, kun taas GitHub tarjoaa verkkopalvelun repositorioiden säilyttämiseen ja yhteistyöhön.

Tässä osassa opit:

- mitä paikallinen repositorio ja etärepositorio tarkoittavat
- miten tarkistat etärepositoriosi osoitteen
- miten lähetät committeja GitHubiin
- miten haet etärepositoriosta uusia muutoksia
- mitä komennot `push`, `fetch` ja `pull` tarkoittavat.

## 1. Tarkista etärepositorio

Avaa terminaali kurssilla käyttämässäsi `seikkailupeli`-repositoriossa ja suorita:

```bash
git remote -v
```

Jos repositorio on yhdistetty GitHubiin, tuloste voi näyttää esimerkiksi tältä:

```text
origin  https://github.com/kayttaja/seikkailupeli.git (fetch)
origin  https://github.com/kayttaja/seikkailupeli.git (push)
```

Tulosteessa:

- `origin` on etärepositoriolle annettu nimi. Se on yleinen oletusnimi.
- `fetch` kertoo osoitteen, josta Git hakee tietoja.
- `push` kertoo osoitteen, johon Git lähettää muutoksia.

Jos komento ei tulosta mitään, paikalliseen repositorioosi ei ole määritetty etärepositoriota. Voit jatkaa lukemista, mutta käytännön lähetysharjoitus edellyttää GitHubiin yhdistettyä repositoriota.

Jos haluat yhdistää repositoriosi GitHubiin, tarvitset ensin GitHubissa luodun repositorion. Kun sinulla on sen osoite, voit lisätä sen paikalliseen repositorioosi näin:

```bash
git remote add origin ETAREPOSITORION_OSOITE
```

Korvaa `ETAREPOSITORION_OSOITE` GitHubissa näkyvällä repositorion osoitteella. Älä kirjoita paikkamerkkiä sellaisenaan.

Jos `origin` on jo määritetty, älä suorita lisäyskomentoa uudelleen. Tarkista ensin nykyinen osoite komennolla `git remote -v`.

## 2. Lähetä commitit GitHubiin: `push`

Kun olet tehnyt commitin paikallisesti, voit lähettää sen etärepositorioon `push`-komennolla.

Tarkista ensin nykyinen haara:

```bash
git branch
```

Tähtimerkki (`*`) osoittaa, mikä haara on aktiivinen.

Jos olet `main`-haarassa ja etärepositorion `main`-haara on jo käytössä, lähetä commitit komennolla:

```bash
git push origin main
```

Komento lähettää paikallisen `main`-haaran commitit `origin`-etärepositorion `main`-haaraan. Jos etärepositoriossa on muutoksia, joita paikallisesta historiastasi puuttuu, lähetys ei välttämättä onnistu ennen kuin haet ja yhdistät nämä muutokset.

Jos julkaiset uuden haaran ensimmäistä kertaa, voit käyttää:

```bash
git push -u origin uuden-haaran-nimi
```

Korvaa `uuden-haaran-nimi` oman haarasi nimellä. `-u` asettaa seurantasuhteen paikallisen haaran ja etähaaran välille. Sen jälkeen voit yleensä käyttää kyseisessä haarassa lyhyempiä `git push`- ja `git pull`-komentoja.

**Muista:** `git push` ei tallenna muutoksia commitiksi. Tee ensin commit paikallisesti ja lähetä se vasta sen jälkeen.

## 3. Hae tietoa etärepositoriosta: `fetch`

Etärepositoriossa saattaa olla committeja, joita paikallisessa repositoriossasi ei vielä ole.

Voit hakea ne ja päivittää etähaarojen seurantatiedot komennolla:

```bash
git fetch origin
```

Tämä ei automaattisesti yhdistä haettuja muutoksia nykyiseen paikalliseen haaraasi. Voit siis tarkastella uutta historiaa ennen kuin päätät, miten muutokset yhdistetään.

Tarkastele tämän jälkeen haaroja ja historiaa:

```bash
git log --oneline --graph --all
```

Komento näyttää commit-historian eri haaroista. Jos etärepositoriossa on uusia committeja, ne voivat näkyä esimerkiksi `origin/main`-haaran yhteydessä.

**Muista:** `fetch` hakee tiedot, mutta ei itsessään tuo muutoksia nykyiseen haaraasi.

## 4. Hae ja yhdistä muutokset: `pull`

Komento `git pull` hakee etärepositoriosta muutoksia ja integroi ne nykyiseen haaraasi. Tavallisesti tämä tarkoittaa yhdistämistä, mutta tarkka toimintatapa voi riippua Gitin asetuksista.

Jos paikallinen `main`-haarasi seuraa etärepositorion `main`-haaraa, voit toimia näin:

```bash
git switch main
git status
git pull
```

Tarkista ennen `pull`-komentoa, että työskentelytilanteesi on kunnossa. Jos sinulla on keskeneräisiä muutoksia, tallenna ne tarvittaessa commitiksi tai käsittele ne ennen etämuutosten hakemista.

Jos paikallinen ja etärepositorion historia eroavat toisistaan, Git voi joutua yhdistämään muutoksia. Jos samoja kohtia on muokattu ristiriitaisesti, yhdistämisessä voi syntyä konflikti. Opit ratkaisemaan tällaisia tilanteita seuraavassa osassa.

**Muista:** `pull` hakee muutokset ja integroi ne nykyiseen haaraasi. Se ei tarkoita samaa kuin pelkkä `fetch`.

## 5. `push`, `fetch` ja `pull` – mitä eroa niillä on?

| Komento | Mitä se tekee? |
|---|---|
| `git push` | Lähettää paikallisia committeja etärepositorioon. |
| `git fetch` | Hakee uusia committeja ja päivittää etähaarojen seurantatiedot, mutta ei yhdistä muutoksia nykyiseen haaraan. |
| `git pull` | Hakee muutoksia ja integroi ne nykyiseen haaraan. |

Muistisääntö:

- **Push:** lähetä commitit eteenpäin.
- **Fetch:** hae uudet tiedot ja tarkastele niitä.
- **Pull:** hae muutokset ja tuo ne nykyiseen haaraan.

## 6. Kokeile itse

Tee harjoitus kurssilla käyttämässäsi `seikkailupeli`-repositoriossa, jos se on yhdistetty GitHubiin.

1. Tarkista etärepositorio komennolla `git remote -v`.
2. Tarkista nykyinen haara komennolla `git branch`.
3. Tarkista työskentelytilanne komennolla `git status`.
4. Tee pieni muutos `main.py`-tiedostoon. Voit lisätä esimerkiksi rivin:

   ```python
   print("Kuulet kaukaa salaperäistä ääntä.")
   ```

   Jos olet jo lisännyt tämän rivin aiemmassa harjoituksessa, tee jokin muu pieni muutos.

5. Tarkastele muutosta komennolla:

   ```bash
   git diff
   ```

6. Lisää tiedosto staging-alueelle ja tee commit:

   ```bash
   git add main.py
   git commit -m "Lisää uusi tapahtuma seikkailuun"
   ```

7. Lähetä commit GitHubiin:

   ```bash
   git push
   ```

   Tämä lyhyt komento toimii, jos nykyisellä haaralla on etärepositorio ja seurantasuhde määritettynä. Muussa tapauksessa tarkista haaran nimi ja käytä tarvittaessa oikeaa `git push origin haaran-nimi` -komentoa.

8. Avaa repositoriosi GitHubissa ja tarkista, että commit ja muutos näkyvät siellä.
9. Hae etärepositorion tiedot:

   ```bash
   git fetch origin
   ```

10. Tarkastele historiaa:

    ```bash
    git log --oneline --graph --all
    ```

Jos GitHub-repositoriota ei ole vielä yhdistetty paikalliseen repositorioosi, pyydä opettajalta sopiva harjoitusrepositorio tai käytä omaa repositoriotasi. Varmista ennen lähettämistä, että sinulla on oikeus tehdä muutoksia kyseiseen etärepositorioon.

## Osa on valmis, kun…

- [ ] Ymmärrät paikallisen repositorion ja etärepositorion eron.
- [ ] Osaat tarkistaa etärepositorion tiedot komennolla `git remote -v`.
- [ ] Ymmärrät, mitä `git push` tekee.
- [ ] Ymmärrät eron komentojen `git fetch` ja `git pull` välillä.
- [ ] Osaat lähettää commitin GitHubiin, kun etärepositorio on määritetty.
- [ ] Ymmärrät, miten GitHub auttaa projektin jakamisessa ja yhteistyössä.

## Seuraavaksi

[Seuraava osa: 09 – Yhdistämiskonfliktit](../09_yhdistamiskonfliktit/)

[← Edellinen osa: 07 – Haarojen yhdistäminen](../07_haarojen_yhdistaminen/)

[← Kurssin etusivulle](../README.md)