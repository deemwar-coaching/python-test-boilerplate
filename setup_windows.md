Certainly! Below is a step-by-step guide for installing Python, Poetry, Visual Studio Code (VS Code), and Git on Windows. This guide is designed to be clear and easy to follow for your team members, regardless of their familiarity with these tools.

---

### Installation Guide for Python, Poetry, VS Code, and Git on Windows

#### Installing Python

1. **Download Python**:
   - Visit the official Python website at [python.org](https://www.python.org/).
   - Go to the Downloads section and choose the latest version for Windows.
   - Click on the download link for "Windows x86-64 executable installer" for most users.

2. **Run the Installer**:
   - Once downloaded, run the installer.
   - Important: Ensure you check the box that says "Add Python 3.x to PATH" at the bottom of the installer window.
   - Click on "Install Now".

3. **Verify Installation**:
   - Open Command Prompt and type `python --version`.
   - You should see the Python version number if the installation was successful.

#### Installing Poetry

1. **Install Poetry**:
   - Open PowerShell as an administrator.
   - Run the following command:
     ```powershell
     (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -

     ```

2. **Verify Installation**:
   - In PowerShell, type `poetry --version`.
   - You should see the installed Poetry version.

#### Installing Visual Studio Code (VS Code)

1. **Download VS Code**:
   - Visit the [Visual Studio Code website](https://code.visualstudio.com/).
   - Click on the download for Windows.

2. **Run the Installer**:
   - Execute the downloaded file.
   - Follow the installation instructions, leaving all default settings.

3. **Verify Installation**:
   - Once installed, open VS Code to ensure it runs correctly.

#### Installing Git

1. **Download Git**:
   - Go to the [Git website](https://git-scm.com/).
   - Click on "Download for Windows".

2. **Run the Installer**:
   - Open the downloaded file and follow the installation prompts.
   - Leave all default settings unless you have specific preferences.

3. **Verify Installation**:
   - Open Command Prompt or PowerShell.
   - Type `git --version`.
   - You should see the installed Git version.

---

#### Post-Installation

- **Configure Git**:
  - Set up your Git user name and email, which are important for commit messages.
  - In Command Prompt or PowerShell, run:
    ```bash
    git config --global user.name "Your Name"
    git config --global user.email "your.email@example.com"
    ```

- **Install VS Code Extensions**:

1. Python Extension Pack
2. Python Test Explorer for Visual Studio Code

- **Check for Updates Regularly**:
  - Regularly check for updates to Python, Poetry, VS Code, and Git to ensure you have the latest features and security updates.

