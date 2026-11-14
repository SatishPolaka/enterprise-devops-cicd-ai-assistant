# 🚀 Enterprise DevOps CI/CD and GitOps Implementation on AWS

An end-to-end Enterprise DevOps project demonstrating automated Continuous Integration (CI) using Jenkins and Continuous Deployment (CD) using Argo CD (GitOps). The project integrates GitHub, Maven, SonarQube, Quality Gates, Nexus Repository, Docker, and Kubernetes (kOps) to build, validate, package, containerize, and deploy a Java-based web application on AWS.

---

## 📌 Project Overview

This project implements an end-to-end DevOps workflow for a Java-based VProfile web application.

The main objective is to automate the complete application delivery lifecycle, starting from source code management to application deployment on a highly available Kubernetes cluster.

The implementation separates CI and CD responsibilities:

**Continuous Integration – Jenkins**
- Clone application source code from GitHub.
- Build the application using Maven.
- Perform static code analysis using SonarQube.
- Validate code quality using SonarQube Quality Gates.
- Publish application artifacts to Nexus Repository.
- Build and scan Docker images.
- Push validated images to a container registry.

**Continuous Deployment – Argo CD**
- Monitor the Kubernetes configuration repository.
- Detect changes in Kubernetes manifests.
- Synchronize the desired application state.
- Deploy application updates to the Kubernetes cluster.
- Maintain GitOps-based deployment management.

**Infrastructure and Orchestration**
- Provision AWS infrastructure using Terraform.
- Manage Kubernetes cluster infrastructure using kOps.
- Deploy application and database workloads using Kubernetes.
- Implement high availability, autoscaling, storage, networking, and security configurations.

---

## 🏗️ Architecture

