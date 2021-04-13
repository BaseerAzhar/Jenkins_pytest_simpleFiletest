pipeline {
    agent any
    stages {
        stage('---clean---') {
            steps {
                sh "python -m tools.path_cleaner clear-all-cache"
            }
        }
        stage('--test--') {
            steps {
                bat "pytest -v -s -m webtest"
            }
        }
        
    }
}
