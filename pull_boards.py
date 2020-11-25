import json
import requests
from sporting import sporting
from config import Config as cfg
from bs4 import BeautifulSoup

def pull_pyzel():
    response = sporting.request(cfg.unofficial_endpoint_pyzel)
    jdata = json.loads(response.text)
    X = []
    for row in jdata:
        X.append(row['img']['deck'])
        X.append(row['img']['bottom'])

    X = list(filter(None, X))

    for i in range(len(X)):
        X[i] = requests.get(X[i].content)
    image_index = save_locally(X,image_index)
    return j

def pull_gensurf(image_index,pagination=True):
    X = []
    page = 0
    limit = 144
    headers = {'limit:' str(limit), 'offset:' str(page*limit)}
    response = requests.get(cfg.gensurf_URL,headers=headers)
    html_soup = BeautifulSoup(response.text, 'html.parser')
    products = html_soup.find_all('h3', class_= 'product-count').text
    print(products)
    # while page*limit < :
    #     try:
    #         response = requests.get(cfg.gensurf_URL,headers = {'limit:' str(limit), 'offset:' str(page * limit)} )
    #     except:
    #         break
    #     html_soup = BeautifulSoup(response.text, 'html.parser')
    #     for image in images:
    #         if image is not None:
    #             X.append(requests.get("https:{}".format(image['src'])).content)
    #             print("https:{}".format(image['src']))
    return None
    # save_locally(X,image_index)

# DHD sucks at posting product images so we will not use them
# def pull_dhd(image_index):
#     #DHD stores all of their products via pagination. Here we iterate through each page to get all images.
#     X = []
#     pages = 11
#     for page in range(pages):
#         if page == 0:
#             response = requests.get(cfg.ci_surfboard_collection)
#         elif page == 1:
#             continue
#         else:
#             response = requests.get(cfg.ci_surfboard_collection+"{}".format("?page=" + str(page)))
#         html_soup = BeautifulSoup(response.text, 'html.parser')
#         images = html_soup.find_all('img', class_= 'product-card__image')
#         for image in images:
#             if image is not None:
#                 X.append(requests.get("https:{}".format(image['src'])).content)
#                 print("https:{}".format(image['src']))
#     save_locally(X,image_index)

def save_locally(arr,image_index):
    for i in range(len(arr)):
        with open("assets/board{}.jpg".format(str(image_index)), "wb") as f:
            f.write(arr[i])
            image_index += 1
    return image_index + i
#image_index  = pull_pyzel()
image_index = 188
image_index = pull_gensurf(image_index)
