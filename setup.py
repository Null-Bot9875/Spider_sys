from setuptools import setup,find_packages

setup(
    name = 'Spider_sys',
    version = '0.1',
    description = 'Spider System vase on Django',
    author = 'Null',
    url = '',
    license = 'MIT',
    packages = find_packages('Spider_sys'),
    package_dir = {'':'Spider_sys'},
    package_data = {
        ' ' : [
        'themes/*/*/*/*',
        ]},
    install_requires = [
        'django>=2.23,<3.0',
    ],
    extras_require = {
        'ipython': ['ipython==6.2.1']
    },
    scripts=[
        'Spider_sys/manage.py'
    ],
    entry_points={
        'console_scripts': [
            'Spider_sys_manage = manage:main',
        ]
    },
)
classfiers=[

]