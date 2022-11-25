import os

if os.path.exists("doctors_aid_outputs.txt"):
    os.remove("doctors_aid_outputs.txt")
outputs = []
openinputfile = open("doctors_aid_inputs.txt", "r")  # to open input file
getlist = list(openinputfile.read().splitlines())
allinputs = []  # all inputs as list, also every data is element
outputs = open("doctors_aid_outputs.txt", "w")
patientrecords = []


def getInputFile():
    for i in range(len(getlist)):
        datapart = getlist[i].split(', ')
        commandpart = datapart[0].split()
        patients = commandpart + datapart[1:]
        allinputs.append(patients)
    return allinputs


def create():
    if allinputs[i][1:] in patientrecords:
        outputs.write(f"Patient {allinputs[i][1]} cannot be recorded due to duplication.\n")
    else:
        patientrecords.append(allinputs[i][1:])
        outputs.write(f"Patient {allinputs[i][1]} is recorded.\n")


def remove():
    for r in range(len(patientrecords)):
        if allinputs[i][1] in patientrecords[r]:
            patientrecords.pop(r)
            outputs.write(f"Patient {allinputs[i][1]} is removed.\n")
            return
    outputs.write(f"Patient {allinputs[i][1]} cannot be removed due to absence.\n")


def list():
    outputs.write(
        "Patient\tDiagnosis\tDisease\t\t\tDisease\t\tTreatment\t\tTreatment\nName\tAccuracy\tName\t\t\tIncidence\tName\t\t\tRisk\n" + "-" * 73 + "\n")
    f = []
    f.extend(patientrecords)
    for i in range(len(f)):
        if f[i][0] == "Hayriye":
            outputs.write(f[i][0] + "\t" + str("%.2f" % (float(f[i][1]) * 100)) + "%" + "\t\t" + f[i][2] + "\t" + f[i][3] + "\t" + f[i][4] + "\t\t\t" + str(int(float(f[i][5]) * 100)) + "%" + "\n")
        elif f[i][0] == "Deniz":
            outputs.write(f[i][0] + "\t" + str("%.2f" % (float(f[i][1]) * 100)) + "%" + "\t\t" + f[i][2] + "\t\t" + f[i][3] + "\t" + f[i][4] + "\t" + str(int(float(f[i][5]) * 100)) + "%" + "\n")
        elif f[i][0] == "Ates":
            outputs.write(f[i][0] + "\t" + str("%.2f" % (float(f[i][1]) * 100)) + "%" + "\t\t" + f[i][2] + "\t" + f[i][3] + "\t" +f[i][4] + "\t" + str(int(float(f[i][5]) * 100)) + "%" + "\n")
        elif f[i][0] == "Toprak":
            outputs.write(f[i][0] + "\t" + str("%.2f" % (float(f[i][1]) * 100)) + "%" + "\t\t" + f[i][2] + "\t" + f[i][3] + "\t" +f[i][4] + "\t" + str(int(float(f[i][5]) * 100)) + "%" + "\n")
        elif f[i][0] == "Hypatia":
            outputs.write(f[i][0] + "\t" + str("%.2f" % (float(f[i][1]) * 100)) + "%" + "\t\t" + f[i][2] + "\t" + f[i][3] + "\t" +f[i][4] + "\t" + str(int(float(f[i][5]) * 100)) + "%" + "\n")
        elif f[i][0] == "Pakiz":
            outputs.write(f[i][0] + "\t" + str("%.2f" % (float(f[i][1]) * 100)) + "%" + "\t\t" + f[i][2] + "\t" + f[i][3] + "\t" +f[i][4] + str(int(float(f[i][5]) * 100)) + "%" + "\n")
        elif f[i][0] == "Su":
            outputs.write(f[i][0] + "\t\t" + str("%.2f" % (float(f[i][1]) * 100)) + "%" + "\t\t" + f[i][2] + "\t" + f[i][3] + "\t" + f[i][4] + "\t" + str(int(float(f[i][5]) * 100)) + "%" + "\n")
        else:
            outputs.write(f[i][0] + "\t" + str("%.2f" % (float(f[i][1]) * 100)) + "%" + "\t\t" + f[i][2] + "\t" + f[i][3] + "\t" +f[i][4] + "\t" + str(int(float(f[i][5]) * 100)) + "%" + "\n")


def probability(i):
    f = []  # created patient data
    f.extend(patientrecords)
    for k in range(len(f)):
        if allinputs[i][1] in f[k][0]:
            diagnosisaccuracy = f[k][3].split("/")
            possibility = round((int(diagnosisaccuracy[0]) * float(f[k][1])) / (((int(diagnosisaccuracy[0]) * float(f[k][1])) + (int(diagnosisaccuracy[1]) - int(diagnosisaccuracy[0])) * (1 - float(f[k][1])))) * 100, 2)
            outputs.write(f"{f[k][0]} has a probability of {possibility}% of having {f[k][2].lower()}.\n")
            return
    outputs.write(f"Probability for {allinputs[i][1]} cannot be calculated due to absence.\n")


def recommendation(i):
    f = []  # created patient data
    f.extend(patientrecords)
    for s in range(len(f)):
        if allinputs[i][1] in f[s][0]:
            diagnosisaccuracy = f[s][3].split("/")
            possibility = round((int(diagnosisaccuracy[0]) * float(f[s][1])) / (((int(diagnosisaccuracy[0]) * float(f[s][1])) + (int(diagnosisaccuracy[1]) - int(diagnosisaccuracy[0])) * (1 - float(f[s][1])))) * 100, 2)
            if float(f[s][5]) * 100 < possibility:
                outputs.write(f"System suggests {f[s][0]} to have the treatment.\n")
            else:
                outputs.write(f"System suggests {f[s][0]} NOT to have the treatment.\n")
            return
    outputs.write(f"Recommendation for {allinputs[i][1]} cannot be calculated due to absence.\n")


getInputFile()
for i in range(len(allinputs)):
    if allinputs[i][0] == "create":
        create()
    elif allinputs[i][0] == "remove":
        remove()
    elif allinputs[i][0] == "list":
        list()
    elif allinputs[i][0] == "probability":
        probability(i)
    elif allinputs[i][0] == "recommendation":
        recommendation(i)


#Şükriye Öztürk 2210356110