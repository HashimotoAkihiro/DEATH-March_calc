import sys

argv = sys.argv
argc = len(argv)
timelist = []

def calc_result():
    print "argv: ",
    print argv
    print "argc",
    print argc

    filename = "%s" % (argv[1])
    resultfile = "team_result.txt"
    try:
        f = open(filename,"r")
        result = open(resultfile,"a")
    except:
        print "Error",
        print u"Please write a current filename".encode('utf-8')
    
 
    for i in f.readlines():
        timelist.append(float(i))
 
    ave = sum(timelist)/len(timelist)
    print "average time :" + format(ave) + "[sec]"
    result.write(format(ave)+"\n")
    
    f.close()
    result.close()

if __name__ == '__main__':
    calc_result()

