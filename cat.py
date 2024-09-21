import requests

def cat_img():
    url = "https://cataas.com/cat"

    response = requests.get(url)

    if response.status_code == 200:
        mushuk = response.content

        return mushuk
    else:
        return "Xatolik qaytardi !"

