from django.db.models import F, Max, Subquery, Q
from django.http import HttpResponse
from django.shortcuts import render

from .models import Product, Price


def index(request):
    # prices = Price.objects.all()
    # actual_date_price = prices.values('product_id').annotate(last_date=Max('date'))
    # actual_prices = prices.filter(
    #     product_id__in=actual_date_price.values_list('product_id', flat=True),
    #     date__in=actual_date_price.values_list('last_date', flat=True)
    # )

    # Два условия в аннотации
    product = Product.objects.annotate(
        Q(actual_date=Max('price__date')),
        Q(price__product_id=F('id'))
    )

    # context = {
    #     'products': actual_prices
    # }
    # return render(request, 'product/index.html', context)

    return HttpResponse(product)

