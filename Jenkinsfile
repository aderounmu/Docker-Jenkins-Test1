pipeline {
  agent none
  stages {
    stage('Build') {
      agent {
        docker {
          image 'python:3.8-alpine'
        }

      }
      steps {
        sh 'python3 --version'
      }
    }

    stage('login') {
      agent any
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