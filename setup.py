from setuptools import setup, find_packages


setup(
    name='thegoat',
    version='0.1',
    license='MIT',
    description='The Goat CLI',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'thegoat = thegoat.cli:main',
        ],
    },
    author='thegoat.ir',
    author_email='we@thegoat.ir',
    url='https://github.com/thegoat-ir/cli-py',
    keywords=[
        'thegoat',
        'whois',
        'whois lookup',
        'thegoat-cli',
    ],
    install_requires=[
        "urllib3"
    ],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.9',
    ],
    python_requires='>=3',

)
