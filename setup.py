try:
    from setuptools import setup
    from setuptools import find_packages
    packages = find_packages()
except ImportError:
    from distutils.core import setup
    import os
    packages = [x.strip('./').replace('/','.') for x in os.popen('find -name "__init__.py" | xargs -n1 dirname').read().strip().split('\n')]

if bytes is str:
    raise Exception("This module is designed for python 3 only. Please install an older version to use python 2.")

setup(
    name='cle',
    description='CLE Loads Everything (at least, many binary formats!) and provides a pythonic interface to analyze what they are and what they would look like in memory.',
    version='8.19.10.30',
    python_requires='>=3.5',
    packages=packages,
    install_requires=[
        'pyelftools>=0.25',
        'cffi',
        'archinfo==8.19.10.30',
        'pyvex==8.19.10.30',
        'pefile',
        'sortedcontainers>=2.0',
        'minidump==0.0.10',
    ]
)
