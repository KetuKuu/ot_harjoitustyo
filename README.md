# Collecting-app

Sovellus on tarkoitettu keräilyharrastuskäyttöön yksityishenkilöille. 
Sovelluksen avulla keräilijät voivat hallinnoida ja seurata kokoelmassaan olevia Nokia-puhelimia. 
Sovellukseen voi kirjautua ja käyttäjä voi lisätä, muokata, seurata ja poistaa puhelimia kokoelmastaan.


# Asennus

1.Avaa terminaalissa kansio, johon haluat kloonata projektin ja käytä komentoa:

```git clone https://github.com/KetuKuu/ot_harjoitustyo.git```

2.Siirry Collecting-app kansioon ja asenna riippuvuudet komennolla:

```poetry install tai poetry install --no-root ```

3.Luo virtualiympäristö:

```poetry shell```

4.Käynnistä sovellus komennolla:

```poetry run invoke start```


# Dokumentaatio
[vaatimusmäärittely](Collecting-app/Dokumentaatio/vaatimusmaarittely.md)

[Työaikakirjanpito](Collecting-app/Dokumentaatio/tuntikirjanpito.md)

[Changelog](Collecting-app/Dokumentaatio/changelog.md)

[Käyttöohjeet](Collecting-app/Dokumentaatio/kayttoohje.md)

[Arkkitehtuuri](Collecting-app/Dokumentaatio/arkkitehtuuri.md)

[Testausdokumentti](Collecting-app/Dokumentaatio/testaus.md)


# Komentorivitoiminnot


### Ohjelman suorittaminen

Ohjelman pystyy suorittamaan komennolla:

```bash
poetry run invoke start
```

### Testaus

Testit suoritetaan komennolla:

```bash
poetry run invoke test
```

### Testikattavuus

Testikattavuusraportin voi generoida komennolla:

```bash
poetry run invoke coverage-report
```

Raportti generoituu _htmlcov_-hakemistoon.

### Pylint

Tiedoston .pylintrc tarkistukset voi suorittaa komennolla:

```bash
poetry run invoke lint
```

