pipeline {
  agent {
    docker {
      image 'python:3.8-alpine'
    }

  }
  stages {
    stage('Build') {
      steps {
        sh 'python3 --version'
      }
    }

    stage('login') {
      steps {
        sh 'echo hello'
      }
    }

    stage('docker test') {
      agent {
        node {
          label 'built-in'
        }

      }
      steps {
        sh 'docker --version'
      }
    }

  }
  environment {
    dockerhub = credentials('dockerhub')
  }
}