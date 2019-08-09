pipeline {
  agent any
  stages {
    stage('Artifacts') {
      agent any
      steps {
        sh '''mkdir -p ./artifacts

touch ./artifacts/testFile01.log
touch ./artifacts/testFile02.log

ls -hal
ls -hal ./artifacts'''
        archiveArtifacts(artifacts: './artifacts', allowEmptyArchive: true, fingerprint: true, onlyIfSuccessful: true)
      }
    }
    stage('Second step') {
      steps {
        sh 'ls -hal'
      }
    }
  }
}