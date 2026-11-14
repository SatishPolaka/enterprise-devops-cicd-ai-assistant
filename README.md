<<<<<<< HEAD
# 🚀 End-to-End DevOps CI/CD Pipeline with AI-Powered DevOps Assistant

## 📌 Project Overview

In this project, I have implemented an end-to-end DevOps CI/CD pipeline for the VProfile Java application using major DevOps and AWS technologies.

The main objective of this project is to understand how application code moves from a developer's machine to a Kubernetes cluster through an automated CI/CD pipeline.

I have integrated multiple tools for source code management, build automation, code quality analysis, artifact management, containerization, security scanning, GitOps-based deployment and monitoring.

Along with the DevOps implementation, I have also integrated **Amazon Bedrock with Nova Lite** to build an AI-powered DevOps Assistant. It allows users to enter DevOps-related issues through a web interface and receive AI-generated troubleshooting explanations and recommendations.

This project helped me understand how different DevOps tools work together in a real-world deployment workflow and how Generative AI can support DevOps troubleshooting.

---

# 🏗️ 1. Complete Project Architecture

```text
                       DEVELOPER
                           |
                           v
                    GITHUB REPOSITORY
                           |
                           v
                       JENKINS CI
                           |
                  +--------+--------+
                  |                 |
                  v                 v
               GIT CLONE       SOURCE CODE
                                    |
                                    v
                               MAVEN BUILD
                                    |
                                    v
                                SONARQUBE
                                    |
                                    v
                               QUALITY GATE
                                    |
                                PASS / FAIL
                                    |
                                    v
                            NEXUS REPOSITORY
                                    |
                                    v
                              DOCKER BUILD
                                    |
                                    v
                             TRIVY SCANNING
                                    |
                                    v
                           CONTAINER REGISTRY
                                    |
                                    v
                         UPDATE IMAGE IN GITOPS
                                    |
                                    v
                                 ARGO CD
                                    |
                                    v
                           KOPS KUBERNETES
                                CLUSTER
                                    |
                                    v
                           APPLICATION DEPLOYMENT
                                    |
                                    v
                           PROMETHEUS MONITORING
                                    |
                                    v
                              GRAFANA DASHBOARD
```

---

# 🔄 2. CI/CD Pipeline Workflow

### Step 1: Source Code Management – Git & GitHub

- Maintained application source code in GitHub.
- Used Git for version control.
- Jenkins retrieves the source code from the GitHub repository.
- Changes pushed to GitHub trigger the CI/CD workflow through the configured Jenkins integration.

### Step 2: Continuous Integration – Jenkins

Jenkins is used to automate the CI/CD pipeline.

The pipeline performs the following activities:

- Clone source code.
- Build the application using Maven.
- Perform SonarQube code analysis.
- Validate the Quality Gate.
- Upload build artifacts to Nexus.
- Build Docker images.
- Scan Docker images using Trivy.
- Push container images to the registry.
- Update the image reference in the GitOps repository.

### Step 3: Build Automation – Maven

Used Maven to build the Java-based VProfile application.

```bash
mvn clean install
```

The build generates the WAR artifact required for containerization.

### Step 4: Code Quality – SonarQube

Integrated SonarQube into the Jenkins pipeline.

Used it to analyse source code and identify code quality issues.

The pipeline includes a Quality Gate validation before proceeding with subsequent stages.

### Step 5: Artifact Management – Nexus Repository

Used Nexus Repository 3 to store the Maven build artifacts.

The generated WAR file is uploaded to the configured Nexus hosted repository.

This separates application build artifacts from container images.

### Step 6: Containerization – Docker

Used Docker to package the application and its required runtime environment.

Created Docker images using the application artifact and Dockerfile.

### Step 7: Image Security – Trivy

Integrated Trivy into the pipeline for Docker image vulnerability scanning.

It helps identify vulnerabilities in container images before they are pushed to the container registry.

### Step 8: Container Registry – Docker Hub / Amazon ECR

Used container registries to store Docker images.

- Docker Hub for container image management.
- Amazon ECR for AWS-based container image storage.

### Step 9: GitOps – Argo CD

