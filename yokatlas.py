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

        ul_tag = soup.find('ul', {'id': 'myUl'})
        li_tags = ul_tag.find_all('li', class_='unilist')

        for li_tag in li_tags:
            data_id = li_tag.find('a', href=True)['data-id']
            university_name_tr = li_tag.find('h3', class_='baslik').text.strip()

            # Türkçe çevirisini al
            university_name_en = translator.translate(university_name_tr, src='tr', dest='en').text

            # Verileri birleştir
            university_data.append({
                'id': data_id,
                'name_en': university_name_en,
                'name_tr': university_name_tr
            })

        return university_data

    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        return []

def save_to_txt(data):
    with open('output11.txt', 'w', encoding='utf-8') as file:
        file.write("ID,Name (EN),Name (TR)\n")
        for entry in data:
            file.write(f"{entry['id']},{entry['name_en']},{entry['name_tr']}\n")

if __name__ == "__main__":
    url = "https://yokatlas.yok.gov.tr/universite.php"  # Bu yeri kendi sayfanızın URL'si ile değiştirin

    print(f"University data for {url}:")
    university_data = get_university_data(url)

    for entry in university_data:
        print(f"ID: {entry['id']}, Name (EN): {entry['name_en']}, Name (TR): {entry['name_tr']}")

    save_to_txt(university_data)
    print("Data saved to output.txt")
