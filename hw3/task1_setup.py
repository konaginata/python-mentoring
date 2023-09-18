from setuptools import setup, find_packages

setup(
    name='python-mentoring',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'certifi==2023.7.22'
        'charset-normalizer==3.2.0'
        'decorator==5.1.1'
        'idna==3.4'
        'isort==6.0.0b2'
        'prettytable==3.9.0'
        'pycodestyle==2.11.0'
        'pywin32==306'
        'requests==2.31.0'
        'self==2020.12.3'
        'urllib3==2.0.4'
        'wcwidth==0.2.6'
    ],
    entry_points={
        'console_scripts': [
            'hello=my_project.hello:main',
        ],
    },
    author='konaginata',
    author_email='konaginata@some.email',
    description='My tasks solution for the Python mentoring program',
    url='https://github.com/konaginata/python-mentoring',
    classifiers=[
        'Programming Language :: Python :: 3.11',
        'Operating System :: OS Independent',
    ],
)
