
from setuptools import setup

setup(
    name="django-project",
    version="0.1",
    description="Django app using buildout",
    author="Aaron Madison",

    package_dir={'': 'src'},
    install_requires = (
        'django==1.3-beta-1',
        'mock',          # used for testing purposes
        'django-debug-toolbar',
#        'south',         # incredibly useful for database migrations
#        'pyyaml',        # useful for fixtures and testing
#        'coverage',      # useful for continuous integration, tells how much of code is covered by tests
#        'clonedigger',   # useful for continuous integration, looks for duplicate chunks of code
#        'unittest-xml-reporting', # useful for continuous integration, makes nice test results
#        'pylint',        # useful for continuous integration, looks at code quality
    ),
    dependency_links = ('http://www.djangoproject.com/download/1.3-beta-1/tarball/#egg=django-1.3-beta-1',),
)
