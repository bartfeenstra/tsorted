"""Integrates TSorted with Python's setuptools."""

import os

from setuptools import setup, find_packages

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

with open('/'.join((ROOT_PATH, 'VERSION'))) as f:
    VERSION = f.read()

with open('/'.join((ROOT_PATH, 'README.md'))) as f:
    long_description = f.read()

SETUP = {
    'name': 'tsorted',
    'description': 'TSorted lets you sort your data topologically, such as for dependency resolution or task management.',
    'long_description': long_description,
    'long_description_content_type': 'text/markdown',
    'version': VERSION,
    'license': 'MIT',
    'author': 'Bart Feenstra & contributors',
    'author_email': 'bart@mynameisbart.com',
    'url': 'https://github.com/bartfeenstra/tsorted',
    'classifiers': [
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    'python_requires': '~= 3.6',
    'install_requires': [
        'orderedset ~= 2.0',
    ],
    'extras_require': {
        'development': [
            'autopep8 ~= 1.5',
            'codecov ~= 2.1',
            'coverage ~= 5.5',
            # flake8 3.8 fails on circular imports caused by string-based type hints.
            'flake8 ~= 3.7.0',
            'pytest ~= 6.2.2',
            'setuptools ~= 54.2',
            'twine ~= 3.4',
            'wheel ~= 0.36',
        ],
    },
    'packages': find_packages(),
    'data_files': [
        ('', [
            'LICENSE.txt',
            'README.md',
            'VERSION',
        ])
    ],
}

if __name__ == '__main__':
    setup(**SETUP)
