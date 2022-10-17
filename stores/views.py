from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect

from stores import models
from stores.forms import StoreItemForm


def get_store_items(request: HttpRequest) -> HttpResponse:
    store_items: list[models.StoreItem] = list(models.StoreItem.objects.all())
    context = {
        "store_items": store_items,
    }
    return render(request, "store_item_list.html", context)


def create_store_item(request):
    create_item = StoreItemForm()
    if request.method == "POST":
        _create_item = StoreItemForm(request.POST)
        if _create_item.is_valid():
            _create_item.save()
            return redirect("store-item-list")


    context = {
        "create_item": create_item,
    }
    return render(request, "create_store_item.html", context)

