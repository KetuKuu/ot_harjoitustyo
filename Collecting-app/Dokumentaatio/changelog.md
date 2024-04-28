# Changelog

## Viikko 3

1. Käyttäjä näkee kirjautumissivun, käyttäjän luomissivun ja käyttäjäsivun. Käyttäjä ei pysty navigoimaan sivuilla!
2. Toteuta projektille seuraavat Invoke-tehtävät:
	- poetry run invoke start käynnistää ohjelman
3. Siistitty repositorio, päivitetty tuntikirjanpito ja kunnostettu README.md-tiedost
4. Varmistetty harjoitustyön toimivuus
5. Testit puuttuu

## Viikko 4


1. Sovelluksen koodi on uusittu vastaamaan kerrosarkkitehtuurin periaatteita (lisätty, index,py, ui,py, ui, repositories,entities, service).
2. Lisätty UserRepository-luokka, UserService-luoka, User-luokka ja pilkottu LoginView-, CreateUserView-, UserView Pilkottu itsenäisiin tietostoihin.
3.  Käyttäjän pitäisi pystyä kirjautumaan sisään ja ulos.
4. Käyttäjä näkee kirjautumisen jälkeen käyttäjäsivun.

## Viikko 5


1. Tietokanta ei toimi.
2. Lisätty AddView-luokka. Back-näppäin ei toimi, joten sivulta ei pääse takaisin muuten kuin sulkemalla koko sivun.
3. Käyttäjä voi vaihtaa ohjelman sivujen välillä kunnes siirryt sivulle Lisää projekti.
4. CSV-tiedoston lataamisen perustoiminnallisuus toimii. Tiedostoa itse ei voi vielä ladata."
5. Ohjelman toiminnallisuudessa on vielä paljon puutteita

## Viikko 6
1. Tietokanta toimii.
2.Korjattu drop_tables-metodia joka pudoti tiedokantataulut automaattisesti ohjelman käynnistyessä. Lisätty user_service.py moduliin käyttäjätunnuksen ja salasanan validointi ja korjattu metodi find_by_username(self, username):
3.LoginView luokassa _handle_login-metodissa kutsu self._handle_login() sisältä itsesi. Korjattu.`UserView`-kutsun parametrit laittaa oikeaan järjestykseen. virhe pysy sama: korjattu ja koodi päivitetty, virhe sama.

Traceback (most recent call last):
  File "/usr/lib/python3.10/tkinter/__init__.py", line 1921, in __call__
    return self.func(*args)
TypeError: UI._show_user_view() missing 1 required positional argument: 'user'


