pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Puedes realizar la descarga de tu código fuente aquí si es necesario.
            }
        }

        stage('Ejecutar Pruebas') {
            steps {
                sh 'python3 main.py'
            }
        }

        stage('Generar Reporte') {
            steps {
                sh 'allure generate -c -o allure-results'
            }
        }
    }

    post {
        always {
            archiveArtifacts 'allure-results'
            allure([includeProperties: false, jdk: '', properties: [], reportBuildPolicy: 'ALWAYS', results: [[path: 'allure-results']]])
        }
    }
}
