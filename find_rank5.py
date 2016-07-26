import sys, subprocess

def write(string):
    fname = 'C:/Users/Harry/Documents/Algo/find_rank5.sikuli/output' + str(a) + str(b) + '.txt'
    with open(fname, 'w') as f:
        f.write(string)

            
def wait_hole():
    wait_region = Region(496,417,43,86)

    while True:
        if wait_region.exists(Pattern("1438195060501.png").similar(0.90)):
            return 'end from pre-flop'
        if check_region.exists("1437935359726.png"):
            pass
        else: 
            return 'null hole'


def wait_flop():
    while True:
        if check_region.exists(Pattern("1437931422173.png").similar(0.83)):
            
            if check_region.exists("1437935359726.png"):
                return 'end from flop'
            
        else:
            return 'null flop'



def wait_turn():
    while True:
        if check_region.exists(Pattern("1437342126033.png").similar(0.76)):
            
            if check_region.exists("1437935359726.png"):
                return 'end from turn'
            
        else:
            return  'null turn'

def wait_river():
    while True:
        if check_region.exists("1437935359726.png"):
            write('natural end')
            return 
        

def find_hole_rank():
    hole_num_rank = [0]*14
    hole_num_rank[13] = 1
    for i in range(a,b):
        try:
            rank_check_region.findAll(hole_rank[i])
            match = list(rank_check_region.getLastMatches())
            hole_num_rank[i] = len(match)
            write(str(hole_num_rank))
            hole_num_rank = [0]*14
            hole_num_rank[13] = 1
        except:
            pass
            

    





def find_flop_rank():
    num_flop_rank = [0]*14
    num_flop_rank[13] = 2
    for i in range(a,b):
        try:
            flop_region.findAll(rank[i])
            match = list(flop_region.getLastMatches())
            num_flop_rank[i] = len(match)
            write(str(num_flop_rank))
            num_flop_rank = [0]*14
            num_flop_rank[13] = 2
        except:
            pass

    



def find_turn_rank():
    num_turn_rank = [0]*14
    num_turn_rank[13] = 3
    for i in range(a,b):
        try:
            turn_region.find(rank[i])
            num_turn_rank[i] = 1
            write(str(num_turn_rank))
            break
        except:
            pass




def find_river_rank():
    num_river_rank = [0]*14
    num_river_rank[13] = 4
    for i in range(a,b):
        try:
            river_region.find(rank[i])
            num_river_rank[i] = 1
            write(str(num_river_rank))
            break
        except:
            pass
        
    




def find_rank():
    global check_region
    while True:
        while True:
            find_hole_rank()

            string1 = wait_hole()
            if 'end' in str(string1):
                write(str(string1))
                break
   
            find_flop_rank()
            

            string2 = wait_flop()
            if 'end' in str(string2):
                write(str(string2))
                break
            

            find_turn_rank()


            string3 = wait_turn()
            if 'end' in str(string3):
                write(str(string3))
                break
            
            find_river_rank()
            
            wait_river()
            



rank_check_region = Region(469,440,56,23)
check_region = Region(418,311,232,44)
flop_region = Region(427,287,118,31)


turn_region = Region(528,287,57,28) 
river_region = Region(566,287,61,27) 

rank = []

rank.append(Pattern("1438442613064.png").similar(0.80))#a
rank.append(Pattern("1438438259274.png").similar(0.80))#2
rank.append(Pattern("1438438176194.png").similar(0.80))#3
rank.append(Pattern("1438438162034.png").similar(0.80))#4
rank.append(Pattern("1438438273430.png").similar(0.95))#5
rank.append(Pattern("1438443428318.png").similar(0.95))#6
rank.append(Pattern("1438442630361.png").similar(0.80))#7
rank.append(Pattern("1438442714627.png").similar(0.80))#8
rank.append(Pattern("1438442650233.png").similar(0.80))#9 redo
rank.append(Pattern("1438442741422.png").similar(0.80))#10
rank.append(Pattern("1438438145646.png").similar(0.80))#j
rank.append(Pattern("1438438358530.png").similar(0.80)) #q  
rank.append(Pattern("1438438288201.png").similar(0.80))#k


hole_rank = []

hole_rank.append(Pattern("1438443577816.png").similar(0.80))
hole_rank.append(Pattern("1438443731280.png").similar(0.80))
hole_rank.append(Pattern("1438443661962.png").similar(0.80))
hole_rank.append(Pattern("1438443590308.png").similar(0.80))
hole_rank.append(Pattern("1438444002651.png").similar(0.80))
hole_rank.append(Pattern("1438444254136.png").similar(0.80))
hole_rank.append(Pattern("1438443993134.png").similar(0.80))
hole_rank.append(Pattern("1438443832299.png").similar(0.80))
hole_rank.append(Pattern("1438443842297.png").similar(0.80))
hole_rank.append(Pattern("1438444237585.png").similar(0.80))
hole_rank.append(Pattern("1438443682831.png").similar(0.80))
hole_rank.append(Pattern("1438444063578.png").similar(0.80))   
hole_rank.append(Pattern("1438443742151.png").similar(0.80))



a = int(raw_input())
b = int(raw_input())


find_rank()


