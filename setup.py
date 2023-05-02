from setuptools import setup, find_packages

setup(
    name='data-beaver',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'google-cloud-core',
        'google-cloud-bigquery',
    ],
    description='Beaverish about data.',
    author='Luke Anthony Pollen',
    author_email='luke@pollenanalytics.com',
    url='https://github.com/rainbowpusheenthe3rd/dataBeaver',
)