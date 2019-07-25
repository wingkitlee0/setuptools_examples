from setuptools import setup, find_packages

setup(
    name='testscript2',
    version='0.1.0',
    package_dir={'': 'src'},
    packages=find_packages('src'),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'testscript2 = testscript2.testscript2:main',
        ],
    },
)
