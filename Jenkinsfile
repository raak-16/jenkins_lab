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
                sh '''
                    python3 --version
                    python3 -m venv venv
                    source venv/bin/activate
                    pip install --upgrade pip
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    source venv/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Deploy (Run App)') {
            steps {
                sh '''
                    source venv/bin/activate
                    nohup streamlit run app.py --server.port 8501 > output.log 2>&1 &
                '''
            }
        }
    }
}
