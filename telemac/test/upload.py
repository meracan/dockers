import os
from meracanapi.apitelemac import uploadFile
import argparse

parser = argparse.ArgumentParser(description='Upload telemac files to AWS')
parser.add_argument('path', type=str, help='Path of cas file')


if __name__ == "__main__":
  args = parser.parse_args()
  path=args.path
  if not os.path.exists(path):raise Exception("Path does not exist")
  uploadFile(path)