# from django import forms
# from .models import Sobrevivente

# class descontoForm(forms.ModelForm):
#     class Meta:
#         model = Sobrevivente
#         fields = ('lat', 'long')

#     def clean_lat(self):
#         if self.cleaned_data["lat"] > 90 or :
#             raise forms.ValidationError("Limite de lat excedido")

#         return self.cleaned_data["desconto"]
    
#     def clean_long(self):
#         if self.cleaned_data["long"] > 10:
#             raise forms.ValidationError("Limite de long excedido")

#         return self.cleaned_data["long"]