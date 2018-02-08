import re
from pathlib import Path

from setuptools import find_packages, setup

VERSION_REGEX = r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]'

init = Path('aioipfsapi/__init__.py')
# readme = Path(__file__).with_name('README.rst')
version_match = re.search(VERSION_REGEX, init.read_text('utf-8'), re.MULTILINE)

if version_match:
    version = version_match.group(1)
else:
    raise RuntimeError('Cannot find version information')

setup(
    name='aioipfs-api',
    version=version,
    description='asyncio ipfs client',
    # long_description=readme.read_text('utf-8'),
    author='Quan Zhou',
    author_email='hi@cole.io',
    url='https://github.com/zh0uquan/aioipfs-api',
    packages=find_packages('aioipfs-api'),
    package_dir={'': 'aioipfsapi'},
    license='MIT',
    keywords=['', 'ipfs', 'asyncio'],
    install_requires=[
        'aiohttp>=2.3.1',
        'ipfsapi==0.4.2',
        'asyncio_extras==1.3.0'
    ]
)
