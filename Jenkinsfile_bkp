pipeline {
    agent any

    stages {

        stage('Clone') {
            steps {
                echo 'Cloning repository...'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t flask-cicd-demo .'
            }
        }

        stage('Stop Old Container') {
            steps {
                sh 'docker stop flask-app || true'
                sh 'docker rm flask-app || true'
            }
        }

        stage('Run New Container') {
            steps {
                sh '''
                docker run -d \
                --name flask-app \
                -p 5000:5000 \
                flask-cicd-demo
                '''
            }
        }
    }
}
