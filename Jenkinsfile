pipeline {
  agent none
  environment {
    DOCKERHUB_CREDENTIALS  = credentials('dockerhub')
  }
  stages {
    stage('Test') {
      agent {
        docker {
          image 'python:3.8-alpine'
        }

      }
      steps {
        sh 'python3 --version'
      }
      steps {
        sh 'pip install -r requirements.txt'
      }
      steps {
        sh 'pytest'
      }
    }
    stage('Build') {
      agent {
        node {
          label 'built-in'
        }

      }
      steps {
        sh 'docker --version'
      }

      steps {
        sh 'docker build -t aderounmu/docker-flask:python:3.8-alpine .'
      }
    }

    stage('Login') {
      agent {
        node {
          label 'built-in'
        }

      }
      steps {
        sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
      }
    }

    stage('Push') {
      agent {
        node {
          label 'built-in'
        }
      }
      steps {
        sh 'docker push aderounmu/docker-flask:python:3.8-alpine'
      }
    }

  }
  post {
    agent {
      node {
        label 'built-in'
      }
    }
    
    always {
      sh 'docker logout'
    }
  }
  
}