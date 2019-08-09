pipeline {
  agent any
  stages {
    stage('Artifacts') {
      steps {
        sh '''mkdir -p ./artifacts
touch ./artifacts/testFile01.log

ls -hal'''
        archiveArtifacts(artifacts: 'artifacts', allowEmptyArchive: true, fingerprint: true, onlyIfSuccessful: true)
        sh 'ls -hal'
      }
    }
    stage('Second step') {
      steps {
        sh 'ls -hal'
      }
    }
  }
}