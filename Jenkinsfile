pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/KhajaHamza/AdvSWENGG.git']])
            }
        }
        stage('Build') {
            steps {
                git branch: 'main', url: 'https://github.com/KhajaHamza/AdvSWENGG.git'
                echo 'Hamza is Here'
                bat 'C:\\Users\\khaja\\AppData\\Local\\Programs\\Python\\Python39\\python.exe math_utils.py'


            }
        }
        stage('Test') {
            steps {
                bat 'C:\\Users\\khaja\\AppData\\Local\\Programs\\Python\\Python39\\python.exe -m pytest --junitxml=results.xml'
            }
        }
    }

    post {
        always {
            // Actions in this block will always be executed, regardless of the build status
            junit '/results.xml' // Publish JUnit test results
        }
    }
}
