'''
    Será nesse arquivo que criaremos os nossos formulários.
'''

'''
    Importação da biblioteca de formulários do Django.
'''
from django import forms

'''
    Importação da biblioteca do Django responsável pelo envio
        de emails.
'''
from django.core.mail.message import EmailMessage

from core.models import Produto

'''
    Aqui estamos criando uma classe de formulário Django.
'''
class ContatoForm(forms.Form):

    '''
        Aqui estamos definando os campos do nosso formulário.
    '''
    nome = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='Email')
    assunto = forms.CharField(label='Assunto')

    '''
        Nesse campo em específico estamos importando um widget
            que determinará qual tipo de input esse campo será.
        Nesse caso específicamos que o campo será um campo de
            texto.
        rows = Número de linhas visíveis.
        cols = Número de colunas visíveis.
    '''
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea(
            attrs={          
            'rows': 4,
            'cols': 40
            }
    ))

    '''
        Função responsável pelo envio de emails no Django.
    '''
    def send_mail(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        assunto = self.cleaned_data['assunto']
        mensagem = self.cleaned_data['mensagem']

        conteudo = f'Nome: {nome} \n E-mail: {email} \n Assunto: {assunto} \n Mensagem: {mensagem}'
        
        '''
            Aqui estamos preparando o email.
        '''
        mail = EmailMessage(
            subject='E-mail enviado pelo sistema django2',
            body=conteudo,
            from_email='contato@seudominio.com',
            to=['contato@seudominio.com.br', 'outro@seuemail.com'],
            headers={'Reply-To': email}
        )

        '''
            Aqui fazemos o envio do email.
        '''
        mail.send()

class ProdutoModelForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'preco', 'estoque', 'imagem']