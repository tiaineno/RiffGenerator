# Ohjelman rakenne #
Itse algoritmi on kirjoitettu tiedoston markov.py luokkaan Generator. Luokkaa alustaessa se tallentaan halutun asteen sekä luo itselleen trie-tietorakenteen, joka on kirjoitettu tiedostoon trie.py. Algoritmin käyttämiseen on vain kaksi metodia, joista insert syöttää sille dataa listana ja generate palauttaa generoidun sekvenssin listana. Kaikki generointiin liittyvä tapahtuu generate ja get_probabilities funktioissa. Midi-tiedostojen käsittely on ulkoistettu erikseen tiedostoon midi.py. Se tarjotaa listan muuttamisen tiedostoksi ja toisinpäin. Main.py tarjoaa ohjelmalle käyttöliittymän ja hoitaa samalla esimerkiksi midi-tiedostojen käsittelyn.

# Aika ja tilavaativuudet #
Syötteen lisääminen ja generointi vievät kummatkin aikaa O(n*k), missä n on syötteen pituus nuotteina/tuotettavan sekvenssin haluttu pituus ja k taas aste, sillä jokaista nuottia varten käydään tietorakenteessa asteen mittainen looppi läpi. Myös tietorakenteen viemä tila on O(n*k), sillä lähes jokaista nuottia kohden tallennetaan asteen verran lapsia.

# Puitteet ja parannusehdotukset #
Musiikin generointi on monimutkainen kokonaisuus, jonka vuoksi joudun tekemään hieman kompromisseja. Toistaiseksi ohjelma generoi suoraviivaisesti vain neljäsosanuotteja, mutta muita huomioon otettavia tekijöitä ovat mm. rytmi, tahtilajit, sävellaji, luonnollinen lopetus ja tempo. Tavoitteena on ottaa vielä rytmi mukaan, mutta tässäkin joudun päättämään, otetaanko syötteenä vain 4/4-tahteja vai generoidaanko rytmejä välittämättä tahdeista. 

# Tekoälyn käyttö #
Olen käyttänyt Chat Gpt:tä apuna esimerkiksi ideoinnissa, markovin ketjuun tutustuessa ja koodin kirjoittamisessa. Etenkin testaus- ja midi-tiedostoja käsittelevän kirjaston käyttö helpottui huomattavasti tekoälyn avulla. 

# Lähteet #
- https://www.youtube.com/watch?v=V7OPB6zmSdM
- https://en.wikipedia.org/wiki/Trie
- https://en.wikipedia.org/wiki/Markov_chain
- https://courses.mooc.fi/org/uh-mathstat/courses/johdatus-matriisilaskentaan/chapter-9
- https://www.math.utah.edu/~gustafso/s2019/2270/projects-2016/zhang-bopanna/zhangJie-bopannaPrathusha-MarkovChainMusicComposition.pdf