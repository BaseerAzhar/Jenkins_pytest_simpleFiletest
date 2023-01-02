pipeline {
    agent any
    stages {
        stage('--build--') 
        {
            steps 
            {
                bat "python -m venv env"
                bat "call ./env/Scripts/activate.bat"
                bat "pip install -r requirements.txt"
            }
        }
        stage('--test--') 
        {
            steps 
            {
                bat "pytest -v -s -m check"
            }
        }
        stage('--test2--') 
        {
            steps 
            {
                bat "pytest -v -s -m webtest --alluredir=allure-results" 
            }
        }
         stage('--report--') 
        {
            steps 
            {
                allure includeProperties: false, jdk: '', results: [[path: 'allure-results']] 
            }
        }
        
    }
}
