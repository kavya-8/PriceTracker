from django import forms

class PriceTrackForm(forms.Form):
    product_link = forms.URLField(label='Product Link', required=True)
    email = forms.EmailField(label='Email', required=True)
    desired_price = forms.IntegerField(label='Desired Price', required=True)
