from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path("", views.homePageView),
    path("<section>/", views.sectionPageView),
    path("sub/<subsection>/", views.subSectionPageView),
    path("add/<item>/", views.addToCartPageView),
    path("remove/<item>/", views.removedFromCartPageView),
    path("fantasy_inventory/Cart/", views.cartPageView),
    path("admin/", admin.site.urls),
]
