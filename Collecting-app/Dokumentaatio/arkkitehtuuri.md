# Arkkitehtuurikuvaus

## Rakenne

Ohjelman rakenne on kolmitasoinen: ui-kansio sisältää sovelluksen käyttöliittymästä vastaavia luokkia, services-kansio sovelluslogiikan, ja repositories-kansio tietokantatoiminnot. Entities-kansio sisältää käyttäjäluokan, jota services- ja repositories-kansioiden luokat käyttävät.
![Hakemistorakenne](./kuvat/Hakemistotakenne.png)

Pakkaus _ui_ sisältää käyttöliittymästä, _services_ sovelluslogiikasta ja _repositories_ tietojen pysyväistallennuksesta vastaavan koodin. Pakkaus _entities_ sisältää luokkia, jotka kuvastavat sovelluksen käyttämiä tietokohteita.

##Päätoiminnallisuudet

Kuvataan seuraavaksi sovelluksen toimintalogiikka muutaman päätoiminnallisuuden osalta sekvenssikaaviona.

### Sisäänkirjautuminen

![Sekvenssikaavio](./kuvat/sekvenssikaavio.jpg)