### End-to-End CI/CD and GitOps Architecture

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
```

**Note:** This represents the target end-to-end workflow. Each integration should be configured and tested before being marked as completed.

---

## 🛠️ Technology Stack

| Category | Technology |
|---|---|
| Cloud Platform | AWS |
| Infrastructure as Code | Terraform |
| Source Code Management | Git, GitHub |
| CI Pipeline | Jenkins |
| CD / GitOps | Argo CD |
| Build Automation | Maven |
| Code Quality Analysis | SonarQube |
| Quality Validation | SonarQube Quality Gates |
| Artifact Repository | Nexus Repository |
| Containerization | Docker |
| Local Testing | Docker Compose |
| Container Orchestration | Kubernetes |
| Cluster Management | kOps |
| Application | Java, Spring, JSP |
| Application Server | Apache Tomcat 9 |
| Database | MySQL 5.7 |
| Load Balancing | AWS Application Load Balancer |
| Persistent Storage | AWS EBS |
| Container Registry | Docker Hub / Container Registry |

---

## 🔄 CI Pipeline – Jenkins

Jenkins is responsible for automating the Continuous Integration process.

### Pipeline Stages

**Stage 1 – Source Code Management**

- Connect Jenkins with GitHub.
- Clone the application source code.
- Retrieve the latest application changes.

**Stage 2 – Maven Build**

Execute:

```bash
mvn clean install
```

Maven resolves dependencies, compiles the Java application, executes tests and packages the application as a WAR file.

**Stage 3 – SonarQube Analysis**

- Integrate SonarQube with Jenkins.
- Configure SonarQube Scanner.
- Perform static code analysis.
- Identify code quality issues and vulnerabilities.

**Stage 4 – Quality Gate**

- Evaluate the SonarQube analysis results.
- Check whether the application meets the configured quality conditions.
- Stop the pipeline if the quality gate fails.

**Stage 5 – Nexus Artifact Upload**

- Package the application.
- Publish the generated WAR artifact to Nexus Repository.
- Maintain versioned application artifacts.

**Stage 6 – Docker Image Creation**

- Build the application Docker image.
- Use a multi-stage Dockerfile.
- Package the application with Tomcat.
- Run the container using a non-root user.

**Stage 7 – Image Scanning**

Use Trivy to scan Docker images for known vulnerabilities.

**Stage 8 – Container Registry**

Push validated Docker images to the configured container registry.

---

## 🐳 Docker Implementation

The application is containerized using a multi-stage Dockerfile.

### Multi-Stage Build Architecture

```text
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
```

### Docker Implementation Details

- Maven-based application build.
- Multi-stage Docker build.
- Apache Tomcat 9 runtime.
- Java 11 runtime environment.
- Non-root container execution.
- Container-aware JVM memory configuration.
- Reduced final image size by separating build and runtime dependencies.

### Build Application Image

```bash
docker build -t vprofile-app:1.0.0 .
```

### Build Database Image

```bash
docker build -t vprofile-db:1.0.0 Docker-db/
```

### Local Application Testing

```bash
docker compose up --build
```

The application can be accessed through:

```text
http://localhost:1234
```

---

## ☸️ Kubernetes Deployment

The application is deployed on an AWS Kubernetes cluster provisioned using kOps.

The deployment includes application and database workloads.

### Kubernetes Resources

| File | Resource | Purpose |
|---|---|---|
| 01-namespace.yaml | Namespace | Application isolation |
| 02-resourcequota.yaml | ResourceQuota / LimitRange | Resource management |
| 03-configmap.yaml | ConfigMap | Application configuration |
| 04-secret.yaml | Secret | Database credentials |
| 05-storageclass.yaml | StorageClass | Persistent storage |
| 06-statefulset-db.yaml | StatefulSet | MySQL database |
| 07-service.yaml | Services | Application and database communication |
| 08-deployment.yaml | Deployment | Application deployment |
| 09-hpa.yaml | HPA | Automatic application scaling |
| 10-pdb.yaml | PodDisruptionBudget | Application availability |
| 11-ingress.yaml | Ingress | AWS ALB integration |
| 12-networkpolicy.yaml | NetworkPolicy | Network traffic restrictions |

### Application Deployment

The application deployment is configured with:

- Initial three application replicas.
- Rolling update strategy.
- Zero unavailable pods during rolling updates.
- Startup, readiness and liveness probes.
- Pod distribution across availability zones.
- CPU and memory requests and limits.
- Non-root container execution.

### Database Deployment

MySQL is deployed using Kubernetes StatefulSet.

Implementation includes:

- Persistent EBS-backed storage.
- Encrypted gp3 volumes.
- Persistent Volume Claims.
- Database credentials through Kubernetes Secrets.
- Health checks.
- Stable database service discovery.

**Important:** MySQL uses one StatefulSet replica. Its EBS volume is zonal, so this configuration protects against pod and same-AZ node failures but does not provide automatic database failover during an entire Availability Zone outage.

---

## 📈 High Availability and Scalability

The Kubernetes architecture is designed to improve application availability and resilience.

### High Availability Architecture

| Component | Implementation |
|---|---|
| Kubernetes Control Plane | 3 control-plane instances |
| Worker Nodes | Nodes distributed across 3 AZs |
| Application Replicas | Minimum 3 |
| Horizontal Pod Autoscaler | 3 to 9 replicas |
| Pod Disruption Budget | Minimum 2 available pods |
| Deployment Strategy | Rolling Update |
| Load Balancing | AWS Application Load Balancer |
| Persistent Storage | Encrypted AWS EBS gp3 |
| Health Monitoring | Startup, Readiness and Liveness Probes |

### Horizontal Pod Autoscaling

The application uses Horizontal Pod Autoscaler.

Configuration:

```yaml
minReplicas: 3
maxReplicas: 9
```

The HPA targets average CPU utilization of 70%.

### Pod Disruption Budget

The application maintains a minimum of two available pods during voluntary disruptions.

```yaml
minAvailable: 2
```

### Network Policies

Network policies restrict unnecessary incoming traffic.

Implemented policies:

- Default deny ingress.
- Allow application HTTP traffic.
- Allow MySQL connections only from application pods.

---

## 🚀 Continuous Deployment – Argo CD

Argo CD is responsible for the GitOps-based Continuous Deployment workflow.

### Deployment Workflow

```text
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
```

### Argo CD Responsibilities

- Monitor the GitOps repository.
- Track Kubernetes manifest changes.
- Compare desired and actual cluster states.
- Synchronize application configurations.
- Maintain Git as the source of truth.
- Support deployment history and rollback.

**Important:** Jenkins handles CI, while Argo CD handles Kubernetes deployment. Jenkins should not directly deploy application manifests when using this GitOps workflow.

---

## ☁️ AWS Infrastructure

The project uses AWS as its cloud platform.

Infrastructure components include:

| AWS Service | Purpose |
|---|---|
| EC2 | Jenkins and Kubernetes infrastructure |
| VPC | Network isolation |
| IAM | Identity and access management |
| S3 | kOps cluster state storage |
| EBS | Persistent database storage |
| ALB | Application traffic distribution |
| Route 53 | DNS management, where configured |

Terraform is used for infrastructure provisioning, while kOps manages Kubernetes cluster lifecycle and configuration.

---

## 📂 Project Structure

```text
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
```

*The Jenkinsfile, Terraform configuration and GitOps repository structure should be added as those components are implemented. The structure above represents the intended organization.*

---

## ⚙️ Prerequisites

Before starting the project, ensure the following tools are available:

- AWS Account
- AWS CLI
- Terraform
- Git
- Docker
- Docker Compose
- Java 11
- Maven
- Jenkins
- SonarQube
- Nexus Repository
- Trivy
- kubectl
- kOps
- Argo CD

---

## 🔧 Deployment Guide

### Step 1 – Clone the Repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd vprofile-enterprise-cicd-gitops
```

