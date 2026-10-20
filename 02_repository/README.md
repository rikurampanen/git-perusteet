# 02 – Mikä on Git-repository?

## Tavoite

Tässä osassa opit, mikä Git-repository on ja miten projekti otetaan Gitin versionhallintaan.

Opit:
- mitä repository tarkoittaa
- mitä eroa on tavallisella kansiolla ja Git-repositorylla
- miten alustat uuden Git-repositoryn
- miten tarkistat repositoryn tilan

## 1. Repository on projektin versionhallittu kokonaisuus

Edellisessä osassa tutustuit Gitiin ja versionhallinnan ideaan.

Nyt otetaan seuraava askel.

**Repository**, josta käytetään usein myös lyhennettä *repo*, on projektin kokonaisuus, jonka muutoksia Git hallitsee. Repository sisältää projektin tiedostot ja Gitin ylläpitämän tiedon niiden historiasta.

Esimerkiksi seikkailupeliprojektissa voi olla tällaisia tiedostoja:

```text
seikkailupeli/
├── README.md
└── main.py
```

`main.py` sisältää pelin ohjelmakoodin. `README.md` kertoo, mikä projekti on ja miten sitä käytetään.

Kun otat kansion Gitin hallintaan, voit alkaa tallentaa projektin muutoksia ja tarkastella niiden historiaa.

Tällä kurssilla kehität samaa seikkailupeliä vaihe vaiheelta. Käytät siis samaa harjoitusprojektia kaikissa osissa.

**Tärkeää:** kurssimateriaalin kansio ja oma `seikkailupeli`-harjoituskansiosi ovat eri asioita. Git-komennot suoritetaan harjoitusprojektin kansiossa, ellei ohjeessa erikseen sanota muuta.

## 2. Tavallinen kansio ja Git-repository

Tavallinen kansio sisältää tiedostoja. Git-repository sisältää niiden lisäksi Gitin tarvitsemat versionhallinnan tiedot.

Kun Git-repository alustetaan, Git luo kansioon piilotetun `.git`-kansion.

Esimerkiksi:

```text
seikkailupeli/
├── .git/
├── README.md
└── main.py
```

`.git`-kansio sisältää Gitin ylläpitämät tiedot, kuten commit-historian ja haarat. Älä poista tai muokkaa sitä käsin.

Huomaa myös ero Gitin ja GitHubin välillä:

- **Git** on versionhallintatyökalu, jota käytät projektin muutosten hallintaan.
- **GitHub** on verkkopalvelu, jossa voit säilyttää Git-repositoryn etäversion ja jakaa projektin muiden kanssa.

Opit yhdistämään projektin GitHubiin myöhemmin kurssin osassa 8.

## 3. Luo harjoitusprojekti

Luo itsellesi kansio nimeltä `seikkailupeli`. Luo sen sisälle tiedosto `main.py`.

Kirjoita tiedostoon seuraava ohjelma:

```python
pelaaja = input("Mikä on nimesi? ")
terveys = 100

print(f"Tervetuloa seikkailuun, {pelaaja}!")
print(f"Terveytesi on {terveys}.")
print("Edessäsi on synkkä metsä.")
```

Suorita ohjelma ja varmista, että se toimii.

Tässä vaiheessa sinulla on tavallinen projektikansio, jossa on Python-ohjelma. Et ole vielä tallentanut projektin versiota Gitiin.

Pidä tämä harjoitusprojekti tallessa. Jatkat sen kehittämistä kurssin seuraavissa osissa.

## 4. Alusta Git-repository

Avaa komentorivi niin, että olet juuri luomasi `seikkailupeli`-kansion sisällä.

Suorita:

```bash
git init
```

Komento alustaa nykyiseen kansioon uuden Git-repositoryn.

Tarkka tuloste voi vaihdella Git-version ja ympäristön mukaan. Tarkoitus on, että Git luo projektikansioon `.git`-kansion ja ottaa kansion versionhallinnan käyttöön.

**Mitä juuri tapahtui?**

Et vielä tallentanut projektin tiedostoja commitiksi. Loit Git-repositoryn, jossa voit alkaa hallita projektin muutoksia.

Muista suorittaa `git init` vain silloin, kun kyseistä kansiota ei ole vielä alustettu Git-repositoryksi. Älä suorita komentoa kurssimateriaalin kansiossa tämän harjoituksen vuoksi.

## 5. Tarkista repositoryn tila

Varmista ensin, että olet edelleen `seikkailupeli`-kansiossa.

Suorita:

```bash
git status
```

Komento näyttää repositoryn nykyisen tilan.

