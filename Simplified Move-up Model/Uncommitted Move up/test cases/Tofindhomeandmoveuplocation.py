import os
from os import listdir
from os.path import isfile,join
import os.path

print "Let's begin"
#(1)input path:
os.path.abspath('Incident_Zone.txt')
path=os.path.abspath('Data')+'\\'
path1=os.path.abspath('Data\\Reco Logs')+'\\'
path2=os.path.abspath('Data\\tracking')+'\\'

#(2)class definition and initialization
trackfolder=path
files=[f for f in listdir(trackfolder) if isfile(join(trackfolder,f))]
kk=0
for thing in files:
    name=str(thing)
    if name == "Incident.txt":
          name=path+name
          f = open(name, 'r')
          lineiter = f.readlines()
          for line in lineiter:
              kk=kk+1

    if name =="Available Key Word.txt":
          name=path+name
          f=open(name,'r')
          ss=0
          lineiter=f.readlines()
          for line in lineiter:
              ss=ss+1
          word=range(ss)
          s=0
          for line in lineiter:
              word[s]=line[:len(line)-1]
              s=s+1

trackfolder=path1
files=[f for f in listdir(trackfolder) if isfile(join(trackfolder,f))]
nn=0
for thing in files:
    name=str(thing)
    cutname=name[15:28]
    cutdate=name[:8]
    
    if cutname=='New Reco.txt':
        fullpath=str(trackfolder+'/'+name)
        f=open(fullpath,'r')
        lineiter=f.readlines()
        for line in lineiter:
            if ":" in line and "*" not in line:
                nn=nn+1
trackfolder=path
files=[f for f in listdir(trackfolder) if isfile(join(trackfolder,f))]
dd=0
ww=0
for thing in files:
    name=str(thing)
    if name=="Incident_Zone.txt":
        name=trackfolder+name
        f=open(name,'r')
        lineiter=f.readlines()
        
        for line in lineiter:
            dd=dd+1
        #print dd
        
    if name=="Station_Zone.txt":
        name=trackfolder+name
        f=open(name,'r')
        lineiter=f.readlines()
        
        for line in lineiter:
            ww=ww+1
        #print ww

class Incident_Zone:
    def __init__(self,inci,zone):
        self.inci=inci
        self.zone=zone
storeincizone=range(dd)

class Station_Zone:
    def __init__(self,Station,zone,time):
        self.Station=Station
        self.zone=zone
        self.time=time
storestazone=range(ww)

class store:
    def __init__(self,unitname,ready):
        self.unitname=unitname
        self.ready=ready
#storex=range(5)


class storefindtime:
    def __init__(self,stationname,ready,time):
        self.stationname=stationname
        self.ready=ready
        self.time=time
        
class unistation:
    def __init__(self,unitname,station):
        self.unitname=unitname
        self.station=station


class time_home_move:
     def __init__(self,time,unitname,homestation,moveupstation):
        self.time=time
        self.unitname=unitname
        self.homestation=homestation
        self.moveupstation=moveupstation
#storemoveup=range(103)
storemoveup=range(nn)

class incident:
     def __init__(self,IncidentNo,start_time):
        self.IncidentNo=IncidentNo
        self.start_time=start_time
#storeincident=range(10500)
#storeuseful=range(10500)
storeincident=range(kk)
storeuseful=range(kk)

def tofindhomeandmoveuplocation():
    trackfolder=path1
    files=[f for f in listdir(trackfolder) if isfile(join(trackfolder,f))]
    k=0
    for thing in files:
        name=str(thing)
    
        cutname=name[15:28]
        cutdate=name[:8]
    
        if cutname=='New Reco.txt':
        
            fullpath=str(trackfolder+'/'+name)
            f=open(fullpath,'r')
            lineiter=f.readlines()
            
            for line in lineiter:
                if ":" in line and "*" not in line:
                    time=cutdate+line[:2]+line[3:5]+line[6:8]
                    time=int(time)

                    pp1=0
                    pp2=0
                    while(pp1<len(line)):
                        if line[pp1]=="'":
                            pp2=pp1+1
                            while(pp2<len(line)):
                                if line[pp2]=="'":
                                    unitname=line[pp1+1:pp2]
                                    
                                    break
                                else:
                                    pp2=pp2+1
                            break
                        else:
                            pp1=pp1+1
                    #print "unitname",unitname
                    
                        
                    
                    pp=0
                    q=0
                    while(pp<len(line)):
                        if line[pp]=="'":
                            q=q+1
                            if q==3:
                                break
                            else:
                                pp=pp+1
                        else:
                            pp=pp+1
                    homestation=line[pp:]
                    i=0
                    j=0
                    while(i<len(homestation)):
                        if homestation[i]=="'":
                            j=i+1
                            while(j<len(homestation)):
                                if homestation[j]=="'":
                                    homestation=homestation[i+1:j]
                                else:
                                    j=j+1
                        else:
                            i=i+1
                    moveupstation=line[pp+j+1:]
                    
                    i=0
                    j=0
                    while(i<len(moveupstation)):
                        if moveupstation[i]=="'":
                            j=i+1
                            while(j<len(moveupstation)):
                                if moveupstation[j]=="'":
                                    moveupstation=moveupstation[i+1:j]
                                else:
                                    j=j+1
                        else:
                            i=i+1
                    
                    storemoveup[k]=time_home_move(time,unitname,homestation,moveupstation)
                    k=k+1
    return(k,storemoveup)

tofindhomeandmoveuplocation()                
