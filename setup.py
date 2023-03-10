import os
from setuptools import setup, find_packages

from arduino_web_inject.main import __version__

here = os.path.dirname(__file__)

README = """
Project Name
Welcome to Project Name! This is a Python project that does XYZ.

Installation
To install Project Name, you can use pip:

Copy code
pip install project-name
Usage
To use Project Name, you can import it in your Python code:

python
Copy code
import project_name

# Use project_name here
For more details and examples, please refer to the project's documentation on GitHub.

Documentation
For detailed documentation and examples, please refer to the project's documentation on GitHub:

https://github.com/your-username/project-name

License
This project is licensed under the MIT License - see the LICENSE file for details.

Thank you for using Project Name!
"""

LICENSE = open(os.path.join(here, 'LICENSE')).read()

setup(
    name='arduino-web-inject',
    version=__version__,
    license='MIT',
    description='Inject and build web files into your sketches',
    long_description=README,
    url='https://github.com/fulminati/arduino-web-inject',
    download_url='https://github.com/fulminati/arduino-web-inject',
    author='Francesco Bianco',
    author_email='bianco@javanile.org',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=True,
    test_suite='tests.tests.suite',
    tests_require=[],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.2",
        "Topic :: Text Processing :: Markup :: HTML",
    ],
    entry_points={
        'console_scripts': [
            'arduino-web-inject = arduino_web_inject.main:main',
        ],
    },
    install_requires=[
        "watchfiles",
        "csscompressor",
        "htmlmin",
        "binaryornot",
        "rjsmin",
        "slimit"
    ]
)
