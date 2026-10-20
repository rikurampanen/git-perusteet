# Git-perusteet – käytännönläheinen opas versionhallintaan

Tervetuloa Git-perusteet-kurssille!

Tällä kurssilla opit käyttämään Gitiä ohjelmistokehityksen versionhallintaan. Opit tallentamaan muutoksia, seuraamaan projektin historiaa, kokeilemaan uusia ominaisuuksia omissa haaroissaan ja yhdistämään muutokset takaisin päähaaraan.

Kurssin esimerkkiprojektina toimii Pythonilla toteutettava tekstiseikkailu, jota kehitetään vaihe vaiheelta. Opit Gitin komennot käytännössä samalla, kun tutustut ohjelman kehittämiseen ja muuttamiseen.

Kurssi sopii itsenäiseen opiskeluun sekä opetuksen tueksi. Et tarvitse aiempaa kokemusta Gitistä, mutta tarvitset perustaidot tiedostojen muokkaamisesta, Python-ohjelman suorittamisesta ja terminaalin käytöstä.

## Mitä opit?

Kurssin jälkeen osaat:

- ymmärtää, mihin Git-versionhallintaa käytetään
- luoda ja tarkastella Git-repositoriota
- tallentaa muutoksia committeina
- tarkastella tiedostojen muutoksia ja commit-historiaa
- palauttaa tiedostojen muutoksia hallitusti
- luoda haaroja ja vaihtaa haarasta toiseen
- yhdistää eri haaroissa tehdyt muutokset
- tunnistaa ja ratkaista yhdistämiskonflikteja
- siirtää muutoksia paikallisen repositorion ja GitHubin välillä
- käyttää Gitin tavallista työnkulkua omissa projekteissasi.

## Kurssin sisältö

Kurssi koostuu kymmenestä osasta. Suosittelemme etenemään järjestyksessä, sillä myöhemmät osat hyödyntävät aiemmin opittuja komentoja ja käsitteitä.

| Osa | Aihe | Keskeiset asiat |
|---|---|---|
| 01 | [Mikä Git on?](01_mika_on_git/) | Versionhallinnan tarkoitus ja hyödyt |
| 02 | [Mikä on Git-repository?](02_repository/) | Repository, `git init` ja `git status` |
| 03 | [Ensimmäinen commit](03_ensimmainen_commit/) | `git add`, `git commit` ja `git log` |
| 04 | [Muutosten tarkastelu](04_muutosten_tarkastelu/) | `git diff`, `git diff --staged` ja `git show` |
| 05 | [Muutosten palautus](05_muutosten_palautus/) | `git restore` ja staging-alueen hallinta |
| 06 | [Haarautuminen ja branchit](06_haarautuminen/) | Haarojen luominen ja vaihtaminen |
| 07 | [Haarojen yhdistäminen](07_haarojen_yhdistaminen/) | `git merge` ja yhdistämisen tarkistaminen |
| 08 | [Etärepositorio ja GitHub](08_etarepositorio/) | `git remote`, `git push`, `git fetch` ja `git pull` |
| 09 | [Yhdistämiskonfliktit](09_yhdistamiskonfliktit/) | Konfliktin tunnistaminen ja ratkaiseminen |
| 10 | [Git-työnkulku ja yhteenveto](10_git-tyonkulku/) | Käytännön työnkulku ja lopputehtävä |

## Miten kurssia käytetään?

Jokaisessa osassa käsitellään yhtä Gitin keskeistä aihetta. Lue ensin osan `README.md`, seuraa ohjeita ja kokeile komentoja käytännössä.

Kurssin oppimistapa perustuu tekemiseen:

1. **Tutustu** – selvitä, mitä komento tekee ja miksi sitä tarvitaan.
2. **Kokeile** – suorita komento omassa harjoitusrepositoriossasi.
3. **Muokkaa** – tee esimerkkiohjelmaan ohjeistettu muutos.
4. **Tarkastele** – tutki, miten Git tunnistaa muutoksen.
5. **Testaa** – kokeile ohjelmaa ja tarkista muutosten vaikutukset.
6. **Korjaa** – opettele palauttamaan tai yhdistämään muutoksia tarvittaessa.

