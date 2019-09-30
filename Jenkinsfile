/**********************************************************************************
 * JenkinsFile for inmoov
 *
 * for adjusting build number for specific branch build
 * Jenkins.instance.getItemByFullName("inmoov-multibranch/develop").updateNextBuildNumber(185)
 *
 ***********************************************************************************/
properties([buildDiscarder(logRotator(artifactDaysToKeepStr: '', artifactNumToKeepStr: '', daysToKeepStr: '', numToKeepStr: '3')), [$class: 'GithubProjectProperty', displayName: '', projectUrlStr: 'https://github.com/MyRobotLab/inmoov/'], pipelineTriggers([[$class: 'PeriodicFolderTrigger', interval: '2m']])])

node ('ubuntu') { // use any node

// node ('ubuntu') {  // use labels to direct build
   // withEnv(javaEnv) {
   
   parameters {
        choice(
            choices: ['true' , 'false'],
            description: 'this is the description',
            name: 'EXTENDED_VERIFY')
    }
   
   // def mvnHome
   stage('preparation') { // for display purposes
      // Get some code from a GitHub repository
      checkout scm
      // git 'https://github.com/MyRobotLab/inmoov.git'
      // git url: 'https://github.com/MyRobotLab/inmoov.git', branch: 'develop'
      
      sh 'git rev-parse --abbrev-ref HEAD > GIT_BRANCH'
      git_branch = readFile('GIT_BRANCH').trim()
      echo git_branch
    
      sh 'git rev-parse HEAD > GIT_COMMIT'
      git_commit = readFile('GIT_COMMIT').trim()
      echo git_commit
    
      echo git_commit
      echo "git_commit=$git_commit"
      // Run the maven build
      if (isUnix()) {
      // -o == offline      
         // sh "'${mvnHome}/bin/mvn' -Dbuild.number=${env.BUILD_NUMBER} -Dgit_commit=$git_commit -Dgit_branch=$git_branch -Dmaven.test.failure.ignore -q clean compile "
         sh "'ant'"
      } else {
        //  bat(/"${mvnHome}\bin\mvn" -Dbuild.number=${env.BUILD_NUMBER} -Dgit_commit=$git_commit -Dgit_branch=$git_branch -Dmaven.test.failure.ignore -q clean compile  /)
      }
   }
   stage('verify'){
	   if (isUnix()) {
             // -o == offline
	     sh "'${mvnHome}/bin/mvn' verify"
	   } else {
	     bat(/"${mvnHome}\bin\mvn" verify/)
	   }
   }
   stage('extended-verify'){
     if (params.EXTENDED_VERIFY == 'true') {
       echo 'EXTENDED_VERIFY is true'
     } 	   
   }
   stage('archive') {
         archiveArtifacts 'target/*.jar'      
   } 
   stage('publish') {
   
//    	def server = Artifactory.server 'artifactory01' 
//    	def uploadSpec = """{
// 								"files": [
//										    {
//										      "pattern": "target/inmoov.zip",
//										      "target": "org/inmoov/"
//										    }
//										 ]
//										}"""
//		server.upload(uploadSpec)

	}
}
