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
                sh 'pytest --junitxml=pytest_report.xml main.py'
            }
        }
    }
}
