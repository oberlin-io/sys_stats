'''
Read system stats and stream JSON
'''
import os; import re; import json; from time import sleep 

def scan():
    a=os.popen('cat /proc/meminfo |grep -A2 -i memtot').read()
    b=a.split('\n')[:-1]
    
    kre=re.compile('^([A-Z][A-Za-z]+)\:\s+\d+\skB$')
    vre=re.compile('^[A-Z][A-Za-z]+:\s+(\d+)\skB$')

    d=dict()
    for i in b:
        k=kre.findall(i)[0]
        v=vre.findall(i)[0]
        d[k]=v

    c=json.dumps(d)#, indent=2)
    #print(c)
    return c

def main(t=1):
    while True:
        a=scan()
        print(a)
        sleep(t)

if __name__=='__main__':
    main()
