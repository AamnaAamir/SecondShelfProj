from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib import messages
from orders.models import Order
from cart.models import Cart,CartItem
from .models import Payment
from .forms import PaymentForm
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY

@login_required(login_url='/login')
def payment_options(request, order_id):
    order = Order.objects.filter(id=order_id, user=request.user).first()
    if not order:
        messages.error(request, "Order not found.")
        return redirect('/orders/')

    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            method = form.cleaned_data['method']
            if method == 'cod':
                Payment.objects.create(order=order, user=request.user, amount=order.total_amount, status='cod')
                order.status = 'Pending'
                order.save()
                messages.success(request, "Order placed with Cash on Delivery.")
                return redirect('payment_success')
            elif method == 'stripe':
                # create stripe checkout session
                success_url = request.build_absolute_uri('/payment/success/')
                cancel_url = request.build_absolute_uri('/payment/cancel/')
                session = stripe.checkout.Session.create(
                    payment_method_types=['card'],
                    line_items=[{
                        'price_data': {
                            'currency': 'usd',
                            'product_data': {'name': f'Order #{order.id} - SecondShelf'},
                            'unit_amount': int(order.total_amount) * 100,  # cents
                        },
                        'quantity': 1,
                    }],
                    mode='payment',
                    success_url=success_url,
                    cancel_url=cancel_url,
                )
                Payment.objects.create(order=order, user=request.user, amount=order.total_amount,
                                       stripe_session_id=session.id, status='pending')
                return redirect(session.url, code=303)
    else:
        form = PaymentForm()

    return render(request, 'payment_options.html', {'form': form, 'order': order})


@login_required(login_url='/login')
def payment_success(request):
    payment = Payment.objects.filter(user=request.user, status='pending').last()
    if payment:
        payment.status = 'completed'
        payment.save()
        # Remove items from cart now
        cart = Cart.objects.filter(user=request.user).first()
        if cart:
            cart.items.filter(book__in=[d.book for d in payment.order.orderdetail_set.all()]).delete()
    return render(request, 'payment_success.html')


@login_required(login_url='/login')
def payment_cancel(request):
    messages.error(request, "Payment was cancelled.")
    return render(request, 'payment_cancel.html')
