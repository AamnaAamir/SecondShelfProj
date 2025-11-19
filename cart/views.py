# from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
# from .models import Cart, CartItem
# from books.models import Book
# from .forms import AddToCartForm

# @login_required(login_url='/login')
# def add_to_cart(request):
#     form = AddToCartForm(request.POST or None)
#     if form.is_valid():
#         book_id = form.cleaned_data.get('book_id')
#         quantity = form.cleaned_data.get('quantity')
#         book = Book.objects.filter(id=book_id).first()
#         if book is None:
#             return redirect('/')  # Book does not exist
        
#         # Get or create cart for user
#         cart, created = Cart.objects.get_or_create(user=request.user)
        
#         # Add or update CartItem
#         cart_item, created = CartItem.objects.get_or_create(cart=cart, book=book)
#         cart_item.quantity += quantity
#         cart_item.price = book.price
#         cart_item.save()
        
#         return redirect('/cart/')
    
#     return redirect('/')  # fallback

# @login_required(login_url='/login')
# def view_cart(request):
#     cart = Cart.objects.filter(user=request.user).first()
#     items = cart.cartitem_set.all() if cart else []
    
#     total = sum(item.quantity * item.price for item in items)
    
#     context = {
#         'cart': cart,
#         'items': items,
#         'total': total,
#     }
#     return render(request, 'cart/cart.html', context)

# @login_required(login_url='/login')
# def remove_cart_item(request, *args, **kwargs):
#     detail_id = kwargs.get('detail_id')
#     cart_item = CartItem.objects.filter(id=detail_id, cart__user=request.user).first()
#     if cart_item:
#         cart_item.delete()
#     return redirect('/cart/')

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Cart, CartItem
from books.models import Book
from django.db.models import F
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponse

@login_required(login_url='/login')
def add_to_cart(request):
    if request.method != 'POST':
        return redirect('/books')
    book_id = request.POST.get('book_id')
    quantity = int(request.POST.get('quantity') or 1)
    book = Book.objects.filter(id=book_id, active=True).first()
    if book is None:
        messages.error(request, "Book not found")
        return redirect('/books')

    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, book=book, defaults={'quantity': 0, 'price': book.price})
    cart_item.quantity = F('quantity') + quantity
    cart_item.price = book.price
    cart_item.save()
    # refresh from db to get F() applied
    cart_item.refresh_from_db()
    messages.success(request, f"Added {book.title} x{quantity} to cart.")
    return redirect(request.META.get('HTTP_REFERER', '/cart/'))

# @login_required(login_url='/login')
# def view_cart(request):
#     cart = Cart.objects.filter(user=request.user).first()
#     items = cart.cartitem_set.select_related('book', 'cart').all() if cart else []
#     # group items by seller (book.user)
#     groups = {}
#     for item in items:
#         seller = item.book.user
#         groups.setdefault(seller, []).append(item)

#     # compute totals
#     grand_total = sum(item.quantity * item.price for item in items)
#     context = {
#         'cart': cart,
#         'groups': groups.items(),  # iterable of (seller, [items])
#         'grand_total': grand_total,
#     }
#     return render(request, 'cart.html', context)

@login_required(login_url='/login')
def view_cart(request):
    cart = Cart.objects.filter(user=request.user).first()
    # use the related_name 'items'
    items = cart.items.select_related('book', 'cart').all() if cart else []


    # group items by seller (book.user)
    groups = {}
    for item in items:
        seller = item.book.user
        groups.setdefault(seller, []).append(item)

    # compute totals
    grand_total = sum(item.quantity * item.price for item in items)

    context = {
        'cart': cart,
        'groups': groups.items(),  # iterable of (seller, [items])
        'grand_total': grand_total,
    }
    return render(request, 'cart.html', context)


@login_required(login_url='/login')
def update_cart(request):
    if request.method != 'POST':
        return redirect('/cart/')
    # expected fields like quantities: book_item_<id>
    for key, value in request.POST.items():
        if key.startswith('quantity_'):
            try:
                item_id = int(key.split('_', 1)[1])
                qty = int(value)
                cart_item = CartItem.objects.filter(id=item_id, cart__user=request.user).first()
                if cart_item:
                    if qty <= 0:
                        cart_item.delete()
                    else:
                        cart_item.quantity = qty
                        cart_item.save()
            except Exception:
                pass
    messages.success(request, "Cart updated.")
    return redirect('/cart/')

@login_required(login_url='/login')
def remove_from_cart(request, item_id):
    CartItem.objects.filter(id=item_id, cart__user=request.user).delete()
    messages.success(request, "Item removed from cart.")
    return redirect('/cart/')

def cart_size(request):
    # Assuming each user has a cart and you want the total items
    try:
        cart = Cart.objects.get(user=request.user)
        size = cart.items.count()  # adjust 'items' to your related_name
    except Cart.DoesNotExist:
        size = 0
    return HttpResponse(size)