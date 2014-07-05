try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Project ex47',
    'author': 'lingfeng',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'hanxiaomax@qq.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['ex47'],
    'scripts': [],
    'name': 'Project ex47 for automated test'
}

setup(**config)