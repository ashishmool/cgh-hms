import pickle
import csv
# dump
# dumps
# load
# loads

# f=open("students.txt","wb")
# dct={"1":"Ram","2":"Hari"}
# pickle.dump(dct,f)
# f.close()

# f=open("students.txt","rb")
# d=pickle.load(f)
# print(d)
# f.close()

# dict1={1:"abc",2:"Hari"}
# pickle_dict1=pickle.dumps(dict1)
# print (pickle_dict1)
# dec = pickle.loads(pickle_dict1)
# print(dec)

with open('abc.csv','w') as f:
    csv_reader = csv.writer(f, delimiter='-')
    for i in range(2):
        n=input("Enter Name:: ")
        a=input("Address:: ")
        csv_reader.writerow([n,a])
    print ("Stored Successfully")