Used Argo CD to implement GitOps-based Kubernetes deployment.

The Jenkins pipeline updates the container image reference in the GitOps repository.

Argo CD monitors the repository and synchronises the desired configuration with the Kubernetes cluster.

### Step 10: Kubernetes – kOps

Provisioned and managed the Kubernetes cluster using kOps.

Used Kubernetes manifests to deploy and manage the application.

Worked with:

- Deployments
- Services
- Pods
- Configurations
- Network Policies
- Horizontal Pod Autoscaling

### Step 11: Monitoring – Prometheus and Grafana

Integrated Prometheus and Grafana for Kubernetes monitoring.

**Prometheus:**
- Collects monitoring metrics.
- Monitors cluster and workload resources.
- Provides metrics for monitoring and alerting.

**Grafana:**
- Visualises monitoring data.
- Displays Kubernetes cluster information.
- Helps monitor CPU, memory, pods, nodes and workloads.

---

# 🤖 3. AI-Powered DevOps Assistant – Amazon Bedrock

Along with the CI/CD implementation, I started working on an AI-powered DevOps Assistant using Amazon Bedrock.

The objective is to use Generative AI to help DevOps engineers understand technical issues and receive troubleshooting recommendations.

## AI Assistant Architecture

```text
                  DEVOPS ENGINEER
                         |
                         v
                     WEB BROWSER
                         |
                         v
                  FLASK APPLICATION
                       (EC2)
                         |
                         v
                    PYTHON BACKEND
                         |
                         v
                       BOTO3
                         |
                         v
                   AWS BEDROCK
                         |
                         v
                    NOVA LITE
                         |
                         v
                    AI ANALYSIS
                         |
              +----------+----------+
              |                     |
              v                     v
          ROOT CAUSE          RECOMMENDATIONS
              |                     |
              +----------+----------+
                         |
                         v
                  BROWSER RESPONSE
```

## Technologies Used for AI Integration

| Technology | Purpose |
|---|---|
| Amazon EC2 | Hosts the Python application |
| AWS IAM Role | Provides AWS authentication |
| Amazon Bedrock | Generative AI service |
| Amazon Nova Lite | Foundation model |
| Python | Backend application |
| Flask | Web application |
| Boto3 | AWS SDK integration |

## AI Assistant Implementation

### Step 1: Amazon Bedrock Configuration

Enabled and tested Amazon Nova Lite through the Amazon Bedrock Playground.

Configured the following model:

```text
Model Provider : Amazon
Model Name     : Nova Lite
Model ID       : amazon.nova-lite-v1:0
Region         : us-east-1
```

### Step 2: IAM Role Authentication

Configured an IAM Role for the EC2 instance with the required Bedrock permissions.

The Python application uses the EC2 instance role instead of hardcoded AWS access keys.

### Step 3: Python and Boto3 Integration

Installed Boto3 and created a Python script to communicate with Amazon Bedrock.

Tested the `converse()` API operation and successfully received responses from Nova Lite.

### Step 4: Flask Web Application

Created a Flask application to provide a browser-based interface.

The application accepts DevOps-related questions, sends them to Amazon Bedrock and displays the generated responses.

### Step 5: Browser Access

Started the Flask application on EC2 using port 5000.

```bash
python app.py
```

Accessed the application through:

```text
http://<EC2-PUBLIC-IP>:5000
```

Successfully tested the dashboard by submitting Kubernetes troubleshooting questions.

## AI Assistant Testing

Tested the assistant with different DevOps-related questions, including:

**Kubernetes:**
- CrashLoopBackOff troubleshooting.
- Possible pod failure reasons.
- Kubernetes troubleshooting commands.
- Production recommendations.

**Jenkins:**
- Maven build failures.
- Possible Java compatibility issues.
- Pipeline troubleshooting recommendations.

**AWS:**
- EC2 instance status check failures.
- Possible infrastructure issues.
- AWS troubleshooting commands.

The assistant generates recommendations based on the information provided by the user.

**Current limitation:** The AI Assistant currently analyses manually submitted text. Automatic collection of Kubernetes logs, Jenkins logs, Prometheus alerts and Argo CD status has not yet been implemented.

