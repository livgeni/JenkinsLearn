pipeline {
    agent any
    stages {
        stage('WriteFile') {
            steps {
                bat 'python HelloJenkins.py'
            }
        }
        stage('ReadFile') {
            steps {
                bat 'type c:\temp\HelloJenkins.txt'
            }
        }
    }
}
