from django import forms

class AddToCartForm(forms.Form):
    book_id = forms.IntegerField(widget=forms.HiddenInput())
    quantity = forms.IntegerField(
        min_value=1,
        initial=1,
        widget=forms.NumberInput(attrs={"class": "form-control w-25"})
    )

class UpdateCartForm(forms.Form):
    book_id = forms.IntegerField(widget=forms.HiddenInput())
    quantity = forms.IntegerField(
        min_value=0,  # 0 can mean remove
        widget=forms.NumberInput(attrs={"class": "form-control w-25"})
    )
