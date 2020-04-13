import os
import s3telemac

# Get environment variables
CAS_S3_URL = os.getenv('CAS_S3_URL')
TELAMAC_MODULE = os.getenv('TELAMAC_MODULE')
CORES = os.getenv('TELAMAC_CORES')

s3telemac(CAS_S3_URL)