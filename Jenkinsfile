pipeline {
    agent any

    stages {
        stage('Get Code') {
            steps {
                checkout scm
            }
        }

        stage('Install Pytest') {
            steps {
                sh '''python3 -m pip install pytest'''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''python3 -m pytest test_calculator.py'''
            }
        }
    }
}
