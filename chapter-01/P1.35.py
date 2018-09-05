'''
P-1.35 The birthday paradox says that the probability that two people in a room
will have the same birthday is more than half, provided n, the number of
people in the room, is more than 23. This property is not really a paradox,
but many people find it surprising. Design a Python program that can test
this paradox by a series of experiments on randomly generated birthdays,
which test this paradox for n = 5,10,15,20, . . . ,100.
'''
import random
def test_bday_paradox(num_people, num_loops):
    '''
    input: int(n) = number of people in class
           int(num_loops) = number of iterations for the experiment
    output:
        int(num_people) = number of people in class
        int(num_same_bdays) = number of people with same day summer over all experiments
        int(num_loops) = number of experiments
        float(num_same_bdays / num_loops)
    '''
    def rand_month(): return(random.randint(1,12))
    def rand_day(): return(random.randint(1,30))

    def run_exp(num_loops):
        num_same_bdays = 0
        num_diff_bdays = 0
        for n in range(num_loops):
            peeps_rand_month = [rand_month() for i in range(num_people)]
            peeps_rand_day   = [rand_day() for i in range(num_people)]
            bday_set = {(peeps_rand_month[i],peeps_rand_day[i]) for i in range(num_people)}
            if len(bday_set) < num_people:
                num_same_bdays += (num_people - len(bday_set))
        print(num_people, num_same_bdays , num_loops, num_same_bdays / num_loops)

    run_exp(num_loops)

def run_all_exps(n_min, n_max, delta, num_loops):
    '''
    input:
        int(n_min) = lower bound of number of people in class for experiment
        int(n_max) = higher bound of number of people in class for experiment
        int(delta) = increment of number of people in class for experiment
        int(num_loops)  = number of iterations in experiment
    run test_bday_paradox experiments
    '''
    print('num_people', 'num_same_bdays', 'num_loops', 'ratio')
    for n in range(n_min, n_max + delta, delta):
        test_bday_paradox(n, num_loops)

run_all_exps(5,100,5,10000)
