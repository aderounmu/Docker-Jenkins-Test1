pipeline {
  agent none
  stages {
    stage('Test') {
      agent {
        docker {
          image 'python:3.8-alpine'
          args '-u root:sudo -v $HOME/workspace/myproject:/myproject'
        }

      }
      steps {
        sh 'python3 --version'
        sh 'whoami'
        sh 'pip install --user -r requirements.txt'
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