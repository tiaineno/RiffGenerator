Ohjelma käynnistetään juurikansiosta kirjoittamalla konsoliin
```bash
poetry run python src/index.py
```	
Ohjelma kysyy aluksi markovin ketjun astetta, johon 3 on sopiva minor ja major kansioita testattaessa.
Midi tiedostoja kysyttäessä riittää antaa ohjelmalle yksi repon mukana tuleva kansio syötteeksi, kirjoittamalla joko major tai minor (major on hieman kattavampi). Myös muita kansioita tai yksittäisiä tiedostoja voi käyttää, mikäli ne sijaitsevat /data/input/ kansiossa. Enter jatkaa eteenpäin syöttämisen jälkeen.
Pituudeksi toimii esim 32 oikein hyvin.
Generoinnin voi halutessaan tallentaa valitsemallaan nimellä kansioon data/output/, josta sen voi viedä esim. tähän sovellukseen kuunneltavaksi: https://signal.vercel.app.
