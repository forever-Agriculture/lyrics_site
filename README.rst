=======================
DJANGO PROJECT TEMPLATE
=======================


*************
Clone project
*************

For example, we want to create a `superblog` project.

::

    % cd /path/to/your/projects/superblog/
    % git clone git@bitbucket.org:valsorym/django-project-structure.git superblog-source
    % cd ./superblog-source/


Change path to repository in git.

**Note**: We are in the `root directory` of your project.

**Note**: Create repository on the GitHub, Bitbucket or somewhere else.
Example:

::

    % git remote set-url origin git@bitbucket.org:valsorym/superblog-source.git

Or re-create git repository.

::

    % rm -Rf .git
    % git init
    % git remote add origin git@bitbucket.org:valsorym/superblog-source.git


******************************
Creating a virtual environment
******************************

For python 2.6 +

::

    % virtualenv -p/usr/bin/python2.7 venv
    % source venv/bin/activate
    (venv) %

For python 3.4 +

::

    % pyvenv venv
    % source venv/bin/activate
    (venv) %

**Note**: We are in a virtual environment.


***************
Version control
***************

If you not cloned the project, and only copied the files - it is reasonable to create a version control.

::

    (venv) % git init
    (venv) % git add .
    (venv) % git commit -am "Init."

**********************************
Installation of necessary packages
**********************************

For python 2.6 +

::

    (venv) % pip install -r requirements.txt


Now you can install custom tools and django the desired version.

::

    (venv) % pip install django==1.8.15 gunicorn==19.4.5
    (venv) % pip freeze > requirements.txt


For python 3.4 +

::

    (venv) % pip3 install -r requirements.txt


Now you can install custom tools and django the desired version.

::

    (venv) % pip3 install django==1.8.15 gunicorn==19.4.5
    (venv) % pip3 freeze > requirements.txt

***********************
Create a Django project
***********************

First, read the short help in the Makefile.

::

    (venv) % make help

**Note**: The nginx and supervisor must be installed on a server on the local computer is not necessary.

To create the project, do not use the standard approach Django, etc: `django-admin.py startproject <PROJECT_NAME>`. Use `make startproject`.

::

    (venv) % make startproject


**Note**: Now your project is in the `./src/` directory.
The root of the Django project: `./src/basic/`, ie, here are the files as
`settings.py`, `urls.py`, `wsgi.py` etc.


*************************
Settings a Django project
*************************

Open `settings.py` of django project.

::

    (venv) % vim ./src/basic/settings.py

In the beginning of the file paste the code:

::

    import os
    import sys

    # Build paths inside the project like this: os.path.join(BASE_DIR, ...)
    # The root directory of the Django project.
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # The root directory of the project (the lowest level).
    BASE_DIR_UP = os.path.dirname(BASE_DIR)

    # Path to the custom Django applications.
    # ** It is necessary! If a third-party app is just copied to the apps/ but not
    # installed through the pip.
    sys.path.insert(1, os.path.join(BASE_DIR, 'apps'))

    # Path to the server settings.
    sys.path.insert(1, os.path.join(BASE_DIR_UP, 'world/etc'))


In the end of the file:

::

    # Expand the default settings.
    # Loading extension parameters of standard configurations, see: world/etc/.
    try:
        from local_settings import *
    except ImportError:
        pass


Additional settings
-------------------

Default database
^^^^^^^^^^^^^^^^

::

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR_UP, 'world/var/sys/sqlite3/db.sqlite3'),
        }
    }


Static
^^^^^^

::

    _static_dirs = [os.path.join(BASE_DIR, 'website/static'), ]
    for root, dirs, files in os.walk(os.path.join(BASE_DIR, 'apps')):
        if 'static' in dirs:
            _static_dirs.append(os.path.join(root, 'static'))

    STATIC_URL = '/static/'
    STATIC_ROOT = os.path.join(BASE_DIR_UP, 'world/var/www/static')
    STATICFILES_DIRS = _static_dirs


Media
^^^^^

::

    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR_UP, 'world/var/www/media')


Templates
^^^^^^^^^

::

    _template_dirs = [os.path.join(BASE_DIR, 'website/templates'), ]
    for root, dirs, files in os.walk(os.path.join(BASE_DIR, 'apps')):
        if 'templates' in dirs:
            _template_dirs.append(os.path.join(root, 'templates'))

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': _template_dirs,
            ...
        },
    ]

Jinja2 templates support
^^^^^^^^^^^^^^^^^^^^^^^^

**Note**: Need install `django-jinja` app.

