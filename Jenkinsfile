pipeline {
  agent {
    dockerfile {
      filename 'Dockerfile'
    }

  }
  stages {
    stage('Run') {
      steps {
        sh 'docker-compose up'
      }
    }

  }
}