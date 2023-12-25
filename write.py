LabReport=open("objective.txt","w")
# append(a) means add some txt end of the txt
# w override file.
LabReport.write("\n3.This is writing with write option")

LabReport=open("objective.txt","r")
print(LabReport.read())

LabReport.close()