from pathlib import Path
import os
import django_heroku


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-^%jsj(8vebyop0-z=5ox^awj$v52=%(59lg_adye*t_$qr8zno'

'''
    Colocamos DEBUG em false para fazer a publicação em produção.
    Para iniciar precisamos instalar alguns pacotes:
    
    pip install whitenoise      →       Este é responsável por
        
        apresentar os arquivos estáticos em produção.

    pip install gunicorn        →       Este é responsável por

        rodar o python manage.py runserver em um servidor.
'''

'''
    Nessa etapa será necessário também criar dois arquivos na raiz do
        projeto:

    runtime.txt     →       Responsável por informar ao Heroku a versão
        
        do python instalado no projeto.
    
    Proctfile.txt       →       É um arquivo do Heroku. Responsável
        
        por mostrar ao Heroku como iniciar a aplicação.
'''

'''
    Site da Heroku:
    https://www.heroku.com/
    https://devcenter.heroku.com/articles/getting-started-with-python#set-up
    pip install gunicorn
    npm install -g heroku
    pip install django-heroku
    pip install whitenoise
'''

'''
    Após intalar use os comandos:
    heroku login
    heroku create django1-(Nome da Aplicação) --buildpack heroku/python
    git push heroku master
    heroku logs --tail
'''
DEBUG = False

'''
    Caso a publicação seja oficial você colocará nessa lista o seu
        url oficial.
'''
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'django1.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'django1.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_TZ = True

'''
    Configuração responsável por definir qual o Endpoint de acesso
        aos Arquivos Estáticos na nosso URL.
'''
STATIC_URL = 'static/'

'''
    Configuração responsável por representar o caminho para a
        pasta "staticfiles" que é aonde os arquivos carregados
        da pasta "static" serão salvos. Para aplicar essa
        configuração utilizamos o comando "python manage.py
        collectstatic" .
'''
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

'''
    Ao fazer o Logout no Django admin somos redirecionados para
        a página index.
'''
LOGOUT_REDIRECT_URL = 'index'

'''
    Configuração do Servidor Django Heroku.
'''
django_heroku.settings(locals())