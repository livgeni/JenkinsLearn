pipeline {
    agent any
    stages {
        stage('WriteFile') {
            steps {
                from datetime import datetime

                with open('C:\Temp\HelloJenkins.txt', 'a') as file:
                    file.write(f'Current date time: {datetime.now()}')
            }
        }
    }
}