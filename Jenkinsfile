pipeline {
  agent none
  stages {
    stage('Test') {
      agent {
        docker { 
          image 'python:3.8-alpine' 
          args '-u root:root -v $HOME/workspace/myproject:/myproject'
        }

      }
      steps {
        sh 'echo \'Testing\''
        sh 'python3 --version'
        sh 'pip install --user -r requirements.txt'
        sh 'python3 -m pytest --version'
        sh 'python -m pytest'
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
  environment {
    DOCKERHUB_CREDENTIALS = credentials('dockerhub')
  }
  post {
    always {
      node('built-in') {
        sh 'docker logout'
      }

    }

  }
}