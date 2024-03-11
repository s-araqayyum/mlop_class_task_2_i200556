
pipeline {
    agent any

    stages {
        stage ('Checkout') {
            steps {
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/s-araqayyum/mlop_class_task_2_i200556.git']])
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    sh 'python -m pip install -r requirements.txt'
                }
            }
        }

        stage('Execute Test') {
            steps {
                script {
                    sh 'python test.py'
                }
            }
        }

        stage('Deploying') {
            steps {
                script {
                    if (env.BRANCH_NAME == 'main') {
                        echo 'Deploying to production'
                    } else {
                        echo 'Deploying to UAT'
                    }
                }
            }
        }
    }
}
