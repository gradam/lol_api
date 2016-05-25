from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()

setup(
    name='lol_api',
    version='0.1.3',
    description='wrapper and utils for League of Legends API',
    long_description=readme(),
    url='https://github.com/gradam/lol_api',
    author='Jakub "Gradam" Semik',
    author_email='kuba.semik@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Intended Audience :: Developers',
        'Topic :: Internet',
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest', 'pytest-mock'],
    packages=['lol_api'],
    install_requires=[
      'requests',
    ],
    keywords='league of legends api wrapper',
    zip_safe=False,
)
