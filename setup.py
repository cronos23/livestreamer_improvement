from setuptools import setup

setup(
    name='streamlink_helper',
    version='0.1',
    entry_points={
        'console_scripts': ['streamlink_helper=streamlink_helper:main']
    },
    install_requires=["PyYAML", "requests"],
    url='github.com/cronos23/streamlink_helper',
    py_modules=["streamlink_helper", "util", "configuration"],
    license='',
    author='Ossi Kronlöf',
    author_email='ossikronlof@gmail.com',
    description='Just a little helper script for Streamlink'
)