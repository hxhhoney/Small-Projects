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
              word[s]=line[:len(line)]
              #print 'word test:',word[s]
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

class storefindtime:
    def __init__(self,unitname,ready,time):
        self.unitname=unitname
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
storemoveup=range(nn)


class incident:
     def __init__(self,IncidentNo,start_time):
        self.IncidentNo=IncidentNo
        self.start_time=start_time
storeincident=range(kk)
storeuseful=range(kk)

#(3)functions
def dist(station,incident):
    trackfolder=path
    files=[f for f in listdir(trackfolder) if isfile(join(trackfolder,f))]
    
    
    for thing in files:
        name=str(thing)
        if name=="Incident_Zone.txt":
            name=trackfolder+name
            f=open(name,'r')
            lineiter=f.readlines()
            pointer =0
            No1=0
            for line in lineiter:
                while(pointer<len(line)):
                    if line[pointer]==',':
                        inci=line[:pointer]
                        zone=line[pointer+1:len(line)-1]
                        #print inci
                        #print zone
                        storeincizone[No1]=Incident_Zone(inci,zone)
                        break
                    else:
                        pointer=pointer+1
##                print 'No1:',No1
##                print storeincizone[No1].inci,storeincizone[No1].zone
                No1=No1+1
        
        
        if name=="Station_Zone.txt":
            name=trackfolder+name
            f=open(name,'r')
            lineiter=f.readlines()
            pointer=0
            No=0
            linecount = 0
            for line in lineiter:
                splitline = line.split(',')
                Station = splitline[0]
                zone=splitline[1]
                time=splitline[2]
                time=float(time[:len(time)-1])
                storestazone[No]=Station_Zone(Station,zone,time)
                #print storestazone[No].Station#,storestazone[No].zone,storestazone[No].time
                No=No+1
           
    pointerA=0
    pointerB=0
    result=0
    while(pointerA<dd):
        if incident==storeincizone[pointerA].inci:
            #print incident, storeincizone[pointerA].inci
            #print storeincizone[pointerA].zone,station
            while(pointerB<ww):
                if storeincizone[pointerA].zone==storestazone[pointerB].zone and station==storestazone[pointerB].Station:
                    #print storestazone[pointerB].Station
                     
                    
                    #print storeincizone[pointerA].zone,storestazone[pointerB].zone,station,storestazone[pointerB].Station
                    result=storestazone[pointerB].time
                    #print result
                    result=float(result)
                    break
                else:
                    pointerB=pointerB+1
            pointerA=pointerA+1
        else:
            pointerA=pointerA+1
    return result
#dist('SH02','15-06420')    

def comp(loc1,loc2,inci):
    dis1=dist(loc1,inci)
    dis2=dist(loc2,inci)
    #print loc1,loc2,inci
    #print dis1,dis2
    if dis1>=dis2:
        dd=loc2
    else:
        dd=loc1
    return (dd)

#comp('CARI','CAUL1','15-00240')

def accu(moveupstation,homestation,inci):
    if comp(moveupstation,homestation,inci)==moveupstation:
        acc=1
        #print"This is an accurate move-up"
        #This is an accurate move-up,since the new incident happens in a location more close to the move-up station.
    else:
        acc=0
        #print"This is an inaccurate move-up"
        #This is not an accurate move-up, since the new incident happens in a location more far away from the move-up station.
    return(acc)
#accu('CARI','CAUL1','15-00240')

def nearest(Currentlocofunit,AvaiMatrix,inci):
    #aa and bb has the same dimension
    n=len(Currentlocofunit)
    i=0
    j=0
    dis=Currentlocofunit[0]
    while(i<n):
        if AvaiMatrix[i]==1:
            if dis>dist(Currentlocofunit[i],inci):
                #print Currentlocofunit[i]
                dis=dist(Currentlocofunit[i],inci)
                j=i
                i=i+1
            else:
                i=i+1
        else:
            i=i+1
