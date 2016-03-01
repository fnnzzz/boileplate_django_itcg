PIPELINE_CSS = {
    'main_css': {
        'source_filenames': (
          'sass/base.scss',
        ),
        'output_filename': 'css/main.css',
        'variant': 'datauri',
    },  
    'libs_css': {
        'source_filenames': (
          #'fontawesome/css/font-awesome.min.css',
        ),
        'output_filename': 'css/libs.css',
        'variant': 'datauri',
    }
}

PIPELINE_JS = {
    'main_js': {
        'source_filenames': (
          'js/common.js',
        ),
        'output_filename': 'js/common.js',
    },
    'libs_js': {
        'source_filenames': (
          'jquery/dist/jquery.min.js',
        ),
        'output_filename': 'js/libs.js',
    },
     'ie_js': {
        'source_filenames': (
          'html5shiv/dist/html5shiv.min.js',
          'Respond/dest/respond.min.js',
        ),
        'output_filename': 'js/ie.js',
     },
}

PIPELINE_COMPILERS = (
  'pipeline.compilers.sass.SASSCompiler',
)


TEMPLATE_LOADERS = (
    ('pyjade.ext.django.Loader', (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )),
)


# - - - - - - - - - - - - - - - - - - - - - - - -
# urls 
# - - - - - - - - - - - - - - - - - - - - - - - -

from django.views.generic import TemplateView
url(r'^$', TemplateView.as_view(template_name='main-page.html'), name='index'),


# - - - - - - - - - - - - - - - - - - - - - - - -
# meta viewport 
# - - - - - - - - - - - - - - - - - - - - - - - -

<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="viewport" content="width=device-width, initial-scale=0.7, maximum-scale=1.0, user-scalable=1">
<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no">