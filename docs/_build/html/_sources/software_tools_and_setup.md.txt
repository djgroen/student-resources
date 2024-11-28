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
---
## Setting Up Your Local Development Environment
---
## Version Control with Git and GitHub
### 1. Setting Up Git
* Configure Git with your user information:
```
git config --global user.name "Your Name" git config --global user.email "your.email@example.com"
```
* Verify the configuration:
```
git config --list
```
### 2. Creating a GitHub Account
* Go to [GitHub](https://github.com/) and sign up for a free account.
* Verify your email address to complete the setup.

### 3. Creating a Local Repository
* Initialize a new Git repository in your project directory:
```
git init
```
* Add files to the repository:
```
git add .
```
* Commit the changes:
```
git commit -m "Initial commit"
```

### 4. Linking to a GitHub Repository
* Create a new repository on GitHub.
* Copy the repository URL (e.g., `https://github.com/username/repository.git`).
* Link your local repository to the GitHub repository:
```
git remote add origin https://github.com/username/repository.git
```
* Push the local changes to GitHub:
```
git push -u origin main
```
### 5. Pulling Changes from GitHub
* To update your local repository with the latest changes from GitHub:
```
git pull origin main
```
### 6. Creating and Using Branches
* Create a new branch:
```
git branch feature-branch
```
* Switch to the new branch:
```
git checkout feature-branch
```
* Merge the branch back into the main branch:
```
git checkout main git merge feature-branch
```
### 7. Resolving Merge Conflicts
* When Git identifies a conflict, open the conflicting file and look for markers (`<<<<<<<`, `=======`, `>>>>>>>`).
* Edit the file to resolve the conflict.
* Add the resolved file:
```
git add <filename>
```
* Complete the merge:
```
git commit
```
### 8. Using GitHub GUI
* GitHub provides a web interface and desktop application for managing repositories.
* Download [GitHub Desktop](https://desktop.github.com/) for a user-friendly interface
---
## Common Git Issues and Fixes
### 1. Authentication Issues
* If you're using HTTPS and encounter authentication errors, Git may not recognize your username or password:
  * Use a Personal Access Token instead of your password:
    ```
    git remote set-url origin https://<your_username>@github.com/<your_repository>.git
    ```
    When prompted, enter your token as the password.

* To avoid repeated prompts, cache your credentials:
    ```
    git config --global credential.helper cache
    ```

* For SSH setup, generate and add SSH keys to GitHub by following [GitHub's guide](https://docs.github.com/en/authentication/connecting-to-github-with-ssh).

### 2. Merge Conflicts
* If you see a conflict when merging branches:
  1. Open the file(s) with conflicts, which will contain markers like:
     ```
     <<<<<<< HEAD
     Your changes
     =======
     Their changes
     >>>>>>> branch-name
     ```

  2. Edit the file(s) to combine or choose the changes you want to keep.
  3. Add the resolved file(s):
     ```
     git add <filename>
     ```

  4. Complete the merge:
     ```
     git commit
     ```

### 3. Accidentally Committing to the Wrong Branch
* If you commit to the wrong branch, move your commit(s) to the correct branch:
    ```
    git checkout correct-branch
    git cherry-pick <commit-hash>
    ```
* Then, reset the commit from the wrong branch:
    ```
    git checkout wrong-branch
    git reset --hard HEAD~1
    ```

### 4. Undoing Changes
* Undo the last commit but keep your changes:
    ```
    git reset --soft HEAD~1
    ```

* Undo the last commit and discard changes:
    ```
    git reset --hard HEAD~1
    ```

* Discard all uncommitted changes:
    ```
    git checkout .
    git clean -f
    ```

### 5. Push Rejected Due to Non-Fast-Forward Updates
* This happens when your local branch is behind the remote branch:
    ```
    git pull --rebase origin main
    git push origin main
    ```


### 6. Detached HEAD State
* If you accidentally enter a detached HEAD state:
  1. Create a new branch to save your changes:
     ```
     git checkout -b my-temporary-branch
     ```

  2. Switch back to the correct branch and merge if needed:
     ```
     git checkout main
     git merge my-temporary-branch
     ```


### 7. Large File Errors
* If Git fails due to large files, remove them from the history:
    ```
    git filter-branch --force --index-filter \
    'git rm --cached --ignore-unmatch <filename>' \
    --prune-empty --tag-name-filter cat -- --all
    ```

---
