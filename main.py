'''
Created on Jul 24, 2019

@author: leoou
'''
import math
import os.path
from os import path
import datetime

def pValue(df, chi):
    compGamma = 0; #complete gamma function
    botGamma = 0; #lower gamma function
    chi /= 2
    df /= 2
    i = 0
    step = .01
    while i < 9999:
        compGamma += pow(i,df-1)*pow(math.e,-i)*step
        if i < chi:
            botGamma = compGamma
        i += step
    return 1-botGamma/compGamma

def saveData(sides,chi,pvalue,rollData):
    fileNameBase = "d"+str(sides) + " test" #name of the file minus - .txt
    fileName = fileNameBase
    attempt = 0 #attempt number to make a file. Used in numbering the file
    while path.exists(fileName+".txt"): #attempt to make the file without overwriting an existing file
        attempt += 1
        fileName = fileNameBase + " - " + str(attempt)
    file = open(fileName + ".txt","w+") #create and write to the file
    file.write("D"+str(sides) + " Test\n")
    now = datetime.datetime.now()
    file.write("Created: %d/%d/%d\n" %( now.day, now.month, now.year))
    print(chi, pvalue)
    file.write("Chi-squared value: %f\n" %chi)
    file.write("P-value: %f\n" %pvalue)
    file.write("Actual data: \n")
    for i in range(len(rollData)):
        file.write("%d: %d\n" %(i+1,rollData[i]))
    print("Saved to ", fileName + ".txt")
    
sides = int(input("Welcome to dice tester! How many sides does your dice have?"))
rollData = [] #how much we rolled each number
for i in range(sides):
    rollData.append(0)
df = sides - 1 #degrees of freedom
rolls = 0 #the number of rolls
rolled = 0 #the number rolled

print("Roll the dice and type the roll here. For this dice, it is recommended to roll at least", 5*sides,"times")
typed = input("Roll the dice or type \"done\" to stop" ) #input
while typed != "done":
    try:
        rolled = int(typed)
    except TypeError:
        continue
    rollData[rolled-1] += 1
    rolls += 1
    typed = input("Roll the dice or type \"done\" to stop. Rolls: " + str(rolls) + "\n")
    
chi = 0
expected = rolls/sides
pvalue = 0
if expected != 0:
    for i in rollData:#calculate chi squared
        chi += pow(i-expected,2)/expected 
    pvalue = pValue(df,chi) #calculate p-value
print("Your chi-squared value is:", chi, "and your p-value is:", pvalue)
answer = input("Would you like to save this data in a txt file?").lower()
if answer == "y" or answer == "yes" or answer == "yeah":
    saveData(sides,chi,pvalue,rollData)
input("Press any enter to quit")

    


    
    
    
