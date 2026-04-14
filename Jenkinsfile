pipeline {
    agent any

    environment {
        APP_NAME = "streamlit-calculator"
    }

    stages {

        stage('Clone Repo') {
            steps {
                git 'https://github.com/raak-16/jenkins_lab.git'
            }
        }

        stage('Setup Python') {
            steps {
                sh '''
                python3 --version
                python3 -m venv venv
                . venv/bin/activate
                pip install --upgrade pip
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                . venv/bin/activate
                pip install streamlit
                '''
            }
        }

        stage('Test') {
            steps {
                sh '''
                . venv/bin/activate
                echo "No tests defined yet"
                '''
            }
        }

        stage('Deploy (Run App)') {
            steps {
                sh '''
                . venv/bin/activate
                nohup streamlit run app.py --server.port 8501 &
                '''
            }
        }
    }

    post {
        success {
            echo "Pipeline executed successfully 🚀"
        }
        failure {
            echo "Pipeline failed ❌"
        }
    }
}
