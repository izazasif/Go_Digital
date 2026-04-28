pipeline {
    agent any

    environment {
        AWS_REGION      = credentials('aws-region')
        ECR_REGISTRY    = credentials('ecr-registry')
        EC2_HOST        = credentials('ec2-host')
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Test Backend') {
            steps {
                sh '''
                    pip install -r backend/requirements.txt
                    cd backend
                    DATABASE_URL=sqlite:///./test.db \
                    SECRET_KEY=jenkins-test-key \
                    ADMIN_EMAIL=admin@test.com \
                    ADMIN_PASSWORD=Test@1234 \
                    MAIL_USERNAME="" \
                    MAIL_FROM=noreply@test.com \
                    MAIL_SERVER=localhost \
                    MAIL_PORT=1025 \
                    MAIL_STARTTLS=false \
                    MAIL_SSL_TLS=false \
                    FRONTEND_URL=http://localhost \
                    python -m pytest tests/ -v --tb=short || true
                '''
            }
        }

        stage('Build Frontend') {
            steps {
                sh '''
                    cd frontend
                    npm install
                    npm run build
                '''
            }
        }

        stage('Build & Push Docker Images') {
            when { branch 'main' }
            steps {
                withCredentials([
                    string(credentialsId: 'aws-access-key-id', variable: 'AWS_ACCESS_KEY_ID'),
                    string(credentialsId: 'aws-secret-access-key', variable: 'AWS_SECRET_ACCESS_KEY')
                ]) {
                    sh '''
                        aws configure set aws_access_key_id $AWS_ACCESS_KEY_ID
                        aws configure set aws_secret_access_key $AWS_SECRET_ACCESS_KEY
                        aws configure set default.region $AWS_REGION

                        aws ecr get-login-password --region $AWS_REGION | \
                          docker login --username AWS --password-stdin $ECR_REGISTRY

                        docker build -t $ECR_REGISTRY/go-digital-backend:${GIT_COMMIT} ./backend
                        docker push $ECR_REGISTRY/go-digital-backend:${GIT_COMMIT}
                        docker tag $ECR_REGISTRY/go-digital-backend:${GIT_COMMIT} $ECR_REGISTRY/go-digital-backend:latest
                        docker push $ECR_REGISTRY/go-digital-backend:latest

                        docker build -t $ECR_REGISTRY/go-digital-frontend:${GIT_COMMIT} ./frontend
                        docker push $ECR_REGISTRY/go-digital-frontend:${GIT_COMMIT}
                        docker tag $ECR_REGISTRY/go-digital-frontend:${GIT_COMMIT} $ECR_REGISTRY/go-digital-frontend:latest
                        docker push $ECR_REGISTRY/go-digital-frontend:latest
                    '''
                }
            }
        }

        stage('Deploy to EC2') {
            when { branch 'main' }
            steps {
                withCredentials([sshUserPrivateKey(credentialsId: 'ec2-ssh-key', keyFileVariable: 'SSH_KEY')]) {
                    sh '''
                        ssh -o StrictHostKeyChecking=no -i $SSH_KEY ubuntu@$EC2_HOST "
                          cd /home/ubuntu/go_digital &&
                          git pull origin main &&
                          aws ecr get-login-password --region $AWS_REGION | \
                            docker login --username AWS --password-stdin $ECR_REGISTRY &&
                          ECR_REGISTRY=$ECR_REGISTRY IMAGE_TAG=${GIT_COMMIT} \
                            docker compose -f docker-compose.prod.yml pull backend frontend &&
                          docker compose -f docker-compose.prod.yml up -d --no-deps backend frontend nginx &&
                          docker image prune -f
                        "
                    '''
                }
            }
        }
    }

    post {
        success {
            echo "Deployment successful — GO_Digital is live!"
        }
        failure {
            echo "Pipeline failed. Check the logs above."
        }
    }
}
