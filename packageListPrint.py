import os
import subprocess

__author__ = 'tony'

f = open("pack_list.txt", 'r')
wf = open("pack_desc.txt", 'w')
packageList = []

packageDesc = []

while 1:
    item = f.readline()
    if not item : break
    packageList.append(item)

for item in packageList:
    command = "rpm -qi " + item
    p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    packageDesc.append(p.communicate()[0])

for item in packageDesc:
    wf.writelines(item)
    wf.writelines('\n')

print "done"