Älä tyydy vain kopioimaan komentoja. Tarkista niiden tulosteet ja pyri ymmärtämään, mitä Git tekee.

## Esimerkkiprojekti: tekstiseikkailu

Kurssin aikana kehität yksinkertaista Python-tekstiseikkailua. Ohjelma laajenee vähitellen: pelaaja esitellään, metsässä liikutaan, uusia polkuja tutkitaan ja lopulta pelaaja voi löytää aarteen.

Sama projekti auttaa näkemään, miten versionhallinta tukee ohjelmiston kehittämistä. Voit kokeilla muutoksia, tallentaa toimivia versioita ja harjoitella haarojen yhdistämistä.

Git-harjoitusten tarkoituksena ei ole rakentaa mahdollisimman monimutkaista peliä, vaan oppia hallitsemaan ohjelmaan tehtäviä muutoksia.

## Työskentely repositoriossa

Kurssilla on kaksi erillistä kokonaisuutta:

- **Kurssimateriaalit:** sisältävät osien ohjeet ja esimerkkitiedostot.
- **Harjoitusprojekti `seikkailupeli`:** on oma Git-repositoriosi, jossa suoritat Git-komennot ja kehität peliä.

Kurssin osien kansiot eivät ole harjoitusprojektisi. Tee harjoitukset `seikkailupeli`-repositoriossa ja pidä se samana koko kurssin ajan, jotta commit-historia ja haarat muodostavat yhtenäisen kokonaisuuden.

Aloita luomalla harjoitusprojekti osan 02 ohjeiden mukaan. Älä luo uutta repositoriota jokaista osaa varten äläkä suorita `git init` -komentoa uudelleen jo alustetussa harjoitusrepositoriossa.

Osien esimerkkitiedostot näyttävät, miltä ohjelma voi kyseisessä vaiheessa näyttää. Kun ohje pyytää muokkaamaan `main.py`-tiedostoa, tee muutos harjoitusprojektissasi. Älä korvaa koko tiedostoa uudella esimerkillä, ellei ohje nimenomaan pyydä tekemään niin, sillä muuten voit menettää aiemmissa osissa rakentamasi ohjelman.

Jos yhdistät harjoitusprojektin GitHubiin, voit harjoitella myös muutosten lähettämistä etärepositorioon ja niiden hakemista sieltä. Gitin perusasiat voi kuitenkin oppia myös paikallisessa repositoriossa.

## Hyödyllinen perusrutiini

Kun työskentelet projektissa, voit käyttää seuraavaa rutiinia:

```bash
git status
git diff
git add main.py
git diff --staged
git commit -m "Kuvaava viesti muutoksesta"
git status
```

Komennot auttavat tarkistamaan tilanteen, tarkastelemaan muutoksia, valmistelemaan ne commitia varten ja tallentamaan ne historiaan.

Tämä on esimerkki tavallisesta työnkulusta, ei jokaisessa tilanteessa pakollinen komentojärjestys. Jos muutat useita tiedostoja, lisää staging-alueelle ne tiedostot, jotka kuuluvat samaan committiin.

## Ennen aloittamista

Kurssi keskittyy Gitin käyttöön eikä ohjelmointiympäristön asentamiseen. Oletuksena on, että osaat avata projektin tiedostot, suorittaa Python-ohjelman ja käyttää terminaalia.

Jos jokin komento ei toimi odotetusti, tarkista ensin:

- oletko oikeassa projektikansiossa
- mikä haara on käytössä
- mitä `git status` kertoo
- onko tiedosto tallennettu
- seuraako Git kyseistä tiedostoa
- oletko tekemässä komentoa paikallisessa repositoriossa vai etärepositorion kanssa.

Jos jokin tilanne tuntuu epäselvältä, älä suorita palautus- tai yhdistämiskomentoja sokkona. Tarkista ensin nykyinen tilanne ja palaa tarvittaessa kyseisen aiheen ohjeisiin.

## Aloita kurssi

Etene rauhassa, kokeile komentoja käytännössä ja palaa tarvittaessa aiempiin osiin. Tavoitteena on oppia ymmärtämään Gitin toimintaa niin, että osaat käyttää sitä myös omissa projekteissasi.

[Aloita ensimmäisestä osasta: 01 – Mikä Git on?](01_mika_on_git/)