##    if j==0 and AvaiMatrix[0]==0:
##        Currentlocofunit[j]=0
    return(Currentlocofunit[j],j)


#############################################################################################

   
def Legitimate():
    trackfolder=path
    files=[f for f in listdir(trackfolder) if isfile(join(trackfolder,f))]
    for thing in files:
        name = str(thing)
        if name == "Legitimate Threshold.txt":
                fullpath=str(trackfolder + "/" + name)
                f = open(fullpath, 'r')
                lineiter = f.readlines()                           
                p1=0
                small=0
                large=0
                for line in lineiter:
                    if p1==1:
                        small=int(line)
                    if p1==3:
                        large=int(line)
                    p1=p1+1
    return ([small, large])
#Legitimate()

def tofindcurrentlocation(t):
    trackfolder=path2

    files=[f for f in listdir(trackfolder) if isfile(join(trackfolder,f))]
    t=str(t)
    t1=int(t[0:12])
    t2=int(t)
    for thing in files:
        name = str(thing)
        namecut = name[13:]
        if namecut == "Tracking Info.txt":
            datesearch =int(name[0:12])
            datesearch2 = name[4:-24] + "/" + name[6:-22] + "/" + name[2:-26]
            if t1>datesearch:
                fullpath=str(trackfolder + "/" + name)
                f = open(fullpath, 'r')
                lineiter = f.readlines()                           
                for line in lineiter:
                    if (line[0:8] == datesearch2 ):
                        time= "20" +line[6:8]+line[0:2]+line[3:5]+line[9:11]+line[12:14]+line[15:17]
                        time=int(time)
                        if time<t2:
                            fullpath=str(trackfolder + "/" + name)
                            break
    #print fullpath
    f=open(fullpath,"r")
    lineiter=f.readlines()

    qq1=0
    for line in lineiter:
        if "Units	Stations" in line:
            #print line
            break
        else:
            qq1=qq1+1

    qq2=0
    for line in lineiter:
        if "MUM Units and Home Stations  End" in line:
            #print line
            break
        else:
            qq2=qq2+1
    zz=qq2-qq1+1
    storeunit=range(zz)
    rr=0
    i=0
    for line in lineiter:
        if rr>qq1 and rr<qq2:
            lineinterested=line
            new=line.split('    ')
            unit=new[0]
            station=new[1]
            station=station[:len(station)]
            storeunit[i]=unistation(unit,station)
            i=i+1
            rr=rr+1
        else:
            rr=rr+1

    CurrentLo=range(i)
    h=0
    while(h<i):
        CurrentLo[h]=storeunit[h].station
        CurrentLo[h]=CurrentLo[h][:len(CurrentLo[h])-1]
        
        h=h+1
    return (i,CurrentLo)
#tofindcurrentlocation(2015020108140000)

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
                                    break
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

#tofindhomeandmoveuplocation()                