### Step 2 – Build the Application

```bash
mvn clean install
```

### Step 3 – Build Docker Images

```bash
docker build -t <DOCKERHUB_USER>/vprofile-app:1.0.0 .

docker build -t <DOCKERHUB_USER>/vprofile-db:1.0.0 Docker-db/
```

### Step 4 – Push Images

```bash
docker push <DOCKERHUB_USER>/vprofile-app:1.0.0

docker push <DOCKERHUB_USER>/vprofile-db:1.0.0
```

Update the image references in the Kubernetes deployment files.

### Step 5 – Create Kubernetes Cluster

Configure AWS credentials and cluster state storage.

```bash
export AWS_REGION=us-east-1

export NAME=vprofile.k8s.local

bash kops/create-cluster.sh
```

### Step 6 – Configure Database Secrets

Generate secure passwords:

```bash
openssl rand -base64 24
```

Update the Kubernetes Secret template locally.

Never commit actual credentials to GitHub.

### Step 7 – Deploy Kubernetes Resources

```bash
kubectl apply -f k8s/
```

### Step 8 – Verify Application

```bash
kubectl get nodes

kubectl -n vprofile get pods -o wide

kubectl -n vprofile get services

kubectl -n vprofile get pvc

kubectl -n vprofile get hpa

kubectl -n vprofile get pdb
```

---

## 🧪 High Availability Testing

The following tests can be performed to validate application resilience.

**1. Application Pod Failure**

```bash
kubectl -n vprofile delete pod -l app=vprofile-app --wait=false
```

Verify that Kubernetes recreates the application pods.

**2. Database Pod Restart**

```bash
kubectl -n vprofile delete pod mysql-0
```

Verify that MySQL restarts with the existing persistent data.

**3. Node Maintenance**

```bash
kubectl drain <NODE_NAME> \
  --ignore-daemonsets \
  --delete-emptydir-data
```

Verify that the Pod Disruption Budget protects application availability.

**4. Kubernetes Rolling Update**

```bash
kops rolling-update cluster \
  --name "$NAME" \
  --yes \
  --force
```

Verify that nodes are replaced through the kOps rolling-update process.

---

## 🔐 Security Considerations

The project incorporates several security practices:

- Kubernetes Secrets for database credentials.
- IAM roles and policies for AWS access.
- Non-root Docker containers.
- Non-root Kubernetes application pods.
- Restricted Pod Security Standards.
- Network Policies.
- Encrypted EBS volumes.
- SonarQube code quality analysis.
- Trivy container image vulnerability scanning.

**Note:** Kubernetes Secrets are encoded, not encrypted by default. Production deployments should use appropriate secret-management and encryption solutions.

---

## ⚠️ Known Limitations and Future Improvements

The following improvements can make this implementation more production-ready:

- Configure AWS ACM certificates for HTTPS.
- Integrate an external session store such as Redis.
- Migrate MySQL to Amazon RDS Multi-AZ for database high availability.
- Move uploaded profile photos to Amazon S3.
- Implement centralized monitoring using Prometheus and Grafana.
- Configure centralized logging.
- Implement automated Docker image scanning in Jenkins.
- Integrate Argo CD notifications.
- Implement automated GitOps image updates.
- Introduce Helm charts for application deployments.
- Integrate external secret management.
- Add automated integration and security testing.

---

## 🎯 Project Objectives

Through this implementation, the project demonstrates practical experience with:

- End-to-end CI/CD pipeline implementation.
- Jenkins pipeline automation.
- Maven application builds.
- SonarQube code quality analysis.
- Quality Gate integration.
- Nexus artifact management.
- Docker image creation and optimization.
- Kubernetes application deployment.
- AWS infrastructure provisioning.
- kOps cluster administration.
- GitOps-based deployment using Argo CD.
- Kubernetes high availability and autoscaling.
- Application and database persistence.
- Container and Kubernetes security.

---

## 👨‍💻 Author

**Satish Polaka**

AWS DevOps Engineer | CI/CD Automation | Kubernetes | Docker | Terraform | Jenkins

GitHub: https://github.com/SatishPolaka

---

⭐ If you find this project useful, consider giving the repository a star.

**Built to demonstrate practical Enterprise DevOps, CI/CD automation, and GitOps implementation on AWS.**
