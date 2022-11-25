outputs = []
openinputfile = open("doctors_aid_inputs.txt", "r")  # to open input file
getlist = list(openinputfile.read().splitlines())  # to get datas as a list
allinputs = []  # all inputs as list, also every data is element
def getInputFile():
    for i in range(len(getlist)):
        datapart = getlist[i].split(', ')
        commandpart = datapart[0].split()
        patients = commandpart + datapart[1:]
        allinputs.append(patients)

    datas = []  # the list of datas which does not contain patients names
    patients = []  # the list of patient names
    functions = []  # the cluster of functions in case of necessity
    patientrecords = []
    for i in range(len(allinputs)):
        functions.append(allinputs[i][0])
        if int(len(allinputs[i])) > 2:
            patients.append(allinputs[i][1])
            datas.append(allinputs[i][1:])
    diagnosisaccuracy = []  # i've created this list to write diagnosis accurancy as a float, also use them in probabality command
    for i in range(len(datas)):
        diagnosisaccuracy.append(datas[i][1])
        diagnosisaccuracy = [float(i) for i in diagnosisaccuracy]
    diagnosisaccuracy = [i * 100 for i in diagnosisaccuracy]
    treatmentrisk = []  # i've created this list to write treatment risk as a float, also to use them in recommadation command
    for i in range(len(datas)):
        treatmentrisk.append(datas[i][5])
        treatmentrisk = [float(i) for i in treatmentrisk]
        treatmentrisk = [round(i, 2) for i in treatmentrisk]
    treatmentrisk = [i * 100 for i in treatmentrisk]
    treatmentrisk = [int(i) for i in treatmentrisk]
    diseaseincidence = []
    incidence = []
    for i in range(len(datas)):
        diseaseincidence.append(datas[i][3])
        numeratorpart = [diseaseincidence[i][0:2].split("/") for i in range(len(diseaseincidence))]
        numeratorpart = [item for sublist in numeratorpart for item in sublist]
        numeratorpart = [int(i) for i in numeratorpart]
        denominatorpart = [diseaseincidence[i][3:] for i in range(len(diseaseincidence))]
        denominatorpart = [int(i) for i in denominatorpart]
def create():
    if allinputs[i] in patientrecords:
        outputs.write("Patient", allinputs[i][1], "cannot be recorded due to duplication.")
    else:
        patientrecords.append(allinputs[i][1:])
        outputs.write("Patient", allinputs[i][1], "is recorded.")
def remove():
    for r in range(len(patientrecords)):
        if allinputs[i][1] in patientrecords[r]:
            patientrecords.pop(r)
            outputs.write("Patient", allinputs[i][1], "is removed.")
            return
    outputs.write("Patient", allinputs[i][1], "cannot be removed due to absence.")

def list():
    outputs.write("Patient\tDiagnosis\tDisease\t\t\tDisease\t\tTreatment\t\tTreatment\nName\tAccuracy\tName\t\t\tIncidence\tName\t\t\tRisk\n" + "-" * 73)
    for i in patients[0:]:
        f = datas
        l = treatmentrisk
        k = diagnosisaccuracy
        if i == patients[0]:
            outputs.write(f[0][0] + "\t" + str("%.2f" % k[0]) + "%" + "\t\t" + f[0][2] + "\t" + f[0][3] + "\t" + f[0][4] + "\t\t\t" + str(l[0]) + "%")
        elif i == patients[1]:
            outputs.write(f[1][0] + "\t" + str(k[1]) + "%" + "\t\t" + f[1][2] + "\t\t" + f[1][3] + "\t" + f[1][4] + "\t" + str(l[1]) + "%")
        elif i == patients[2]:
            outputs.write(f[2][0] + "\t" + str("%.2f" % k[2]) + "%" + "\t\t" + f[2][2] + "\t" + f[2][3] + "\t" + f[2][4] + "\t" + str(l[2]) + "%")
        elif i == patients[3]:
            outputs.write(f[3][0] + "\t" + str("%.2f" % k[3]) + "%" + "\t\t" + f[3][2] + "\t" + f[3][3] + "\t" + f[3][4] + "\t" + str(l[3]) + "%")
        elif i == patients[4]:
            outputs.write(f[4][0] + "\t" + str(k[4]) + "%" + "\t\t" + f[4][2] + "\t" + f[4][3] + "\t" + f[4][4] + "\t" + str(l[4]) + "%")
        elif i == patients[5]:
            outputs.write(f[5][0] + "\t" + str(k[5]) + "%" + "\t\t" + f[5][2] + "\t" + f[5][3] + "\t" + f[5][4] + str(l[5]) + "%")
        else:
            outputs.write(f[6][0] + "\t\t" + str("%.2f" % k[6]) + "%" + "\t\t" + f[6][2] + "\t" + f[6][3] + "\t" + f[6][4] + "\t" + str(l[6]) + "%")
def probability():
    global possibility
    for i in range(len(allinputs)):
        if "probability" in allinputs:
            possibility = round(((numeratorpart[i] * diagnosisaccuracy[i] / 100 / (((denominatorpart[i] - numeratorpart[i] *diagnosisaccuracy[i] / 100) * (1 - diagnosisaccuracy[i] / 100)) + numeratorpart[i] *diagnosisaccuracy[i] / 100)) * 100), 2)
            if possibility != 0:
                outputs.write(patients[i], "has a probability of", possibility, "%", "of having breast cancer.")
            else:
                outputs.write("Probability for", patients[i], "cannot be calculated due to absence.")
def recommendation():
    global possibility
    for i in range(len(datas)):
        if treatmentrisk[i] != 0:
            if treatmentrisk[i] < possibility:
                outputs.write("System suggests", patient[i], "to have the treatment.")
            else:
                outputs.write("System suggests", patient[i], "NOT to have the treatment.")
        else:
            outputs.write("Recommendation for", patient[i], "cannot be calculated due to absence.")
def getOutputFile():
    outputs.write("doctors_aid_outputs.txt", "r+")
print(getOutputFile)
for i in range(len(allinputs)):
    getInputFile()
    if functions == "create":
        create()
    elif functions == "remove":
        remove()
    elif functions == "list":
        list()
    elif functions == "probability":
        probability()
    elif functions == "recommendation":
        recommendation()