Koska `main.py` on luotu ennen ensimmäistä committia eikä sitä ole lisätty staging-alueelle, Git ilmoittaa sen tavallisesti seuraamattomaksi tiedostoksi (*untracked file*).

Tämä tarkoittaa, että tiedosto on olemassa projektikansiossa, mutta sitä ei ole vielä valmisteltu committiin.

Muista nämä kaksi komentoa:

- `git init` alustaa uuden repositoryn.
- `git status` kertoo repositoryn tilanteen.

## 6. Kokeile itse

Tee seuraavat vaiheet:

1. Avaa `seikkailupeli`-kansio komentorivillä.
2. Suorita `git init`.
3. Suorita `git status`.
4. Etsi tulosteesta `main.py`.
5. Tarkista, ilmoittaako Git tiedoston seuraamattomaksi.

Pohdi:

- Miksi Git näyttää tiedoston, vaikka et ole vielä tallentanut sitä commitiksi?
- Mitä eroa on sillä, että tiedosto on olemassa, ja sillä, että sen muutokset on tallennettu Gitin historiaan?

**Vastaus:** Git tunnistaa tiedoston projektikansiossa, mutta sitä ei ole vielä lisätty staging-alueelle eikä tallennettu commitiksi. Opit lisäämään tiedoston ja tekemään ensimmäisen commitin seuraavassa osassa.

## 7. Riko ja korjaa

Kokeillaan, mitä tapahtuu, jos suoritat Git-komennon väärässä paikassa.

Siirry komentorivillä johonkin kansioon, joka ei ole Git-repository eikä minkään repositoryn alikansio. Suorita:

```bash
git status
```

Git ilmoittaa, ettei nykyinen sijainti ole Git-repositoryn sisällä.

Palaa sitten `seikkailupeli`-kansioon ja suorita komento uudelleen:

```bash
git status
```

Nyt Git näyttää harjoitusprojektisi tilan.

Tämä harjoitus auttaa ymmärtämään, että Git-komennot toimivat sen repositoryn yhteydessä, jossa työskentelet. Siksi oikean kansion tarkistaminen on tärkeä tapa ennen komentojen suorittamista.

## 8. Entä jos repository on jo olemassa?

Jos olet jo alustanut `seikkailupeli`-kansion Git-repositoryksi, älä suorita `git init` -komentoa uudelleen vain harjoituksen vuoksi.

Tarkista ensin:

```bash
git status
```

Jos komento näyttää repositoryn tilan, voit jatkaa työskentelyä siinä.

Jos olet epävarma siitä, missä kansiossa olet, tarkista sijaintisi ennen kuin suoritat Git-komentoja. Älä luo uutta repositorya olemassa olevan repositoryn sisälle.

Tällä kurssilla käytät samaa harjoitusprojektia osasta 2 alkaen. Et tarvitse erillistä repositorya jokaista kurssin osaa varten.

## 9. Tarkista, mitä opit

Vastaa omin sanoin:

1. Mikä on Git-repository?
2. Mitä `git init` tekee?
3. Mitä `git status` näyttää?
4. Mikä on `.git`-kansio?
5. Tarkoittaako repositoryn alustaminen sitä, että tiedostot on jo tallennettu commitiksi?
6. Miksi Git-komentoja pitää suorittaa oikeassa projektikansiossa?

### Vastaukset tarkistettavaksi

1. Repository on Gitin hallitsema projektin ja sen versionhallinnan kokonaisuus.
2. `git init` alustaa nykyiseen kansioon uuden Git-repositoryn.
3. `git status` näyttää repositoryn tilan, kuten seuraamattomat ja muuttuneet tiedostot.
4. `.git`-kansio sisältää Gitin versionhallinnan tiedot.
5. Ei. Alustaminen luo repositoryn, mutta commitit tehdään erikseen.
6. Git-komennot kohdistuvat siihen repositoryyn, jonka yhteydessä komento suoritetaan.

## 10. Osa on valmis, kun…

- [ ] Osaat selittää, mikä repository on.
- [ ] Ymmärrät tavallisen kansion ja Git-repositoryn eron.
- [ ] Osaat alustaa uuden repositoryn komennolla `git init`.
- [ ] Osaat tarkistaa repositoryn tilan komennolla `git status`.
- [ ] Ymmärrät, ettei repositoryn luominen vielä tallenna tiedostoja commitiksi.
- [ ] Tiedät, että jatkat samalla harjoitusprojektilla kurssin seuraavissa osissa.

---

## Seuraavaksi

[Seuraava osa: 03 – Ensimmäinen commit](../03_ensimmainen_commit/)

[← Edellinen osa: 01 – Mikä Git on?](../01_mika_on_git/)

[← Kurssin etusivulle](../README.md)