# <span style="display:block;text-align: center;color:blue;">Creating a new package</span>

#### <p style="display:block;text-align: center;color:darkblue;">Python Package Building and Installation Guide</p>

## Overview

This guide provides detailed instructions for building and installing a Python package. It covers the steps to prepare your project, create distribution files, and install or upload the package.

## Prerequisites

1. **Python**: Ensure Python is installed on your system.
2. **Virtual Environment** (optional but recommended): Create a virtual environment to isolate your package and its dependencies.

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. Ensure Dependencies: Make sure setuptools and wheel are installed.

   ```
   sh
   pip install --upgrade setuptools wheel
   ```

## Directory Structure

Ensure your project directory contains at least the following:

    ```
    PackageBuilding/
    │
    ├── \custom_module/
    │ ├── __init__.py
    │ ├── __main__.py
    │ └── my_module.py
    │
    ├── setup.py
    ├── LICENSE
    └── README.md
    ```

## setup.py Configuration

Ensure your setup.py file is properly configured. Example:

    ```
    #python

    #!/usr/bin/env python

    from setuptools import setup, find_packages

    setup(
        name='PackageBuilding', # Name of the package
        version='1.0.0', # Version number
        description='Sample for packaging the Python project', # Description
       # The below data will be shown in the PyPI documentation
       long_description=open('README.md').read(),  # Read the detailed description from README
       long_description_content_type='text/markdown',  # Specify the format of README
        author='Gopi Krishna', # Author name
        author_email='bgk@gmail.com', # Author email
        packages=find_packages(), # Automatically discover all packages
        entry_points={
        'console_scripts': [
        'mycustom_module=custom_module.__main__:main',
        ],
        }, # Console script entry points
        python_requires='>=3.8', # Required Python version
        license='MIT', # License type
        platforms='Linux', # Supported platforms
        license_files='LICENSE' # Path to the license file
    )
    ```

## Building the Package

To create distribution files, run the following commands from the root directory of your project (where setup.py is located):

    ```
    sh
    # Build source distribution and wheel distribution
    python setup.py sdist bdist_wheel
    ```

This command will generate distribution archives in the dist/ directory.

### Example Output

Check the contents of the dist/ directory to verify the build:

    ```
    sh
    ls dist/
    ```

You should see files like:

    ```
    PackageBuilding-1.0.0.tar.gz (source distribution)
    PackageBuilding-1.0.0-py3-none-any.whl (wheel distribution)
    ```

## Installing the Package Locally

To install the package from the wheel file:

    ```
    sh
    pip install dist/PackageBuilding-1.0.0-py3-none-any.whl
    ```

Replace "PackageBuilding-1.0.0-py3-none-any.whl" with the exact filename if it differs.

## Uploading to PyPI

If you want to upload the package to PyPI (Python Package Index):

1. Install twine (if not already installed):

   ```
   sh
   pip install twine
   ```

2. Upload the distribution files:
   ```
   sh
   twine upload dist/\*
   ```
   You will be prompted for your PyPI username and password.

### Verifying the Installation

After installation, verify the package:

    ```
    sh
    pip show PackageBuilding
    ```

Replace PackageBuilding with the actual name of your package.

### Summary

###### 1. Prepare Project:

Ensure setup.py and other necessary files are in place.

###### 2. Build:

Use python setup.py sdist bdist_wheel to create distribution files.

###### 3. Install:

Use pip install to install the package locally.

###### 4. Upload:

Use twine to upload to PyPI.

###### 5. Verify:

Check the installation and package details.

By following these steps, you can efficiently build, install, and distribute your Python package.

## <span style="color:red;"><u>Note:</u></span>

1. Is __main__.py file is optional?

   ```
   Yes, the __main__.py file is optional and is only needed if you want to define a script or command-line interface (CLI) entry point for your package.

   Purpose of __main__.py
    1. Command-Line Interface: When you specify an entry point in the setup.py file under the console_scripts section (or other entry points), the command you define is expected to execute a function or script within your package.
    2. Executable Module: The __main__.py file is used to allow a module to be run as a script. If the package directory contains a __main__.py file, you can run the package directory as a script using Python's module execution feature.
   ```
