import operator as op
from functools import reduce

num_A = int(input("Please input number of balls of first colour -- A : "))
num_B = int(input("Please input number of balls of first colour -- B : "))
num_C = int(input("Please input number of balls of first colour -- C : "))

# storing the entire tree as dictionary
level_nodes_dict = {0:{'':{'probability':1.0,'num_A':num_A,'num_B':num_B,'num_C':num_C}}}

# compute n choose r
def comb(n,r):
    r = min(r,n-r)
    return reduce(op.mul, range(n,n-r,-1), 1) / reduce(op.mul, range(r,1,-1), 1)


# create the nodes for the next draw
def create_next_level(level_nodes_dict,level):
    next_level_nodes_dict = {}
    for key_string,value_dict in level_nodes_dict[level].items():
        total_balls = value_dict['num_A'] + value_dict['num_B'] + value_dict['num_C']
        # Got 2 'A' balls in the next draw
        if(value_dict['num_A']>=2):
            next_level_nodes_dict[key_string + '_AA'] = {'probability': value_dict['probability'] * comb(value_dict['num_A'],2)/comb(total_balls,2),
'num_A':value_dict['num_A']-2, 'num_B':value_dict['num_B'], 'num_C':value_dict['num_C']}
        # Got 2 'B' balls in the next draw
        if(value_dict['num_B']>=2):
            next_level_nodes_dict[key_string + '_BB'] = {'probability': value_dict['probability'] * comb(value_dict['num_B'],2)/comb(total_balls,2),
'num_A':value_dict['num_A'], 'num_B':value_dict['num_B']-2, 'num_C':value_dict['num_C']}
        # Got 2 'C' balls in the next draw
        if(value_dict['num_C']>=2):
            next_level_nodes_dict[key_string + '_CC'] = {'probability': value_dict['probability'] * comb(value_dict['num_C'],2)/comb(total_balls,2),
'num_A':value_dict['num_A'], 'num_B':value_dict['num_B'], 'num_C':value_dict['num_C']-2}
        # Got 1 'A' ball and 1 'B' in the next draw
        if(value_dict['num_A']>=1 and value_dict['num_B']>=1):
            next_level_nodes_dict[key_string + '_AB'] = {'probability': value_dict['probability'] * (value_dict['num_A']*value_dict['num_B'])/comb(total_balls,2), 'num_A':value_dict['num_A']-1, 'num_B':value_dict['num_B']-1, 'num_C':value_dict['num_C']}
        # Got 1 'A' ball and 1 'C' in the next draw
        if(value_dict['num_A']>=1 and value_dict['num_C']>=1):
            next_level_nodes_dict[key_string + '_AC'] = {'probability': value_dict['probability'] * (value_dict['num_A']*value_dict['num_C'])/comb(total_balls,2), 'num_A':value_dict['num_A']-1, 'num_B':value_dict['num_B'], 'num_C':value_dict['num_C']-1}
        # Got 1 'B' ball and 1 'C' in the next draw
        if(value_dict['num_B']>=1 and value_dict['num_C']>=1):
            next_level_nodes_dict[key_string + '_BC'] = {'probability': value_dict['probability'] * (value_dict['num_B']*value_dict['num_C'])/comb(total_balls,2), 'num_A':value_dict['num_A'], 'num_B':value_dict['num_B']-1, 'num_C':value_dict['num_C']-1}

    level_nodes_dict[level+1] = next_level_nodes_dict


# create all the levels for the three draws
create_next_level(level_nodes_dict,0)
create_next_level(level_nodes_dict,1)
create_next_level(level_nodes_dict,2)

# print the entire tree as dictionary
print(level_nodes_dict)

# compute the result : the probability of getting the same color balls in the third draw
result = 0.0
for key_string,value_dict in level_nodes_dict[3].items():
    last_draw_result = key_string.split('_')[-1]
    if(last_draw_result[0]==last_draw_result[1]):
        result += value_dict['probability']

print('-------------\nResult:{}-------------\n',result)