---

# 🛠️ 4. Complete Technology Stack

| Category | Technologies |
|---|---|
| Cloud Platform | AWS |
| Cloud Services | EC2, IAM, S3, ECR |
| Infrastructure as Code | Terraform |
| Configuration Management | Ansible |
| Operating System | Linux / Amazon Linux |
| Programming Languages | Python, Shell Scripting |
| Version Control | Git, GitHub |
| CI/CD | Jenkins |
| Build Automation | Maven |
| Code Quality | SonarQube |
| Quality Validation | SonarQube Quality Gate |
| Artifact Repository | Nexus Repository 3 |
| Containerization | Docker, Docker Compose |
| Image Security | Trivy |
| Container Registry | Docker Hub, Amazon ECR |
| Container Orchestration | Kubernetes |
| Cluster Provisioning | kOps |
| GitOps | Argo CD |
| Monitoring | Prometheus |
| Visualization | Grafana |
| AI / Generative AI | Amazon Bedrock |
| Foundation Model | Amazon Nova Lite |
| Web Framework | Flask |
| AWS SDK | Boto3 |

---

# 📂 5. Project Components

The project consists of two major implementations:

### Component 1: End-to-End DevOps CI/CD Pipeline

Covers the complete application delivery workflow:

- Source code management.
- Automated application builds.
- Code quality analysis.
- Artifact management.
- Docker image creation.
- Container security scanning.
- Container image publishing.
- GitOps deployment.
- Kubernetes orchestration.
- Application monitoring.

### Component 2: AI-Powered DevOps Assistant

Covers the Generative AI integration:

- AWS EC2 hosting.
- IAM Role authentication.
- Amazon Bedrock configuration.
- Amazon Nova Lite integration.
- Python and Boto3.
- Flask web application.
- Browser-based AI troubleshooting.

---

# 🔐 6. Security Considerations

Implemented and considered the following security practices:

- IAM Role-based AWS authentication.
- Avoiding hardcoded AWS credentials.
- Docker image vulnerability scanning using Trivy.
- SonarQube code quality analysis.
- Kubernetes Network Policies.
- Container image management through registries.
- Controlled GitOps deployment using Argo CD.

For production deployment, additional security controls such as HTTPS, application authentication, restricted network access, least-privilege IAM policies and secure secret management should be implemented.

---

# 📊 7. Implementation Status

| Component | Status |
|---|---|
| AWS infrastructure and EC2 | Implemented |
| Terraform and Ansible practice | Implemented |
| Git and GitHub integration | Implemented |
| Jenkins CI/CD pipeline | Implemented |
| Maven build | Implemented |
| SonarQube analysis | Implemented |
| Nexus artifact management | Implemented |
| Docker containerization | Implemented |
| Trivy image scanning | Implemented |
| Docker Hub / Amazon ECR | Implemented |
| Kubernetes cluster using kOps | Implemented |
| Argo CD GitOps deployment | Implemented |
| Prometheus monitoring | Implemented |
| Grafana dashboards | Implemented |
| Amazon Bedrock integration | Implemented |
| Nova Lite API integration | Implemented |
| Flask AI dashboard | Implemented |
| Automatic Kubernetes log analysis using AI | Planned |
| Jenkins log analysis using AI | Planned |
| Prometheus alert analysis using AI | Planned |
| Argo CD status analysis using AI | Planned |
| AI-powered automated remediation | Planned |

---

# 🚀 8. Future Enhancements

I am planning to extend the AI DevOps Assistant with additional capabilities.

1. Integrate Kubernetes to collect actual pod logs and events.
2. Connect Jenkins to retrieve and analyse pipeline failure logs.
3. Integrate Prometheus alerts for AI-based incident analysis.
4. Connect Argo CD to analyse application health and synchronisation status.
5. Generate AI-powered incident reports.
6. Introduce engineer approval before executing any remediation action.

The initial approach will remain read-only, where AI analyses issues and recommends solutions rather than directly modifying infrastructure.

---

# 🎯 9. What I Learned From This Project

Through this hands-on implementation, I gained practical experience with:

