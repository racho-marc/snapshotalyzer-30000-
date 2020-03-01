from setuptools import setuptools

setup(
    name='snapshotalyzer-30000',
    version='0.1',
    author="Marc Racho",
    author_email="me@marcracho.com",
    description="SnapshotAlyzer 30000 is a tool to manage AWS EC2 instances",
    license="GPLv3+",
    packages=['shotty'],
    url="https://github.com/racho-marc/snapshotalyzer-30000-",
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
        [console_scripts]
        shotty=shotty.shotty:cli
    ''',


)