def tofindAvaiMatrix(t):
    jj=tofindcurrentlocation(t)[0]
    #print jj
    storex=range(jj)
    t=str(t)
    t1=int(t[0:12])
    t2=int(t)
    trackfolder=path2

    files=[f for f in listdir(trackfolder) if isfile(join(trackfolder,f))]
    
    for thing in files:
        name = str(thing)
        namecut = name[13:]
        if namecut == "Tracking Info.txt":
            datesearch =int(name[0:12])
            datesearch2 = name[4:-24] + "/" + name[6:-22] + "/" + name[2:-26]
            if t1>datesearch:
                fullpath=str(trackfolder + "/" + name)
                f = open(fullpath, 'r')
                lineiter = f.readlines()                           
                for line in lineiter:
                    if (line[0:8] == datesearch2 ):
                        t3= "20" +line[6:8]+line[0:2]+line[3:5]+line[9:11]+line[12:14]+line[15:17]
                        t3=int(t3)
                        if t3<t2:
                            fullpath=str(trackfolder + "/" + name)
                            break
    #print fullpath
    f=open(fullpath,"r")
    lineiter=f.readlines()

    qq1=0
    for line in lineiter:
        if "Units	Status	Stations	IncidentType" in line:
            #print line
            break
        else:
            qq1=qq1+1

    qq2=0
    for line in lineiter:
        if " All UsingTCPIPCAD Unit Status and Home Stations  End " in line:
            #print line
            break
        else:
            qq2=qq2+1

    rr=0
    i=0
    for line in lineiter:
        if rr>qq1 and rr<qq2:
            lineinterested=line
            
            
            pointer1=0
            while(pointer1<len(lineinterested)):
                if lineinterested[pointer1]=='\t':
                    unitname=lineinterested[:pointer1]
                    break
                else:
                    pointer1=pointer1+1

            status=lineinterested[pointer1:]
            ff=0
            gg=0
            while(ff<len(status)):
                if status[ff]!='\t':
                    gg=ff+1
                    while(gg<len(status)):
                        if status[gg]=='\t':
                            status=status[ff:gg]
                            break
                        else:
                            gg=gg+1
                    break          
                else:
                    ff=ff+1
            
            wordlen=len(word)
            wordi=0
            while(wordi<wordlen):
                #print "status",status
                #print 'word',word[wordi]
                
                if status==word[wordi]:
                    ready=1
                    #print 'ready',ready
                    break
                else:
                    ready=0
                    wordi=wordi+1
                

            
##            if status==word[0]:
##                ready=1
##            else:
##                ready=0
            if len(unitname)!=0:
                storex[i]=store(unitname,ready)
                #print storex[k].unitname,storex[k].ready
                i=i+1
                
            #print storex[abc].unitname, storex[abc].ready
 
            #print lineinterested
            rr=rr+1
        else:
            rr=rr+1
    trackfolder= path2

    files=[f for f in listdir(trackfolder) if isfile(join(trackfolder,f))]
    
    for thing in files:
        name = str(thing)
        namecut = name[13:]

        if namecut == "Tracking Info.txt":
            datesearch =int(name[0:12])
            datesearch2 = name[4:-24] + "/" + name[6:-22] + "/" + name[2:-26]
            #print name
            if t1>datesearch:
                fullpath=str(trackfolder + "/" + name)
                f = open(fullpath, 'r')
                lineiter = f.readlines()
                for line in lineiter:
                    y=0
                    while(y<len(line)):
                        if line[y]==" ":
                            break
                        else:
                            y=y+1
                    if (line[0:y] == datesearch2 ):
                        time= "20" +line[y-2:y]+line[y-8:y-6]+line[y-5:y-3]

                        while(y<len(line)):
                            if line[y]!=' ':
                                break
                            else:
                                y=y+1
                        time=time+line[y:y+2]+line[y+3:y+5]+line[y+6:y+8] 
                        time=int(time)                        
                        if time<t2:
                          unitname=line[y+8:]
                          y1=0
                          y2=0
                          while(y1<unitname):
                              if unitname[y1]!='\t':
                                  y2=y1+1
                                  while(y2<len(unitname)):
                                      if unitname[y2]=="\t":
                                          unitname=unitname[y1:y2]
                                          break
                                      else:
                                          y2=y2+1
                                  break
                              else:
                                  y1=y1+1
                          stationname=line[y+8+y2:]
                          z1=0
                          z2=0
                          while(z1<stationname):
                              if stationname[z1]!='\t':
                                  z2=z1+1
                                  while(z2<len(stationname)):
                                      if stationname[z2]=="\t":
                                          stationname=stationname[z1:z2]
                                          break
                                      else:
                                          z2=z2+1
                                  break
                              else:
                                  z1=z1+1

                          ready1=line[y+8+y2+z2:]
                          pointer=0
                          counter=0
                          while (pointer<len(ready1)):
                              if ready1[pointer]=="\t" and ready1[pointer+1]!='\t':
                                  counter=counter+1
                                  pointer=pointer+1
                              elif ready1[pointer]!="\t" and ready1[pointer+1]=='\t':
                                  counter=counter+1
                                  pointer=pointer+1
                              else:
                                  pointer=pointer+1
                              if counter==5:
                                  break
                          pointer2=pointer+1
                          while(pointer2<len(ready1)):
                              if ready1[pointer2]=="\t":
                                  ready1=ready1[pointer:pointer2]
                                  break
                              else:
                                  pointer2=pointer2+1
                          s=0
                          ready=0
                          while (s<ss):
                                if word[s]==ready1:
                                    ready=1
                                    break
                                else:
                                    ready=0
                                    s=s+1
                                         
                          temp=store(unitname,ready)
                          #print temp.ready
                          k=0
                          while(k<i):
                             #print storex[k].unitname,temp.unitname
                              if storex[k].unitname==temp.unitname:
                                  ##print temp.ready
                                  storex[k].ready=temp.ready
                                  break
                              else:
                                  k=k+1
    j=0
    AvailableMatrix=range(i)
    while(j<i):
        #print storex[j].ready
        AvailableMatrix[j]=storex[j].ready
        j=j+1

    return AvailableMatrix