- Building an end-to-end CI/CD pipeline.
- Integrating multiple DevOps tools.
- Automating Java application builds using Jenkins and Maven.
- Implementing code quality checks.
- Managing artifacts using Nexus.
- Building and scanning Docker images.
- Deploying applications on Kubernetes.
- Implementing GitOps using Argo CD.
- Monitoring Kubernetes using Prometheus and Grafana.
- Provisioning cloud infrastructure using Terraform.
- Working with configuration management using Ansible.
- Integrating Generative AI into a Python application using Amazon Bedrock.
- Building a browser-based AI DevOps Assistant using Flask.

---

# 📝 Conclusion

This project helped me understand how different DevOps tools work together to automate application delivery, deployment and monitoring.

I also explored how Generative AI can be integrated into DevOps workflows using Amazon Bedrock.

The main focus was not just installing individual tools, but understanding their integration and how they contribute to the complete application lifecycle.

I will continue extending this project with more automation, monitoring and AI-based troubleshooting capabilities.

**Technologies:** AWS | Terraform | Ansible | Jenkins | Maven | SonarQube | Nexus | Docker | Trivy | Kubernetes | kOps | Argo CD | Prometheus | Grafana | Python | Flask | Boto3 | Amazon Bedrock | Nova Lite
=======
🚀 Enterprise DevOps CI/CD and GitOps Implementation on AWS
An end-to-end Enterprise DevOps project demonstrating automated Continuous Integration (CI) using Jenkins and Continuous Deployment (CD) using Argo CD (GitOps). The project integrates GitHub, Maven, SonarQube, Quality Gates, Nexus Repository, Docker, and Kubernetes (kOps) to build, validate, package, containerize, and deploy a Java-based web application on AWS.

📌 Project Overview
This project implements an end-to-end DevOps workflow for a Java-based VProfile web application.

The main objective is to automate the complete application delivery lifecycle, starting from source code management to application deployment on a highly available Kubernetes cluster.

The implementation separates CI and CD responsibilities:

Continuous Integration – Jenkins

Clone application source code from GitHub.
Build the application using Maven.
Perform static code analysis using SonarQube.
Validate code quality using SonarQube Quality Gates.
Publish application artifacts to Nexus Repository.
Build and scan Docker images.
Push validated images to a container registry.
Continuous Deployment – Argo CD

Monitor the Kubernetes configuration repository.
Detect changes in Kubernetes manifests.
Synchronize the desired application state.
Deploy application updates to the Kubernetes cluster.
Maintain GitOps-based deployment management.
Infrastructure and Orchestration

Provision AWS infrastructure using Terraform.
Manage Kubernetes cluster infrastructure using kOps.
Deploy application and database workloads using Kubernetes.
Implement high availability, autoscaling, storage, networking, and security configurations.
🏗️ Architecture
End-to-End CI/CD and GitOps Architecture
                  DEVELOPER
                      |
                      v
                GITHUB REPOSITORY
                      |
                      v
                  JENKINS CI
                      |
             +--------+--------+
             |                 |
             v                 v
          GIT CLONE        SOURCE CODE
                               |
                               v
                         MAVEN BUILD
                               |
                               v
                          SONARQUBE
                               |
                               v
                          QUALITY GATE
                               |
                       PASS / FAIL
                               |
                               v
                       NEXUS REPOSITORY
                               |
                               v
                         DOCKER BUILD
                               |
                               v
                         IMAGE SCANNING
                               |
                               v
                       CONTAINER REGISTRY
                               |
                               v
                   UPDATE IMAGE IN GITOPS
                               |
                               v
                         ARGO CD
                               |
                               v
                      KOPS KUBERNETES
                           CLUSTER
                               |
                               v
                       APPLICATION
                         DEPLOYMENT
Note: This represents the target end-to-end workflow. Each integration should be configured and tested before being marked as completed.

