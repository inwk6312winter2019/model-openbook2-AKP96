
def dotuple():
    myfile = open("Street_Centrelines.csv","r")
    for f in myfile:
        f = f.split(",")
        string = (f[2],f[4],f[6],f[7])
        print(string) 

def mainhistogram():
    mydict = dict()
    myfile = open("Street_Centrelines.csv","r")
    for f in myfile:
        f = f.split(",")
        if f[12] not in mydict:
            mydict[f[12]] = 1
        else:
            mydict[f[12]] += 1
    print(mydict)
def list_owners():
    myfile = open("Street_Centrelines.csv","r")
    owners = []
    for f in myfile:
        f = f.split(",")
        f = f[11].strip()
        if f not in owners:
            owners.append(f)
    print(owners)
def get_street_class():
    stclass = []
    myfile = open("Street_Centrelines.csv","r")
    for f in myfile:
        f = f.split(",")
        f = f[10].strip()
        f = f.replace(" ","")
        if f not in stclass:
            if len(f) >= 1:
                stclass.append(f)
    return stclass


def streeclassnstreets():
    stclass = get_street_class()
    myfile = open("Street_Centrelines.csv","r")
    print(stclass)
    my_file = open("Street_Centrelines.csv","r")
    for st in stclass:
        print(".",st)
        for fm in my_file:
            fm = fm.split(",")
            fcm = fm[10].strip()
            fcm = fcm.lower()
            fcm = fcm.replace(" ","")
            print(fm[12])
do_tuple()
main_histogram()
list_owners()
streeclassnstreets()

