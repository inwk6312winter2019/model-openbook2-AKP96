def my_task():
    street = []
    nstreet = []
    reader1 = open('Street_Centrelines.csv', 'r')
    reader2 = open('Bus_Stops.csv', 'r')
    for rea in reader1:
        nrea = rea.split(",")
        if nrea[10] == "ARTERIAL":
            stee = nrea[4].strip()
            stee = stee.lower()
            if stee not in street:
                 street.append(stee)
    for j in street:
         if j not in nstreet:
             nstreet.append(j)
    
    metro = []
    for k in nstreet:
        for p in reader2:
            nder = p.split(",")
            if nder[7] == "Accessible":
                haystack = nder[6].strip()
                haystack = haystack.lower()
                if haystack.find(k) >= 0:
                     metro.append(nder[2])
		
    print("Stop Number    |    Location    |    FCODE")
    for bus in metro:
        for l in open('Bus_Stops.csv', 'r'):
            nre = l.split(",")
            if nre[2].find(bus) >= 0:
                print(nre[4],"",nre[6],"",nre[10])
    

my_task()

