pipeline {
  agent { docker { image 'python:3.6-stretch' } }
  stages {
    stage('build') {
      steps {
        sh 'pip install -r requirements.txt'
      }
    }
  }
}
