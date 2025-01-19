# HOW TO USE

1. Instal library needed <br>
run ```pip install -r requirements.txt```<br>

2.Download Chromedriver and extract <br>
- Visit this <a href="https://developer.chrome.com/docs/chromedriver/downloads">link</a>
- Cari chromedriver yang sesuai dengan version dari google chrome dan download it
- file yang sudah di download di extract di file manapun
- sesudah di extract, copy file path chromedriver.exe tsb dan ubah main.py line 12 dengan file path tsb

3. Running main.py file

##NOTE
untuk csv file (main.py line 61) bisa diubah nama csv-nya namun csv harus dengan template berikut

example :
| provinsi | stasiun | link |
| -------- | ------- | ---- |
| Jakarta  | Kemayoran | https://jakarta.bps.go.id/id/statistics-table/2/MzczIzI=/curah-hujan-di-stasiun-kemayoran-menurut-bulan--mm-.html |
