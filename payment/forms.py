from django import forms

PAYMENT_METHODS = (
    ('stripe', 'Credit/Debit Card (Stripe)'),
    ('cod', 'Cash on Delivery'),
)

class PaymentForm(forms.Form):
    method = forms.ChoiceField(choices=PAYMENT_METHODS, widget=forms.RadioSelect)