#tofindAvaiMatrix(20150201110000)           

def durationtimetransfer(t,tt):
    import datetime
    t=str(t)
    #print "t:",t
    tt=str(tt)
    #print "tt:",tt
    start=datetime.datetime.strptime(t,'%Y%m%d%H%M%S')
    end=datetime.datetime.strptime(tt,'%Y%m%d%H%M%S')
    diff=end-start
    print "diff:",diff
    duration=diff.seconds/60
    return duration
#durationtimetransfer(20150210142224,20150210142239)

def findtimeboolean():
    trackfolder=path
    files=[f for f in listdir(trackfolder) if isfile(join(trackfolder,f))]
    
    for thing in files:
        name = str(thing)
        if name == "findtime boolean.txt":
                fullpath=str(trackfolder + "/" + name)
                f = open(fullpath, 'r')
                lineiter = f.readlines()                           
                p1=0
                #print 'aaa'
                for line in lineiter:
                    if p1==1:
                        #print line
                        if 'True' in line:
                            status=1
                        else:
                            status=0
                        break
                    else:
                        p1=p1+1
               # print status
                return (status)
#findtimeboolean()

def findtime(t,oriunitname):
    
    trackfolder=path2

    files=[f for f in listdir(trackfolder) if isfile(join(trackfolder,f))]

    #given a time t with a form such as: 20150205080544, which means 02/05/15 08:05:44

    t=str(t)
    t1=int(t[0:12])
    t2=int(t)

    storex=range(2)
    storex[0]=storefindtime(oriunitname,0,t2)
    storex[1]=storefindtime(oriunitname,0,t2)
 
    j=0
    for thing in files:
         name = str(thing)
         namecut = name[13:]
         if namecut == "Tracking Info.txt":
            datesearch =int(name[0:12])
            datesearch2 = name[4:-24] + "/" + name[6:-22] + "/" + name[2:-26]
            #print name
            if t1>datesearch:
                fullpath=str(trackfolder + "/" + name)
                f = open(fullpath, 'r')
                lineiter = f.readlines()
                for line in lineiter:
                    y=0
                    while(y<len(line)):
                        if line[y]==" ":
                            break
                        else:
                            y=y+1
                    if (line[0:y] == datesearch2 ):
                        time= "20" +line[y-2:y]+line[y-8:y-6]+line[y-5:y-3]

                        while(y<len(line)):
                            if line[y]!=' ':
                                break
                            else:
                                y=y+1
                        time=time+line[y:y+2]+line[y+3:y+5]+line[y+6:y+8] 
                        time=int(time)                        
                        if time>t2:
                          unitname=line[y+8:]
                          y1=0
                          y2=0
                          while(y1<unitname):
                              if unitname[y1]!='\t':
                                  y2=y1+1
                                  while(y2<len(unitname)):
                                      if unitname[y2]=="\t":
                                          unitname=unitname[y1:y2]
                                          break
                                      else:
                                          y2=y2+1
                                  break
                              else:
                                  y1=y1+1
                          stationname=line[y+8+y2:]
                          z1=0
                          z2=0
                          while(z1<stationname):
                              if stationname[z1]!='\t':
                                  z2=z1+1
                                  while(z2<len(stationname)):
                                      if stationname[z2]=="\t":
                                          stationname=stationname[z1:z2]
                                          break
                                      else:
                                          z2=z2+1
                                  break
                              else:
                                  z1=z1+1

                          ready1=line[y+8+y2+z2:]
                          pointer=0
                          counter=0
                          while (pointer<len(ready1)):
                              if ready1[pointer]=="\t" and ready1[pointer+1]!='\t':
                                  counter=counter+1
                                  pointer=pointer+1
                              elif ready1[pointer]!="\t" and ready1[pointer+1]=='\t':
                                  counter=counter+1
                                  pointer=pointer+1
                              else:
                                  pointer=pointer+1
                              if counter==5:
                                  break
                          pointer2=pointer+1
                          while(pointer2<len(ready1)):
                              if ready1[pointer2]=="\t":
                                  ready1=ready1[pointer:pointer2]
                                  break
                              else:
                                  pointer2=pointer2+1
                          ready=0
                          if word[0] == ready1 or word[1]==ready1:
                              ready=1
                          else:
                              ready=0  
                          temp=storefindtime(unitname,ready,time)
                         #print temp.unitname
                         #print temp.ready
                    
                          if storex[0].unitname==temp.unitname:
                              #print temp.time
                              #print temp.ready
                              if temp.ready==1:          
                                  storex[1].time= temp.time
                                  break
                          #print "temp.time:",temp.time
                       
    if storex[1].time==storex[0].time:
        if findtimeboolean()==1:
           storex[1].time=temp.time

    return storex[1].time
    #This is the time that the certain unit will come back to its home station.
