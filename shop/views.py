from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Cart, CartItem, Order, OrderItem

# Shop Page
def shop(request):
    products = Product.objects.filter(is_available=True)
    return render(request, 'shop/shop.html', {'products': products})


# Add to Cart
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    cart_id = request.session.get('cart_id')
    if not cart_id:
        cart = Cart.objects.create()
        request.session['cart_id'] = cart.id
    else:
        cart = Cart.objects.get(id=cart_id)

    item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        item.quantity += 1
        item.save()

    return redirect('shop')


# View Cart
def cart_view(request):
    cart_id = request.session.get('cart_id')
    cart = Cart.objects.get(id=cart_id) if cart_id else None

    total = 0
    if cart:
        for item in cart.items.all():
            total += item.total_price()

    return render(request, 'shop/cart.html', {'cart': cart, 'total': total})

# Checkout
def checkout(request):
    cart_id = request.session.get('cart_id')
    cart = Cart.objects.get(id=cart_id)

    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        address = request.POST['address']

        order = Order.objects.create(name=name, phone=phone, address=address)

        for item in cart.items.all():
            OrderItem.objects.create(
                order=order,
                product_name=item.product.name,
                price=item.product.price,
                quantity=item.quantity
            )

        cart.delete()
        request.session['cart_id'] = None

        return redirect('order_success')

    return render(request, 'shop/checkout.html', {'cart': cart})

def update_cart(request, item_id, action):
    item = CartItem.objects.get(id=item_id)

    if action == 'increase':
        item.quantity += 1
    elif action == 'decrease':
        item.quantity -= 1
        if item.quantity <= 0:
            item.delete()
            return redirect('cart')

    item.save()
    return redirect('cart')


def remove_item(request, item_id):
    item = CartItem.objects.get(id=item_id)
    item.delete()
    return redirect('cart')

def order_success(request):
    return render(request, 'shop/success.html')