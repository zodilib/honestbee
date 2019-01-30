import requests
import numpy
import csv 
import os
import sys 

class GitCall():
    def __init__(self, param, filename):
        self.p = param
        self.file = filename

    
    def writerepoinfo(self):
        link = "https://api.github.com/repos/"+self.p
        r = requests.get(link)
        val_1 = r.json()
        repo_name = val_1["name"]
        owner_name = val_1["owner"]["login"]
        clone_url = val_1["clone_url"]
        latest_commit = val_1["pushed_at"]
        print("repo_name = {0:2s} || owner_name = {1:3s} || clone_url = {2:4s} || latest_commit = {3:5s}".format(repo_name, owner_name, clone_url, latest_commit))
        f = open(self.file,'ab')
        a = numpy.asarray([ [repo_name, owner_name, clone_url, latest_commit], ])
        numpy.savetxt(f, a, fmt="%s",delimiter=",")
        f.close()

if __name__ == "__main__":
    

    if len(sys.argv) < 2:
        raise SystemExit("%s <repolist filename>" % sys.argv[0])
        
    repolist  = sys.argv[1]

    if os.path.exists("repoinfo.csv"):
        os.remove("repoinfo.csv")

    lines = tuple(open(repolist, 'r'))
    
    m = open('repoinfo.csv', 'ab')
    a = numpy.asarray([ ["repo_name", "owner_name", "clone_url", "latest_commit"], ])
    numpy.savetxt(m, a, fmt="%s",delimiter=",")
    m.close()
    
    for l in lines:
       obj = GitCall(l.rstrip('\n'), 'repoinfo.csv')
       try:
            obj.writerepoinfo()
       except: 
        print("The repo is not public")
        
     

