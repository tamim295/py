Lab_Report =open("objective.txt","r")

for lab in Lab_Report.readlines():
    print(lab)
#print(Lab_Report.readlines()[0])
#print(Lab_Report.readline())
Lab_Report.close()