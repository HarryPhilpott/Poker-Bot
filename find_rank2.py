import sys, subprocess

def wait_hole():
    wait_region = Region(496,417,43,86)

    while True:
        print 'gottlob'
        sys.stdout.flush()

        if wait_region.exists(Pattern("1438195060501.png").similar(0.90)):
            return 'end from pre-flop'
        if check_region.exists("1437935359726.png"):
            print 'waiting for flop'
            sys.stdout.flush()
        else: 
            return


def wait_flop():
    while True:
        if check_region.exists(Pattern("1437931422173.png").similar(0.83)):
            if check_region.exists("1437935359726.png"):
                return 'end from flop'
            else:
                print 'waiting for turn'
        else: break
    return 'gottlob'



def wait_turn():
    while True:
        if check_region.exists(Pattern("1437342126033.png").similar(0.76)):
            if check_region.exists("1437935359726.png"):
                return 'end from flop'
            else:
                print 'waiting for river'
        else: break
    return 'gottlob'



def find_hole_rank(a,b):

    hole_num_rank = [0]*14
    hole_num_rank[13] = 1
    for i in range(a,b):
        print 'gottlob'
        sys.stdout.flush()
        try:
            print 'gottlob'
            sys.stdout.flush()
            rank_check_region.findAll(hole_rank[i])
            match = list(rank_check_region.getLastMatches())
            hole_num_rank[i] = len(match)
            print 'gottlob'
            sys.stdout.flush()
        except:
            print 'gottlob'
            sys.stdout.flush()
            
        if sum(hole_num_rank[:14]) == 2:
            return hole_num_rank

    
    return hole_num_rank




def find_flop_rank(a,b):
    global check_region, flop_region
    num_flop_rank = [0]*14
    num_flop_rank[13] = 2
    for i in range(a,b):
        print 'gottlob'
        sys.stdout.flush()
        try:
            print 'gottlob'
            sys.stdout.flush()
            flop_region.findAll(rank[i])
            match = list(flop_region.getLastMatches())
            num_flop_rank[i] = len(match)
        except:
            print 'gottlob'
            sys.stdout.flush()

        if check_region.exists("1437935359726.png"):
            return 'end from flop'


    if check_region.exists("1437935359726.png"):
        return 'end from flop'
    else:
        return num_flop_rank




def find_turn_rank(a,b):
    global check_region, turn_region
    num_turn_rank = [0]*14
    num_turn_rank[13] = 3
    for i in range(a,b):
        match = 0
        print 'gottlob'
        sys.stdout.flush()
        if turn_region.exists(rank[i]):
            num_turn_rank[i] = 1
            print 'gottlob'
            sys.stdout.flush()
            return num_turn_rank


        if check_region.exists("1437935359726.png"):
            return 'end from turn'


    if check_region.exists("1437935359726.png"):
        return 'end from turn'
    else:
        return num_turn_rank



def find_river_rank(a,b):
    global check_region, river_region
    num_river_rank = [0]*14
    num_river_rank[13] = 4
    for i in range(a,b):
        print 'gottlob'
        sys.stdout.flush()
        if river_region.exists(rank[i]):
            num_river_rank[i] = 1
            print 'gottlob'
            sys.stdout.flush()
            return num_river_rank


        if check_region.exists("1437935359726.png"):
            return 'end from river'



    if check_region.exists("1437935359726.png"):
        return 'end from river'
    else:
        return num_river_rank




def find_rank(a,b):
    global check_region
    while True:
        while True:
            print 'gottlob'
            sys.stdout.flush()
            num_hole_rank = find_hole_rank(a,b)
            print num_hole_rank
            sys.stdout.flush()
            
            wait0 = wait_hole()
            if 'end' in str(wait0):
                print str(wait0)
                sys.stdout.flush()
                break
            
    
            num_comm_cards = find_flop_rank(a,b)
            if 'end' in str(num_comm_cards):
                print str(num_comm_cards)
                sys.stdout.flush()
                break
            
            print num_comm_cards
            sys.stdout.flush() 

            wait1 = wait_flop()
            if 'end' in wait1:
                print wait1
                sys.stdout.flush()
                break
            num_comm_cards = find_turn_rank(a,b)
            
            if 'end' in str(num_comm_cards):
                print str(num_comm_cards)
                sys.stdout.flush()
                break
            
            print num_comm_cards
            sys.stdout.flush()
            
            wait2 = wait_turn()
            if 'end' in wait2:
                print wait2
                sys.stdout.flush()
                break
            
            num_comm_cards = find_river_rank(a,b)
            
            if 'end' in str(num_comm_cards):
                print 'gottlob'
                sys.stdout.flush()
                print str(num_comm_cards)
                sys.stdout.flush()
                break
            
            print num_comm_cards
            sys.stdout.flush()
            
            while True:
                print 'gottlob'
                sys.stdout.flush()
                if check_region.exists("1437935359726.png"):
                    print 'natural end'
                    sys.stdout.flush()
                    break
                print 'gottlob'
                sys.stdout.flush()



rank_check_region = Region(469,440,39,25)
check_region = Region(418,311,232,44)
flop_region = Region(429,287,98,26)


turn_region = Region(549,285,18,26) 
river_region = Region(588,286,21,27) 

rank = []

rank.append(Pattern("1434129022901.png").similar(0.75))
rank.append(Pattern("1434129896249.png").similar(0.75))
rank.append(Pattern("1434130059538.png").similar(0.75))
rank.append(Pattern("1434129033215.png").similar(0.75))
rank.append(Pattern("1434129582566.png").similar(0.75))
rank.append(Pattern("1434129597672.png").similar(0.75))
rank.append(Pattern("1434129113292.png").similar(0.75))
rank.append(Pattern("1434129411318.png").similar(0.75))
rank.append(Pattern("1434129588792.png").similar(0.75))
rank.append(Pattern("1434129123291.png").similar(0.75))
rank.append(Pattern("1434129196462.png").similar(0.75))
rank.append(Pattern("1434129204463.png").similar(0.75))    
rank.append(Pattern("1434129225983.png").similar(0.75))


hole_rank = []

hole_rank.append(Pattern("1435693298558.png").similar(0.75))
hole_rank.append(Pattern("1435693335745.png").similar(0.75))
hole_rank.append(Pattern("1435693585803.png").similar(0.75))
hole_rank.append(Pattern("1435694138274.png").similar(0.75))
hole_rank.append(Pattern("1435693051867.png").similar(0.75))
hole_rank.append(Pattern("1435693211666.png").similar(0.75))
hole_rank.append(Pattern("1435694336179.png").similar(0.75))
hole_rank.append(Pattern("1435693460565.png").similar(0.75))
hole_rank.append(Pattern("1435693594837.png").similar(0.75))
hole_rank.append(Pattern("1435693103255.png").similar(0.75))
hole_rank.append(Pattern("1435694602344.png").similar(0.75))
hole_rank.append(Pattern("1435693885891.png").similar(0.75))   
hole_rank.append(Pattern("1435693518398.png").similar(0.75))



a = int(raw_input())
b = int(raw_input())


find_rank(a,b) 
