"""
This program will get the md5 sum of all files in a directory and all sug-directories.
It creates two files in the scanned root
  example: rootDir is '/Users/blainekuhn/Git'
    md5_log is the file created after a scan to get the initial md5 values
    md5_error_log will contain any files that don't have the same md5 sum
  If errorLog exists it will be deleted before beginning
  if md5_log does not exist it will be created and populated

"""
import sys, getopt, os, hashlib

md5 = hashlib.md5()
d_dict = {}
f_dict = []
log_dict = {}
rootDir = '/Users/blainekuhn/Documents/1Job Hunt'
#logFile = rootDir+"/"+"md5_log"
#errorLog = rootDir+"/"+"md5_error_log"
#check command-line inputs
for a in range(len(sys.argv)):
  if a == 1:
    logFile = rootDir+"/"+"md5_log"
    print("your md5 log will be written to %s" % logFile)
  else:
    errorLog = rootDir+"/"+"md5_error_log"
    print("your error log will be written to %s" % errorLog)

def checksum_md5(filename):
  #print filename
  import hashlib
  md5 = hashlib.md5()
  with open(filename,'rb') as f: 
    for chunk in iter(lambda: f.read(8192), b''): 
      md5.update(chunk)
    result = md5.hexdigest()
    #print result
  return result

def create_log_file(file_w_path):
  for dirName, subdirList, fileList in os.walk(rootDir):
    for fname in fileList:
      filename = os.path.join(dirName,fname)
      d_dict[filename] = checksum_md5(filename)
  if not os.path.exists(logFile):
    with open(logFile, "w") as b:
      b.close()
  with open(logFile, 'r+') as f:
      f.write(str(d_dict))
      f.write("\n")
  f.close()

def check_files(cPath):
  md5_dict = {}
  md5_error_log = (errorLog)
  with open(logFile, "r") as f:
    md5_log = open(logFile, 'r')
    md5_log = eval(md5_log.read())
    for dirName, subdirList, fileList in os.walk(rootDir):
      for fname in fileList:
        filename = os.path.join(dirName,fname)
        md5_dict[filename] = checksum_md5(filename)
    """Checking md5 sum on all files, IF the keys in each dictionary are NOT the same"""
    if not all(md5_log[n]==md5_dict[n] for n in md5_log):
      result = "\nThere was an error.  See %s" % md5_error_log
      for log_key in md5_log:
        if log_key in md5_dict:
          if not md5_log[log_key] == md5_dict[log_key]:
            if not log_key == logFile:
              with open(md5_error_log, "a") as b:
                b.write(str(md5_log[log_key] + "\t" + log_key + "\n" ))
    else:
      result = "No files have changed."
  return result

if os.path.exists(errorLog):
  os.remove(errorLog)
if not os.path.exists(logFile):
  create_log_file(logFile)

print(check_files(rootDir))
