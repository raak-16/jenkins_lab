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
                    python --version
                    python -m venv venv
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
