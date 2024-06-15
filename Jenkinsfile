pipeline {
    
    agent any 
    
    environment {
        IMAGE_TAG = "${BUILD_NUMBER}"
    }
    
    stages {
        
        stage('Checkout'){
           steps {
                git branch: 'main', 
                credentialsId: 'demo-app', 
                url: 'https://github.com/vpha1986/flask-demo-be.git'
           }
        }

        stage('Build Docker'){
            steps{
                script{
                    sh '''
                    echo 'Buid Docker Image'
                    docker build -t vphatarp/app-kubeprac-backend:${BUILD_NUMBER} .
                    '''
                }
            }
        }

        stage('Push the artifacts'){
           steps{
                withCredentials([usernamePassword(credentialsId: 'dockerHub-login', passwordVariable: 'dockerHubPassword', usernameVariable: 'dockerHubUser')]) {
                    sh "docker login -u ${env.dockerHubUser} -p ${env.dockerHubPassword}"
                    sh 'docker push vphatarp/app-kubeprac-backend:${BUILD_NUMBER}'
                }
            }
        }
        
        // stage('Checkout K8S manifest SCM'){
        //     steps {
        //         git credentialsId: 'f87a34a8-0e09-45e7-b9cf-6dc68feac670', 
        //         url: 'https://github.com/iam-veeramalla/cicd-demo-manifests-repo.git',
        //         branch: 'main'
        //     }
        // }
        
        // stage('Update K8S manifest & push to Repo'){
        //     steps {
        //         script{
        //             withCredentials([usernamePassword(credentialsId: 'f87a34a8-0e09-45e7-b9cf-6dc68feac670', passwordVariable: 'GIT_PASSWORD', usernameVariable: 'GIT_USERNAME')]) {
        //                 sh '''
        //                 cat deploy.yaml
        //                 sed -i '' "s/32/${BUILD_NUMBER}/g" deploy.yaml
        //                 cat deploy.yaml
        //                 git add deploy.yaml
        //                 git commit -m 'Updated the deploy yaml | Jenkins Pipeline'
        //                 git remote -v
        //                 git push https://github.com/iam-veeramalla/cicd-demo-manifests-repo.git HEAD:main
        //                 '''                        
        //             }
        //         }
        //     }
        // }
    }
}