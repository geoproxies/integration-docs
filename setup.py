from setuptools import setup

setup(
    name='Geoproxies',
    version='0.2.0',
    description='Documentation for the Geoproxies Proxy service',
    author='Ojutiku Oluwatobi',
    author_email='toby@globaledge-software.com',
    packages=['geoproxies'],
    keywords=['settings', 'proxy', 'integration API'],
    license='All rights reserved.',
    install_requires=['sphinx'],
    zip_safe=False,
    include_package_data=True,
)
