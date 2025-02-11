import requests
from bs4 import BeautifulSoup

url = 'http://127.0.0.1:5500/index.html'

response = requests.get(url)

if response.status_code == 200:

    soup = BeautifulSoup(response.text, 'html.parser')
    with open("scrap.txt", "w") as scrap:
        h1 = soup.find('h1')
        print('Heading Utama:', h1.get_text() if h1 else 'Tidak ditemukan')

        for level in range(1, 7):
            for heading in soup.find_all(f'h{level}'):
                print(f'H{level}:', heading.get_text())
                scrap.write(f'H{level}: {heading.get_text()}\n')
        
        tentang = soup.find('article', id='About')
        if tentang:
            paragraphs = tentang.find_all('p')
            for idx, p in enumerate(paragraphs, 1):
                print(f'Paragraf {idx} dalam Tentang:', p.get_text())
                scrap.write(f'Paragraf {idx} dalam Tentang: {p.get_text()}\n')

        
        nav = soup.find('nav')
        if nav:
            links = nav.find_all('a')
            for link in links:
                print('Link Navigasi:', link.get('href'), '-', link.get_text())
                scrap.write(f'Link Navigasi {link.get('href')} - {link.get_text()}\n')
        
        footer = soup.find('footer')
        if footer:
            inputs = footer.find_all('input')
            for inp in inputs:
                tipe = inp.get('type')
                nama = inp.get('name')
                print('Input Form:', nama, 'Tipe:', tipe)
                scrap.write(f'Input Form {nama} Tipe: {tipe}\n')
else:
    print("Gagal mengambil halaman. Status Code:", response.status_code)