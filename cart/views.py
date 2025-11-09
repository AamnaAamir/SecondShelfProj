from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Cart, CartItem
from books.models import Book
from .forms import AddToCartForm

@login_required(login_url='/login')
def add_to_cart(request):
    form = AddToCartForm(request.POST or None)
    if form.is_valid():
        book_id = form.cleaned_data.get('book_id')
        quantity = form.cleaned_data.get('quantity')
        book = Book.objects.filter(id=book_id).first()
        if book is None:
            return redirect('/')  # Book does not exist
        
        # Get or create cart for user
        cart, created = Cart.objects.get_or_create(user=request.user)
        
        # Add or update CartItem
        cart_item, created = CartItem.objects.get_or_create(cart=cart, book=book)
        cart_item.quantity += quantity
        cart_item.price = book.price
        cart_item.save()
        
        return redirect('/cart/')
    
    return redirect('/')  # fallback

@login_required(login_url='/login')
def view_cart(request):
    cart = Cart.objects.filter(user=request.user).first()
    items = cart.cartitem_set.all() if cart else []
    
    total = sum(item.quantity * item.price for item in items)
    
    context = {
        'cart': cart,
        'items': items,
        'total': total,
    }
    return render(request, 'cart/cart.html', context)

@login_required(login_url='/login')
def remove_cart_item(request, *args, **kwargs):
    detail_id = kwargs.get('detail_id')
    cart_item = CartItem.objects.filter(id=detail_id, cart__user=request.user).first()
    if cart_item:
        cart_item.delete()
    return redirect('/cart/')
