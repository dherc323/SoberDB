# from django import forms
# from .models import Lab_Item
# #
# # #Lab_ItemForm is the name of our form. 'ModelForm' takes care of setting up our form so we don't have to hardcode it.
# class Lab_ItemForm(forms.Form):
#     Item_name = forms.CharField(label = 'Item name', max_length = 200)
# # Here we tell Django to use our model 'Lab_Item' to create the form.
#     class Meta:
#         model = Lab_Item
#         #Specify which fields you want in your forms:
#         fields = ('Item_name', '',)
