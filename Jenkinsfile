pipeline {
    agent any
    stages {
        stage('--build--') 
        {
            steps 
            {
                bat "pip install -r requirements.txt"
            }
        }
        stage('--test--') 
        {
            steps 
            {
                bat "pytest -v -s -m check"
            }
        }stage('--report--') 
        {
            steps 
            {
                bat "pytest -v -s -m webtest --alluredir=allure-results"
            }
        }
        
    }
}
