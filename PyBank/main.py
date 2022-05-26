import os

import csv

path='C:/Users/MOHAMMED/Python-Challenge/PyBank/Resources/budget_data.csv'
#path='C:/Users/MOHAMMED/hw3_1_test.csv'
#path = os.path.join('..','Users','MOHAMMED','Python-Challenge','PyBank','Resources','budget_data.csv')

with open(path) as csvfile:
    budget = csv.reader(csvfile)
    next(budget)

    i=0
    profit =0
    x2=867884
    x3=0
    x4=0
    x5=0
    x6=100000

    for line in budget:
        i=i+1
        a,b=(line)
        n=int(b)
        
        profit= profit + n
        change = n - x2
        change2= n - x6
        
        if change2 > x4:
            profit1=change2
            date1=a
            x4 = change2
        if change2 < x5:
            profit0=change2
            date0=a
            x5 = change2
        
        x2=n
        x6=n
        x3=x3+change
        
        
        
average = (x3)/(i-1)


with open("C:/Users/MOHAMMED/Python-Challenge/PyBank/analysis/BankResults.txt", "w") as external_file:
    print('Financial Analysis\n------------------\nTotal Months:',i,file=external_file)
    print('Total:',"${:.2f}".format(profit),file=external_file)
    print('Average Change:',"${:,.2f}".format(average),file=external_file)
    print('Greatest Increase in Profits:',date1, ':',"${:,.2f}".format(profit1),file=external_file)
    print('Greatest Decrease in Profits:',date0, ':',"${:,.2f}".format(profit0),file=external_file)
    external_file.close()
        