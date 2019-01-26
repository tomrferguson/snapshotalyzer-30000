from setuptools import setup

setup(
    name='snapshotalyzer-3000',
    version='0.1',
    author="tom ferguson",
    author_email="tomrferguson@gmail.com",
    description="snapshotalyzer 3000 is a tool to manage AWS EC2 snapshots",
    license="GPLv3+",
    packages=['shotty'],
    url="https://github.com/tomrferguson/snapshotalyzer-30000",
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
        [console_scripts]
        shotty=shotty.shotty:cli
    ''',
)
