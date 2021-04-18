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

pipeline {
   // https://plugins.jenkins.io/agent-server-parameter/
   // agent { label params['agent-name'] }
   agent any

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
            cleanWs()
         }
      }

      stage('check out') {
         steps {
            checkout scm
         }
      }

      stage('build') {
         steps {
            script {
               if (isUnix()) {
                  sh '''
                        echo "building ${JOB_NAME}..."
                        mkdir resource
                        mkdir resource/InMoov
                        echo "1.1.${BUILD_NUMBER}" > resource/InMoov/version.txt
                        mvn package
                  '''
               } else {
                  bat('''
                        type "building ${JOB_NAME}..."
                        mkdir 'resource'
                        mkdir 'resource/InMoov'
                        type '1.1.${BUILD_NUMBER}' > 'resource/InMoov/version.txt'
                        mvn package
                  ''')
               } // isUnix
            } // script
         } // steps
      } // stage

     stage('archive') {
         steps {
            archiveArtifacts 'target/inmoov-${VERSION}.zip'
         }
      }


      /**
      * deployment locally by installing into maven like repo with nginx serving the repo directory
      */
      /*
      stage('install') {
         steps {
            script {
                if (isUnix()) {
                  sh '''
                        mvn install:install-file  -Dfile=target/inmoov-${VERSION}.zip \
                                            -DgroupId=${GROUP_ID} \
                                            -DartifactId=${ARTIFACT_ID} \
                                            -Dversion=${VERSION} \
                                            -Dpackaging=zip \
                                            -DlocalRepositoryPath=/repo/artifactory/myrobotlab/

                  '''
               } else {
                  bat('''
                ''')       
               }         
            }
         }
      */
      // sh "cp ${artifactId}-${version}.zip ${repo}latest.release/${artifactId}-latest.release.zip"
      }
   } // stages
} // pipeline
