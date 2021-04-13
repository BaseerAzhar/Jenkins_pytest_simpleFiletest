pipeline {
    agent any
    stages {
        stage('---clean---') {
            steps {
                bat "python -m tools.path_cleaner clear-all-cache"
            }
        }
        stage('--test--') {
            steps {
                bat "pytest -v -s -m webtest"
            }
        }
        
    }
}
