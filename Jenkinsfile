pipeline {
    agent any
    environment {
      DOCKERHUB_CREDENTIALS = credentials('docker-hub')
    }
        stages {
            stage('Build') {
                steps {
                    sh 'docker build -t kenn643r/contractoffice:latest .'
                }
            }
            stage('Test') {
                steps {
                    echo 'This is the Testing Stage'
                }
            }
            stage('Deploy') {
                steps {
                    echo 'This is the Deploy Stage'
                }
            }
        }
    }