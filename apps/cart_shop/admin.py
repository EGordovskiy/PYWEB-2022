from django.contrib import admin
from .models import CartItemShop, Product, WishList, WishListItem

admin.site.register(CartItemShop)
admin.site.register(Product)
admin.site.register(WishList)
admin.site.register(WishListItem)
