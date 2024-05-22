import requests
from bs4 import BeautifulSoup
import random
import time

# Load user agents from a file
with open('user-agents.txt', 'r') as f:
    user_agents = f.read().splitlines()

def get_university_data(url):
    headers = {
        'User-Agent': random.choice(user_agents)
    }
    max_retries = 5
    for attempt in range(max_retries):
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            university_data = []

            rows = soup.select('table.sticky-enabled tbody tr')
            for row in rows:
                # Check if the row contains the Turkish flag
                flag_cell = row.select_one('td:nth-of-type(4) center img')
                if flag_cell and 'tr.png' in flag_cell['src']:
                    continue

                rank = row.select_one('td:nth-of-type(1) center').text.strip()
                university_name = row.select_one('td:nth-of-type(2) a').text.strip()

                university_data.append({
                    'rank': rank,
                    'name_en': university_name
                })

            return university_data
        else:
            print(f"Failed to retrieve the page. Status code: {response.status_code}. Attempt {attempt + 1}/{max_retries}")
            time.sleep(2 ** attempt)  # Exponential backoff

    print(f"Giving up after {max_retries} attempts. URL: {url}")
    return []

def save_to_txt(data):
    with open('universiteler.txt', 'w', encoding='utf-8') as file:
        file.write("rank,name_en\n")
        for entry in data:
            file.write(f"{entry['rank']},{entry['name_en']}\n")

if __name__ == "__main__":
    base_url = "https://webometrics.info/en/world?page="
    all_university_data = []

    for page in range(121):
        url = f"{base_url}{page}"
        print(f"University data for {url}:")
        university_data = get_university_data(url)
        all_university_data.extend(university_data)
        print("\n")
        time.sleep(random.uniform(1, 3))

    save_to_txt(all_university_data)
    print("Data saved to universiteler.txt")
