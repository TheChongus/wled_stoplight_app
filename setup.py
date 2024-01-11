from setuptools import setup, find_packages

setup(
    name='wled-stoplight',
    version='0.1.0',
    description='',
    author='Luke Levesque',
    author_email='Luke.LVSQ5@gmail.com',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    python_requires='>=3.11',
)