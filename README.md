# Dockers
Docker containers for Marine Energy Resource Assessment Canada.

## List of Docker Containers
- telemac2dv8p1: Container to run Telemac 2d with s3-cas api.
- osmgmsh: Container to run osmgmsh

## Installation
#### Set environment variables
```bash
export AWS_REPO="awsbatch/telemac2d"
export AWS_REPOTAG="v8p1r0"
export AWS_REGION="us-east-1"
```

#### Create repository
```bash
# Get AWS Account Id to environment variable
$( echo "$values" | aws sts  get-caller-identity | jq -r '.Account as $k | "export AWS_ACCOUNT=\($k)"') 

ecr create-repository --repository-name $AWS_REPO
aws ecr get-login-password --region $AWS_REGION | docker login --username AWS --password-stdin $AWS_ACCOUNT.dkr.ecr.$AWS_REGION.amazonaws.com/$AWS_REPO
```

#### Push container to repository
```bash
docker build -t $AWS_REPO . 
docker tag $AWS_REPO:$AWS_REPOTAG $AWS_ACCOUNT.dkr.ecr.$AWS_REGION.amazonaws.com/$AWS_REPO:$AWS_REPOTAG
docker push $AWS_ACCOUNT.dkr.ecr.$AWS_REGION.amazonaws.com/$AWS_REPO
```