import os.path
import requests
from bs4 import BeautifulSoup

main_folder_name = 'DataSet'


def flower(url, subfolder_name, flower_name):
    main_folder_path = os.path.join(os.getcwd(), main_folder_name)  # Полный путь до главной папки
    subfolder_path = os.path.join(main_folder_path, subfolder_name)  # Полный путь до подпапки

    if not os.path.exists(main_folder_path):
        os.makedirs(main_folder_path)

    if not os.path.exists(subfolder_path):
        os.makedirs(subfolder_path)
    iterator = 0
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'lxml')
        div_elements_rose = soup.find_all('img', class_='serp-item__thumb justifier__thumb')
        for img in div_elements_rose:
            iterator += 1
            file_extension = 'png'
            photo_name = flower_name + str(iterator)
            file_name = f"{photo_name}.{file_extension}"
            img_src = img.get('src')
            if img_src:
                img_src = 'https:' + img_src
                download_rose_img = requests.get(img_src)
                if download_rose_img.status_code != 200:
                    print("Опять Яндекс мешает собиарть дорогие фотки")
                elif not div_elements_rose:
                    print("Why Yandex, why?")
                else:
                    file_path = os.path.join(subfolder_path, file_name)
                    with open(file_path, 'wb') as f:
                        noop = f.write(download_rose_img.content)
                        print(f'Saved {photo_name}')


flower('https://yandex.ru/images/search?text=rose', 'Rose', "Rose")
#flower('https://yandex.ru/images/search?text=%D0%A2%D1%8E%D0%BB%D1%8C%D0%BF%D0%B0%D0%BD', 'Tulip', "Tulip")
