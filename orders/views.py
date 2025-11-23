from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Order, OrderDetail
from cart.models import Cart, CartItem
from .forms import CheckoutForm
from django.utils import timezone
from django.contrib import messages
from django.core.mail import EmailMessage
from django.conf import settings


@login_required(login_url='/login')
def checkout(request):
    # By default we'll checkout entire cart. Optionally ?seller=ID to checkout items per seller
    seller_id = request.GET.get('seller')
    cart = Cart.objects.filter(user=request.user).first()
    if not cart:
        messages.warning(request, "Your cart is empty.")
        return redirect('/cart/')

    # items = cart.cartitem_set.select_related('book').all()
    items = cart.items.select_related('book').all()
    if seller_id:
        items = items.filter(book__user__id=seller_id)

    if not items:
        messages.warning(request, "No items to checkout.")
        return redirect('/cart/')

    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            full_name = form.cleaned_data.get('full_name')
            address = form.cleaned_data.get('address')
            city = form.cleaned_data.get('city')
            phone_num = form.cleaned_data.get('phone_num')
            payment_method = form.cleaned_data.get('payment_method')

            total_amount = sum(item.quantity * item.price for item in items)
            order = Order.objects.create(
                user=request.user,
                total_amount=total_amount,
                order_date=timezone.now(),
                status='Pending',
                address=f"{address}, {city}",
                phone=phone_num,
            )

            for item in items:
                OrderDetail.objects.create(
                    order=order,
                    book=item.book,
                    quantity=item.quantity,
                    price=item.price
                )

            # Remove checked items from cart
            # items.delete()

            # Send confirmation email (saved as file in sent_emails)
            subject = f"Order #{order.id} confirmation - SecondShelf"
            body = f"Hi {request.user.username},\n\nThank you for your order #{order.id}.\nTotal: {total_amount} Rs.\n\nWe will notify you when seller confirms the order.\n\nRegards,\nSecondShelf"
            email = EmailMessage(subject=subject, body=body, to=[request.user.email], from_email=settings.DEFAULT_FROM_EMAIL)
            email.send()

            messages.success(request, "Order created. Please select your payment method.")
            
            # REDIRECT TO PAYMENT OPTIONS PAGE
            return redirect(f'/payment/options/{order.id}/')
    else:
        form = CheckoutForm()

    cart_items = items
    total_amount = sum(item.quantity * item.price for item in items)

    context = {
        'form': form,
        'cart_items': cart_items,
        'total_amount': total_amount,
    }
    return render(request, 'checkout.html', context)


@login_required(login_url='/login')
def order_history(request):
    orders = Order.objects.filter(user=request.user).order_by('-order_date')
    return render(request, 'order_history.html', {'orders': orders})


@login_required(login_url='/login')
def order_detail(request, order_id):
    order = Order.objects.filter(id=order_id, user=request.user).first()
    if not order:
        return redirect('/orders/')
    details = OrderDetail.objects.filter(order=order).select_related('book')
    return render(request, 'order_detail.html', {'order': order, 'details': details})
