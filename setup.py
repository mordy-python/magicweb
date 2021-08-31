from setuptools import setup, find_packages

with open('README.md') as readme_file:
    README = readme_file.read()

setup_args = dict(
    name='Magicweb',
    version='1.0.1',
    description='A simple web framework',
    long_description_content_type="text/markdown",
    long_description=README,
    license='MIT',
    packages=find_packages(),
    author='Israel Waldner',
    author_email='imky171@gmail.com',
    keywords=['Web', 'Web framework', 'framework'],
    url='https://replit.com/@IsraelW/webframeworkpypi',
    download_url='https://pypi.org/project/magicweb/'
)

install_requires = ['parse', 'webob', 'waitress']
if __name__ == '__main__':
    setup(**setup_args, install_requires=install_requires)