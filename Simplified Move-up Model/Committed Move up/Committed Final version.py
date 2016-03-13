import os
from os import listdir
from os.path import isfile,join
from Tkinter import *
import os.path
os.path.abspath('OutputDistances.txt')
path=os.path.abspath('')+'\\'

#initialize:
trackfolder=path
files=[f for f in listdir(trackfolder) if isfile(join(trackfolder,f))]

for thing in files:
    name=str(thing)
    if name=="OutputDistances.txt":
        f=open(name,'r')
        lineiter=f.readlines()
        ii=0
        for line in lineiter:
            ii=ii+1
        
    if name == "moveup list.txt":
        f=open(name,'r')
        lineiter=f.readlines()
        jj=0
        for line in lineiter:
            jj=jj+1

    if name =="service list.txt":
        f=open(name,'r')
        lineiter=f.readlines()
        pp=0
        for line in lineiter:
            pp=pp+1    

class station_incident_timecost:
    def __init__(self,stationname,incidentname,timecost):
        self.stationname=stationname
        self.incidentname=incidentname
        self.timecost=timecost
storetimecost=range(ii)

class moveuplist:
    def __init__(self,unitname,duration,moveupstarttime,moveupendtime,homestation,moveupstation):
        self.unitname=unitname
        self.duration=duration
        self.moveupstarttime=moveupstarttime
        self.moveupendtime=moveupendtime
        self.homestation=homestation
        self.moveupstation=moveupstation

storemoveuplist=range(jj)

class servicelist:
    def __init__(self,unitname,IncidentID,IncidentDate):
        self.unitname=unitname
        self.IncidentID=IncidentID
        self.IncidentDate=IncidentDate
storeservicelist=range(pp)

class duration_move_incident_home:
    def __init__(self,duration,moveupstation,IncidentID,homestation):
        self.duration=duration
        self.moveupstation=moveupstation
        self.IncidentID=IncidentID
        self.homestation=homestation
storerelationship=range(jj)
         
def dist(station,incident):
    trackfolder=path
    files=[f for f in listdir(trackfolder) if isfile(join(trackfolder,f))]
    i=0
    for thing in files:
        name=str(thing)
        if name=="OutputDistances.txt":
            f=open(name,'r')
            lineiter=f.readlines()
            for line in lineiter:
                stationname=line
                
                xx=0
                while(xx<len(line)):
                    if line[xx]==',':
                        stationname=stationname[:xx]
                        break
                    else:
                        xx=xx+1
                #print stationname
                
                    
                incidentname=line[xx+1:]
                yy=0
                while(yy<len(incidentname)):
                    if incidentname[yy]==",":
                        incidentname=incidentname[:yy]
                        break
                    else:
                        yy=yy+1
                #print incidentname

                timecost=line[xx+yy+2:-1]#'-1 here is to delete \n'
                timecost=float(timecost)

                storetimecost[i]=station_incident_timecost(stationname,incidentname,timecost)
                
                i=i+1
    k=0
    distan=0
    while(k<i):
        if storetimecost[k].stationname==station and storetimecost[k].incidentname==incident:
            distan=storetimecost[k].timecost
            break
        else:
            k=k+1
    return(distan)    
#dist('CARI','15-00169')

def classification(duration,moveupstation,inci,homestation,Targettime):

   
    #s1 is move-up location(2 by 1 matrix, coordinate)
    #inci is incident location(2 by 1 matrix,coordinate)
    #s2is original location where the move-up come from(2 by 1 matrix, coordinate

    if duration>10 and duration<600:
        #print("The move-up is a Legitimate Move-up.")
        NoLegi=1

        if inci!=0:
            #print("The move-up is a Productive Move-up.")
            Nopro=1
            ##The Incident occurred in the area covered by the Move-Up location
            

            if dist(homestation,inci)>=dist(moveupstation,inci):
                #print("The move-up is an Accurate Move-up. ")
                NoAcc=1
                
                if dist(moveupstation,inci)<=(Targettime):
                    #print("The response time is Less than desired time target.")
                    NoMeetTarget=1
                else:
                   #print ("The response time is More than desired time target")
                   NoMeetTarget=0
            else:
                #print("The move-up is an Inaccurate Move-up.")
                NoAcc=0
                NoMeetTarget=0
        else:
              #print("The move-up is a unproductive Move-up. ")
              Nopro=0
              NoAcc=0
              NoMeetTarget=0
        
    else:
          #print("The move-up is a Illegitimate Move-up ")
          NoLegi=0
          Nopro=0
          NoAcc=0
          NoMeetTarget=0
    return[NoLegi,Nopro,NoAcc,NoMeetTarget]
