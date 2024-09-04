from django.contrib import admin
from django.urls import path, include

'''
    Aqui estamos importando a biblioteca responsável do Django
        usada para lidar com URL's para servir arquivos estáticos 
        fora de produção.
'''
from django.conf.urls.static import static

'''
    Aqui estamos importando a biblioteca responsável pelas
        configurações do nosso servidor Django.
'''
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

'''
    Aqui estamos fazendo a configuração necessária para ter acesso
        aos arquivos de media que vamos fazer upload em nosso 
        projeto.
'''