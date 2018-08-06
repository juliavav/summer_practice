from urllib.error import HTTPError
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import time


from cat import Cat


def get_bs_object(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e)
        return None
    return BeautifulSoup(html, "html.parser")


def get_info(bs_object):   # tests
    cats = []
    short_url = "https://murkosha.ru"
    cat_items = bs_object.find_all("div", {"class": "catItemBody"})
    for cat_item in cat_items:
        ''' Image processing '''
        img = cat_item.find("img").attrs["src"]
        img = img[:-5]
        img += "XL.jpg"
        img = short_url + img
        ''' Name processing '''
        name = cat_item.find("a").attrs["title"]
        ''' Gender '''
        sex = cat_item.find("li", {"class": "odd typeRadio grouppol"}).get_text().strip()
        ''' Age '''
        age = cat_item.find("li", {"class": "even typeTextfield groupVozpast"}).get_text().strip()
        age = age[30:].strip()
        cats.append(Cat(name, sex, age, img))

    return cats


def murkosha_cats_list():
    short_url = "https://murkosha.ru"
    full_url = short_url + "/laskovie-koshki-i-kotyata"
    bs_obj = get_bs_object(full_url)
    if bs_obj is None:
        print("Error in connection with " + full_url)
        return None
    else:
        pages = bs_obj.find("div",
                            {"class": "k2Pagination"}).find_all("a",
                                                                {"class": re.compile("^pagenav$")})

        links = [full_url]
        cats_info = []

        for page in pages:
            links.append(short_url + page.attrs['href'])
        links = list(set(links))
        for link in links:
            bs_obj = get_bs_object(link)
            info = get_info(bs_obj)
            for one in info:
                print(one.age)
                print(one.sex)
                print(one.name)
                print(one.img_url)
            cats_info.extend(info)
            time.sleep(5)

    return cats_info


# murkosha_cats_list()
