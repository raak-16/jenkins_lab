pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                git 'https://github.com/raak-16/jenkins_lab.git'
            }
        }

        stage('Setup Python') {
            steps {
                bat """
                    @echo off
                    for /f "delims=" %%i in ('where python 2^>nul') do (
                        set PYTHON_EXE=%%i
                        goto :found
                    )
                    echo ERROR: Python not found in PATH & exit /b 1

                    :found
                    echo Found Python at %PYTHON_EXE%
                    "%PYTHON_EXE%" --version
                    "%PYTHON_EXE%" -m venv venv
                    venv\\Scripts\\python.exe -m pip install --upgrade pip
                """
            }
        }

        stage('Install Dependencies') {
            steps {
                bat "venv\\Scripts\\pip.exe install -r requirements.txt"
            }
        }

        stage('Deploy (Run App)') {
            steps {
                bat 'start /B venv\\Scripts\\streamlit.exe run app.py --server.port 8501'
            }
        }
    }
}
