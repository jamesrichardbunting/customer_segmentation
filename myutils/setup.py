from setuptools import setup, find_packages

setup(
    name='myutils',
    version='0.1',
    packages=find_packages(),
    description='A utility package for personal data science projects',
    author='James Bunting',
    author_email='jamesrichardbunting@gmail.com',
    keywords=['utility', 'data science'],
    install_requires=[
        # Any dependencies you need, for example:
        # 'numpy',
        # 'pandas',
    ]
)
