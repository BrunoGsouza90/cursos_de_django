'''
    Aqui neste arquivo faremos todas configurações do nosso projeto
        Django Framework.
'''

from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-^%jsj(8vebyop0-z=5ox^awj$v52=%(59lg_adye*t_$qr8zno'

'''
    Aqui podemos ativar ou desativar o modo de depuração do Django.
'''
DEBUG = True

'''
    Aqui determinamos quais HOSTs e Domínios pode ser acessados
        quando o modo de depuração do Django está desativado
        ( DEBUG = False ).
    Se aplicarmos ['*'] , estamos dizendo ao Django que todos os
        Domínios e Hosts são permitidos.
'''
ALLOWED_HOSTS = ['*']


'''
    Aqui ficam instalados os APPs padrões do Django e é aonde
        inslaremos os nossos APPs do projeto.
'''
INSTALLED_APPS = [
    
    #   App responsável pela parte administrativa do Django.
    'django.contrib.admin',
    
    #   App responsável pela autentificação na área administrativa.
    'django.contrib.auth',

    #   App responsável por permitir diferentes tipos de contéudos.
    'django.contrib.contenttypes',
    
    #   App responsável por criar sesões para os usuários autenticados.
    'django.contrib.sessions',
    
    #   App responsável por fazer a troca de mensagens entre as
    #       aplicações.
    'django.contrib.messages',

    #   Aplicação responsável por gerenciar arquivos estáticos, como
    #       imagens, favicons, vídeos, áudios, e etc.
    'django.contrib.staticfiles',
    
    # Adição dos nossos aplicativos:
    'core',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
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
        
        #   Estamos indicando aqui que dentro do nosso app, onde
        #       armazenaremos nossos templates HTML.
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


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases


'''
    Por padrão o Django uso o Banco de Dado SQLite, mais podemos
        configurar o ambiente para o Banco de Dados de nossa
        preferência.
'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

'''
    Configuração para o idioma português do Brasil.
'''
LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'