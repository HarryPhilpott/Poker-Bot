import subprocess as sub
import sys


def str_list(string):
    char_list = list(string)
    int_list = []
    
    for i in char_list:
        try:
            int_list.append(int(i))
        except:
            pass

    return int_list


def read(fname):
    try:
        with open(fname, 'r') as f:
            string = f.readline()
        with open(fname, 'w') as f:
            f.write('')
        return str(string)
    except:
        print 'error opening file ', fname
        print string
    



def find_decision(position, card1, card2):
    
    if position < 1/3.0 and position > 0.0:
        with open('C:/Users/Harry/Documents/Algo/poker/early.txt', 'r') as f:
            lines = f.readlines()
            list1 = str_list(lines[card1])
        return list1[card2]

    if position >= 1/3.0 and position <= 1/6.0:
        with open('C:/Users/Harry/Documents/Algo/poker/middle.txt', 'r') as f:
            lines = f.readlines()
            list1 = str_list(lines[card1])
        return list1[card2]

    if position > 1/6.0 or position == 0.0:
        with open('C:/Users/Harry/Documents/Algo/poker/late.txt', 'r') as f:
            lines = f.readlines()
            list1 = str_list(lines[card1])
        return list1[card2]
        

def sum_list(*args):
    ret_list = []
    summ = 0
    for i in range(len(args[0][:])):
        for j in range(len(args[:][:])):
            summ += args[j][i]
        ret_list.append(summ)
        summ = 0

    return ret_list




def pre_flop_decision(suit_hole_list, hole_card_list, position):
    global suited
    suited = False
    print hole_card_list
    for i in range(4):
        if suit_hole_list[i] == 2:
            suited = True
            break
        else:
            suited = False
    click_region = Region(389,521,271,121)

    hole_card1 = 0
    hole_card2 = 0
    
    for i in range(13):
        if hole_card_list[i] == 2:
            hole_card1 = i
            hole_card2 = i
            break
        
        if hole_card_list[i] == 1 and hole_card1 == 0:
            hole_card1 = i

        if hole_card_list[i] == 1 and hole_card1 > 0:
            hole_card2 = i
            break

        
    decision1 = find_decision(position,hole_card1,hole_card2)
    
    if decision1 == 0:
        try:
            click_region.click("1438715739175.png")
        except:
        
            try:
                click_region.click("1438977375425.png")
            except:
                print 'error in finding check/fold'
        

    if decision1 == 1:
        try:
            click_region.click("1438715856500.png")
        except:
            print 'error in finding bet'

    if decision1 == 2:
        try:
            click_region.click("1438715914025.png")
        except:
            print 'error in finding call'

    if decision1 == 2.5 and suited == True:
        try:
            click_region.click("1438715914025.png")
        except:
           print 'error in finding call' 
        

def post_flop_decision(hole_card_list, comm_card_list, suit_comm_list, suit_hole_list):
    
    rating = hand_rating(hole_card_list, comm_card_list, suit_comm_list, suit_hole_list)
    
    if rating < 0.8:
        try:
            click_region.click("1438715739175.png")
        except:
        
            try:
                click_region.click("1438977375425.png")
            except:
                print 'error in finding check/fold'
    else:
        try:
            click_region.click("1441561385405.png")
            click_region.click("1441561481097.png")
        except:

            try:
                click_region.click("1438715914025.png")
            except:
                print "can't find all in"
        
        
        
def hand(hole_card_list, comm_card_list, suit_comm_list, suit_hole_list):
    result = 0
    pair_sum = 0
    pair_list = sum_list(hole_card_list, comm_card_list)
    pair = []       #This is too determine the rank of the pairs


    flush_list = sum_list(suit_comm_list, suit_hole_list)
    flush = False

    straight = False
    
    for i in range(13):
        if pair_list[i] == 2:
            pair_sum += pair_list[i]
            pair.append(i)

    for i in range(4):
        if flush_list[i] == 5:
            flush = True                #flush
            result = 5

    for i in range(9):
        if sum(pair_list[i:i+5]) == 5:
            kicker = (i+5)*0.01         #straight
            straight = True
            result = 4 + kicker

            

    if pair_sum == 2:       #pair
        kicker = pair_kicker(pair_list, pair[0])
        result = 1 + kicker*0.01
        return result

    

    if pair_sum == 4 and len(pair) == 2:        #two pair
        if pair[1] > pair [0]:
            kicker = (pair[1] + 1)*0.01 + (pair[0] + 1)*0.0001
        else:
            kicker = (pair[0] + 1)*0.01 + (pair[1] + 1)*0.0001
            
        kicker1 = two_pair_kicker(pair_list, pair[0], pair[1])
        
        result = 2 + kicker + kicker1*0.0000001
        return result

    

    if pair_sum == 3 and len(pair) == 1:        #three of a kind
        kicker = pair_kicker(pair_list, pair[0])
        result = 3 + kicker*0.01
        return result


    

    if pair_sum == 5 and len(pair) == 2:        #full house
        if pair[1] > pair [0]:
            kicker = (pair[1] + 1)*0.01 + (pair[0] + 1)*0.0001
        else:
            kicker = (pair[0] + 1)*0.01 + (pair[1] + 1)*0.0001
            
        result = 6 + kicker
        return result


    

    if pair_sum == 4 and len(pair) == 1:        #quad
        kicker = pair_kicker(pair_list, pair[0])
        result = 7 + kicker*0.01
        return result

    if straight == True and flush == True:      #straight flush
        result = 8 + kicker
        return result

    return result    




