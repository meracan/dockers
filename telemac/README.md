# Docker-Telemac
Docker container to run telemac with aws services. 
The container downloads a steering file(.cas) and input files(geo.slf,lqd.lqd,etc) from S3, runs a simluation (t2d,t2d,tom,sis) and upload the results to S3.
The container was created using `V8p1r0`.

## Build and push to AWS
```bash
export AWS_REPO="awsbatch/telemac"
export AWS_REPOTAG="v8p1r0"
export AWS_REGION="us-east-1"
# Build
docker build -t $AWS_REPO . 

# Test
# See below

# Push
docker tag $AWS_REPO:$AWS_REPOTAG $AWS_ACCOUNT.dkr.ecr.$AWS_REGION.amazonaws.com/$AWS_REPO:$AWS_REPOTAG
docker push $AWS_ACCOUNT.dkr.ecr.$AWS_REGION.amazonaws.com/$AWS_REPO
```

## Environment Variables
The container requires a few environment variables to run:
- `TELEMAC_CAS_ID`
- `AWS_TABLECAS`
- `AWS_TABLEDATA`
- `AWS_BUCKETNAME`
- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`
- `AWS_DEFAULT_REGION`

## Simple Testing
#### Step 1
Create AWS services, if necessary. 
Please review [https://github.com/meracan/aws-cloudformation](https://github.com/meracan/aws-cloudformation)
```bash
export AWS_TEMPLATES=meracan-templates
export AWS_PROJID=meracan
export AWS_STACKNAME=$AWS_PROJID-telemac
export AWS_TABLECAS=$AWS_PROJID-Cas
export AWS_TABLEDATA=$AWS_PROJID-Data
export AWS_BUCKETNAME=$AWS_PROJID

export AWS_TABLECAS=TestTableCas
export AWS_TABLEDATA=TestTableData
export AWS_BUCKETNAME=mercantest
export AWS_DEFAULT_REGION=us-east-1

aws cloudformation create-stack 
  --stack-name $AWS_STACKNAME  
  --template-url "https://$AWS_TEMPLATES.s3.amazonaws.com/templates/telemac/basic.yaml" 
  --parameter-overrides BucketTemplateName=$AWS_TEMPLATES BucketName=$AWS_BUCKETNAME
```

#### Step 2
Install meracan-api.

```bash
conda create -n meracan python=3.8
conda activate meracan
conda install -c conda-forge boto3

pip install -e ./meracan-api
```
#### Step 3
Upload telemac files to AWS. 
In this case, we have copied the `telemac2d/confluence` example from opentelemac.
```bash
python3 test/upload.py test/telemac2d/confluence/t2d_confluence.cas
```
#### Step 4
Test container using environment variables.
```bash
docker run -it \
  --name test \
  --env TELEMAC_CAS_ID="138000d5-d62b-422c-9386-eeb4edea5a97" \
  --env AWS_TABLECAS=$AWS_TABLECAS \
  --env AWS_TABLEDATA=$AWS_TABLEDATA \
  --env AWS_BUCKETNAME=$AWS_BUCKETNAME \
  -v $HOME/.aws/credentials:/root/.aws/credentials:ro \
  awsbatch/telemac

docker rm test
```

#### Environment Variables
- TELEMAC_CAS_ID
- AWS_TABLECAS
- AWS_TABLEDATA
- AWS_BUCKETNAME

## Testing
**Step1**
Follow *Installation* in [aws-cloudformation](https://github.com/meracan/aws-cloudformation)
**Step2**
```bash
aws cloudformation create-stack --stack-name $AWS_PROJID-telemac --template-url "https://$BucketName.s3.amazonaws.com/templates/telemac/simple.yaml" --parameter-overrides BucketName=$AWS_PROJID
```


**Step 2**
Create Bucket and DynamoDB tables
```