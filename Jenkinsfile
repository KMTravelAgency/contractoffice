pipeline {
    environment {
      DOCKER = credentials('docker-hub')
    }
    agent any
        stages {
            stage('Build') {
                steps {
                    sh 'docker build -f Dockerfile \
                    -t contractoffice:latest .'
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