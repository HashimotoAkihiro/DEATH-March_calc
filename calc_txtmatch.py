import time
import commands
import subprocess
import sys

argv = sys.argv
argc = len(argv)
timelist = []

def calc_time():
    print "argv: ",
    print argv
    print "argc: ",
    print argc
    
    # cmd = "./%s" % (argv[1]) # cmd = argv[1] ex) a.out
    cmd = "%s" % (argv[1]) # cmd = argv[1] ex) a.out
    index = 1
    if argc > 2:
        while index < argc-1:
            index = index + 1
            option = " %s" % (argv[index])
            #print option
            cmd = cmd + option
            #print argv[index]

     
    # print "start prog = ",
    # print cmd
    # start = time.time()
    # subprocess.call( cmd.strip().split(" ")  ) 
    # elapsed_time = time.time() - start
    # print ("elapsed_time:{0}".format(elapsed_time)) + "[sec]"

    print "start prog = ",
    print cmd


    start = time.time()
    subprocess.call( cmd.strip().split(" ")  ) 
    elapsed_time = time.time() - start
    print ("elapsed_time:{0}".format(elapsed_time)) + "[sec]"

    f = open("result_txtmatch.txt","a")
    f.write(format(elapsed_time)+"\n")
    

if __name__ == '__main__':
    calc_time()
