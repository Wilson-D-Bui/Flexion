pipeline {
  agent any
  stages {
    stage('SCM Checkout') {
      steps {
        git(url: 'https://github.com/Wilson-D-Bui/Flexion.git', branch: 'master', changelog: true, poll: true, credentialsId: 'Wilson-D-Bui')
      }
    }
    stage('Build') {
      steps {
        sh '#python -m py_compile #FILE1 #FILE2 #FILE3'
      }
    }
    stage('Deploy') {
      steps {
        sh '#mv -v ./* ~/../flexion'
      }
    }
  }
}