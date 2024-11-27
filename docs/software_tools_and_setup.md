# Software Tools and Setup

## Installing Essential Development Tools (e.g., Python, Git, IDEs)
### Mac:
#### 1. Installing Python
* macOS typically comes with Python preinstalled, but it's recommended to install the latest version.
* Use Homebrew to manage installations:
```
# For Bash Shells:
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# For Zsh Shells:
/bin/zsh -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

```
```
brew install python3
```
* Verify the installation:
```
python3 --version # E.g. Python 3.9.20
pip3 --version # E.g. pip 24.3.1 from /Path/to/Python
```
#### 2. Installing Git and Github
Version control is essential for managing changes to your codebase and collaborating with others. 
Git is a popular version control system, and [Github](https://github.com/) is a cloud-based platform for hosting Git repositories which can be used directly in the command-line or as a GUI through their website or app.
* Install Git using Homebrew:
```
brew install git
```
* Verify the installation:
```
git --version
```
#### Installing an IDE (e.g. VS Code)
* Simply follow the instructions [here](https://code.visualstudio.com/)
### Windows:
#### 1. Installing Python
* Download Python from the [official website](https://www.python.org/).
* During installation, ensure you check the box **"Add Python to PATH"**.
* Verify the installation:
```
python --version pip --version
```
#### 2. Installing Git
* Download Git from [git-scm.com](https://git-scm.com/).
* During installation:
  - Select **"Git from the command line and also from 3rd-party software"**.
  - Choose your preferred text editor (e.g., Vim, Nano, or VS Code).
  - Leave other options as default unless you have specific preferences.
* Verify the installation:
```
git --version
```
#### 3. Installing an IDE (e.g., VS Code)
* Download Visual Studio Code from [VS Code for Windows](https://code.visualstudio.com/).
* Run the installer and follow the setup instructions.
* During installation:
  - Ensure **"Add to PATH"** is selected.
* Open a terminal to verify the `code` command:
```
code --version
```
### Linux:
#### 1. Installing Python
* Most Linux distributions come with Python preinstalled. Check the version:
```
python3 --version
```
* Update or install Python if needed:
```
sudo apt update 
sudo apt install python3 python3-pip
```
* Verify the installation:
```
python3 --version # E.g., Python 3.9.20 
pip3 --version # E.g., pip 24.3.1 from /Path/to/Python
```
#### 2. Installing Git
* Use your package manager to install Git:
```
sudo apt install git # For Debian/Ubuntu-based systems 
sudo yum install git # For Red Hat-based systems
```
* Verify the installation:
```
git --version
```
#### 3. Installing an IDE (e.g., VS Code)
* Download the `.deb` package for Ubuntu/Debian or the `.rpm` package for Fedora from [VS Code for Linux](https://code.visualstudio.com/).
* Install the package:
```
sudo apt install ./code.deb # Debian-based systems 
sudo rpm -i code.rpm # Red Hat-based systems
```
## Setting Up Your Local Development Environment

## Version Control with Git and GitHub

## Basics of Git (commits, branches, merges)

## Common Git Issues and Fixes
