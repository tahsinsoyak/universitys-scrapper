# University Data Scraping

This repository contains Python scripts for scraping university data from two different sources: YOK Atlas and Webometrics.

## YOK Atlas

The `yokatlas_scraper.py` script retrieves university information from the YOK Atlas website (https://yokatlas.yok.gov.tr/universite.php).

### Requirements

- Python 3
- Requests library
- BeautifulSoup library
- Googletrans library

### Usage

1. Install the required libraries:

   ```bash
   pip install requests beautifulsoup4 googletrans==3.1.0a0

Run the script:

```bash
python yokatlas_scraper.py
```

The scraped data will be printed to the console and saved to the output.txt file.

## Webometrics

The webometrics_scraper.py script retrieves university ranking data from the Webometrics website (https://www.webometrics.info/).

### Requirements
- Python 3
- Requests library
- BeautifulSoup library
- Googletrans library
  
### Usage
1. Install the required libraries:

```bash
pip install requests beautifulsoup4 googletrans==3.1.0a0
```

Run the script:
```bash
python webometrics_scraper.py
```

The scraped data will be printed to the console.

Feel free to customize and use these scripts according to your needs.

Üniversite Verisi Çekme
Bu depo, iki farklı kaynaktan üniversite verisi çekmek için Python betiklerini içermektedir: YOK Atlas ve Webometrics.

YOK Atlas
yokatlas_scraper.py betiği, YOK Atlas web sitesinden (https://yokatlas.yok.gov.tr/universite.php) üniversite bilgilerini çeker.

Webometrics
webometrics_scraper.py betiği, Webometrics web sitesinden (https://www.webometrics.info/) üniversite sıralama verilerini çeker.

Bu betikleri ihtiyacınıza göre özelleştirip kullanabilirsiniz.
