import os
import re

from setuptools import find_packages, setup


def get_version(package):
    # Thanks to Tom Christie
    init_py = open(os.path.join(package, '__init__.py')).read()
    return re.search("__version__ = ['\"]([^'\"]+)['\"]", init_py).group(1)


def read_md(path):
    try:
        import pypandoc
        return pypandoc.convert(path, 'rst')
    except ImportError:
        return open(path).read()


version = get_version('zalgo_telegram_bot')

setup(
    name="zalgo-telegram-bot",
    version=version,
    packages=find_packages(),
    include_package_data=True,
    license='GPLv3',
    description='Zalgo Telegram Bot',
    long_description=read_md('README.md'),
    url='https://gitlab.com/edg/zalgo-telegram-bot',
    author='Emanuele Di Giacomo',
    author_email="emanuele@digiacomo.cc",
    install_requires=['python-telegram-bot'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3)',
        'Framework :: Django',
        'Framework :: Django :: 1.9',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
