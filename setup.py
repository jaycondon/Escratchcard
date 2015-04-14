from setuptools import setup

setup(
    name='ESCGProject',
    version='1.0',
    long_description=__doc__,
    packages=['runserver'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
    'Flask>=0.10',
    'SQLAlchemy>=1.0',
    'WTF>=.11'
	]
)
