from setuptools import setup
import os.path

setup(
    name='mandrill-37',
    version='2.0.0',
    author='Florian Mounier. Forked by Virtusize team',
    author_email='community@mandrill.com',
    description='A CLI client and Python API library for the Mandrill email as a service platform. Forked fork python 3.7 support',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README')).read(),
    license='Apache-2.0',
    keywords='mandrill email api',
    package=[
        "mandrill"
    ],
    py_modules=['mandrill'],
    install_requires=['requests >= 0.13.2', 'docopt == 0.4.0'],
    provides='mandrill',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache Software License',
        'Topic :: Communications :: Email'
    ]
)
