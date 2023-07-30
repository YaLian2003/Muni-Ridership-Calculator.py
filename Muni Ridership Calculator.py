Yangyang Lian
07/08/2023
CS 10 Muni Ridership Calculator

#Calculating and returning the average
def calcavg(days,riders):
return riders/days
#welcome statement
print("Welcome to the Muni Ridership Calculator.")
#taking input parameters
print("Which Muni line did you survey?")
muniline=input()
print("How many days did you survey ridership?")
days=int(input())
print("How many riders did you count?")
riders=int(input())
# Function call to calculate average and rounding to two decimal place
res= round(calcavg(days,riders),2)
#print output
print("According to your survey, an average of", res ,"people rode the", muniline ,"per day.")
