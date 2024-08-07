## Instructions for Deploying on AWS EC2

### Installing Docker on Amazon Linux 2

1. **Update Your System:**
   
   ```bash
   sudo yum update -y
   ```
2. **Install Docker**
   ```bash
   sudo yum install docker -y
   ```
3. **Start and Enable Docker**
   ```bash
   sudo systemctl start docker
   ```
   ```bash
   sudo systemctl enable docker
   ```
5. **Verify Docker Installation**
   ```bash
   sudo docker --version
   ```
6. **Add EC2-User to the Docker's User group**
   ```bash
   sudo usermod -aG docker $USER
   ```
7. **Log out and Log Back in for the Changes to Take Effect**
   ```bash
   exit
   ```
   ```bash
   ssh -i /path/to/your/private-key.pem ec2-user@ec2-instance-public-ip
   ```

### Installing Docker Compose on Amazon Linux 2

1. **Download the Docker Compose binary**
   
   ```bash
   sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
   ```

2. **Make the Downloaded Binary Executable**
   ```bash
   sudo chmod +x /usr/local/bin/docker-compose
   ```

3. **Verify Installation**
   ```bash
   docker-compose --version
   ```

### Starting the Flask Web Service

1. **Building the Docker Image Using Docker Compose**
   
   ```bash
   docker-compose build
   ```

2. **Running the Docker Container**
   ```bash
   docker-compose up
   ```