#=============================
'''
Name: Faishal Monir
ID: Null
Section: 09 
CSE-422 LAB-3
'''
#=============================

import math
graph={"A":["B","C"],"B":["D","E"],"C":["F","G"],"D":["H","I"],"E":["J","K"],"F":["L","M"],"G":["N","O"],"H":[1,1],"I":[-1,-1],"J":[1,-1],"K":[-1,1],"L":[1,-1],"M":[-1,1],"N":[1,1],"O":[-1,-1]}
otpt=open("output.txt","w")

round={}

def printer(game,starting_player,result):  
    f=f"\n======{game}======\n"
    if starting_player==0:
        f+="Game started with:Scorpion\n"
    else:
        f+="Game started with:Sub-Zero\n"

    if result==1:
        f+="Winner: Sub-zero\n\n"
    else:
        f+="Winner: Scorpion\n\n"
        
    for key,value in round.items():
        rnd=int(key)+1
        val=None
        status=value.pop(0)
        if status==True:
            val=max(value)
        else:
            val=min(value)          
        f+=f"winner of round {rnd}:"
        if val==1:
            f+="Sub-Zero\n"
        else:
            f+="Scorpion\n"
    f+="====================\n"
    # print(f)
    otpt.write(f)
    
#====================MINIMAX=======================

def minimax_game_engine(player,pos,depth):
    if player==0:
        player=False
    else:
        player=True
    
    if pos==1 or pos==-1 :
        return pos
        
    if player:
        score=-math.inf
        for i in graph[pos]:
            eval=minimax_game_engine(0,i,depth-1)
            score=max(score,eval)
            
            if str(depth) not in round:
                round[str(depth)]=[player,score]
            else:
                round[str(depth)].append(score)
        return score
        
    else:
        score=math.inf
        for i in graph[pos]:
            eval=minimax_game_engine(1,i,depth-1)
            score=min(score,eval)
            
            if str(depth) not in round:
                round[str(depth)]=[player,score]
            else:
                round[str(depth)].append(score)
            
        return score
    
starting_player=0
result=minimax_game_engine(starting_player,"A",3)
# print(round)
printer("Minimax",starting_player,result)


round={}       
#====================Alpha Beta Pruning================

def alpha_beta_game_engine(player,pos,depth,alpha,beta):
    if player==0:
        player=False
    else:
        player=True
    
    if pos==1 or pos==-1 :
        return pos
        
    if player:
        score=-math.inf
        for i in graph[pos]:
            eval=alpha_beta_game_engine(0,i,depth-1,alpha,beta)
            score=max(score,eval)
            alpha=max(alpha,score)
            if alpha>=beta:
                break            
            if str(depth) not in round:
                round[str(depth)]=[player,score]
            else:
                round[str(depth)].append(score)
        return score
        
    else:
        score=math.inf
        for i in graph[pos]:
            eval=alpha_beta_game_engine(1,i,depth-1,alpha,beta)
            score=min(score,eval)
            beta=min(beta,score)
            if alpha>=beta:
                break            
            if str(depth) not in round:
                round[str(depth)]=[player,score]
            else:
                round[str(depth)].append(score)
            
        return score
    
starting_player=0
result=alpha_beta_game_engine(starting_player,"A",3, -math.inf, math.inf)
# print(round)
printer("Alpha Beta",starting_player,result)

#===================Packman============================
otpt.write("\n===============PACKMAN================\n")
round={}
graph={"A":["B","C"],"B":["D","E"],"C":["F","G"],"D":[3,6],"E":[2,3],"F":[7,1],"G":[2,0]}



def alpha_beta_pacman(player,pos,depth,alpha,beta,test):
    if player==0:
        player=False
    else:
        player=True
        
    if type(pos)==int:
        return pos
    
    if player==1 and test==1:
        score=-math.inf
        for i in graph[pos]:
            eval=alpha_beta_pacman(1,i,depth-1,alpha,beta,test)
            score=max(score,eval)
            alpha=max(alpha,score)
            if alpha>=beta:
                break            
            if str(depth) not in round:
                round[str(depth)]=[player,score]
            else:
                round[str(depth)].append(score)
        return score
    
    elif player==1 and test==0:
        score=-math.inf
        for i in graph[pos]:
            eval=alpha_beta_pacman(0,i,depth-1,alpha,beta,test)
            score=max(score,eval)
            alpha=max(alpha,score)
            if alpha>=beta:
                break            
            if str(depth) not in round:
                round[str(depth)]=[player,score]
            else:
                round[str(depth)].append(score)
        return score
        
        
    else:
        score=math.inf
        for i in graph[pos]:
            eval=alpha_beta_pacman(1,i,depth-1,alpha,beta,test)
            score=min(score,eval)
            beta=min(beta,score)
            if alpha>=beta:
                break            
            if str(depth) not in round:
                round[str(depth)]=[player,score]
            else:
                round[str(depth)].append(score)
            
        return score


def pacman_game(flag):
    global round
    normal=alpha_beta_pacman(1,"A",2, -math.inf, math.inf,0)
    round={}
    dark_magic=alpha_beta_pacman(1,"A",2, -math.inf, math.inf,1)   
    dmagic_cost=dark_magic-flag
    
    f=""
    if normal>dmagic_cost:
        f=f"--> The Minimax Value is {normal}.\nPacman does not use dark magic\n\n"
    else:
        direction="left"
        dir_data=list(round.values())[-1]
        ans=max(dir_data)
        if ans==dir_data[2]:
            direction="right"

        f=f"--> The new minimax value is {dmagic_cost}.\nPacman goes {direction} and uses dark magic\n\n"
    otpt.write(f)
    
    

pacman_game(2)
pacman_game(5)