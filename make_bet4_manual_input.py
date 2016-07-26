import subprocess as sub
import sys
import hand
import stringlist as s
import sumlist as su



def read(fname):
    try:
        with open(fname, 'r') as f:
            string = f.readline()

        length = len(list(string))
    except:
        print 'error in opening file'

    if length > 0:

        try:
            with open(fname, 'w') as f:
                f.write('')
        
        except:
            print 'error closing file '
            print string
            return 'gottlob'
    
    return str(string)


def find_decision(position, card1, card2):

    
    if position < 1/3.0 and position > 0.0:
        with open('C:/Users/Harry/Documents/Algo/poker/early.txt', 'r') as f:
            lines = f.readlines()
            list1 = s.str_list(lines[card1])
        return list1[card2]

    if position >= 1/3.0 and position <= 1/6.0:
        with open('C:/Users/Harry/Documents/Algo/poker/middle.txt', 'r') as f:
            lines = f.readlines()
            list1 = s.str_list(lines[card1])
        return list1[card2]

    if position > 1/6.0 or position == 0.0:
        with open('C:/Users/Harry/Documents/Algo/poker/late.txt', 'r') as f:
            lines = f.readlines()
            list1 = s.str_list(lines[card1])
        return list1[card2]
        


def pre_flop_decision(suit_hole_list, hole_card_list, position):
    global suited
    suited = False

    for i in range(4):
        if suit_hole_list[i] == 2:
            suited = True
            break
        else:
            suited = False
    

    hole_card1 = 0
    hole_card2 = 0
    
    for i in range(13):
        if hole_card_list[i] == 2:
            hole_card1 = i 
            hole_card2 = i 
            break

        if hole_card_list[i] == 1 and hole_card1 > 0:
            hole_card2 = i 
            break
        
        if hole_card_list[i] == 1 and hole_card1 == 0:
            hole_card1 = i 

        

        
    decision1 = find_decision(position,hole_card1,hole_card2)


    
    if decision1 == 0:
        try:
            click_region.click("1442162013585.png")
        except:
            print 'error in finding check/fold'
            try:
                click_region.click("1442162249040.png")
            except:
                print 'error in finding check'
                try:
                    click_region.click("1442166141295.png")
                except:
                    print 'error in finding fold'
            

    if decision1 == 1:
        try:
            click_region.click("1442166579034.png")
        except:
            print 'error in finding bet'

            try:
                click_region.click("1441561481097.png")
            except:
                'error in finding raise'

    if decision1 == 2:
        try:
            click_region.click("1442165769004.png")
        except:
            print 'error in finding call'

    if decision1 == 2.5 and suited == True:
        try:
            click_region.click("1442165769004.png")
        except:
           print 'error in finding call' 
        

def post_flop_decision(hole_card_list, comm_card_list, suit_comm_list, suit_hole_list):
    print 'post flop decision'
    
    rating = hand_rating(hole_card_list, comm_card_list, suit_comm_list, suit_hole_list)
    
    if rating < 0.8:
        try:
            click_region.click("1442162013585.png")
        except:
            print 'error in finding check/fold'
           
            try:
                click_region.click("1442162249040.png")
            except:
                try:
                    click_region.click("1442166141295.png")
                    print 'fold'
                except:
                    print "can't find fold"
    else:
        try:
            click_region.click("1441561385405.png")
            
        except:
            print "can't find all in"
            try:
                click_region.click("1442165769004.png")
            except:
                print "can't find call"

        try:
            click_region.click("1442166579034.png")
        except:
            print "can't find bet"
            
            try:
                click_region.click("1441561481097.png")
            except:
                print "can't find raise"
                
        
        
    
            

def hand_rating(hole_card_list, comm_card_list, suit_comm_list, suit_hole_list):
    print ''
    print 'hole card list = ', hole_card_list
    print 'comm card list = ', comm_card_list
    print ''
    num_better_hands = 0
    my_result = hand.hand(hole_card_list, comm_card_list, suit_comm_list, suit_hole_list)
    hole_card_list = [0]*13
    suit_hole_list = [0]*4
    summ = 0
    for i in range(52):
        for j in range(i+1, 52):
            hole_card_list[i%13] += 1           #need to prevent overcounting
            hole_card_list[j%13] += 1
            suit_hole_list[i/13] += 1
            suit_hole_list[j/13] += 1


            opponent_result = hand.hand(hole_card_list, comm_card_list, suit_comm_list, suit_hole_list)

                     
            if opponent_result > my_result:
                num_better_hands += 1

                
            hole_card_list = [0]*13
            suit_hole_list = [0]*4


    print 'rating = ', 1 - num_better_hands/1326.0, 'my result = ', my_result
    return 1 - num_better_hands/1326.0      #there are 1326 possible hands

    

    


#process = sub.Popen('C:/python27/python.exe C:/Users/Harry/Documents/Algo/write_to_file.py')
#process = sub.Popen('C:/python27/python.exe C:/Users/Harry/Documents/Algo/poker/basic_interact_test8.py')
#process = sub.Popen('C:/Sikuli/runIDE.cmd -r C:/Users/Harry/Documents/Algo/find_suit3.sikuli')
#process2 = sub.Popen('C:/Sikuli/runIDE.cmd -r C:/Users/Harry/Documents/Algo/find_position.sikuli')


file1 = 'C:/Users/Harry/Documents/Algo/poker/totaloutput.txt'


click_region = Region(388,526,272,120)

i = 0
position = 0
hole_card_list = [0]*13
comm_card_list = [0]*13
suit_comm_list = [0]*4
suit_hole_list = [0]*4
suited = False

while True:
    while True:
        string = read(file1)            #need to prevent making the same decision twice
        i += 1


        if 'end' in string:
            print 'end ', string 
            hole_card_list = [0]*13
            comm_card_list = [0]*13
            suit_comm_list = [0]*4
            suit_hole_list = [0]*4
            position = (position + 1)%9
            break

        b_list = s.str_list(string)
        length = len(b_list)

        if length == 1:
            position = int(string)

        
        if length == 14:

            if b_list[13] == 1:
                hole_card_list = b_list[:13]
                pre_flop_decision(suit_hole_list, hole_card_list, position)
            else:
                comm_card_list = su.sum_list(comm_card_list, b_list[:13])

                post_flop_decision(hole_card_list, comm_card_list, suit_comm_list, suit_hole_list)


        if length == 5:
            if b_list[4] == 6:
                suit_hole_list = b_list[:4]
                pre_flop_decision(suit_hole_list, hole_card_list, position)
            else:
                suit_comm_list = b_list[:4]
                sum_suit_comm_list = sum(suit_comm_list)

                post_flop_decision(hole_card_list, comm_card_list, suit_comm_list, suit_hole_list)

        

#C:/Sikuli/runIDE.cmd -r C:/Users/Harry/Documents/Algo/make_bet4_manual_input.sikuli






                
