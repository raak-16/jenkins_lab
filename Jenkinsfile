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
                bat '''
                python --version
                python -m venv venv
                venv\\Scripts\\activate
                pip install --upgrade pip
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '''
                venv\\Scripts\\activate
                pip install -r requirements.txt
                '''
            }
        }

        stage('Deploy (Run App)') {
            steps {
                bat '''
                venv\\Scripts\\activate
                start streamlit run app.py --server.port 8501
                '''
            }
        }
    }
}
