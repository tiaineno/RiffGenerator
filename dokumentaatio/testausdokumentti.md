Ohjelmaa on testattu automaattisesti sekä yksikkö, että integraatiotestauksella käyttäen pytestiä. Testit voidaan ajaa juurikansiosta komennolla
```bash
poetry run pytest .
```
tai
```bash
poetry run pytest kansio/yksittäinen_testi
```

Tietorakenteen testaamiseen riittivät yksikkötestit. Sen oleelliset toiminnallisuudet on testattu monipuolisesti. Insertin testaaminen oli tosin vaikeaa erikseen, joten sitä ei ole toteutettu. Testaamisessa on käytetty yksinkertaisia käsinkirjoitettuja nuottijonoja.

Midi-tiedostoja käsittelevää moduulia on testattu tallentaen uusi käsinkirjoitettu nuottijono midi-tiedostona, mikä helpotti testaamista. Midi to list ja list to midi testaaminen oli melko suoraviivaista.

Itse algoritmi on testattu integraatiotestauksella, sillä siinä yhdistyvät kaikki ydintoiminnan muodostavat toiminnot. Syötteenä on käytetty sekä käsinkirjoitettuja sävelmiä, sekä valmiita midi-tiedostoja. Oikeanlaista generointia on testattu tarkistaen ovatko kaikki aste+1-pituiset nuottisarjat osa syötettä. Viimeinen testi testaa oikeastaan koko ohjelman ydintoiminnot, kun se alustaa tietorakenteen, antaa syötteen midi-tiedostoina ja tarkistaa generoinnin oikeanlaisuuden. Myös moduulin apufunktiot on testattu.

Automaattisen testaamisen lisäksi manuaalinen/empiirinen testaaminen on ollut oleellinen osa kehitystä, sillä sävellysten luonnollisuuden arvioiminen vaatii myös niiden kuuntelua. Tätä varten olen käyttänyt tiedostoa manual_testing.py, sekä käyttöliittymää. Olen soittanut midi soittimella sekä kitaralla algoritmin tuottamia riffejä niitä testatessa.

Name                       Stmts   Miss  Cover
----------------------------------------------
src/markov.py                 44      0   100%
src/midi.py                   28      0   100%
src/tests/test_markov.py      58      0   100%
src/tests/test_midi.py        19      0   100%
src/tests/test_trie.py        56      0   100%
src/trie.py                   37      0   100%
----------------------------------------------
TOTAL                        242      0   100%