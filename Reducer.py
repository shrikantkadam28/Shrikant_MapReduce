#!/usr/bin/env python

import sys

# specify default values
foundKey = ""
foundValue = ""
isFirst = 1
currentTotalSale = 0
currentCustomerID = "-1"
currentState = "-1"
isCustMappingLine = False

# Define dictionay which will hold the transaction totals state wise

finaloutput = {}

# input comes from STDIN

for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    try:
        # parse the input we got from Mapper.py
        CustomerID, CustomerName, State, TotalSale = line.split('^')

        if currentCustomerID != CustomerID:
           currentCustomerID = CustomerID
           currentState = '%s - Unkown Customer State' % currentCustomerID

           currentKey = currentState

        if foundKey != currentKey:
                if isFirst == 0  :
            
                  if foundKey in finaloutput:
                      finaloutput[foundKey] += currentTotalSale
                  else:
                      finaloutput[foundKey] = currentTotalSale
                  currentTotalSale = 0  # reset the transation amount
                else:
                   isFirst = 0
                foundKey = currentKey

        currentKey=State
        foundKey = currentKey  # make the found key what we see so when we loop again can see if we increment or print out
        currentTotalSale = float(currentTotalSale) + float(TotalSale)  # add transactions

    except:
            pass
# for the last records in the loop

try:
    #print(State,currentTotalSale)
    if State in finaloutput:
        finaloutput[State] += currentTotalSale
    else:
        finaloutput[State] = currentTotalSale
except:
    pass

#Write the output of the dictionary to the file

fo = open("/Users/shrikantkadam/Desktop/INT/out_StateWise_States.csv", "w")
fo.write('State,TotalSales\n')

for state in finaloutput.keys():
    fo.write(state + ',' + str(finaloutput[state])+'\n')
 
  
