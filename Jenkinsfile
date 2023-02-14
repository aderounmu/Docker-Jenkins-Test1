pipeline {

  agent {
    node {
      label 'jenkin-agent-alpine'
    }

  }
  environment{
    dockerhub=credentials('dockerhub')
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
        sh 'docker login -u $dockerhub_USR -p $dockerhub_PSW'
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