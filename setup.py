from setuptools import setup, find_packages

setup(
    name='haversine',
    version='0.0.1',
    url='https://github.com/lkilcommons/sphinx-tutorial.git',
    author='Liam Kilcommons',
    author_email='liam.kilcommons@colorado.edu',
    description='Calculate shortest distance betweeen two points on a sphere',
    packages={'haversine'},
    package_dir={'haversine':'haversine'},
    install_requires=['numpy']
)