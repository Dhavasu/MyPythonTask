from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.1.0',
    packages=find_packages(),
    description='A collection of utility functions for various tasks.',
    author='Dhavasu',
    author_email='dhavasumani05@gmail.com',
    url='https://github.com/Dhavasu/my_utilities',
    install_requires=[],  # Add any package dependencies here
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
