from django.urls import path
from .views import ViewCart, ViewWishlist, \
    ViewCartBuy, ViewCartDel, ViewCartAdd

app_name = 'cart_shop'

urlpatterns = [
    path('', ViewCart.as_view(), name='cart'),
    path('whishlist/', ViewWishlist.as_view(), name='wishlist'),
    path('buy/<int:product_id>', ViewCartBuy.as_view(), name='buy'),
    path('del/<int:item_id>', ViewCartDel.as_view(), name='del_from_cart'),
    path('add/<int:product_id>', ViewCartAdd.as_view(), name='add_to_cart'),
]

# для CART путь такой 127.0.0.1:8000/cart/ выведет шаблон 'cart_shop/cart.html'
# для Wishlist 127.0.0.1:8000/cart/wishlist/ => 'cart_shop/wishlist.html'
