from distutils.core import setup
from setuptools import find_packages

pkgs = find_packages()

setup(name='conda-devsummit-2017-talk',
      version='1.0',
      description='Python presentation from Dev Summit 2017.',
      author='Shaun Walbridge',
      author_email='cdow@esri.com',
      url='http://www.arcgis.com',
      packages=pkgs,
      include_package_data=True,
      license='Apache', )
