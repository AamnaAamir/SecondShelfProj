from django import forms

class CheckoutForm(forms.Form):
    full_name = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Full Name"})
    )
    address = forms.CharField(
        max_length=500,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Address"})
    )
    city = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "City"})
    )
    phone_num = forms.CharField(
        max_length=15,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Phone Number"})
    )
    payment_method = forms.ChoiceField(
        choices=[('COD', 'Cash on Delivery'), ('Online', 'Online Payment')],
        widget=forms.Select(attrs={"class": "form-select"})
    )
