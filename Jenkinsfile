pipeline {
    agent any

    stages {
        stage('Install Pytest') {
            steps {
                bat 'python -m pip install pytest'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'python -m pytest test_calculator.py'
            }
        }
    }
}
