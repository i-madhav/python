from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import Cart, CartItem, Product

def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create()

    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
    cart_item.save()

    return redirect('index')

def view_cart(request):
    cart = Cart.objects.first()  # This assumes a single cart for simplicity
    cart_items = CartItem.objects.filter(cart=cart)
    return render(request, 'cart.html', {'cart_items': cart_items})
