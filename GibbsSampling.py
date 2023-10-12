import math
from operator import truediv
import random
import numpy as np
import matplotlib.pyplot as plt
from turtle import color 

#Define the Markov Network in terms of the factors:
#We define the factors as 2d arrays, for which the factor_X_Y means for example x^0, y^1 factor_X_Y[0][1]
factor_A_B = [[30, 5], [1, 10]]
factor_B_C = [[100, 1], [1, 100]]
factor_C_D = [[1, 100], [100, 1]]
factor_D_A = [[100, 1], [1, 100]]
#Constants for indexing the next pick"
CONSTANT_A = 0
CONSTANT_B = 1
CONSTANT_C = 2
CONSTANT_D = 3
#Gibb's Sampling of a given BNet:
#Define the current sample list respectively A, B, C, D in alphabetical order

def gibbs_sampling_procedure(num_iterations, current_sample_list):
    count_success = 0
    count_total = 1

    for i in range(num_iterations):
        if(viable_sample_list(current_sample_list)):
            count_success += 1
        count_total += 1
        next_pick = random.randint(0, 2)
        sample_distribution = []
        indexer = None
        #We want to randomly sample A, C, and D. But keep B constant to B = 1 (Observed Variable)
        if(next_pick == 0):
            sample_distribution = markov_blanket_A(current_sample_list)
            indexer = 0
        elif(next_pick == 1):
            sample_distribution = markov_blanket_C(current_sample_list)
            indexer = 2
        elif(next_pick == 2):
            sample_distribution = markov_blanket_D(current_sample_list)
            indexer = 3
        
        #Pick the 0 or 1 based of the sample_distribution: 
        rand = random.uniform(0, 1)
        next_value = None
        if(rand <= sample_distribution[1]):
            next_value = 1
        else:
            next_value = 0

        #Change the current_sample_list:
        current_sample_list[indexer] = next_value

    return ((count_success / count_total), current_sample_list)













#Helper Functions:
#Functions for each given markov blanket
#A: D,B
def markov_blanket_A(current_sample_list):
    A_1 = factor_A_B[1][current_sample_list[CONSTANT_B]]*factor_D_A[current_sample_list[CONSTANT_D]][1]
    A_0 = factor_A_B[0][current_sample_list[CONSTANT_B]]*factor_D_A[current_sample_list[CONSTANT_D]][0]
    norm_A_1 = (A_1) / (A_1 + A_0)
    norm_A_0 = (A_0) / (A_1 + A_0)
    distribution_0_1 = [norm_A_0, norm_A_1]
    return distribution_0_1

#B: C,A
def markov_blanket_B(current_sample_list):
    B_1 = factor_A_B[current_sample_list[CONSTANT_A]][1]*factor_B_C[1][current_sample_list[CONSTANT_C]]
    B_0 = factor_A_B[current_sample_list[CONSTANT_A]][0]*factor_B_C[0][current_sample_list[CONSTANT_C]]
    norm_B_1 = (B_1)/(B_1 + B_0)
    norm_B_0 = (B_0)/ (B_1 + B_0)
    distribution_0_1 = [norm_B_0, norm_B_1]
    return distribution_0_1

#C: D, B
def markov_blanket_C(current_sample_list):
    C_1 = factor_C_D[1][current_sample_list[CONSTANT_D]]*factor_B_C[current_sample_list[CONSTANT_B]][1]
    C_0 = factor_C_D[0][current_sample_list[CONSTANT_D]]*factor_B_C[current_sample_list[CONSTANT_B]][0]
    norm_C_1 = (C_1)/ (C_1 + C_0)
    norm_C_0 = (C_0)/(C_1 + C_0)
    distribution_0_1 = [norm_C_0, norm_C_1]
    return distribution_0_1

#D: A, C
def markov_blanket_D(current_sample_list):
    D_1 = factor_D_A[1][current_sample_list[CONSTANT_A]]*factor_C_D[current_sample_list[CONSTANT_C]][1]
    D_0 = factor_D_A[0][current_sample_list[CONSTANT_A]]*factor_C_D[current_sample_list[CONSTANT_C]][0]
    norm_D_1 = (D_1)/(D_1 + D_0)
    norm_D_0 = (D_0)/ (D_1 + D_0)
    distribution_0_1 = [norm_D_0, norm_D_1]
    return distribution_0_1

#Check if the current sample list is viable for P(A | B = b^1)
def viable_sample_list(current_sample_list):
    if(current_sample_list[CONSTANT_A] == 1):
        return True 
    else: 
        return False





#MAIN CODE: 
max_iterations = 10000
prob_y = []
curr_sample = [0,1,0,0]
for i in range(max_iterations):
    gibb_return = gibbs_sampling_procedure(i, curr_sample)
    prob_y.append(gibb_return[0])
    curr_sample = gibb_return[1]

x_1 = np.arange(len(prob_y))
variable_elimination_y = 0.0565
plt.plot(np.log(x_1), prob_y)
plt.axhline(variable_elimination_y, color = 'r')
plt.show()