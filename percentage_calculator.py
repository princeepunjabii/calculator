print= input('PRESS ENTER KEY TO START FILLING THE APPLICATION FORM.')
print= input('TYPE THE DETAILS ASKED AND PRESS ENTER.')


clas= input("CLASS")
name1= input("NAME OF STUDENT")
roll_np= input('ROLL NUMBER')

english= input("Enter marks obtained in ENGLISH")
hindi= input("Enter marks obtained in HINDI")
maths= input("Enter marks obtained in MATHS")
science= input("Enter marks obtained in SCIENCE")
sst= input("Enter marks obtained in SOCIAL SCIENCE")
marks= int(english) + int(hindi) + int(maths) + int(science) + int(sst)
stu_percent= (marks/500)*100

print[name1,
      "obatined",
      marks,
      "in the CBSE EXAMINATION 2023.",
      "CLICK ENTER TO SEE PERCENTAGE OBTAINED"]
print[name1,
      "of class",
      clas,
      "has scored",
      stu_percent,
      "%",
      "in the CBSE EXAMINATION 2023.",
      "WE WISH YOU A BRIGHT FUTURE!"]

