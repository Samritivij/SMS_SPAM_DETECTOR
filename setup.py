from setuptools import setup, find_packages

setup(
    name='your_project_name',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'streamlit',
        'nltk',
        'numpy==1.23.4',
        'scikit-learn==1.2.0'
    ],
)
