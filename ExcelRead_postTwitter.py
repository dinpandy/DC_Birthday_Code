# import required packages 
import pandas as pd 
import datetime 
import time
from createapi import tweet_message

def make_ordinal(n):
    '''
    Convert an integer into its ordinal representation::

        make_ordinal(0)   => '0th'
        make_ordinal(3)   => '3rd'
        make_ordinal(122) => '122nd'
        make_ordinal(213) => '213th'
    '''
    n = int(n)
    suffix = ['th', 'st', 'nd', 'rd', 'th'][min(n % 10, 4)]
    if 11 <= (n % 100) <= 13:
        suffix = 'th'
    return str(n) + suffix

# driver code 
if __name__=="__main__": 
    dataframe = pd.read_excel("DC_Details.xlsx")
    today = datetime.datetime.now().strftime("%d-%m")
    #print("current date is",today)
    yearNow = datetime.datetime.now().strftime("%Y")
    #print("current Year is",yearNow)
    writeInd = []
    for index,item in dataframe.iterrows():
        name=str(item['Name'])
        twitterid = item['TwitterID']
        bday = item['DOB'].strftime("%d-%m")
        birthyear=item['DOB'].strftime("%Y")
        Age=int(yearNow)-int(birthyear)
        #print("birthyear is",birthyear)
        #print("birthday is",bday)
        Age1=make_ordinal(Age)
        msg = "Happy {} Birthday {} .. Many Many Happy Returns of the day".format(Age1 ,name)
        
        if (today == bday):
            print("Today is birthday for {} and his Age is {} and his ID is {}".format(name,Age,twitterid))
            print(msg)
            tweet_message(name,Age,twitterid)
            
            