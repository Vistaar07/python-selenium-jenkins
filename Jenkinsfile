pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out code...'
                git branch: 'main', url: 'https://github.com/Vistaar07/python-selenium-jenkinsgit'
            }
        }
        stage('Setup Environment') {
            steps {
                echo 'Setting up Python virtual environment...'
                sh 'python3 -m venv venv'
                sh 'source venv/bin/activate && pip install -r requirements.txt'
            }
        }
        stage('Run Selenium Tests') {
            steps {
                echo 'Running Pytest with Selenium...'
                sh 'source venv/bin/activate && pytest test_app.py'
            }
        }
    }
    post {
        always {
            echo 'Pipeline finished.'
        }
    }
}