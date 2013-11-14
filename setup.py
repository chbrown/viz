from setuptools import setup, find_packages

setup(
    # package information
    name='viz',
    version='0.0.2',
    author='Christopher Brown',
    author_email='io@henrian.com',
    url='https://github.com/chbrown/viz',
    keywords='console terminal data visualization plot histogram',
    description='Data visualization in the terminal',
    long_description=open('README.rst').read(),
    license=open('LICENSE').read(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Text Processing :: General',
    ],
    # setup instructions
    install_requires=[
        'numpy'
    ],
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'viz = viz.cli:main'
        ],
    },
    include_package_data=True,
)
