import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 's^k9dgn$2v030icga%8=9!9s)+h9!xmz#6h2!9tf7lf5y_p+)v'
DEBUG = True

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'casinogoodorbad@gmail.com'
EMAIL_HOST_PASSWORD = 'Jkf__Tefs+=th76Kdf(98'
EMAIL_PORT = 587
DEFAULT_FROM_EMAIL = "Support <casinogoodorbad@gmail.com>"


ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'account.apps.AccountConfig',
    'django.contrib.auth',
    'django.contrib.messages',
    'fluent_comments',
    'crispy_forms',
    'threadedcomments',
    'django_comments',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'ckeditor',
    'ckeditor_uploader',
    'django.contrib.staticfiles',
    'search_en',
    'promo_en',
    'articles_en.apps.ArticlesEnConfig',
    'casino_online_en.apps.CasinoOnlineEnConfig',
    'contact_en.apps.ContactEnConfig',
    'social_django',
    'memcache_status',
    'news_en',
    'robots',
    'rest_framework',
    'streams',
]


ROBOTS_SITEMAP_URLS = [
    'https://casinogoodorbad.com/sitemap.xml',
]

ROBOTS_USE_HOST = False
ROBOTS_SITEMAP_VIEW_NAME = 'django.contrib.sitemaps.views.sitemap'

COMMENTS_APP = 'fluent_comments'

FLUENT_COMMENTS_EXCLUDE_FIELDS = ('name', 'email', 'url', 'title')
FORMAT_MODULE_PATH = 'settings.locale'

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'account.authentication.EmailAuthBackend',
    'social_core.backends.google.GoogleOAuth2',
]

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '658199992451-fuvpkm80dshuqjugqk1avq2n26cfojbr.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'UPevgvMpRdwN-zIHTW4IvHrI'

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale/'),
)

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

STATIC_PRECOMPILER_ROOT = os.path.join('precompiler-static')

ROOT_URLCONF = 'myproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.media',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

WSGI_APPLICATION = 'myproject.wsgi.application'

CACHE_MIDDLEWARE_ALIAS = 'default'
CACHE_MIDDLEWARE_SECONDS = 0
CACHE_MIDDLEWARE_KEY_PREFIX = ''

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
        'TIMEOUT': None,
    }
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'defaultdb',
        'USER': 'doadmin',
        'PASSWORD': 'ynsc4mg6qz2gri46',
        'HOST': 'casinogob-do-user-6051346-0.a.db.ondigitalocean.com',
        'PORT': '25060',
    }
}

SITE_ID = 3

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

LANGUAGE_CODE = 'en-GB'
TIME_ZONE = 'UTC'
USE_I18N = False
USE_L10N = True
USE_TZ = True



STATIC_URL = '/static/'
STATIC_DIR = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [STATIC_DIR, ]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_CONFIGS = {
    'default': {
        # 'skin': 'moono',
        # 'skin': 'office2013',
        'toolbar_Basic': [
            ['Source', '-', 'Bold', 'Italic']
        ],
        'toolbar_YourCustomToolbarConfig': [
            {'name': 'document', 'items': ['Source', '-', 'Save', '-', 'Templates']},
            {'name': 'clipboard',
             'items': ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo']},
            {'name': 'editing', 'items': ['Find', 'Replace', '-', ]},  # 'SelectAll'
            # {'name': 'forms',
            #  'items': ['Form', 'Checkbox', 'Radio', 'TextField', 'Textarea', 'Select', 'Button', 'ImageButton',
            #            'HiddenField']},
            # '/',
            {'name': 'basicstyles',
             'items': ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-',
                       'RemoveFormat']},
            {'name': 'paragraph',
             'items': ['NumberedList', 'BulletedList', '-', '-', 'Blockquote', '-',
                       'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-']},
            # 'Outdent', 'Indent', 'CreateDiv',  'BidiLtr', 'BidiRtl', 'Language'
            {'name': 'links', 'items': ['Link', 'Unlink', 'Anchor']},
            {'name': 'insert', 'items': ['Image', 'Youtube', 'Table', 'Smiley']},
            # 'HorizontalRule', 'SpecialChar', 'PageBreak'
            # '/',
            {'name': 'styles', 'items': ['Styles', 'Format', 'Font', 'FontSize']},
            {'name': 'colors', 'items': ['TextColor', 'BGColor']},
            {'name': 'tools', 'items': ['Maximize', 'ShowBlocks']},
            # {'name': 'about', 'items': ['About']},
            # '/',  # put this to force next toolbar on new line
            {'name': 'yourcustomtools', 'items': [
                # put the name of your editor.ui.addButton here
                'Preview',
                'Maximize',
                'CodeSnippet',
            ]},
        ],
        'toolbar': 'YourCustomToolbarConfig',  # put selected toolbar config here
        'toolbarGroups': [{'name': 'document', 'groups': ['mode', 'document', 'doctools']}],
        'height': 300,
        # 'width': '100%',
        'filebrowserWindowHeight': 725,
        # 'filebrowserWindowWidth': 940,
        # 'toolbarCanCollapse': True,
        # 'mathJaxLib': '//cdn.mathjax.org/mathjax/2.2-latest/MathJax.js?config=TeX-AMS_HTML',
        'tabSpaces': 4,
        'extraPlugins': ','.join([
            'uploadimage',  # the upload image feature
            # your extra plugins here
            'div',
            'autolink',
            'autoembed',
            'embedsemantic',
            # 'autogrow',
            # 'devtools',
            'widget',
            'lineutils',
            'clipboard',
            'dialog',
            'dialogui',
            'elementspath',
            'codesnippet',
            'youtube'
        ]),
    },
}
