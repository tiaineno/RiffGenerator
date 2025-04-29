# Ohjelman rakenne #
Itse algoritmi on kirjoitettu tiedoston markov.py luokkaan Generator. Luokkaa alustaessa se ottaa parametrinä halutun asteen ja luo sekä rytmille, että melodialle trie-tietorakenteen, joka on kirjoitettu tiedostoon trie.py. Algoritmin käyttämiseen liittyy vain kaksi metodia, joista insert syöttää sille dataa ja generate palauttaa generoidun sekvenssin. Syöte ja ulostulo annetaan tupleina, jonka ensimmäinen alkio on melodian sisältävä lista ja toinen alkio rytmin sisältävä lista. Kaikki generointiin liittyvä tapahtuu generate (ja get_probabilities) funktiossa. Midi-tiedostojen käsittely on ulkoistettu erikseen tiedostoon midi.py. Se tarjoaa generaattorin palauttaman tuplen muuttamisen tiedostoksi ja toisinpäin. Main.py tarjoaa ohjelmalle käyttöliittymän ja hoitaa samalla esimerkiksi midi-moduulin kutsumisen.

# Aika ja tilavaativuudet #
Syötteen lisääminen ja generointi vievät kummatkin aikaa O(n*k), missä n on syötteen pituus nuotteina/tuotettavan sekvenssin haluttu pituus ja k taas aste, sillä jokaista nuottia varten käydään tietorakenteessa asteen mittainen looppi läpi. Myös tietorakenteen viemä tila on O(n*k), sillä lähes jokaista nuottia kohden tallennetaan asteen verran lapsia. Rytmin toteutus ei muuta näitä vaativuuksia.

# Puitteet ja parannusehdotukset #
Ohjelma generoi rytmin ja melodian erikseen. Rajallisella määrällä syötettä tätä on kuitenkin hankala muuttaa, joten lopputulos ei ole täysin luonnollisen kuuloinen. Tällä hetkellä ohjelmassa on ongelmana jotkin erikoiset tahtilajit sekä samanaikaisesti soivat äänet, jotka voivat aiheuttaa epäsäännällisyyttä datan syöttämiseen, mutta eivät aiheuta virheitä. Muita huomioon otettavia tekijöitä ovat mm. tahtilajit, sävellaji, luonnollinen lopetus ja tempo. Syötteitä valittaessa etenkin niiden sävellajin ja yleisen samankaltaisuuden tulisi olla sama. Tämä jää käyttäjän vastuulle (käytettäessä muita kuin oletussyötteitä), mikä voi olla huono lähtökohta musiikista vain vähän ymmärtävälle.

# Tekoälyn käyttö #
Olen käyttänyt Chat Gpt:tä apuna esimerkiksi ideoinnissa, markovin ketjuun tutustuessa ja koodin kirjoittamisessa. Etenkin testaus- ja midi-tiedostoja käsittelevän kirjaston käyttö helpottui huomattavasti tekoälyn avulla. 

# Lähteet #
- https://www.youtube.com/watch?v=V7OPB6zmSdM
- https://en.wikipedia.org/wiki/Trie
- https://en.wikipedia.org/wiki/Markov_chain
- https://courses.mooc.fi/org/uh-mathstat/courses/johdatus-matriisilaskentaan/chapter-9
- https://www.math.utah.edu/~gustafso/s2019/2270/projects-2016/zhang-bopanna/zhangJie-bopannaPrathusha-MarkovChainMusicComposition.pdf