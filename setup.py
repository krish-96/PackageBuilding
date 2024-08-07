from setuptools import setup, find_packages

setup(
    name="PackageBuilding",
    version="1.0.3",
    description="How to build the custom package in Python",
    # The below data will be shown in the PyPI documentation
    long_description=open('README.md').read(),  # Read the detailed description from README
    long_description_content_type='text/markdown',  # Specify the format of README
    author="Krishna Belamkonda",
    author_email="Krishna@gmail.com",
    packages=find_packages(),  # Automatically discover all packages and sub-packages
    python_requires='>=3.8',  # Required Python version
    license='MIT',  # License type
    platforms='Any',  # Supported platforms
    license_files='LICENSE',  # Path to the license file
    # The below key is required when we are working with Command-Line Interface and Executable Module
    # entry_points={
    #     'console_scripts': [
    #         'my_custom_package=custom_module.__main__:main',  # CLI command and entry point
    #     ],
    # },
)