def pair_kicker(list1, pair):
    kicker = 0
    for i in range(13):
        if list1[i] > 0 and i != pair:
            kicker = i + 1
    return kicker



def two_pair_kicker(list1, pair1, pair2):
    kicker = 0
    for i in range(13):
        if list1[i] > 0 and i != pair1 and i != pair2:
            kicker = i + 1

    return kicker


            

def hand_rating(hole_card_list, comm_card_list, suit_comm_list, suit_hole_list):
    num_better_hands = 0
    my_result = hand(hole_card_list, comm_card_list, suit_comm_list, suit_hole_list)
    hole_card_list = [0]*13
    suit_hole_list = [0]*4
    summ = 0
    for i in range(52):
        for j in range(i+1, 52):
            hole_card_list[i%13] += 1           #need to prevent overcounting
            hole_card_list[j%13] += 1
            suit_hole_list[i/13] += 1
            suit_hole_list[j/13] += 1


            opponent_result = hand(hole_card_list, comm_card_list, suit_comm_list, suit_hole_list)

                     
            if opponent_result > my_result:
                num_better_hands += 1

                
            hole_card_list = [0]*13
            suit_hole_list = [0]*4


    return 1 - num_better_hands/1326.0      #there are 1326 possible hands

    

    



process = sub.Popen('C:/python27/python.exe C:/Users/Harry/Documents/Algo/poker/basic_interact_test8.py')
#process = sub.Popen('C:/Sikuli/runIDE.cmd -r C:/Users/Harry/Documents/Algo/find_suit3.sikuli')
#process2 = sub.Popen('C:/Sikuli/runIDE.cmd -r C:/Users/Harry/Documents/Algo/find_position.sikuli')

files = [0,1]
files[0] = 'C:/Users/Harry/Documents/Algo/poker/totaloutput.txt'
files[1] = 'C:/Users/Harry/Documents/Algo/find_suit3.sikuli/output.txt'

i = 0
position = 0
hole_card_list = [0]*13
comm_card_list = [0]*13
suit_comm_list = [0]*4
suit_hole_list = [0]*4
suited = False

while True:
    while True:
        string = read(files[i%2])
        i += 1


        if 'end' in string:
            print 'end ', string 
            hole_card_list = [0]*13
            comm_card_list = [0]*13
            suit_comm_list = [0]*4
            suit_hole_list = [0]*4
            position = (position + 1)%9
            break

        b_list = str_list(string)
        length = len(b_list)

        if length == 1:
            position = int(string)

        
        if length == 14:
            if b_list[13] == 1:
                hole_card_list = b_list[:13]
                pre_flop_decision(suit_hole_list, hole_card_list, position)
            else:
                comm_card_list = b_list[:13]
                sum_comm_card_list = sum(comm_card_list)
                
                if sum_comm_card_list > 2:
                    post_flop_decision(hole_card_list, comm_card_list, suit_comm_list, suit_hole_list)


        if length == 5:
            if b_list[4] == 6:
                suit_hole_list = b_list[:4]
                pre_flop_decision(suit_hole_list, hole_card_list, position)
            else:
                suit_comm_list = b_list[:4]
                sum_suit_comm_list = sum(suit_comm_list)
                
                if sum_comm_card_list > 2:
                    post_flop_decision(hole_card_list, comm_card_list, suit_comm_list, suit_hole_list)

        

#C:/Sikuli/runIDE.cmd -r C:/Users/Harry/Documents/Algo/make_bet3.sikuli






                
