pipeline {
  agent none
    environment {
      DOCKERHUB_CREDENTIALS = credentials('dockerhub')
    }
  stages {
    stage('Test') {
      agent {
        docker { 
          image 'python:3.8-alpine' 
          // args '-u root'
        }

      }

      steps {
        withEnv(["HOME=${env.WORKSPACE}"]){
        sh 'echo \'Testing\''
        sh 'python3 --version'
        sh 'pip install --user -r requirements.txt'
        sh 'python3 -m pytest --version'
        sh 'python -m pytest'
        sh 'ls -l'
      }
        // sh 'find . -name \'__pycache__\' | grep -v \'__pycache__/$\' | xargs rm -rf'
      }
      
    }

    stage('Build') {
      agent {
        docker {
            image 'docker:latest'
            args '-v /var/run/docker.sock:/var/run/docker.sock'
        }

      }
      steps {
        sh 'docker --version'
        sh 'docker build -t aderounmu/docker-flask:python:3.8-alpine .'
      }
    }

    stage('Login') {
      agent {
        docker {
            image 'docker:latest'
            args '-v /var/run/docker.sock:/var/run/docker.sock'
        }

      }
      steps {
        sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
      }
    }

    stage('Push') {
      agent {
        docker {
            image 'docker:latest'
            args '-v /var/run/docker.sock:/var/run/docker.sock'
        }

      }
      steps {
        sh 'docker push aderounmu/docker-flask:python:3.8-alpine'
      }
    }

  }
  post {
    always {
      node('built-in') {
        sh 'docker logout'
      }
    }

  }
}