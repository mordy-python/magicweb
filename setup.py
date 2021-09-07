from setuptools import setup, find_packages
from magicweb import __version__
with open('README.md') as readme_file:
    README = readme_file.read()

setup_args = dict(
    name='Magicweb',
    version=__version__,
    description='A simple web framework',
    long_description_content_type="text/markdown",
    long_description=README,
    license='MIT',
    packages=find_packages(),
    author='Israel Waldner',
    author_email='imky171@gmail.com',
    keywords=['Web', 'Web framework', 'framework'],
    url='https://github.com/mordy-python/magicweb',
    download_url='https://pypi.org/project/magicweb/',
    documentation="https://magicweb-docs.web.app"
)

install_requires = ['parse', 'webob', 'waitress', 'jinja2']
if __name__ == '__main__':
    setup(**setup_args, install_requires=install_requires)