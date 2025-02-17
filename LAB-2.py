#=============================
'''
Name: Faishal Monir
ID: Null
Section: 09 
CSE-422 LAB-2
'''
#=============================

import random
inpt=open("input.txt","r")
otpt=open("output.txt","w")
x=inpt.readline().split(" ")
x[1]=x[1][0:1:]
n=int(x[0])
t=int(x[1])

population=[]
fitness={}

size=100 #int(input("Enter the population size You want to generate:"))

def pupulation_builder(n,t):
    f=""
    for i in range(size):
        for j in range(t):
            f+=str(random.randint(0,1))
        if len(f)==(n*t):
            population.append(f)
            f=""

pupulation_builder(n,t)


def mutate(ch):
    f=""
    for i in range(len(ch)):
        val=random.randint(0,5)
        if val%2==0:
            if ch[i]=="1":
                f+="0"
            else:
                f+="1"
        else:
            f+=ch[i]
    return f
                




def single_crossover(c1,c2):
    n1=""
    n2=""
    point=len(c1)//2
    n1=c1[0:point]+c2[point:]
    n2=c2[0:point]+c1[point:]
    population.append(n1)
    population.append(n2)
    
    return([n1,n2])

    
def double_crossover(c1,c2):
    n1=""
    n2=""
    p1=2
    p2=6 
    if p1>p2:
        p1,p2=p2,p1        
    n1=c1[0:(p1+1)]+c2[(p1+1):(p2+1)]+c1[(p2+1):]
    n2=c2[0:(p1+1)]+c1[(p1+1):(p2+1)]+c2[(p2+1):]
    return([n1,n2])
    
    
var1=random.sample(population, 2)
print(double_crossover(var1[0],var1[1]))

def fit(c1):
    temp=[]
    counter=0
    f=""
    score=0
    
    for i in c1:
        f+=i
        counter+=1
        if counter==t:
            temp.append(f)
            counter=0
            f=""
            
    consistent=[0]*t
    for i in temp:
        ovlp=i.count("1")
        score+=(ovlp-1)
        for j in range(0,len(i)):
            if i[j]=="1":
                consistent[j]+=1
    for i in consistent:
        score+=abs(i-1)
    fitness.update({c1:-score})
    return -score

        
# print(fit("110110010"))

def genetic(pplt):
    sample=33 #int(input("Enter The Genetic algo limit:"))
    if sample > len(pplt):
        print("Invalid parameter: The sample is larger than the population!!!")
        
    result=None
    for i in range(sample):
        node=random.sample(pplt, 2)
        cross=double_crossover(node[0],node[1])
        offspring=""
        for i in cross:
            offspring=mutate(i)
            
        if offspring not in fitness:
            temp=fit(offspring)
            fitness.update({offspring:temp})
            population.append(offspring)
            
            if temp==0:
                result=[offspring,temp]
        
    if result==None:
        return("No solution found")
    return result



genetic(population)

solution_space=[]
others=[]

for key,values in fitness.items():
    # otpt.write(key+" "+str(values)+"\n")
    if values==0:            
            solution_space.append(key+" "+str(values)+"\n")
    else:
        others.append(key+" "+str(values)+"\n")
        
otpt.write("Solutions (Chromosomes:Fitness):\n")
for i in solution_space:
    otpt.write(i)
otpt.write("\nOthers (Chromosomes:Fitness):\n")
for i in others:
    otpt.write(i)

inpt.close()
otpt.close()

    





    



