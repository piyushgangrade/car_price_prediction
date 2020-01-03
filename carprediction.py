import csv
import random
import math
#import pandas as pd
TrainingData = open('train.csv','r')
StructuredTrainingData = list(csv.reader(TrainingData))
#a=len(TrainingData.columns)

TestingData = open('test.csv','r')
StructuredTestingData = list(csv.reader(TestingData))

thetas = [0.25,0.25,0.25,0.25,0.25,0.25,0.25]
alpha = 0.00001

DataNeeded = []

for i in range(1,len(StructuredTrainingData)):
    BlankList = []
    BlankList.append(1)
    BlankList.append(float(StructuredTrainingData[i][0]))
    BlankList.append(float(StructuredTrainingData[i][1]))
    BlankList.append(float(StructuredTrainingData[i][2]))
    BlankList.append(float(StructuredTrainingData[i][3]))
    BlankList.append(float(StructuredTrainingData[i][4]))
    BlankList.append(float(StructuredTrainingData[i][5]))
    BlankList.append(float(StructuredTrainingData[i][6]))
    DataNeeded.append(BlankList)

for iternumber in range(0,1000):
    #lemda=10
    Dels = [0, 0, 0, 0, 0, 0, 0]
    CostFun = 0

    for SingleData in DataNeeded[0:]:
        for j in range(0,7):
            Dels[j] += (2*(thetas[0]*SingleData[0] + thetas[1]*SingleData[1] + thetas[2]*SingleData[2] +
                           thetas[3]*SingleData[3] + thetas[4]*SingleData[4] +thetas[5]*SingleData[5] +
                           thetas[6]*SingleData[6] - SingleData[7])*SingleData[j])

    for j in range(0,7):
        Dels[j] = Dels[j]/len(StructuredTrainingData)

    for j in range(0,7):
        thetas[j] = thetas[j] -alpha* Dels[j]

       # print('thetas are:'+str(thetas[j]))
    for SingleData in DataNeeded[0:len(StructuredTrainingData)]:
        CostFun += (math.pow((thetas[0]*SingleData[0]+ thetas[1]*SingleData[1] + thetas[2]*SingleData[2] +thetas[3]*SingleData[3] + 
                              thetas[4]*SingleData[4] + thetas[5]*SingleData[5] +thetas[6]*SingleData[6] -
                              SingleData[7]),2))

    CostFun = CostFun/len(StructuredTrainingData)

    print('The Cost Function value in iteration number '+str(iternumber)+" is "+str(CostFun))

#testing
DataTestNeeded=[]
for i in range(1,len(StructuredTestingData)):
    BlankList = []
    BlankList.append(1)
    BlankList.append(float(StructuredTestingData[i][0]))
    BlankList.append(float(StructuredTestingData[i][1]))
    BlankList.append(float(StructuredTestingData[i][2]))
    BlankList.append(float(StructuredTestingData[i][3]))
    BlankList.append(float(StructuredTestingData[i][4]))
    BlankList.append(float(StructuredTestingData[i][5]))
    
    DataTestNeeded.append(BlankList)

myresult=[]
for SingleData1 in DataTestNeeded[0:len(StructuredTestingData)]:
    NewPrice= (int)((thetas[0]*SingleData1[0] + thetas[1]*SingleData1[1] + thetas[2]*SingleData1[2]+
                thetas[3]*SingleData1[3] + thetas[4]*SingleData1[4]+thetas[5]*SingleData1[5]))
    
    print('The value of Cost  in iteration number ' + str(SingleData1) + " is " + str(NewPrice))
    myresult.append(NewPrice)
    
#print(myresult)

with open("\\Users\\user\\PycharmProjects\\carprediction.prediction.csv", "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    for val in myresult:
        writer.writerow([val])     
  
# Piyush Gangrade