pipeline {
    agent any
    environment {
      DOCKERHUB_CREDENTIALS = credentials('docker-hub')
    }
        stages {
            stage('Build') {
                steps {
                    echo 'This is the build stage'
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