#classification(10,'SH04','15-16248','SH06',60,50)

def countnumber(A,Targettime):
    #A is a Matrix, every row of it includes all information about (duration,s1,inci,s2,r,Targettime,v)
    n=len(A)
    i=0
    count=[0,0,0,0]
    while i<n:
        a=A[i]
        x=a.duration
        y=a.moveupstation
        z=a.IncidentID
        k=a.homestation
        #print x,y,z,k,dist(y,z),dist(k,z)
       
        temp=classification(x,y,z,k,Targettime)
        count=[m+p for m,p in zip(count,temp)]
        i= i+1
    return (count)
    
#countnumber([[500,[0,1],[0,2],[0,5],2,3,1],[400,[0,7],[0,2],[0,1],1,1,1]])

def readfiles():
    trackfolder= path

    files=[f for f in listdir(trackfolder) if isfile(join(trackfolder,f))]
    for thing in files:
       name = str(thing)
   
       if name == "moveup list.txt":
          f = open(name, 'r')
          lineiter = f.readlines()

          i=0
          for line in lineiter:
              unitname=line
              xx=0
              while(xx<len(line)):
                  if line[xx]=="\t":
                      unitname=line[:xx]
                      break
                  else:
                      xx=xx+1

                      
              duration=line[xx:]
              yy1=0
              yy2=0
              while(yy1<len(duration)):
                  if duration[yy1]!="\t":
                      yy2=yy1+1
                      while(yy2<len(duration)):
                          if duration[yy2]=="\t":
                              #print duration[yy1:yy2]
                              duration=duration[yy1:yy2]
                              break
                          else:
                              yy2=yy2+1
                      break      
                  else:
                      yy1=yy1+1
              duration=int(duration[0:2])*60+int(duration[3:5])
              #print duration
              moveupstarttime=line[xx+yy2:]
              #print moveupstarttime
              zz1=0
              zz2=0
              while (zz1<len(moveupstarttime)):
                  if moveupstarttime[zz1]!='\t':
                      zz2=zz1+1
                      while (zz2<len(moveupstarttime)):
                          if moveupstarttime[zz2]=='\t':
                              moveupstarttime=moveupstarttime[zz1:zz2]
                              break
                          else:
                              zz2=zz2+1
                      break
                  else:
                      zz1=zz1+1
              moveupstarttime=int(moveupstarttime)
 
              homestation=line[xx+yy2+zz2:]
              aa1=0
              aa2=0
              while (aa1<len(homestation)):
                  if homestation[aa1]!='\t':
                      aa2=aa1+1
                      while(aa2<len(homestation)):
                          if homestation[aa2]=='\t':
                              homestation=homestation[aa1:aa2]
                              break
                          else:
                              aa2=aa2+1
                      break
                  else:
                      aa1=aa1+1
              #print homestation
              moveupendtime=line[xx+yy2+zz2+aa2:]
              #print moveupendtime
              bb1=0
              bb2=0
              while(bb1<len(moveupendtime)):
                  if moveupendtime[bb1]!='\t':
                      bb2=bb1+1
                      while(bb2<len(moveupendtime)):
                          if moveupendtime[bb2]=="\t":
                              moveupendtime=moveupendtime[bb1:bb2]
                              break
                          else:
                              bb2=bb2+1
                      break
                  else:
                      bb1=bb1+1
              moveupendtime=int(moveupendtime)
              moveupstation=line[xx+yy2+zz2+aa2+bb2:]
              cc1=0
              cc2=0
              while(cc1<len(moveupstation)):
                  if moveupstation[cc1]!='\t':
                      cc2=cc1+1
                      while (cc2<len(moveupstation)):
                          if moveupstation[cc2]=='\n':
                              moveupstation=moveupstation[cc1:cc2]
                              break
                          else:
                              cc2=cc2+1
                      break
                  else:
                      cc1=cc1+1
              #print moveupstation
              storemoveuplist[i]=moveuplist(unitname,duration,moveupstarttime,moveupendtime,homestation,moveupstation)
              #print storemoveuplist[i].unitname
              i=i+1
             
       if name == "service list.txt":
            f = open(name, 'r')
            lineiter = f.readlines()

            j=0
            for line in lineiter:
              unitname=line
              xx=0
              while(xx<len(line)):
                  if line[xx]=="\t":
                      unitname=line[:xx]
                      break
                  else:
                      xx=xx+1
              #print unitname

              IncidentID=line[xx:]
              yy1=0
              yy2=0
              while(yy1<len(IncidentID)):
                  if IncidentID[yy1]!="\t":
                      yy2=yy1+1
                      while(yy2<len(IncidentID)):
                          if IncidentID[yy2]=="\t":
                              IncidentID=IncidentID[yy1:yy2]
                              break
                          else:
                              yy2=yy2+1
                      break      
                  else:
                      yy1=yy1+1
              #print IncidentID

              IncidentDate=line[xx+yy2:]
              #print IncidentDate
              zz1=0
              while (zz1<len(IncidentDate)):
                  if IncidentDate[zz1]!='\t':
                      Incidentdate=IncidentDate[zz1:zz1+14]
                      break
                  else:
                      zz1=zz1+1
              IncidentDate=int(IncidentDate)
              storeservicelist[j]=servicelist(unitname,IncidentID,IncidentDate)
              #print storeservicelist[j].unitname
              j=j+1

      
    #print i,j
    k=0
    while(k<i):
            m=0
            IncidentID=0
            while(m<j):
                if storemoveuplist[k].unitname==storeservicelist[m].unitname:                   
                    if storemoveuplist[k].moveupstarttime<=storeservicelist[m].IncidentDate and storemoveuplist[k].moveupendtime>storeservicelist[m].IncidentDate:
                        IncidentID=storeservicelist[m].IncidentID
                        #print "from", storemoveuplist[k].moveupstarttime ,'to' ,storemoveuplist[k].moveupendtime
                        #print IncidentID
                        break
                    else:
                        m=m+1
                else:
                    m=m+1
            #print IncidentID
            storerelationship[k]=duration_move_incident_home(storemoveuplist[k].duration,storemoveuplist[k].moveupstation,IncidentID,storemoveuplist[k].homestation)
            #print storerelationship[k].duration
            k=k+1
        
    return storerelationship

