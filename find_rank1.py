import sys, subprocess


def find_hole_rank(a,b):
    rank_check_region = Region(456,455,80,44)
    num_rank = [0]*14
    num_rank[13] = 6
    for i in range(a,b):
        print 'gottlob'
        sys.stdout.flush()
        try:
            rank_check_region.findAll(hole_rank[i])
            match = list(rank_check_region.getLastMatches())
            num_rank[i] = len(match)
        except:
            print 'gottlob'
            sys.stdout.flush()
            
    return num_rank

def find_comm_rank(a,b):
    check_region = Region(424,312,187,27)
    num_rank = [0]*14
    num_rank[13] = 5
    for i in range(a,b):
        print 'gottlob'
        sys.stdout.flush()
        if exists("1435763469443.png"):
            num_rank = [0]*14
            num_rank[13] = 5
            return 'end'
        try:
            check_region.findAll(rank[i])
            match = list(check_region.getLastMatches())
            num_rank[i] = len(match)
        except:
            print 'gottlob'
            sys.stdout.flush()
            
    return num_rank

def find_rank(a,b):
    check_region = Region(420,282,241,69)
    while True:
        print 'gottlob'
        sys.stdout.flush()
        if check_region.exists("1435763469443.png"):
            num_hole_cards = find_hole_rank(a,b)
            print num_hole_cards
            sys.stdout.flush()
        else:
            no_repeat = False
            num_comm_cards = find_comm_rank(a,b)
            print num_comm_cards
            sys.stdout.flush()


        
        
                

rank_name = []

rank_name.append('ace')
rank_name.append('2')
rank_name.append('3')
rank_name.append('4')
rank_name.append('5')
rank_name.append('6')
rank_name.append('7')
rank_name.append('8')
rank_name.append('9')
rank_name.append('10')
rank_name.append('Jack')
rank_name.append('Queen')
rank_name.append('King')

rank = []

rank.append(Pattern("1434129022901.png").similar(0.90))
rank.append(Pattern("1434129896249.png").similar(0.90))
rank.append(Pattern("1434130059538.png").similar(0.90))
rank.append(Pattern("1434129033215.png").similar(0.90))
rank.append(Pattern("1434129582566.png").similar(0.90))
rank.append(Pattern("1434129597672.png").similar(0.90))
rank.append(Pattern("1434129113292.png").similar(0.90))
rank.append(Pattern("1434129411318.png").similar(0.90))
rank.append(Pattern("1434129588792.png").similar(0.90))
rank.append(Pattern("1434129123291.png").similar(0.90))
rank.append(Pattern("1434129196462.png").similar(0.90))
rank.append(Pattern("1434129204463.png").similar(0.90))    
rank.append(Pattern("1434129225983.png").similar(0.90))


hole_rank = []

hole_rank.append(Pattern("1435693298558.png").similar(0.90))
hole_rank.append(Pattern("1435693335745.png").similar(0.90))
hole_rank.append(Pattern("1435693585803.png").similar(0.90))
hole_rank.append(Pattern("1435694138274.png").similar(0.90))
hole_rank.append(Pattern("1435693051867.png").similar(0.90))
hole_rank.append(Pattern("1435693211666.png").similar(0.90))
hole_rank.append(Pattern("1435694336179.png").similar(0.90))
hole_rank.append(Pattern("1435693460565.png").similar(0.90))
hole_rank.append(Pattern("1435693594837.png").similar(0.90))
hole_rank.append(Pattern("1435693103255.png").similar(0.90))
hole_rank.append(Pattern("1435694602344.png").similar(0.90))
hole_rank.append(Pattern("1435693885891.png").similar(0.90))   
hole_rank.append(Pattern("1435693518398.png").similar(0.90))



a = int(raw_input())
b = int(raw_input())


    



find_rank(a,b) 
    
