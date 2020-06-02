import json
import argparse
import os

def main():

    p = argparse.ArgumentParser(description="Requires user to supply directory")
    p.add_argument("-path", required=True, dest='path')

    args = p.parse_args()
    
    dirInfo = []

    files = os.listdir(args.path)
    for file in files:
        path = args.path + file
        results = os.stat(path)
        fileInfo = {}
        fileInfo['name'] = file
        if os.path.isdir(path):
            fileInfo['type'] = "Directory"
        elif os.path.isfile(path):
            fileInfo['type'] = "File"
        else:
            fileInfo['type'] = "Special File"
        fileInfo['st_mode'] = results.st_mode
        fileInfo['st_ino'] = results.st_ino
        fileInfo['st_size'] = results.st_size
        fileInfo['st_atime'] = results.st_atime
        fileInfo['st_gid'] = results.st_gid
        fileInfo['st_dev'] = results.st_dev
        fileInfo['st_nlink'] = results.st_nlink
        fileInfo['st_uid'] = results.st_uid
        fileInfo['st_mtime'] = results.st_mtime
        fileInfo['st_ctime'] = results.st_ctime
        dirInfo.append(fileInfo)

    with open('directoryInfo.json', 'w') as f:
        for i in dirInfo:
            f.write(json.dumps(i) +"\n")

main()