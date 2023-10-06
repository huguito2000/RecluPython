pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Run Selenium Tests') {
            steps {
                sh 'python3 test_selenium.py'
            }
        }
    }
}