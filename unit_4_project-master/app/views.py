from django.shortcuts import render
from django.http.request import HttpRequest
from app import models


def homePageView(request):
    models.ITEM.objects.all().delete()
    models.initialize_items()
    return render(request, "homePageTemplate.html")


def sectionPageView(request, section):
    sections = []
    all_items = models.ITEM.objects.all()
    for items in all_items:
        if items.section == section:
            items.subsection.replace("-", " ")
            if items.subsection not in sections:
                sections.append(items.subsection)
    current_section = section.replace("-", " ")
    context = {"sections": sections, "section_name": current_section}
    return render(request, "sectionTemplate.html", context)


def cartPageView(request):
    context = {"cart": models.cart}
    return render(request, "cartTemplate.html", context)


def subSectionPageView(request, subsection):
    subsections = []
    other = []
    all_items = models.ITEM.objects.all()
    for item in all_items:
        item.subsection = item.subsection.replace(" ", "-")
        if item.subsection == subsection:
            item.subsection = item.subsection.replace("-", " ")
            subsections.append(item)
            other.append(item.subsection)
    for all in other:
        this = all
    context = {"subSectionName": this, "subs": subsections}
    return render(request, "subSectionTemplate.html", context)


def addToCartPageView(request, item):
    selected_item = models.ITEM.objects.get(name=item)
    models.cart.append(selected_item)
    context = {"item": selected_item}
    return render(request, "successfully_added_page.html", context)


def removedFromCartPageView(request, item):
    for i in models.cart:
        if i.name == item:
            no = models.cart.index(i)
            models.cart.pop(no)
    return render(request, "successfully_removed_page.html")
