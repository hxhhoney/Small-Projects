# Add your python script here

# coding: utf-8
import csv
import matplotlib.pyplot as pl
import numpy as np
#------------------------------Class identification----------------------------------------

class Event(object):
    
    def __init__(self,time,sender,recipient):
        self.time=time
        self.sender=sender
        self.recipient=recipient

class Record(object):
    def __init__(self,person,sent,received):
        self.person=person
        self.sent=sent
        self.received=received
   
            
#--------------------------------Data Package and Algorithm----------------------------------      

#Every line stands for an Event(see class Event)
#Use hashmap to store sent-and-received Record for every people(see class Record)
#I assume name is unique here.
#For hashmap, key is the name of people;the velue is Record.
#In every event, its sender let the cooresponding name's sent +1;
#In every event, its recipient has many persons, each person let cooresponding name's received+1

csvfile=file('enron-event-history-all.csv','rb')
reader=csv.reader(csvfile)

count=len(open(r"enron-event-history-all.csv",'rU').readlines())
event=range(count)
i=0
dict={}
for line in reader:
    event[i]=Event(line[0],line[2],line[3])
    if event[i].sender not in dict:
        dict[event[i].sender]=Record(event[i].sender,1,0)
    else:
        dict[event[i].sender].sent= dict[event[i].sender].sent +1
    
    for people in event[i].recipient.split('|'):
        if people not in dict:
            dict[people]=Record(people,0,1)
        else:
            dict[people].received=dict[people].received +1
    i=i+1
#--------------------------------Format and Output for Part 1----------------------------------
#Find out all Records, stored them in list record.
#sort record on sent in descending order.
#It should generate a csv_test.csv file under requirement
j=0
record=range(len(dict))
for key in dict.keys():
    record[j]=[dict[key].person,dict[key].sent,dict[key].received]
    j=j+1

record.sort(cmp=lambda x,y:cmp(y[1],x[1]))

outputfile=open('csv_test.csv','w')
writer=csv.writer(outputfile)
writer.writerows(record)
outputfile.close()
#-------------------------------Data Visualizing for Part 2-------------------------------------
#I use matplotlib to visulize the data,implement it in IDE first then we can run the programMultipleLocator.MAXTICKS=100000
event1=range(10)
event2=range(10)
event3=range(10)
num1=0
num2=0
num3=0
timeunit=(int(event[i-1].time)-int(event[0].time))/10
x=range(10)

k=0
while k<10:
    if k==0:
        x[k]=int(event[0].time)+timeunit
    else:
        x[k]=x[k-1]+timeunit
    k=k+1

csvfile=file('enron-event-history-all.csv','rb')
reader=csv.reader(csvfile)

k=0
for line in reader:
    if line[2]==record[0][0] and int(line[0])<=x[k]:
        num1=num1+1
    if line[2]==record[1][0] and int(line[0])<=x[k]:
        num2=num2+1
    if line[2]==record[2][0] and int(line[0])<=x[k]:
        num3=num3+1
    if(int(line[0])>x[k]):
        event1[k]=num1
        event2[k]=num2
        event3[k]=num3
        num1=0
        num2=0
        num3=0
        k=k+1


fig=pl.figure(figsize=(10,8))
y=event1
z=event2
w=event3

plot1=pl.plot(x,y,label='jeff dasovich',color='red')
plot2=pl.plot(x,z,label='sara shackleton',color='blue')
plot3=pl.plot(x,w,label='pete davis',color='black')


ax=pl.gca()


pl.ylim(0,np.max(y))
pl.xlim(int(event[0].time)+timeunit,np.max(x)+timeunit)

pl.subplots_adjust(bottom=0.15)

pl.grid()

pl.title('Number of sent email based on time')
pl.xlabel("Time(milisecond)")
pl.ylabel("Number of Sent")
pl.legend()


fig.autofmt_xdate()

pl.savefig('line.png')

#---------------------------Data Visualizing for Part 3----------------------------
csvfile=file('enron-event-history-all.csv','rb')
reader=csv.reader(csvfile)
dict.clear()
adict={}
bdict={}
cdict={}
contact1=range(10)
contact2=range(10)
contact3=range(10)
total=range(10)
num1=0
num2=0
num3=0
k=0
for line in reader:
    if line[2]==record[0][0] and int(line[0])<=x[k]:
        for people in line[3].split('|'):
            if people not in adict:
                adict[people]=1
                num1=num1+1
            if people==record[1][0] and people not in bdict:
                bdict[people]=1
                num2=num2+1
            if people==record[2][0] and people not in cdict:
                cdict[people]=1
                num3=num3+1
                
    if line[2]==record[1][0] and int(line[0])<=x[k]:
         for people in line[3].split('|'):
            if people not in bdict:
                bdict[people]=1
                num2=num2+1
            if people==record[0][0] and people not in adict:
                bdict[people]=1
                num1=num1+1
            if people==record[2][0] and people not in cdict:
                cdict[people]=1
                num3=num3+1
    if line[2]==record[2][0] and int(line[0])<=x[k]:
         for people in line[3].split('|'):
            if people not in cdict:
                cdict[people]=1
                num3=num3+1
            if people==record[0][0] and people not in adict:
                adict[people]=1
                num1=num1+1
            if people==record[1][0] and people not in bdict:
                bdict[people]=1
                num2=num2+1
    if(int(line[0])>x[k]):
        contact1[k]=num1
        contact2[k]=num2
        contact3[k]=num3
        num1=0
        num2=0
        num3=0
        k=k+1



ind=np.arange(10)
width=0.30
fig,ax=pl.subplots(figsize=(10,8))

rects1 = ax.bar(ind, contact1, width, color='r')
rects2 = ax.bar(ind+width, contact2, width, color='y')
rects3 = ax.bar(ind+width+width, contact3, width, color='b')
 
# add some
ax.set_ylabel('Unique Contacts')
ax.set_xlabel('Time(miliseconds)')
ax.set_title('Group-by-People Unique Contact Changing Graph ')
ax.set_xticks(ind+width)
ax.set_xticklabels( x )

ax.legend( (rects1[0], rects2[0],rects3[0]), ('jeff dasovich', 'sara shackleton','pete davis') )
 
def autolabel(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2., 1.05*height, '%d'%int(height),
                ha='center', va='bottom')
 
autolabel(rects1)
autolabel(rects2)
fig.autofmt_xdate()
 
pl.savefig('hist.png')