🛠️ Technology Stack
Category	Technology
Cloud Platform	AWS
Infrastructure as Code	Terraform
Source Code Management	Git, GitHub
CI Pipeline	Jenkins
CD / GitOps	Argo CD
Build Automation	Maven
Code Quality Analysis	SonarQube
Quality Validation	SonarQube Quality Gates
Artifact Repository	Nexus Repository
Containerization	Docker
Local Testing	Docker Compose
Container Orchestration	Kubernetes
Cluster Management	kOps
Application	Java, Spring, JSP
Application Server	Apache Tomcat 9
Database	MySQL 5.7
Load Balancing	AWS Application Load Balancer
Persistent Storage	AWS EBS
Container Registry	Docker Hub / Container Registry
🔄 CI Pipeline – Jenkins
Jenkins is responsible for automating the Continuous Integration process.

Pipeline Stages
Stage 1 – Source Code Management

Connect Jenkins with GitHub.
Clone the application source code.
Retrieve the latest application changes.
Stage 2 – Maven Build

Execute:

mvn clean install
Maven resolves dependencies, compiles the Java application, executes tests and packages the application as a WAR file.

Stage 3 – SonarQube Analysis

Integrate SonarQube with Jenkins.
Configure SonarQube Scanner.
Perform static code analysis.
Identify code quality issues and vulnerabilities.
Stage 4 – Quality Gate

Evaluate the SonarQube analysis results.
Check whether the application meets the configured quality conditions.
Stop the pipeline if the quality gate fails.
Stage 5 – Nexus Artifact Upload

Package the application.
Publish the generated WAR artifact to Nexus Repository.
Maintain versioned application artifacts.
Stage 6 – Docker Image Creation

Build the application Docker image.
Use a multi-stage Dockerfile.
Package the application with Tomcat.
Run the container using a non-root user.
Stage 7 – Image Scanning

Use Trivy to scan Docker images for known vulnerabilities.

Stage 8 – Container Registry

Push validated Docker images to the configured container registry.

🐳 Docker Implementation
The application is containerized using a multi-stage Dockerfile.

Multi-Stage Build Architecture
          SOURCE CODE
               |
               v
        MAVEN BUILD STAGE
               |
               v
          APPLICATION WAR
               |
               v
       TOMCAT RUNTIME STAGE
               |
               v
         DOCKER IMAGE
               |
               v
        CONTAINER REGISTRY
Docker Implementation Details
Maven-based application build.
Multi-stage Docker build.
Apache Tomcat 9 runtime.
Java 11 runtime environment.
Non-root container execution.
Container-aware JVM memory configuration.
Reduced final image size by separating build and runtime dependencies.
Build Application Image
docker build -t vprofile-app:1.0.0 .
Build Database Image
docker build -t vprofile-db:1.0.0 Docker-db/
Local Application Testing
docker compose up --build
The application can be accessed through:

http://localhost:1234
☸️ Kubernetes Deployment
The application is deployed on an AWS Kubernetes cluster provisioned using kOps.

The deployment includes application and database workloads.

Kubernetes Resources
File	Resource	Purpose
01-namespace.yaml	Namespace	Application isolation
02-resourcequota.yaml	ResourceQuota / LimitRange	Resource management
03-configmap.yaml	ConfigMap	Application configuration
04-secret.yaml	Secret	Database credentials
05-storageclass.yaml	StorageClass	Persistent storage
06-statefulset-db.yaml	StatefulSet	MySQL database
07-service.yaml	Services	Application and database communication
08-deployment.yaml	Deployment	Application deployment
09-hpa.yaml	HPA	Automatic application scaling
10-pdb.yaml	PodDisruptionBudget	Application availability
11-ingress.yaml	Ingress	AWS ALB integration
12-networkpolicy.yaml	NetworkPolicy	Network traffic restrictions
Application Deployment
The application deployment is configured with:

Initial three application replicas.
Rolling update strategy.
Zero unavailable pods during rolling updates.
Startup, readiness and liveness probes.
Pod distribution across availability zones.
CPU and memory requests and limits.
Non-root container execution.
Database Deployment
MySQL is deployed using Kubernetes StatefulSet.

Implementation includes:

Persistent EBS-backed storage.
Encrypted gp3 volumes.
Persistent Volume Claims.
Database credentials through Kubernetes Secrets.
Health checks.
Stable database service discovery.
Important: MySQL uses one StatefulSet replica. Its EBS volume is zonal, so this configuration protects against pod and same-AZ node failures but does not provide automatic database failover during an entire Availability Zone outage.

