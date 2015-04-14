from setuptools import setup

setup(
    name='ESCGProject',
    version='1.0',
    long_description=__doc__,
    packages=['ESCGProject'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
    'Flask>=0.10',
    'PyMySQL>=0.6',
    'Flask-WTF>=0.11',
    'paypalrestsdk>=1.1.0'
	]
)
