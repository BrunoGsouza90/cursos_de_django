from django.http import Http404, HttpResponseRedirect, HttpResponse # type: ignore
from django.shortcuts import render # type: ignore
from exatas_cadastros.models import Cadastro, Categoria, Conta
from datetime import datetime
from decimal import Decimal
import pandas as pd # type: ignore
from django.conf import settings # type: ignore
import os
import subprocess

def banco(request):
    queryset = Cadastro.objects.values('id','descricao', 'valor', 'data', 'conta__registros', 'categoria__registros')
    df = pd.DataFrame(list(queryset))
    df = df.rename(columns={
        'conta__registros': 'Conta',
        'categoria__registros': 'Categoria',
        'id': 'ID',
        'descricao': 'Descrição',
        'valor': 'Valor',
        'data': 'Data'
    })
    df['Valor'] = df['Valor'].apply(lambda x: f'R$ {x:.2f}'.replace('.', ','))
    df['Data'] = pd.to_datetime(df['Data']).dt.strftime('%d/%m/%Y')
    html_table = df.to_html(classes='table table-striped')
    html_table = html_table.replace('<th>', '<th style="text-align: center;">')
    context = {'html_table':html_table}
    return render(request,'exatas_cadastros/banco_de_dados.html', context)

def fazer_backup(request):
    nome_arquivo = 'backup_exata.sql'
    caminho_backup = os.path.join(settings.BASE_DIR, nome_arquivo)
    caminho_pg_dump = r'"C:\Program Files\PostgreSQL\16\bin\pg_dump.exe"'
    
    cmd = f'{caminho_pg_dump} -U postgres -h localhost -p 4321 -Fp -f "{caminho_backup}" exata_cadastro'
    os.environ['PGPASSWORD'] = 'root'
    try:
        subprocess.run(cmd, shell=True, check=True)
        with open(caminho_backup, 'rb') as f:
            response = HttpResponse(f.read(), content_type='application/octet-stream')
            response['Content-Disposition'] = f'attachment; filename="{nome_arquivo}"'
        
        return response
    except subprocess.CalledProcessError as e:
        return HttpResponse(f'Ocorreu um erro ao fazer o backup: {str(e)}', status=500)

def cadastro(request):
    if request.method == 'POST':
        cadastro_novo_descricao = request.POST.get('descricao')
        cadastro_novo_valor = request.POST.get('valor')
        cadastro_novo_data = request.POST.get('data')

        if not cadastro_novo_descricao or not cadastro_novo_valor or not cadastro_novo_data:
            return HttpResponseRedirect('/error/')

        try:
            # Substituir vírgulas por pontos e converter para Decimal
            cadastro_novo_valor = Decimal(cadastro_novo_valor.replace(',', '.'))
        except ValueError:
            context = {'error_message': 'Valor inválido. Use apenas números e uma vírgula para separar decimais.'}
            return render(request, 'exatas_cadastros/index.html', context)

        try:
            cadastro_novo_data = datetime.strptime(cadastro_novo_data, '%d/%m/%Y').strftime('%Y-%m-%d')
        except ValueError:
            context = {'error_message': 'Formato de data inválido. Use dd/mm/yyyy.'}
            return render(request, 'exatas_cadastros/index.html', context)

        categoria_id = request.POST.get('categoria')
        conta_id = request.POST.get('conta')

        cadastro_novo_categoria = Categoria.objects.get(pk=categoria_id)
        cadastro_novo_conta = Conta.objects.get(pk=conta_id)
        novo_cadastro = Cadastro(descricao=cadastro_novo_descricao,valor=cadastro_novo_valor,data=cadastro_novo_data,categoria=cadastro_novo_categoria,conta=cadastro_novo_conta)
        novo_cadastro.save()

        return HttpResponseRedirect('/')

    cadastros = Cadastro.objects.all()
    categorias = Categoria.objects.all()
    contas = Conta.objects.all()
    context = {'cadastros':cadastros, 'categorias':categorias, 'contas': contas}
    return render(request, 'exatas_cadastros/index.html', context)

def error(request):
    return render(request,'exatas_cadastros/error.html')