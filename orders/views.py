from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Order, OrderDetail
from cart.models import Cart, CartItem
from .forms import CheckoutForm
from django.utils import timezone

@login_required(login_url='/login')
def checkout(request):
    form = CheckoutForm(request.POST or None)
    cart = Cart.objects.filter(user=request.user).first()
    items = cart.cartitem_set.all() if cart else []
    
    if not items:
        return redirect('/cart/')  # nothing to checkout
    
    if form.is_valid():
        full_name = form.cleaned_data.get('full_name')
        address = form.cleaned_data.get('address')
        city = form.cleaned_data.get('city')
        phone_number = form.cleaned_data.get('phone_number')
        payment_method = form.cleaned_data.get('payment_method')
        
        # Create order
        total_amount = sum(item.quantity * item.price for item in items)
        order = Order.objects.create(
            user=request.user,
            full_name=full_name,
            address=address,
            city=city,
            phone_number=phone_number,
            payment_method=payment_method,
            total_amount=total_amount,
            status='Pending',
            order_date=timezone.now()
        )
        
        # Move cart items to order details
        for item in items:
            OrderDetail.objects.create(
                order=order,
                book=item.book,
                quantity=item.quantity,
                price=item.price
            )
        
        # Clear the cart
        items.delete()
        
        return redirect('/orders/')  # redirect to order history
    
    context = {
        'form': form,
        'cart_items': items
    }
    return render(request, 'orders/checkout.html', context)


@login_required(login_url='/login')
def order_history(request):
    orders = Order.objects.filter(user=request.user).order_by('-order_date')
    context = {
        'orders': orders
    }
    return render(request, 'orders/order_history.html', context)
