from sys import *
import os
import hashlib

def hashlib(path,blocksize=1024):
	fd=open(path,'rb')
	hasher=hashlib.md5()
	buf=fd.read(blocksize)

	while len(buf)>0:
		hasher.update(buf)
		buf=fd.read(blocksize)
	fd.close()
	return hasher.hexdigest()

def FindDuplicate(path):
	flag=os.path.isabs(path)

	if flag==False:
		path=os.path.abspath(path)

	exists=os.path.isdir(path)
	dups={}

	if exists:
		for dirName,subdirs,fileList in os.walk(path):
			for filen in fileList:
				path=os.path.join(dirName,filen)
				file_hash=hashfile(path)
				if file_hash in dups:
					dups[file_hash].append(path)
				else:
					dups[file_hash]=[path]
			return dups
		else:
			print("Invalid path")

def PrintDuplicate(dict1):
	results=list(filter(lambda x:len(x)>1,dict1.values()))
	
	if len(results)>0:
		print("Duplicates found")
		
		print("the following files are identical")

		icnt=0;
		for result in results:
			for subresult in result:
				icnt+=1
				if icnt>=2:
					print('\t\t%s'%subresult)
	else:
		print("No duplicate files found")

def main():
	print("Duplicate File")
	
	print("Application name:"+argv[0])

	if(len(argv)!=2):
		print("Error:Invalid number of arguments")
		exit()

	if(argv[1]=="-h")or(argv[1]=="-H"):
		ptint("Traverse")
		exit()

	if(argv[1]=="-u")or(argv[1]=="-U"):
		print("usage Duplicate files")
		exit()

	try:
		arr={}
		arr=FindDuplicate(argv[1])
		PrintDuplicate(arr)

	except ValueError:
		print("Error:invalid datatype of input")

if __name__ == "__main__":
    main()
