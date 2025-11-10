from django import forms 
from django.contrib.auth.models import User

class dateInput(forms.DateInput):
    input_type = 'date'

class sellBookForm(forms.Form):

  book_name = forms.CharField(
        widget=forms.TextInput(attrs={"class":"form-control mb-4", "placeholder":"Enter your Book Name"}),
        label="Book Name"
    )
  book_author = forms.CharField(
        widget=forms.TextInput(attrs={"class":"form-control mb-4", "placeholder":"Enter your Book Author"}),
        label="Book Author"
    )
  book_publisher = forms.CharField(
        widget=forms.TextInput(attrs={"class":"form-control mb-4", "placeholder":"Enter your Book Publisher"}),
        label="Book Publisher"
    )
  book_edition = forms.IntegerField(
        widget=forms.NumberInput(attrs={"class":"form-control mb-4", "placeholder":"Enter your Book Edition"}),
        label="Book Edition"
    )
  book_language = forms.CharField(
        widget=forms.TextInput(attrs={"class":"form-control mb-4", "placeholder":"Enter language of your Book"}),
        label="Book language"
    )
  price = forms.IntegerField(
        widget=forms.NumberInput(attrs={"class":"form-control mb-4", "placeholder":"Enter your Book Price"}),
        label="Book Price"
    )
  CHOICES =(
    (1, "Children's Books"),
    (2, "Young Adult"),
    (3, "Comics and Graphic Novels"),
    (4, "Fiction"),
    (5, "Entry Test Preparation"),
    (6, "Non-Fiction"),
    (7, "Academic Textbooks"),
    (8, "Literature & Poetry"),
    (9, "Reference Materials"),
)
  category = forms.ChoiceField(
        widget=forms.Select(attrs={"class":"form-select mb-4",}),
        choices=CHOICES, 
        label="Category"
    )
  
  description = forms.CharField(
    widget=forms.Textarea(attrs={'rows':"5",'class':'form-control mb-5', 'placeholder':'Enter the description of the book'}),
    label = "description"
  )
  book_pic = forms.ImageField(
        widget=forms.FileInput(attrs={"class":"form-control mb-4","id":"file"})
    )