#findtime(20150201081309,'SH02')


def incident_Matrix(time1,time2):
    trackfolder= path

    files=[f for f in listdir(trackfolder) if isfile(join(trackfolder,f))]


    #Here 10500 is i found below
    

    for thing in files:
       name = str(thing)
       if name == "Incident.txt":
          name=trackfolder+name
          f = open(name, 'r')
          lineiter = f.readlines()
 
          i=0
          for line in lineiter:
              IncidentNo=line
              xx=0
              while(xx<len(line)):
                  if line[xx]=="\t":
                      IncidentNo=line[:xx]
                      break
                  else:
                      xx=xx+1

              starttime=line[xx:]
              yy1=0
              while(yy1<len(starttime)):
                  if starttime[yy1]!="\t":
                      starttime='20'+starttime[yy1+6:yy1+8]+starttime[yy1:yy1+2]+starttime[yy1+3:yy1+5]
                      break
                  else:
                      yy1=yy1+1

              starttime1=line[xx+yy1+8:]
              yy1=0
              while(yy1<len(starttime1)):
                  if starttime1[yy1]!="\t":
                      starttime1=starttime1[yy1:yy1+2]+starttime1[yy1+3:yy1+5]+starttime1[yy1+6:yy1+8]
                      break
                  else:
                      yy1=yy1+1
              
             
              start_time=starttime+starttime1
              start_time=int(start_time)
              #print start_time
              storeincident[i]=incident(IncidentNo,start_time)

              i=i+1
    j=0
    m=0
    
    #print time1
    while(j<i):
        cc=storeincident[j].start_time
        #print cc
        if cc>=time1 and cc<=time2:
            storeuseful[m]=storeincident[j]
            m=m+1
            j=j+1

        else:
            j=j+1
    k=0
    INCIDENT=range(m)
    while(k<m):
        INCIDENT[k]=storeuseful[k].IncidentNo
        k=k+1
    return INCIDENT
