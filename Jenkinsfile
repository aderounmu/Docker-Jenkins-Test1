pipeline {
  agent {
    docker {
      // image 'docker:latest'
      image 'python:3.8-alpine'
      // args '-v /var/run/docker.sock:/var/run/docker.sock'
    }

  }
  stages {
    stage('Build') {
      steps {
        // sh 'docker image build -t mytest/flask_docker_test .'
        sh 'python3 --version'
      }
    }

    stage('login') {
      steps {
        // sh 'docker login -u $dockerhub_USR -p $dockerhub_PSW'
        sh  'echo hello'
      }
    }

    // stage('Push') {
    //   steps {
    //     // sh 'docker push mytest/flask_docker_test:latest'
    //   }
    // }

  }
  environment {
    dockerhub = credentials('dockerhub')
  }
}
