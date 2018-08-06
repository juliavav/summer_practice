import re
import time

from cat import Cat
from murkosha import get_bs_object, murkosha_cats_list

def get_info_pr(bs_object, age):  # tests
    cats = []
    short_url = "http://www.izpriuta.ru"
    cat_items = bs_object.find_all("div", {"class": "card box"})
    for cat_item in cat_items:
        ''' Image processing '''
        img = cat_item.find("img").attrs["src"]
        img = img.replace('styles/400box/public/', '')
        ''' Name processing '''
        name = cat_item.find("h2").get_text().strip()
        ''' Gender '''
        sex = cat_item.find("span", {"class": "gender"}).get_text().strip()
        cats.append(Cat(name, sex, age, img))

    return cats


def izpriuta_cats_list():
    short_url = "http://www.izpriuta.ru"
    full_url03 = short_url + "/koshki?field_pet_male_value=All&field_pet_age_value=2&title="
    full_url35 = short_url + "/koshki?field_pet_male_value=All&field_pet_age_value=3&title="
    bs_obj = get_bs_object(full_url03)
    if bs_obj is None:
        print("Error in connection with " + full_url03)
        return None
    else:
        pages = bs_obj.find_all("a", {"title": re.compile("^На страницу номер")})

        links = [full_url03]
        cats_info = []

        for page in pages:
            links.append(short_url + page.attrs['href'])
        print(links)

        for link in links:
            bs_obj = get_bs_object(link)
            info = get_info_pr(bs_obj, "0-3 года")
            cats_info.extend(info)
            time.sleep(2)
        bs_obj = get_bs_object(full_url35)
        cats_info.extend(get_info_pr(bs_obj, "3-5 лет"))

    return cats_info

