<hr/>

# <span style="display:block;text-align: center;color:blue;margin-top:0px; padding-top:0px;">Creating a new package in PyPI</span>

<hr/>

## <p style="display:block;text-align: center;color:darkblue;">Python Package Building and Installation Guide</p>

### Overview

This guide provides detailed instructions for building and installing a Python package. It covers the steps to prepare your project, create distribution files, and install or upload the package.

### Prerequisites

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

### Directory Structure

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

### setup.py Configuration

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

### Building the Package

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

### Installing the Package Locally

To install the package from the wheel file:

    ```
    sh
    pip install dist/PackageBuilding-1.0.0-py3-none-any.whl
    ```

Replace "PackageBuilding-1.0.0-py3-none-any.whl" with the exact filename if it differs.

### Uploading to PyPI

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

1. <b>Prepare Project: </b> Ensure setup.py and other necessary files are in place.

2. <b>Build: </b> Use python setup.py sdist bdist_wheel to create distribution files.

3. <b>Install: </b> Use pip install to install the package locally.

4. <b>Upload: </b> Use twine to upload to PyPI.

5. <b>Verify: </b> Check the installation and package details.

By following these steps, you can efficiently build, install, and distribute your Python package.

<hr/>

# <span style="display:block;text-align: center;color:blue;">GitHub Workflow for Python Package</span>

To automate the process of building and uploading your Python package, you can use GitHub Actions. Below is a complete example of a GitHub Actions workflow configuration file with detailed explanations.

## Creating the Workflow File

1. Create a Workflow File:
   Save the following content in a file named .github/workflows/workflow.yml in your GitHub repository.
2. Add the Workflow Configuration:

   Please refer to the file located in the code at
   [github/workflows/workflow.yml](.github/workflows/workflow.yml)

## Summary:

- <b>Trigger</b>: The workflow runs on pushes to version tags.
- <b>Job</b>: Includes steps to check out code, set up Python, install dependencies, build the package, and publish it to PyPI.
- <b>Environment</b>: The job runs on the latest Ubuntu environment provided by GitHub Actions.

  <hr>

# <p style="display:block;text-align: center;color:darkblue;">Steps to Add PYPI_TOKEN Secret</p>

To securely store and use your PyPI API token in your GitHub Actions workflow, follow these steps to set it up as a secret in your GitHub repository:

## 1. Generate Your PyPI API Token

- <b>Log in to PyPI: </b>Go to PyPI and log in to your account.
- <b>Navigate to API Tokens:</b>Go to your account settings and find the "API tokens" section
- <b>Create a New Token</b>
  - Click "Add API token" or "Create token".
  - Give your token a name or description (e.g., "GitHub Actions").
  - Choose the scope of the token. For uploading packages, you generally need "Entire account" or "Specific project" access.
  - Click "Add" or "Create" to generate the token.
- <b>Copy the Token: </b>Save the token somewhere secure as you'll need it for the next steps. You won’t be able to view it again after you navigate away.

## 2. Add the Token as a Secret in GitHub

- <b>Go to Your GitHub Repository: </b>Navigate to your GitHub repository where you want to set up the workflow
- <b>Open Repository Settings:</b>Click on the "Settings" tab, which is typically located in the top menu of your repository page.

- <b>Access Secrets and Variables:</b>In the left sidebar, click on "Secrets and variables" and then "Actions"
- <b>Add a New Repository Secret:</b>

  - Click the "New repository secret" button
  - <b>Name the Secret: </b>In the "Name" field, enter PYPI_TOKEN. This name must match the secret name used in your GitHub Actions workflow file.
  - <b>Enter the Token: </b> In the "Value" field, paste the PyPI API token you copied earlier.
  - Click "Add secret" to save it.

  <hr>

# <p style="display:block;text-align: center;color:darkblue;">Tags</p>

<span> In the below examples v1.0.0 is the tagname</span>

- <b>Creating a Tag:</b> git tag v1.0.0
- <b>Create an annotated tag with a message:</b> git tag -a v1.0.0 -m "Release version 1.0.0"
- <b>List all tags:</b> git tag
- <b>List tags with additional details: </b> git tag -n
- <b>Show details of a specific tag: </b> git show v1.0.0
- <b>Delete a local tag: </b> git tag -d v1.0.0
- <b>Delete a remote tag:</b> git push origin --delete v1.0.0
- <b>Push a specific tag to a remote:</b> git push origin v1.0.0
- <b>Push all tags to a remote:</b> git push --tags
- <b>Fetch tags from a remote: </b> git fetch --tags

  <hr>

# <span style="color:red;text-align:center;display:block;"><u>FAQ</u></span>

1. Is **main**.py file is optional?

   ```
   Yes, the __main__.py file is optional and is only needed if you want to define a script or command-line interface (CLI) entry point for your package.

   Purpose of __main__.py
    1. Command-Line Interface: When you specify an entry point in the setup.py file under the console_scripts section (or other entry points), the command you define is expected to execute a function or script within your package.
    2. Executable Module: The __main__.py file is used to allow a module to be run as a script. If the package directory contains a __main__.py file, you can run the package directory as a script using Python's module execution feature.
   ```

2. When workflow will be triggered?
   ```
   As per the workflow given at github/workflows/workflow.yml,
   whenever the push event occurs and the tag pattern matches then only the workflow will run
   ```
