from setuptools import setup, find_packages

DESCRIPTION = 'PyVDP: VISA APIs. Wrapped in Python.'


CLASSIFIERS = [
    'Environment :: Web Environment',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
]

setup(
    name='pyvdp',
    version='1.2.0',
    author='Pavel Pokrovskiy',
    author_email='ppokrovsky@gmail.com',
    license='MIT',
    description=DESCRIPTION,
    keywords=['visa', 'vdp', 'payment'],
    platforms=['OS Independent'],
    classifiers=CLASSIFIERS,
    packages=find_packages(exclude=["tests", "tests.*"]),
    install_requires=[
        'setuptools',
        'six',
        'requests',
        'jsonpickle'
    ],
    url='https://www.github.com/ppokrovsky/pyvdp',
    include_package_data=True,
    package_data={'': ['LICENSE.txt', 'README.rst'], 'pyvdp': ['configuration.ini.example']},
)
