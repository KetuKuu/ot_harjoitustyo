# Collecting-app

Sovellus on tarkoitettu keräilyharrastuskäyttöön yksityishenkilöille. 
Sovelluksen avulla keräilijät voivat hallinnoida ja seurata kokoelmassaan olevia Nokia-puhelimia. 
Sovellukseen voi kirjautua ja käyttäjä voi lisätä, muokata, seurata ja poistaa puhelimia kokoelmastaan.


# Asennus
Siirry ensin Collecting-app kansioon
1.Asenna riippuvuudet komennolla:
poetry install


2.Käynnistä sovellus komennolla:

poetry run invoke start



# Dokumentaatio
[vaatimusmäärittely](Collecting-app/Dokumentaatio/vaatimusmaarittely.md)

[Työaikakirjanpito](Collecting-app/Dokumentaatio/tuntikirjanpito.md)

# HUOM!
Sovellus on vielä keskeneräinen. Sovelluksen käynnistäessä avautuu sisäänkirjautumissivu. 
Sivujen välillä navigointi ei toimi vielä ja käyttöliittymä Kaipaa vielä kehitystä. 
Login-näkymästä vastaavat login_view.py ja user_view.py(src/ui-hakemistössä) tuottavat myös käyttäjänäkymän.
