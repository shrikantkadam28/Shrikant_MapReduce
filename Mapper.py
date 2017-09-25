#!/usr/bin/env python
 
import sys
 
# input comes from STDIN (standard input)
for line in sys.stdin:
    try: #to deal with bad data
         
        CustomerID = "-1" #default sorted as first
        CustomerName= "-1"
        State = "-1"  # default sorted as first
        SalesPrice = "0"  # default sorted as first
         
        # remove leading and trailing whitespace
        line = line.strip()
         
        splits = line.split(",")
         
        if len(splits) == 6: #Customer_Data
            CustomerID = splits[0]
            CustomerName = splits[1]
            State = splits[4]
        else: #Tansaction Data
            CustomerID = splits[1]
            SalesPrice = splits[2]

        PrintRow='%s^%s^%s^%s' % (CustomerID, CustomerName ,State, SalesPrice)
        print (PrintRow)


    except: #errors are going to make your job fail which you may or may not want
        pass