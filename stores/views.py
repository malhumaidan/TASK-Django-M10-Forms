from multiprocessing import context
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


def update_store_item(request, item_id):
    store_item = models.StoreItem.objects.get(id=item_id)
    form = StoreItemForm(instance=store_item)
    if request.method == "POST":
        _store_item = StoreItemForm(request.POST, instance=store_item)
        if _store_item.is_valid():
            _store_item.save()
            return redirect("store-item-list")


    context = {
        "store_item": store_item,
        "form": form,
    }
    return render(request, "update_store_item.html", context)

