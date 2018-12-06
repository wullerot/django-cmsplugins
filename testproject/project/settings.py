from __future__ import unicode_literals

import os

SECRET_KEY = '7m!09^g9z#ksr%cc6c(7-wlw&!ir-z47s0j6&3_*q69i#lbsc^'
DEBUG = True
SITE_ID = 1
LANGUAGE_CODE = 'de'
LANGUAGES = [
    ('de', 'Deutsch'),
    ('fr', 'Fancais'),
]
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

ALLOWED_HOSTS = []
ROOT_URLCONF = 'project.urls'
WSGI_APPLICATION = 'project.wsgi.application'
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STORAGE_ROOT = os.path.join(BASE_DIR, 'storage')
STATIC_ROOT = os.path.join(STORAGE_ROOT, 'static')
MEDIA_ROOT = os.path.join(STORAGE_ROOT, 'media')

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
]

THUMBNAIL_QUALITY = 95

# Application definition
INSTALLED_APPS = [

    'project',
    'cmsplugins',
    'cmsplugins.plugins.columns',
    'cmsplugins.plugins.headers',
    'cmsplugins.plugins.iframes',
    'cmsplugins.plugins.maps',
    'cmsplugins.plugins.pictures',
    'cmsplugins.plugins.sections',
    'cmsplugins.plugins.sliders',
    'cmsplugins.plugins.teasers',
    'cmsplugins.plugins.text',
    'cmsplugins.plugins.videos',

    'compressor',
    'easy_thumbnails',
    'filer',
    'mptt',
    'polymorphic',
    'text_ckeditor',
    'text_ckeditor.links',

    'cms',
    'menus',
    'sekizai',
    'treebeard',
    'djangocms_admin_style',

    'django.contrib.redirects',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
]


MIDDLEWARE = [
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.redirects.middleware.RedirectFallbackMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.sites.middleware.CurrentSiteMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.utils.ApphookReloadMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
]


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.media',
                'django.template.context_processors.csrf',
                'django.template.context_processors.tz',
                'sekizai.context_processors.sekizai',
                'django.template.context_processors.static',
                'cms.context_processors.cms_settings'
            ],
        },
    },
]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'}, # NOQA
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},  # NOQA
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},  # NOQA
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},  # NOQA
]


COMPRESS_STORAGE = 'compressor.storage.GzipCompressorFileStorage'
COMPRESS_PRECOMPILERS = (
    ('text/x-scss', 'django_libsass.SassCompiler'),
)
LIBSASS_SOURCE_COMMENTS = True
LIBSASS_OUTPUT_STYLE = 'expanded'


THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)

THUMBNAIL_OPTIMIZE_COMMAND = {
    'png': '/usr/bin/optipng {filename}',
    'gif': '/usr/bin/optipng {filename}',
    'jpeg': '/usr/bin/jpegoptim {filename}'
}


FILER_IS_PUBLIC_DEFAULT = True
FILER_PAGINATE_BY = 200

CMS_MENU_DEBUG = True  # Prints out menu nodes and their properties
CMS_MENU_TITLE_OVERWRITE = True
CMS_REDIRECTS = True
CMS_URL_OVERWRITE = False
CMS_CACHE_DURATIONS = {
    'content': 0,
    'menus': 0,
    'permissions': 0,
}
CMS_LANGUAGES = {
    1: [
        {
            'code': 'de',
            'name': 'Deutsch',
            'fallbacks': ['fr'],
        },
        {
            'code': 'fr',
            'name': 'Francais',
            'fallbacks': ['de'],
        },

    ],
    'default': {
        'fallbacks': ['de', 'fr'],
        'redirect_on_fallback': True,
        'public': True,
        'hide_untranslated': True,
    },
}
CMS_TEMPLATES = (
    ('cms.html', 'Default'),
)
CMS_PLACEHOLDER_CONF = {
    'body': {
        'name': 'Content',
        'plugins': [
            'ColumnPlugin',
            'GalleryPlugin',
            'HeaderPlugin',
            'IFramePlugin',
            'GoogleMapPlugin',
            'PicturePlugin',
            'SectionPlugin',
            'SliderPlugin',
            'StreetViewPlugin',
            'TeaserWrapPlugin',
            'TextCKEditorPlugin',
            'TextPlugin',
            'TitlePlugin',
            'VideoPlugin',
        ],
    },
}
SECTIONS_SECTION_PLUGINS = [
    'TextCKEditorPlugin',
    'PicturePlugin',
    'ContactButtonPlugin',
    'ContactFormPlugin',
    'InquiryButtonPlugin',
    'InquiryFormPlugin',
    'GoogleMapPlugin',
]


MAPS_GOOGLEMAP_BROWSER_KEY = 'xxx'
MAPS_GOOGLEMAP_SERVER_KEY = 'xxx'