#incident_Matrix(20150201081309,20150201102009)


    

def usefulall(duration, moveupstation,homestation,Currentlocofunit,AvaiMatrix,INCIDENT):
     a=0
     b=0
     c=0
     if duration>Legitimate()[0] and duration<Legitimate()[1]:
        a=a+1
        n=len(INCIDENT)
        i=0
        while(i<n):
            local3=nearest(Currentlocofunit,AvaiMatrix,INCIDENT[i])[0]
##            if local3==0:
##                a=0
##                print"We can not have move up at this time, since none of units are ready to be sent."
##                break
##            else:
            print "-------Detail Data for Related Incident",INCIDENT[i],"--------------",'\n'
            print "moveupstation:",moveupstation,"INCIDENT:",INCIDENT[i],"Nearest Station with usable unit:",local3
            print "Dis(moveup station, Incident)", dist(moveupstation,INCIDENT[i])
            print "Dis(nearest avail unit, Incident):",dist(local3,INCIDENT[i]),'\n'
            
            
            
            
            if dist(moveupstation,INCIDENT[i])<=dist(local3,INCIDENT[i]):
                b=b+1
                if accu(moveupstation,homestation,INCIDENT[i])==1:
                    c=c+1
                    break
                else:
                    i=i+1     
            else:
                 i=i+1
     if a!=0:
         a=1
         if b!=0:
             b=1
             if c!=0:
                 c=1
             else:
                 c=0
         else:
             b=0
     else:
         a=0
     
     return (a,b,c)
#usefulall(durationtimetransfer(20150201081309,20150201102009),'SH06',"SH02",tofindcurrentlocation(),tofindAvaiMatrix(20150201081309),incident_Matrix(20150201081309,20150201102009))


def run(t,unitname,homestation,moveupstation):
    tt=findtime(t,unitname)
    print "moveup end time:",tt
    duration=durationtimetransfer(t,tt)
    print "moveup duration:",duration
    Currentlocofunit=tofindcurrentlocation(t)[1]
    AvaiMatrix=tofindAvaiMatrix(t)
    INCIDENT=incident_Matrix(t,tt)
    print "Current Matrix:",Currentlocofunit
    print "Available Matrix:",AvaiMatrix
    print "Related INCIDENT",INCIDENT,'\n'
    stat=usefulall(duration,moveupstation,homestation,Currentlocofunit,AvaiMatrix,INCIDENT)
    


    return stat
#run(20150201081309,'SH06',"SH02")
def allmoveups():

    n=tofindhomeandmoveuplocation()[0]
    move=tofindhomeandmoveuplocation()[1]
    #print n
    i=0
    count=[0,0,0]
    while(i<n):
        
        print "--------------------------------Moveup No.:",i,'-------------------------------------'
        t=move[i].time
        print "Moveup Start time:",t
        unitname=move[i].unitname
        print "Moveup Unit",move[i].unitname
        homestation=move[i].homestation
        print 'homestation:',homestation
        moveupstation=move[i].moveupstation
        print "moveupstation:",moveupstation
        #print t,s2location,s1location
        stat=run(t,unitname,homestation,moveupstation)
        count=[m+p for m,p in zip(count,stat)]
        print 'count:',count
        i=i+1
        
    print "-------------------------------This is Final Results----------------------------------------"
    print "Result:"
    print "The total amount of Move ups is:",n
    print "The total amount of Legitimate Move ups is : ", count[0]
    print "The total amount of Productive Move ups is : ",count[1]
    print "The total amount of Accurate Move ups is : ",count[2]
    return (count)

allmoveups()
    

