from django.shortcuts import render

'''
    Importação da biblioteca de mensagens de sucesso/erro do 
        Django.
'''
from django.contrib import messages

'''
    Importação dos formulários.
'''
from core.forms import ContatoForm

def index(request):
    return render(request, 'index.html')

def contato(request):

    '''
        Aqui estamos importando o formulário "ContatoForm".
        Este pode receber os dados enviados pelo usuário em um
            método HTTP "POST"; ou não pode ter dados quando
            o usuário apenas abrir o formulário.
    '''
    form = ContatoForm(request.POST or None)

    '''
        Se caso o método for "POST" havendo dados entramos na
            condição "IF".
    '''
    if request.method == 'POST':

        '''
            Aqui verificamos se o formulário é válido.
        '''
        if form.is_valid():

            '''
                Caso o formulário seja valido enviamos o email.   
            '''
            form.send_mail()

            '''
                Aqui estamos armazenando os dados que o usuário
                    enviou nos campos do formulário em variáveis.
            '''
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            assunto = form.cleaned_data['assunto']
            mensagem = form.cleaned_data['mensagem']

            '''
                Aqui estamos fazendo o teste no terminal,
                    verificando se os dados foram enviados e
                    armazenados corretamente.
            '''
            print('Mensagem enviada')
            print(f'Nome: {nome}')
            print(f'E-mail: {email}')
            print(f'Assunto: {assunto}')
            print(f'Mensagem: {mensagem}')

            '''
                Essa mensagem pode ser chamada no formulário HTML.
                Se tudo ocorrer corretamente até esse ponto, a
                    mensagem será exibida.
            '''
            messages.success(request, 'E-mail Enviado com sucesso')

            '''
                Aqui limpamos o furmulário para que seja
                    preenchido novamente.
            '''
            form = ContatoForm()
            '''
                Caso o formulário não seja válido caímos na estrutura
                    de condição "else".
            '''
        else:
            '''
                Essa mensagem pode ser chamada no formulário HTML.
                Se o formulário for inválido essa mensagem será
                    exibida.
            '''
            messages.error(request, 'Erro ao enviar o e-mail')

    context = {'form': form}
    return render(request, 'contato.html', context)

def produto(request):
    return render(request, 'produto.html')