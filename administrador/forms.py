from django import forms
from administrador.models import Cliente, Producto, Venta, Pedido

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        exclude = ['user'] 
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class':'form-control'})

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        exclude = ['user'] 
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class':'form-control'})


class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ['importePagado']
     
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['importePagado'].widget.attrs.update({'class': 'form-control'})
class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        exclude = ['user'] 
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class': 'form-control'})
        
        if user:
            self.fields['producto'].queryset = Producto.objects.filter(user=user)
            self.fields['cliente'].queryset = Cliente.objects.filter(user=user)