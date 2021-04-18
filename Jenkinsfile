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
            // deleteDir()
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
                  '''
               } else {
                  bat('''
                        type "building ${env.JOB_NAME}..."
                        mkdir 'resource'
                        mkdir 'resource/InMoov'
                        type '1.1.${env.BUILD_NUMBER}' > 'resource/InMoov/version.txt'
                  ''')
               } // isUnix
            } // script
         } // steps
      } // stage

      stage('zip') {
         steps {
            script {
               if (isUnix()) {
                  sh "zip -r ${artifactId}-${version}.zip resource"
               } else {
                  bat("tar.exe -r ${artifactId}-${version}.zip resource")
               }
            // archiveArtifacts artifacts: 'test.zip', fingerprint: true
            }
         }
      }

      /**
      * deployment locally by installing into maven like repo with nginx serving the repo directory
      */
      stage('install') {
         steps {
            script {
               // deployment variables
               def path = groupId.replace('.', '/') + '/' + artifactId.replace('.', '/')
               def repo = '/repo/artifactory/myrobotlab/' + path + '/'

               // if (isUnix()) {
                  // sh "mkdir -p ${repo}${version}"
                  // sh "cp ${artifactId}-${version}.zip ${repo}${version}"
               // } else {
                  // bat("tar.exe -r ${artifactId}-${version}.zip resource")
               // }

               // ${artifactId}-{version}.pom
               def depFileName = repo + version + '/' + artifactId + '-' + version + '.pom'

               def pom = '<project>\n'
               pom += '<modelVersion>4.0.0</modelVersion>\n'
               pom += '<modelVersion>4.0.0</modelVersion>\n'
               pom += '<groupId>' + groupId + '</groupId>\n'
               pom += '<artifactId>' + artifactId + '</artifactId>\n'
               pom += '<version>' + version + '</version>\n'
               pom += '<description>InMoov2 main service module for InMoov compatible with Nixie release of myrobotlab</description>\n'
               pom += '<url>http://myrobotlab.org</url>\n'
               pom += '</project>\n'

               echo 'writing pom ' + depFileName
               writeFile file: depFileName, text: pom
            }
         }
      // sh "cp ${artifactId}-${version}.zip ${repo}latest.release/${artifactId}-latest.release.zip"
      }
   } // stages
} // pipeline
