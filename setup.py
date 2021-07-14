from setuptools import setup, find_packages

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='exchangelib_listener',
    version='1.0.0',
    author='Evan Brown',
    description='Simple inbox event listener',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://gitlab.com/evan_brown/exchangelib-listener',
    packages=find_packages(exclude=('test.*')),
    install_requires=[
        'backports.zoneinfo==0.2.1',
        'cached-property==1.5.2',
        'certifi==2021.5.30',
        'cffi==1.14.6',
        'charset-normalizer==2.0.1',
        'cryptography==3.4.7',
        'defusedxml==0.7.1',
        'dnspython==2.1.0',
        'exchangelib==4.4.0',
        'idna==3.2',
        'isodate==0.6.0',
        'lxml==4.6.3',
        'ntlm-auth==1.5.0',
        'oauthlib==3.1.1',
        'pycparser==2.20',
        'Pygments==2.9.0',
        'python-dotenv==0.18.0',
        'pytz==2021.1',
        'requests==2.26.0',
        'requests-ntlm==1.1.0',
        'requests-oauthlib==1.3.0',
        'six==1.16.0',
        'tzdata==2021.1',
        'tzlocal==2.1',
        'urllib3==1.26.6',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8'
)