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
