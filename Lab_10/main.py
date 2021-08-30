print("///////////ZAD1////////////")
from datetime import date

def check_peselNumber(Pesel,dateOfBirth,gender):
  try:
    if Pesel[:2] != str(dateOfBirth.year)[2:4]:
      raise ValueError("Year in pesel is not correct!") 
    temp = 0 
    if 1800 <= dateOfBirth.year < 1900:
      temp+=80
    elif 2000 <= dateOfBirth.year < 2100:
      temp+=20
    elif 2100 <= dateOfBirth.year < 2200:
      temp+=40
    elif 2200 <= dateOfBirth.year < 2300:
      temp+=60
    if int(Pesel[2:4]) != dateOfBirth.month+temp:
      raise ValueError("Month in pesel is not correct!") 
    if int(Pesel[4:6]) != dateOfBirth.day:
      raise ValueError("Day in pesel is not correct!") 
    if gender=="kobieta":
      if int(Pesel[6:10]) % 2:
        raise ValueError("Gender in pesel is not correct!")  
    elif gender=="mężczyzna":
      if not int(Pesel[6:10]) % 2:
        raise ValueError("Gender in pesel is not correct!")  
    weight = [1,3,7,9,1,3,7,9,1,3]
    for i in range(10):
      weight[i]*=int(Pesel[i])
    check_11 = sum(weight) % 10
    check_11 = 10 - check_11
    if check_11 % 10 != int(Pesel[10]):
      raise ValueError("Weight in pesel is not correct!")  
    print("Pesel ",Pesel," Is Correct!")
  except ValueError as error:
    print(error)

check_peselNumber("0271803628",date(1902,7,8),"kobieta")
check_peselNumber("02270803624",date(2002,7,8),"kobieta")
check_peselNumber("02270812350",date(2002,7,8),"mężczyzna")

print("///////////ZAD2////////////")

def averageAge(strFile,mode="r"):
  try:
    with open(strFile,"r") as file:
      daysInMonth=[31,28,31,30,31,30,31,31,30,31,30,31]
      sumYears=0
      numOfYears=0
      for line in file.readlines():
        try:
          line=line.split()
          if len(line) != 3:
            raise ValueError("Wrong amount of ingredients!")
          line = [int(i)for i in line]
          if line[1]>12 or 0>=line[1]:
            raise ValueError("Wrong MONTH!")
          elif line[1]!=2:
            if line[0]!=daysInMonth[line[1]-1]:
              raise ValueError("Wrong Number of Days in Month!")
          elif line[2]%4==0 and (line[2]%100!=0 or line[2]%400==0):
            if line[0]!=29:
              raise ValueError("Wrong Number of Days in February(Leap year)!")
          elif line[0]!=28:
            raise ValueError("Wrong Number of Days in February!")     
          sumYears=sumYears+line[2]
          numOfYears=numOfYears+1
        except ValueError as err:
          if mode is "r":
            raise Exception(err)
      print("Average year of inputy is: ",sumYears/numOfYears)    
  except IOError:
    if mode is "r":
      raise Exception("Cannnot open file!")
    else:
      print("Cannnot open file!")
averageAge("daty.in","l")

