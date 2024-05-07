from django import forms


class ProductForm(forms.Form):
    title = forms.CharField(label="Nome do Produto")
    value = forms.DecimalField(label="Preço")
    stars = forms.IntegerField(label="Estrelas")
    quantity = forms.IntegerField(label="Quantidade")
    image = forms.ImageField(label="Imagem")


class CommentForm(forms.Form):
    title = forms.CharField(label="Nome do Comentário")
    description = forms.CharField(label="Descrição")
    stars = forms.IntegerField(label="Estrelas")
    image = forms.ImageField(label="Imagem")


class ResourceForm(forms.Form):
    title = forms.CharField(label="Nome do Recurso")
    description = forms.CharField(label="Descrição")
    image = forms.ImageField(label="Imagem")


class CategorieForm(forms.Form):
    title = forms.CharField(label="Nome da Categoria")
    description = forms.CharField(label="Descrição")
    image = forms.ImageField(label="Imagem")


class BlogForm(forms.Form):
    user = forms.CharField(label="Usuário")
    date = forms.DateField(label="Data")
    title = forms.CharField(label="Nome do Blog")
    description = forms.CharField(label="Descrição")
    image = forms.ImageField(label="Imagem")
