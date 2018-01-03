from setuptools import setup

setup(
    name='id_phonenumbers',
    packages=['id_phonenumbers'],
    version='0.3.0',
    description='Indonesian Phonenumbers Parser',
    license='MIT',
    author='Steven',
    author_email='stvn.bu@gmail.com',
    url='https://github.com/SeiryuZ/id_phonenumbers',
    download_url='https://github.com/SeiryuZ/id_phonenumbers/tarball/0.2.0',
    keywords=['phonenumbers', 'Indonesia'],
    install_requires=['phonenumberslite'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
