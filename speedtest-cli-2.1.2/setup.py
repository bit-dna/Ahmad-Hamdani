import os
import re
import codecs

from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))

def find_version(*file_paths):

    try:
        f = codecs.open(os.path.join(here, *file_paths), 'r', 'latin1')
        version_file = f.read()
        f.close()
    except:
        raise RuntimeError("Unable to find version string.")

    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


try:
    f = codecs.open('README.rst', encoding='utf-8')
    long_description = f.read()
    f.close()
except:
    long_description = ''


setup(
    name='speedtest-cli',
    version=find_version('speedtest.py'),
    description=('Command line interface for testing internet bandwidth using '
                 'speedtest.net'),
    long_description=long_description,
    keywords='speedtest speedtest.net',
    author='Matt Martz',
    author_email='matt@sivel.net',
    url='https://github.com/sivel/speedtest-cli',
    license='Apache License, Version 2.0',
    py_modules=['speedtest'],
    entry_points={
        'console_scripts': [
            'speedtest=speedtest:main',
            'speedtest-cli=speedtest:main'
        ]
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python',
        'Environment :: Console',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.4',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ]
)