def sta():
    #A is a Matrix, every row of it includes all information about (duration,s1,inci,s2,r,Targettime,v)
    A=readfiles()
    n=len(A)

    
    Targettime=float(p.get())
    
    result=countnumber(A,Targettime)
    Legitimate=float(result[0])/n
    Illegitimate=1-Legitimate
    if result[0]==0:
        Pro=0
    else:
        Pro=float(result[1])/result[0]
    Unpro=1-Pro
    if result[1]==0:
        Accurate=0
    else:
        Accurate=float(result[2])/result[1]
    Inaccurate=1-Accurate
    if result[2]==0:
        Less=0
    else:
        Less=float(result[3])/result[2]
    More=1-Less
    print("The total Move-up number is:")
    print n
    print("The number of Legitimate Move-up is:")
    print result[0]
    print("The number of Productive Move-up is:")
    print result[1]
    print("The number of Accurate Move-up is:")
    print result[2]
    print("The number of times that response time is less than the target is:")
    print result[3]
    print("The percentage of Legitimate out of all the move-ups:")
    print Legitimate
    print("The percentage of Productive out of all the move-ups:")
    print Pro
    print("The percentage of Accurate out of all the move-ups:")
    print Accurate
    print("The percentage of number of times that response time is less than the target is:")
    print Less
    
    return (Legitimate,Illegitimate,Pro,Unpro,Accurate,Inaccurate,Less, More) 
         
root = Tk()

# modify the window
root.title("Input Traval Radius and Target Time")
root.geometry("600x600")

p=StringVar()

#Create an Entry
L00=Label(root,text="Please Input Required Move-up Data Below:",fg='blue').grid(row=1,column=1)

targettime=Label(root,text="Target Time:",fg='blue').grid(row=3,column=1)
x01 = Entry(root, bd =10,textvariable=p).grid(row=3,column=11)


confirm=Button(root,text="OK",bd=5,command=sta).grid(row=20,column=11)

# Start the window's event-loop
root.mainloop()