::

    from django_jinja.builtins import DEFAULT_EXTENSIONS as \
        JINJA2_DEFAULT_EXTENSIONS

    ...

    # Templates with Jinja2 support.
    _template_dirs = [os.path.join(BASE_DIR, 'website/templates'), ]
    for root, dirs, files in os.walk(os.path.join(BASE_DIR, 'apps')):
        if 'templates' in dirs:
            _template_dirs.append(os.path.join(root, 'templates'))

    TEMPLATES = [
        {
            'BACKEND': 'django_jinja.backend.Jinja2',
            'APP_DIRS': True,
            'DIRS': _template_dirs,
            'OPTIONS': {
                # Match the template names ending in .html but not the ones in the
                # admin folder.
                'match_extension': ('.jinja', '.txt'),
                'match_regex': r'^(?!admin/).*',
                'app_dirname': 'templates',

                # Can be set to "jinja2.Undefined" or any other subclass.
                'undefined': None,
                'newstyle_gettext': True,
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
                'extensions': JINJA2_DEFAULT_EXTENSIONS,
                'autoescape': True,
                'auto_reload': True,
                'translation_engine': 'django.utils.translation',
            }
        },

        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': _template_dirs,
            # 'APP_DIRS': True, # No use if used loaders!!!
            'OPTIONS': {
                'context_processors': [
                    'django.contrib.auth.context_processors.auth',
                    'django.template.context_processors.i18n',
                    'django.template.context_processors.media',
                    'django.template.context_processors.static',
                    'django.template.context_processors.tz',

                    'django.core.context_processors.request',
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
                'loaders': [
                    'django.template.loaders.filesystem.Loader',
                    'django.template.loaders.app_directories.Loader',
                ],
            },
        },
    ]


****************
Run test project
****************

::

    (venv) % cd ./src/
    (venv) % cd ./manage.py runserver 0.0.0.0:8080

Open in your borowser: http://0.0.0.0:8080/

Now, create your applications in the `apps` directory:

::

    (venv) % cd ./src/apps/
    (venv) % django-admin.py startapp <APP_NAME>


To use the local settings you will need to create a file: `./world/etc/local_settings.py`.
A template of this file can be found here: `./world/usr/options/local_settings.py.ex`.

::

    (venv) % cp ./world/usr/options/local_settings.py.ex ./world/etc/local_settings.py
    (venv) % vim ./world/etc/local_settings.py


*****************
Run on the server
*****************

After creating your project, move the project to the server and run the preset.
Do not forget, all the examples are relative to the root directory of the project.

Step 1
------

Create and activate the virtual environment, and install necessary packages.

::

    (server-venv) % pip3 install -r requirements.txt


Step 2
------

Create local settings of the Django project.

::

    (server-venv) % cp ./world/usr/options/local_settings.py.ex ./world/etc/local_settings.py
    (server-venv) % vim ./world/etc/local_settings.py


Step 3
------

Configure the deployment options.

::

    (server-venv) % cp ./world/usr/options/local_settings.sh.ex ./world/etc/local_settings.sh
    (server-venv) % vim ./world/etc/local_settings.sh

Necessarily:

- PROJECT_NAME - this name will be used to run the project use the supervisor.
- PORT - port where the project will be launched.
- USER - user by which is running the nginx, supervisor etc.
- HOST - your domain name (do not forget to configure / etc / hosts and link
your domain name to the server.)

Other parameters are recommended not to change.

Step 4
------

Deploy the project. Follow the instructions on the screen.

::

    (server-venv) % make deploy


Example of a deployment of the `superblog` project.

::

    Settings successfully loaded...

    The server will be configured with the following parameters:
        PROJECT NAME: superblog
        SOCKET: /path/to/superblog/superblog-source/world/run/superblog.sock
        PORT: 2244
        USER: django
        HOST: superblog.com
        BASE_DIR: /path/to/superblog/superblog-source
        NGINX UPSTREAM NAME: superblog_django_project

    Do you want to continue?
    [y/n]: y
    ***
    Create a link to the Nginx configurations:
    => sudo ln -s /path/to/superblog/superblog-source/world/etc/nginx.conf
    /etc/nginx/conf.d/superblog.conf
    => sudo nginx -s reload

    ***
    Create a link to the Supervisor configurations:
    => sudo ln -s /path/to/superblog/superblog-source/world/etc/supervisor.conf
    /etc/supervisor/conf.d/superblog.conf
    => sudo supervisorctl update

You can have different settings of `nginx` and `supervisor`. So pay attention!

**Nginx settings**: `./world/etc/supervisor.conf `

**Supervisor settings**: `./world/etc/supervisor.conf`

If you use Debian, and have installed `nginx` and `supervisor` use `aptitude` -
just run this four teams.


Step 5
------

Checking the status.

::

    (server-venv) % make status
    Settings successfully loaded...
    superblog       RUNNING    pid 1275, uptime 0:00:07

Stop project.

::

    (server-venv) % make stop

Start project.

::

    (server-venv) % make start

**Now you can open your project in the browser!**


*****
Notes
*****

- `./world/dev/docs` - documentation of the code.
- `./world/dev/fixtures` - fixtures for the development.
- `./world/dev/CURRENTSTEP.TXT` - notes on the latest changes.
- `./world/var/` - the data heart: static, media, logs, database (if used SQLite3), etc.

**************
Makefile tools
**************

============
lesscompiler
============

Automatic compilation of less files using the lesscpy utility.

::

    $ sudo apt-cache search lesscpy
    python-lesscpy - LessCss Compiler for Python 2.x
    python3-lesscpy - LessCss Compiler for Python 3.x


Usage::

    (venv)$ make lesscompiler


Ignore directories:

- `lib/`
- `library/`
- `import/`

Script: `./world/bin/lesscompiler.sh`.


