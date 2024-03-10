import requests
from bs4 import BeautifulSoup
from googletrans import Translator

# Google Translate API için bir çevirmen oluştur
translator = Translator()

def get_university_data(url):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # HTML yapısını gerçek web sitesine göre ayarlayın
        # Aşağıdaki sadece varsayılan bir örnek
        university_data = []

        rows = soup.select('table.sticky-enabled tbody tr')
        for row in rows:
            rank = row.select_one('td:nth-of-type(1) center').text.strip()
            university_name = row.select_one('td:nth-of-type(3) a').text.strip()

            # Türkçe çevirisini al
            turkish_translation = translator.translate(university_name, src='en', dest='tr').text

            # Verileri birleştir
            university_data.append({
                'rank': rank,
                'name_en': university_name,
                'name_tr': turkish_translation
            })

        return university_data

    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        return []

def save_to_txt(data):
    with open('üniversiteler.txt', 'w', encoding='utf-8') as file:
        file.write("rank,name_en,name_tr\n")
        for entry in data:
            file.write(f"{entry['rank']},{entry['name_en']},{entry['name_tr']}\n")

if __name__ == "__main__":
    # Replace these URLs with your actual URLs
    urls = [
        "https://www.webometrics.info/en/Asia/turkey?sort=asc&order=World%20Rank",
        "https://www.webometrics.info/en/Asia/turkey?page=1&sort=asc&order=World%20Rank",
        "https://www.webometrics.info/en/Asia/turkey?page=2&sort=asc&order=World%20Rank",
    ]

    all_university_data = []

    for url in urls:
        print(f"University data for {url}:")
        university_data = get_university_data(url)
        all_university_data.extend(university_data)
        print("\n")

    save_to_txt(all_university_data)
    print("Data saved to output.txt")