📈 High Availability and Scalability
The Kubernetes architecture is designed to improve application availability and resilience.

High Availability Architecture
Component	Implementation
Kubernetes Control Plane	3 control-plane instances
Worker Nodes	Nodes distributed across 3 AZs
Application Replicas	Minimum 3
Horizontal Pod Autoscaler	3 to 9 replicas
Pod Disruption Budget	Minimum 2 available pods
Deployment Strategy	Rolling Update
Load Balancing	AWS Application Load Balancer
Persistent Storage	Encrypted AWS EBS gp3
Health Monitoring	Startup, Readiness and Liveness Probes
Horizontal Pod Autoscaling
The application uses Horizontal Pod Autoscaler.

Configuration:

minReplicas: 3
maxReplicas: 9
The HPA targets average CPU utilization of 70%.

Pod Disruption Budget
The application maintains a minimum of two available pods during voluntary disruptions.

minAvailable: 2
Network Policies
Network policies restrict unnecessary incoming traffic.

Implemented policies:

Default deny ingress.
Allow application HTTP traffic.
Allow MySQL connections only from application pods.
🚀 Continuous Deployment – Argo CD
Argo CD is responsible for the GitOps-based Continuous Deployment workflow.

Deployment Workflow
       JENKINS CI PIPELINE
               |
               v
       BUILD DOCKER IMAGE
               |
               v
       PUSH IMAGE TO REGISTRY
               |
               v
       UPDATE KUBERNETES YAML
               |
               v
       GITOPS GITHUB REPOSITORY
               |
               v
             ARGO CD
               |
               v
       DETECT REPOSITORY CHANGES
               |
               v
        SYNCHRONIZE MANIFESTS
               |
               v
        KUBERNETES CLUSTER
               |
               v
        APPLICATION DEPLOYED
Argo CD Responsibilities
Monitor the GitOps repository.
Track Kubernetes manifest changes.
Compare desired and actual cluster states.
Synchronize application configurations.
Maintain Git as the source of truth.
Support deployment history and rollback.
Important: Jenkins handles CI, while Argo CD handles Kubernetes deployment. Jenkins should not directly deploy application manifests when using this GitOps workflow.

☁️ AWS Infrastructure
The project uses AWS as its cloud platform.

Infrastructure components include:

AWS Service	Purpose
EC2	Jenkins and Kubernetes infrastructure
VPC	Network isolation
IAM	Identity and access management
S3	kOps cluster state storage
EBS	Persistent database storage
ALB	Application traffic distribution
Route 53	DNS management, where configured
Terraform is used for infrastructure provisioning, while kOps manages Kubernetes cluster lifecycle and configuration.

📂 Project Structure
vprofile-enterprise-cicd-gitops/
│
├── src/
│   └── Application source code
│
├── Dockerfile
│
├── Docker-db/
│   ├── Dockerfile
│   └── Seed SQL files
│
├── compose.yml
│
├── pom.xml
│
├── kops/
│   └── create-cluster.sh
│
├── k8s/
│   ├── 01-namespace.yaml
│   ├── 02-resourcequota.yaml
│   ├── 03-configmap.yaml
│   ├── 04-secret.yaml
│   ├── 05-storageclass.yaml
│   ├── 06-statefulset-db.yaml
│   ├── 07-service.yaml
│   ├── 08-deployment.yaml
│   ├── 09-hpa.yaml
│   ├── 10-pdb.yaml
│   ├── 11-ingress.yaml
│   └── 12-networkpolicy.yaml
│
├── Jenkinsfile
│
├── DEPLOYMENT.md
│
└── README.md
The Jenkinsfile, Terraform configuration and GitOps repository structure should be added as those components are implemented. The structure above represents the intended organization.

⚙️ Prerequisites
Before starting the project, ensure the following tools are available:

