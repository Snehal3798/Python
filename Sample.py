from sys import *
import os
def DerectoryWatcher(path):

	flag=os.path.isabs(path)
	if flag==False:
		path=os.path.abspath(path)
	
	exists=os.path.isdir(path)

	if exists:
		for foldername,subfolder,filename in os.walk(path):
			print("Current Folder is:",+foldername)
			for subf in subfolder:
				print("Subfolder of"+foldername+"is:"+subf)
			for filen in filename:
				print("File inside"+foldername+"is:"+filen)
			print('')
	else:
		print("invalid path")


def main():
	print("Welcome to Automation")
	print("Application name"+argv[0])
	
	if(len(argv)!=2):
		print("Error:Invalid no of argv")
		exit()
	if(argv[1]=="-h")or(agrv[1]=="-H"):
		print("Scriot is for traverse")
		exit()
	if (argv[1]=="-u")or(argv=="-U"):
		print("usage:Application name Abosolute path")
		exit()
	
	try:
		DerectoryWatcher(argv[1])
	except ValueError:
		print("Error:Invalid datatype of input")

	except Exception:
		print("Error:Invalid input")
if __name__=="__main__":
	main()