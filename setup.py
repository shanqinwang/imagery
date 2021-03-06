#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

import imagery

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = imagery.__version__

if sys.argv[-1] == 'publish':
    try:
        import wheel
    except ImportError:
        print('Wheel library missing. Please run "pip install wheel"')
        sys.exit()
    os.system('python setup.py sdist upload')
    os.system('python setup.py bdist_wheel upload')
    sys.exit()

if sys.argv[-1] == 'tag':
    print("Tagging the version on github:")
    os.system("git tag -a %s -m 'version %s'" % (version, version))
    os.system("git push --tags")
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

def get_requirements(filepath):
    ''' parse a file of requirements and return a list of requirements within
    '''
    requirements_file = open(filepath)
    requirements = []
    for requirement in requirements_file.readlines():
        # ignore comments and extra links
        if not requirement  or requirement.startswith('#') \
           or requirement.startswith('git')  \
           or requirement.startswith('http') \
           or requirement.startswith('-r'):
            continue
        requirements.append(requirement)
    return requirements

setup(
    name='imagery',
    version=version,
    description="""Django application to manage download and processing of Landsat Imagery""",
    long_description=readme + '\n\n' + history,
    author='Wille Marcel',
    author_email='wille@wille.blog.br',
    url='https://github.com/willemarcel/imagery',
    packages=[
        'imagery',
    ],
    include_package_data=True,
    install_requires=get_requirements('requirements.txt'),
    extras_require={
        'test': get_requirements('requirements-test.txt'),
        'dev': get_requirements('requirements_dev.txt')
    },
    license="BSD",
    zip_safe=False,
    keywords='imagery',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Framework :: Django :: 1.7',
        'Framework :: Django :: 1.8',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