AWS Account
AWS CLI
Terraform
Git
Docker
Docker Compose
Java 11
Maven
Jenkins
SonarQube
Nexus Repository
Trivy
kubectl
kOps
Argo CD
🔧 Deployment Guide
Step 1 – Clone the Repository
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd vprofile-enterprise-cicd-gitops
Step 2 – Build the Application
mvn clean install
Step 3 – Build Docker Images
docker build -t <DOCKERHUB_USER>/vprofile-app:1.0.0 .

docker build -t <DOCKERHUB_USER>/vprofile-db:1.0.0 Docker-db/
Step 4 – Push Images
docker push <DOCKERHUB_USER>/vprofile-app:1.0.0

docker push <DOCKERHUB_USER>/vprofile-db:1.0.0
Update the image references in the Kubernetes deployment files.

Step 5 – Create Kubernetes Cluster
Configure AWS credentials and cluster state storage.

export AWS_REGION=us-east-1

export NAME=vprofile.k8s.local

bash kops/create-cluster.sh
Step 6 – Configure Database Secrets
Generate secure passwords:

openssl rand -base64 24
Update the Kubernetes Secret template locally.

Never commit actual credentials to GitHub.

Step 7 – Deploy Kubernetes Resources
kubectl apply -f k8s/
Step 8 – Verify Application
kubectl get nodes

kubectl -n vprofile get pods -o wide

kubectl -n vprofile get services

kubectl -n vprofile get pvc

kubectl -n vprofile get hpa

kubectl -n vprofile get pdb
🧪 High Availability Testing
The following tests can be performed to validate application resilience.

1. Application Pod Failure

kubectl -n vprofile delete pod -l app=vprofile-app --wait=false
Verify that Kubernetes recreates the application pods.

2. Database Pod Restart

kubectl -n vprofile delete pod mysql-0
Verify that MySQL restarts with the existing persistent data.

3. Node Maintenance

kubectl drain <NODE_NAME> \
  --ignore-daemonsets \
  --delete-emptydir-data
Verify that the Pod Disruption Budget protects application availability.

4. Kubernetes Rolling Update

kops rolling-update cluster \
  --name "$NAME" \
  --yes \
  --force
Verify that nodes are replaced through the kOps rolling-update process.

🔐 Security Considerations
The project incorporates several security practices:

Kubernetes Secrets for database credentials.
IAM roles and policies for AWS access.
Non-root Docker containers.
Non-root Kubernetes application pods.
Restricted Pod Security Standards.
Network Policies.
Encrypted EBS volumes.
SonarQube code quality analysis.
Trivy container image vulnerability scanning.
Note: Kubernetes Secrets are encoded, not encrypted by default. Production deployments should use appropriate secret-management and encryption solutions.

⚠️ Known Limitations and Future Improvements
The following improvements can make this implementation more production-ready:

Configure AWS ACM certificates for HTTPS.
Integrate an external session store such as Redis.
Migrate MySQL to Amazon RDS Multi-AZ for database high availability.
Move uploaded profile photos to Amazon S3.
Implement centralized monitoring using Prometheus and Grafana.
Configure centralized logging.
Implement automated Docker image scanning in Jenkins.
Integrate Argo CD notifications.
Implement automated GitOps image updates.
Introduce Helm charts for application deployments.
Integrate external secret management.
Add automated integration and security testing.
🎯 Project Objectives
Through this implementation, the project demonstrates practical experience with:

End-to-end CI/CD pipeline implementation.
Jenkins pipeline automation.
Maven application builds.
SonarQube code quality analysis.
Quality Gate integration.
Nexus artifact management.
Docker image creation and optimization.
Kubernetes application deployment.
AWS infrastructure provisioning.
kOps cluster administration.
GitOps-based deployment using Argo CD.
Kubernetes high availability and autoscaling.
Application and database persistence.
Container and Kubernetes security.
👨‍💻 Author
Satish Polaka

AWS DevOps Engineer | CI/CD Automation | Kubernetes | Docker | Terraform | Jenkins

GitHub: https://github.com/SatishPolaka

⭐ If you find this project useful, consider giving the repository a star.

Built to demonstrate practical Enterprise DevOps, CI/CD automation, and GitOps implementation on AWS.
>>>>>>> 16ac277 (ai agent)
