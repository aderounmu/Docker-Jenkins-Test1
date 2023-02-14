pipeline {
  agent {
    node {
      label 'jenkin-agent-alpine'
    }

  }
  stages {
    stage('Build') {
      steps {
        sh 'docker image build -t mytest/flask_docker_test .'
      }
    }

    stage('login') {
      agent any
      steps {
        sh 'docker login -u $DOCKERHUB_USER -p $DOCKERHUB_PASSWORD'
      }
    }

    stage('Push') {
      agent any
      steps {
        sh 'docker push mytest/flask_docker_test:latest'
      }
    }

  }
}