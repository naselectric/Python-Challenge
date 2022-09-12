import csv


path='./PyPoll/Resources/election_data.csv'

with open(path) as csvfile:
    poll = csv.reader(csvfile)
    next(poll)


    i=0
    Khan=0
    Li=0
    Correy=0
    OT=0
    Winner =0
    

    for line in poll:
        i=i+1
        a,b,c=(line)
        if c=='Khan':
            Khan=Khan+1
        elif c=='Correy':
                Correy=Correy+1
        elif c=='Li':
            Li=Li+1
        elif c=="O'Tooley": 
             OT=OT+1



if OT>Winner:
    Winner=OT
    Elect="O'Tooley"
if Li>Winner:
    Winner=Li
    Elect='Li'
if Correy>Winner:
    Winner=Correy
    Elect='Correy'
if Khan>Winner:
    Winner=Khan
    Elect='Khan'


    with open("./PyPoll/analysis/PollResults.txt", "w") as external_file:
        print('Election Results \n----------------------\nTotal Votes:',i,'\n----------------------',file=external_file)
        print('Khan:' '{:.3f}%'.format(Khan*100/i),'(',Khan,')','\nCorrey:''{:.3f}%'.format(Correy*100/i),'(',Correy,')',file=external_file)
        print('Li:' '{:.3f}%'.format(Li*100/i),'(',Li,')',"\nO'Tooley:"'{:.3f}%'.format(OT*100/i),'(',OT,')','\n----------------------',file=external_file)
        print('The Winner is:',Elect,'\n----------------------',file=external_file)
        external_file.close()





