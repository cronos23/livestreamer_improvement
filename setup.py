from setuptools import setup, find_packages

setup(
    name='streamlink_helper',
    version='0.1',
    entry_points={
        'console_scripts': ['streamlink_helper=streamlink_helper:main']
    },
    packages=find_packages("venv.lib.site_packages"),
    url='github.com/cronos23/livestream_helper',
    license='',
    author='Ossi Kronlöf',
    author_email='ossikronlof@gmail.com',
    description='Just a little helper script for Streamlink'
)
