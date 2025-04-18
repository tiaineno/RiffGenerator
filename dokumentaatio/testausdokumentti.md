Ohjelmaa on testattu automaattisesti sekä yksikkö, että integraatiotestauksella käyttäen pytestiä. Testit voidaan ajaa juurikansiosta komennolla
```bash
poetry run pytest .
```
tai
```bash
poetry run pytest kansio/yksittäinen_testi.py
```

Tietorakenteen testaamiseen riittivät yksikkötestit. Sen oleelliset toiminnallisuudet on testattu monipuolisesti. Insertin testaaminen oli tosin vaikeaa erikseen, joten sitä ei ole toteutettu. Testaamisessa on käytetty yksinkertaisia käsinkirjoitettuja nuottijonoja.

Midi-tiedostoja käsittelevää moduulia on testattu hyödyntäen input tiedostoja. Parin erityistapauksen lisäksi funktioiden testaaminen oli melko suoraviivaista.

Itse algoritmi on testattu integraatiotestauksella, sillä siinä yhdistyvät kaikki ydintoiminnan muodostavat toiminnot. Syötteenä on käytetty sekä käsinkirjoitettuja sävelmiä, sekä valmiita midi-tiedostoja. Oikeanlaista generointia on testattu tarkistaen ovatko kaikki aste+1-pituiset nuottisarjat osa syötettä. Viimeinen testi testaa oikeastaan koko ohjelman ydintoiminnot, kun se alustaa tietorakenteen, antaa syötteen midi-tiedostoina ja tarkistaa generoinnin oikeanlaisuuden. Myös moduulin apufunktiot on testattu.

Automaattisen testaamisen lisäksi manuaalinen/empiirinen testaaminen on ollut oleellinen osa kehitystä, sillä sävellysten luonnollisuuden arvioiminen vaatii myös niiden kuuntelua. Etenkin midi-tiedostojen muuttaminen listaksi vaati manuaalista testaamista. Olen soittanut midi soittimella sekä kitaralla algoritmin tuottamia riffejä niitä testatessa.


Testikattavuus 18.4.2025:
Name                       Stmts   Miss  Cover
----------------------------------------------
src/markov.py                 58      0   100%
src/midi.py                   78      0   100%
src/tests/test_markov.py      67      0   100%
src/tests/test_midi.py        41      0   100%
src/tests/test_trie.py        56      0   100%
src/trie.py                   37      0   100%
----------------------------------------------
TOTAL                        337      0   100%