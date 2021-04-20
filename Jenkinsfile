/**********************************************************************************
 * JenkinsFile for InMoov2
 *
 * for adjusting build number for specific branch build
 * Jenkins.instance.getItemByFullName("InMoov2-multibranch/develop").updateNextBuildNumber(185)
 *
 * CHANGE build.properties TO BUILD AND DEPLOY A NEW BUILD
 *
 ***********************************************************************************/
// [$class: 'GithubProjectProperty', displayName: '', projectUrlStr: 'https://github.com/MyRobotLab/InMoov2/']

def version = "2.0.${env.BUILD_NUMBER}"
def groupId = 'fr.inmoov'
def artifactId = 'inmoov'
/*
def remote = [:]
   remote.name = 'test'
   remote.host = 'test.domain.com'
   remote.user = 'root'
   remote.password = 'password'
   remote.allowAnyHosts = true
*/
pipeline {
   // https://plugins.jenkins.io/agent-server-parameter/
   // agent { label params['agent-name'] }
   agent any
/*
    stage('Remote SSH') {
      sshCommand remote: remote, command: "ls -lrt"
      sshCommand remote: remote, command: "for i in {1..5}; do echo -n \"Loop \$i \"; date ; sleep 1; done"
    }
*/  

    environment {
        VERSION = "${version}"
        GROUP_ID = "${groupId}"
        ARTIFACT_ID = "${artifactId}"
    }

   options {
      // This is required if you want to clean before build
      skipDefaultCheckout(true)
   }

    // properties([buildDiscarder(logRotator(artifactDaysToKeepStr: '', artifactNumToKeepStr: '', daysToKeepStr: '', numToKeepStr: '3')), [$class: 'GithubProjectProperty', displayName: '', projectUrlStr: 'https://github.com/MyRobotLab/InMoov2/'], pipelineTriggers([pollSCM('* * * * *')])])

   // echo params.agentName
   tools {
      maven 'M3' // defined in global tools - maven is one of the only installers that works well for global tool
   // jdk 'openjdk-11-linux' // defined in global tools
   // git
   }



   stages {
      stage('clean') {
         steps {
            echo 'clean the workspace'
            // cleanWs()

            script {
               if (isUnix()) {
                  sh '''
                     mvn clean
                  '''
               } else {
                  bat('''
                     mvn clean
                  ''')
               }
            }
         }
      } 

      stage('check out') {
         steps {
            checkout scm
         }
      }

      // FIXME - InMoov/version file needs to be created
      stage('build') {
         steps {
            script {
               if (isUnix()) {
                  sh '''
                        echo "building ${JOB_NAME}..."
                        # echo "${VERSION}" > resource/InMoov/version.txt
                        mvn package
                  '''
               } else {
                  bat('''
                        type "building ${JOB_NAME}..."
                        # type '${VERSION}' > 'resource/InMoov/version.txt'
                        mvn package
                  ''')
               } // isUnix
            } // script
         } // steps
      } // stage
/*
     stage('archive') {
         steps {
            archiveArtifacts 'target/inmoov-'+ version +'.zip'
         }
      }
*/      
      /**
      * deployment locally by installing into maven like repo with nginx serving the repo directory
      */
      
      stage('make install') {
         steps {
            script {
                if (isUnix()) {
                  sh '''
                        mvn install:install-file  -Dfile=target/inmoov-${VERSION}.zip \
                                            -DgroupId=${GROUP_ID} \
                                            -DartifactId=${ARTIFACT_ID} \
                                            -Dversion=${VERSION} \
                                            -Dpackaging=zip \
                                            -DlocalRepositoryPath=target/repo/artifactory/myrobotlab/
                  '''
               } else {
                  bat('''
                ''')       
               }         

               
               withCredentials([sshUserPrivateKey(credentialsId: 'myrobotlab2.pem', keyFileVariable: 'identity', passphraseVariable: '', usernameVariable: 'ubuntu')]) {
        
               // def remote = [name: 'repo', identity = identity, host: 'repo.myrobotlab.org', user: 'ubuntu', password: "password123", allowAnyHosts: true]
               def remote = [:]
               remote.name = "node-1"
               remote.host = "10.000.000.153"
               remote.user = userName
               remote.identityFile = identity
               remote.allowAnyHosts = true
               sshCommand remote: remote, command: "for i in {1..5}; do echo -n \"Loop \$i \"; date ; sleep 1; done"

            }
         }
      
      // sh "cp ${artifactId}-${version}.zip ${repo}latest.release/${artifactId}-latest.release.zip"
      } // make install stage
   } // stages

   post {
    success {
         echo "success running post process on ${env.NODE_NAME}"
    }
  }
} // pipeline
