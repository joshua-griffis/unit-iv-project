from django.db import models
from app import item_info


class ITEM(models.Model):
    name = models.TextField()
    desc = models.TextField()
    img = models.TextField()
    price = models.TextField()
    is_in_cart = models.BooleanField()
    subsection = models.TextField()
    section = models.TextField()


def create_item(name, desc, img, price, is_in_cart, subsection, section):
    return ITEM(
        name=name,
        desc=desc,
        img=img,
        price=price,
        is_in_cart=is_in_cart,
        subsection=subsection,
        section=section,
    ).save()


def initialize_items():
    for each in item_info.INITIAL_ITEM_INFO:
        create_item(
            each["name"],
            each["desc"],
            each["img"],
            each["price"],
            each["is_in_cart"],
            each["subsection"],
            each["section"],
        )


def initialize_featured():
    for each in item_info.FEATURED:
        create_item(
            each["name"],
            each["desc"],
            each["img"],
            each["price"],
            each["is_in_cart"],
            each["subsection"],
            each["section"],
        )


cart = []
