#
#
import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

class River():
    '''
    '''
    def __init__(self, num_sites = 1000):
        self.animals        = ['bear', 'fish']
        self.length         = num_sites
        self.sites          = [''] * self.length
        self.empty_sites    = set()
        self.occupied_sites = set()

    def populate_river(self): #O(n) write
        '''
        populates sites list with the animal type
        add indices of empty sites to empty_sites set
        '''
        for s in range(self.length):
            animal = np.random.choice(self.animals + [None])
            self.sites[s] = animal
            if animal == None:                                          # we found an empty site
                self.empty_sites.add(s)
            else:
                self.occupied_sites.add(s)

    def has_fish(self, site_index): #O(1) search
        if self.sites[site_index] == 'fish':
            return(True)
        return(False)

    def make_baby_animal(self, animal_type): #O(1) write
        '''
        populates an empty site with a fish
        '''
        if len(self.empty_sites) == 0:
            sys.exit('There are no empty sites to move to')
        random_site = np.random.choice(list(self.empty_sites))
        self.empty_sites.remove(random_site)                             # site is now occupied
        self.occupied_sites.add(random_site)                             # site is now occupied by fish
        self.sites[random_site] = animal_type                            # update occupancy type

    def encounter_foe(self, from_index, to_index): #O(1) write
        '''
        update type in kill_index site from fish to bear
        update type in from_index site from bear to empty
        '''
        self.sites[from_index] = None #make site empty
        self.sites[to_index]   = 'bear'

        self.empty_sites.add(from_index)
        self.occupied_sites.remove(from_index)

    def move_animal_to_empty(self, animal_type, from_index, to_index):
        '''
        update sites lists if an animal of type animal_type moves
        from from_index to to_index
        '''
        self.sites[from_index] = None
        self.empty_sites.add(from_index)
        self.empty_sites.remove(to_index)

        self.sites[to_index] = animal_type
        self.occupied_sites.add(to_index)
        self.occupied_sites.remove(from_index)

    def step(self):
        '''
        perform one step of random animal movement
        '''
        start_site_index  = np.random.choice(list(self.occupied_sites))     # choose site that has animal: O(1)
        start_animal_type = self.sites[start_site_index]
        move_direction    = np.random.choice([-1,+1])                        # either go fwd or bckw

        new_site_index = start_site_index + move_direction
        if new_site_index >=0 and new_site_index < self.length:
            new_site_index = new_site_index
        else:
            new_site_index = start_site_index - move_direction

        new_animal_type = self.sites[new_site_index]

        print(str(start_animal_type) + ' at ' + str(start_site_index) + ' moved to ' + str(new_site_index))

        if new_animal_type == None:                                               # site is empty, move animal!
            self.move_animal_to_empty(start_animal_type,
                                      start_site_index,
                                      new_site_index)

        elif new_animal_type == start_animal_type:                              # site has same species, procriate !
            self.make_baby_animal(start_animal_type)

        else:                                                                   # site has a different species
            self.encounter_foe(start_site_index, new_site_index)

    def print_configuration(self):
        def make_numeric_type(animal_type):
            if animal_type == None:
                return(0.0)
            elif animal_type == 'fish':
                return(0.5)
            else:
                return(1.0)

        numeric_array = [make_numeric_type(s) for s in self.sites]
        numeric_array = [numeric_array for i in range(self.length)]
        plt.xticks(np.arange(0, self.length, step=1))
        plt.ylim(0,1)
        plt.imshow(numeric_array, interpolation='nearest')
        plt.show()
        # return(numeric_array)
    def step_and_print(self):
        self.step()
        self.print_configuration()


new_river = River(20)
new_river.populate_river()
new_river.print_configuration()
for i in range(50):
    new_river.step_and_print()

























#
