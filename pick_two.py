# Problem Statement :
#    There is bag that contains 3 colours of ball (Red, Green & Blue)
#    Numbers of ball count of each colours are A, B, and C respectively
#    We will 3 picks and in each pick we will take 2 balls out and we won’t replace the picked balls for subsequent picks or draws.
#    We wanted to find out the probability of picking same of colour of balls in 3rd draw.
#    You are NOT allowed to use “conditional probability” formulae to solve this, instead solve algorithmically using data structure.

# Consider all the paths based on all possible outcomes in each draw; Have the probability ...
# ...of each path (multiplication as draws are independent). Multiply path probability with the probability of having ...
# ...same color balls in the third draw travelling via this path. Add all.  

# pick_two returns the probability of picking same color balls in the 3rd draw
# pick_two takes 4 arguments : A,B,C are the number of balls of each color and ...
# ...draw_number is the current draw number so that we can distinguish the third draw
def pick_two(A,B,C,draw_number):
    # There are six possible outcomes we get when we pick 2 balls from balls of 3 colors...
    # ... both of 1st color, both of 2nd color, both of 3rd color, ...
    # ... one of 1st color and other of 2nd color, one 1st color and other 3rd color, 2nd color and 3rd color ...
    # ... Each of these outcomes have different probabilities and give us a different path to ...
    # ... traverse in the next draw (different number of balls remaining)
    # Initializing fraction via each possible outcome as zero
    fraction_via_A2 = fraction_via_B2 = fraction_via_C2 = 0
    fraction_via_A1B1 = fraction_via_A1C1 = fraction_via_B1C1 = 0

    total = A+B+C # total balls reamaining
    if(total>=2):
        num_total2 = (total*(total-1)/2) # number of ways of choosing 2 balls from all the remaining balls
    
    if(A>=2):
        num_A2 = (A*(A-1)/2) # number of ways of choosing 2 balls of 1st color
        prob_A2 = (num_A2 / num_total2)# probability of choosing 2 balls of 1st color
        # If this is the 3rd draw, we just have to see the probability of picking same color balls
        if(draw_number==3):
            fraction_via_ A2 = prob_A2
        else: 
        # Multiplying the current term to path probability and recursive call with remaining balls...
            fraction_via_A2 = prob_A2 * pick_two(A-2,B,C,draw_number+1)
    
    if(B>=2):
        num_B2 = (B*(B-1)/2)# number of ways of choosing 2 balls of 2nd color
        prob_B2 = (num_B2 / num_total2)# probability of choosing 2 balls of 2nd color
        # If this is the 3rd draw, we just have to see the probability of picking same color balls
        if(draw_number==3):
            fraction_via_B2 = prob_B2
        else:
        # Multiplying the current term to path probability and recursive call with remaining balls...
            fraction_via_B2 = prob_B2 * pick_two(A,B-2,C,draw_number+1)
    
    if(C>=2):
        num_C2 = (C*(C-1)/2)# number of ways of choosing 2 balls of 3rd color
        prob_C2 = (num_C2 / num_total2)# probability of choosing 2 balls of 3rd color
        # If this is the 3rd draw, we just have to see the probability of picking same color balls
        if(draw_number==3):
            fraction_via_C2 = prob_C2
        else:
        # Multiplying the current term to path probability and recursive call with remaining balls...
            fraction_via_C2 = prob_C2 * pick_two(A-2,B,C,draw_number+1)
    
    if(A>=1 and B>=1):
        num_A1B1 = (A*B)
        prob_A1B1 = (num_A1B1 / num_total2)
        # If this is the 3rd draw, we just have to see the probability of picking same color balls
        if(draw_number==3):
            fraction_via_A1B1 = 0
        else:
        # Multiplying the current term to path probability and recursive call with remaining balls...
            fraction_via_A1B1 = prob_A1B1 * pick_two(A-1,B-1,C,draw_number+1)

    if(A>=1 and C>=1):
        num_A1C1 = (A*C)
        prob_A1C1 = (num_A1C1 / num_total2)
        # If this is the 3rd draw, we just have to see the probability of picking same color balls
        if(draw_number==3):
            fraction_via_A1C1 = 0
        else:
        # Multiplying the current term to path probability and recursive call with remaining balls...
            fraction_via_A1C1 = prob_A1C1 * pick_two(A-1,B,C-1,draw_number+1)

    if(B>=1 and C>=1):
        num_B1C1 = (B*C)
        prob_B1C1 = (num_B1C1 / num_total2)
        # If this is the 3rd draw, we just have to see the probability of picking same color balls
        if(draw_number==3):
            fraction_via_B1C1 = 0
        else:
        # Multiplying the current term to path probability and recursive call with remaining balls...
            fraction_via_B1C1 = prob_B1C1 * pick_two(A,B-1,C-1,draw_number+1)

    return (fraction_via_A2 + fraction_via_B2 + fraction_via_C2 + 
        fraction_via_A1B1 + fraction_via_A1C1 + fraction_via_B1C1)

