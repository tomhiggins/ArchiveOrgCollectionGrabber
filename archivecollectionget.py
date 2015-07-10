#!/usr/bin/python
import os, sys, getopt
from internetarchive import search_items, get_item

def main(argv):
   collection = ''
   outputdir = ''
   slamall = 0
   fext = ''
   getext = ['.mp3', 'epub', '.pdf', '.cbz', '.cbr', '.avi', 'mp4', 'divx', 'rar']

   try:
      opts, args = getopt.getopt(argv,"hc:o:a",["collection=","outputdir=","all"])
   except getopt.GetoptError:
      print 'archivecollectionget.py -c <archive.org collection> -o <outputdirectory>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'archivecatalogget.py -c <archive.org collection> -o <outputdirectory>'
         sys.exit()
      elif opt in ("-c", "--collection"):
         collection = arg
      elif opt in ("-o", "--outputdir"):
         outputdir = arg
      elif opt in ("-a", "--all"):
         slamall = 1
   print 'I will now scour the Archive.org collection ', collection + ' and put the results in', outputdir
   search = search_items('collection:'+collection)
   print "Items in collection", collection +" = ",search.num_found 
   if not(os.path.isfile(outputdir + collection)):
	   	os.mkdir(outputdir + collection) 
   os.chdir(outputdir + collection)
   for result in search:
	print(result['identifier'])
        item = get_item(result['identifier'])
   	for f in item.iter_files():
		 fext = f.name[(len(f.name)-4):]
                 if fext in getext: 
			print f.name
			if not(os.path.isfile(f.name)):
				f.download() 


if __name__ == "__main__":
   main(sys.argv[1:])



