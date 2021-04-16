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

pipeline {

    // https://plugins.jenkins.io/agent-server-parameter/
    // agent { label params['agent-name'] } 
    agent any

    // properties([buildDiscarder(logRotator(artifactDaysToKeepStr: '', artifactNumToKeepStr: '', daysToKeepStr: '', numToKeepStr: '3')), [$class: 'GithubProjectProperty', displayName: '', projectUrlStr: 'https://github.com/MyRobotLab/InMoov2/'], pipelineTriggers([pollSCM('* * * * *')])])

    // echo params.agentName    
    tools { 
        maven 'M3' // defined in global tools - maven is one of the only installers that works well for global tool
        // jdk 'openjdk-11-linux' // defined in global tools
        // git 
    }

stages {	
   def version = "2.0.${env.BUILD_NUMBER}" 
   def groupId = "fr.inmoov"
   def artifactId = "inmoov"

   // deployment variables
   def path = groupId.replace(".","/") + "/" + artifactId.replace(".","/")
   def repo = "/repo/artifactory/myrobotlab/" + path + "/" 

   stage('clean') { 
      echo 'clean the workspace'
      // deleteDir()
      cleanWs()
   }

   stage('check out') { 
      // checkout scm - apparently below "polls" what is the rate?
      // SHOULD BE -> git 'https://github.com/MyRobotLab/InMoov.git'
      git 'https://github.com/MyRobotLab/inmoov.git'
   }

   stage('build') { 
      sh 'echo \"' + version + '\" > resource/InMoov/version.txt'
   }

   stage('zip') {
   
        sh "zip -r ${artifactId}-${version}.zip resource"
        // archiveArtifacts artifacts: 'test.zip', fingerprint: true    
	}

   /**
    * deployment locally by installing into maven like repo with nginx serving the repo directory
    */
   stage('install') {
      sh "mkdir -p ${repo}${version}"

      sh "cp ${artifactId}-${version}.zip ${repo}${version}"

      // ${artifactId}-{version}.pom
      def depFileName = repo + version + "/" + artifactId + "-" + version + ".pom"
      echo "writing pom " + depFileName
      File file = new File(depFileName)
      file.write("<project>")
      file.append("<modelVersion>4.0.0</modelVersion>")
      file.append("<groupId>"+groupId+"</groupId>")
      file.append("<artifactId>"+artifactId+"</artifactId>")
      file.append("<version>"+version+"</version>")
      file.append("<description>InMoov2 main service module for InMoov compatible with Nixie release of myrobotlab</description>")
      file.append("<url>http://myrobotlab.org</url>")
      file.append("</project>")

      // sh "cp ${artifactId}-${version}.zip ${repo}latest.release/${artifactId}-latest.release.zip"
     }
  }
}
