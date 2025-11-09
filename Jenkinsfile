pipeline {
    agent any

    environment {
        IMAGE_NAME = "flask-ci-cd"
        REGISTRY   = "localhost:5000"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install & Test') {
            steps {
                sh '''
                    python -m venv venv
                    . venv/bin/activate
                    pip install -r flask-ci-cd/requirements.txt
                    export PYTHONPATH=$WORKSPACE/flask-ci-cd
                    pytest -q flask-ci-cd/tests
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${env.IMAGE_NAME}:$BUILD_NUMBER")
                }
            }
        }

        stage('Run Container') {
            steps {
                script {
                    def container = docker.image("${env.IMAGE_NAME}:$BUILD_NUMBER")
                    container.run("-d -p 5000:5000 --name flask_app_$BUILD_NUMBER")
                }
            }
        }
    }

    post {
        success {
            echo '✅ Build succeeded'
            emailext (
                subject: "✅ ${env.JOB_NAME} #${env.BUILD_NUMBER} SUCCESS",
                body: """\
                Build succeeded.
                Docker image: ${env.IMAGE_NAME}:${env.BUILD_NUMBER}
                Container running on host port 5000.
                Build Status: ${currentBuild.currentResult}
                Project: ${env.JOB_NAME}
                Build Number: ${env.BUILD_NUMBER}
                Build URL: ${env.BUILD_URL}""",
                to: "${env.email_addr}"
            )
        }
        failure {
            echo '❌ Build failed'
            emailext (
                subject: "❌ ${env.JOB_NAME} #${env.BUILD_NUMBER} FAILURE",
                body: """\
                Build Failed.
                Kindly check Jenkins console for more details.
                Build Status: ${currentBuild.currentResult}
                Project: ${env.JOB_NAME}
                Build Number: ${env.BUILD_NUMBER}
                Build URL: ${env.BUILD_URL}""",
                to: "${env.email_addr}"
            )
        }
        always {
            script {
                echo "Completed..."
            }
            cleanWs()
        }
    }
}
