from django.forms import ModelForm
from sitepi.models import Faculdades


class Faculdadesform(ModelForm):
    class Meta:
        model = Faculdades
        fields = ['nome_faculdade', 'curso', 'preco', 'descricao', 'datacriacao',
                  'notaenade', 'nota', 'cidade', 'uf', 'modalidade']