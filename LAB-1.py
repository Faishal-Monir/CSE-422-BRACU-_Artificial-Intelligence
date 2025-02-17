#=============================
'''
Name: Faishal Monir
ID: Null
Section: 09 
CSE-422 LAB-1
'''
#=============================

inpt=open("Input_file.txt","r")
otpt=open("output.txt","w")


def graph_maker(data):
    graph={}                  #{Node:[heuristic,(Neighbournode,cost),(Neighbournode,cost)],.....} Map structure
    a=data.read().split("\n")
    for i in a: 
        b=i.split(" ")
        if b[0] not in graph:
            graph.update({b[0]:[int(b[1])]})
             
            node=None
            cost=None
            for k in range(2,len(b)):
                if k%2==0:
                    node=b[k]
                else:
                    cost=int(b[k])
                    
                if node!=None and cost!=None:
                    graph[b[0]].append([node,cost])
                    node=None
                    cost=None
    return graph


path_nodes={}
 
def value_finder(map,val):
    for key,values in map.items():
        if val== key:
            return (key,values)  #('Arad', [366, ['Zerind', 75], ['Timisoara', 118], ['Sibiu', 140]])
        
        
def heuristic_finder(node_values,heuristics_map,path_cost_map):
    frm=node_values[0]
    to=node_values[1]
    actual_cost=path_cost_map[node_values[1]]
    heuristic_cost=None
    
    for i in heuristics_map:
        if i[0]==to:
            heuristic_cost=i[1]
            break
    actual_heuristic=actual_cost+heuristic_cost
    return (frm,to,actual_heuristic)
    

    
def path_cost_updater(ind_path,path_cost_map):
    frm=ind_path[0]
    to=ind_path[1]
    cost=ind_path[2]
    if to not in path_cost_map or path_cost_map[to] > path_cost_map[frm] + cost:
            path_cost_map[to] = path_cost_map[frm] + cost
            path_nodes.update({to:frm})
        
        
        

def a_star(inpt,strt,goal):
    map=graph_maker(inpt)   
    if strt not in map or goal not in map:
        return "No path Found"
    
    heuristics=[]     #[('Arad', 366), ('Craiova', 160), ('Eforie', 161), ('Fagaras', 176)........]
    
    for key in map.keys():
        a=value_finder(map,key)
        heuristics.append((key,a[1][0]))
        
        for i in range(1,len(a)):
            for j in range(1,len(a[i])):
                b=a[i][j]
                b.insert(0,key)

        
                 
    heap=[] #[('Arad', 'Arad', 366)]
    visited=[]
    actual_path_cost={}
    path_nodes.update({strt:"Parent"})
    heap.append((strt,strt,map[strt][0]))
    heap.sort(key=lambda x: x[2])
    
    while heap:
        current=heap.pop(0)

        
        if current[0]==current[1]:
            actual_path_cost.update({current[0]:0})  
                

            
        
        if current[1] not in visited:  
            visited.append(current[1])              
            for key,values in map.items():
                if key==current[1]:
                    for i in range(1,len(values)):
                        path_cost_updater(values[i],actual_path_cost)
                        a=heuristic_finder(values[i],heuristics,actual_path_cost)  #('Arad', 'Zerind', 449))
                        heap.append(a)
                    heap.sort(key=lambda x: x[2])
                    
    return(path_nodes,actual_path_cost)

     
    
start=input("Enter where to start From: ").capitalize()
goal=input("What is your Destination:").capitalize()

# start="Arad"
# goal=""

if start=="":
    print("Please Enter a Start Point")
    exit()  
    
if goal=="":
    goal="Bucharest"               
    
data=a_star(inpt,start,goal)
# print(data)


cost=data[1][goal]
temp=goal
path=[]
while True:
    if temp=="Parent":
        break
    path.insert(0,temp)
    temp=data[0][temp]
string="Path: "
for i in path:
    if i != path[-1]:
        string+=i+"->"
    else:
        string+=i
string+= f"\nTotal distance: {cost} km"
# print(string)
otpt.write(string)

otpt.close()
inpt.close()
    
    
    

    
    



    
