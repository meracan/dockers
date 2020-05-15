import os
from meracanapi.apitelemac import download
import argparse

parser = argparse.ArgumentParser(description='Upload telemac files to AWS')
parser.add_argument('-id',required=False,default=os.environ.get('TELEMAC_CAS_ID',""), type=str, help='Path of cas file')


if __name__ == "__main__":
  args = parser.parse_args()
  id=args.id
  if id=="":raise Exception("Need id")
  download(id)

  

