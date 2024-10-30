import csv

###########################################################################################################################################################################################################

class Parent:

    def __lt__(self, other):
        return self.overall() < other.overall()

    def __gt__(self, other):
        return self.overall() > other.overall()

    def __add__(self, other):
        x = self.overall() + other.overall()
        return round(x/2)
    

########################################################################################################################################################################

class Striker(Parent):

    def __init__(self, name, pace, shooting, passing, dribbling, defending, physical, finishing, reaction, inter):

        self._name = name

        self._inter = inter
        
        self._pace = pace
        self._shooting = shooting
        self._passing = passing
        self._dribbling = dribbling
        self._defending = defending
        self._physical = physical
        self._finishing = finishing
        self._reaction = reaction
        


    def __repr__(self):
        return f'Striker(name = {self._name}, pace = {self._pace}, shooting = {self._shooting}, passing = {self._passing}, dribbling = {self._dribbling}, defending = {self._defending}, physical = {self._physical}, finishing = {self._finishing}, reaction = {self._reaction}, international = {self._inter})'
         

    def __str__(self):
        return f'{self._name}, pace = {self._pace}, shooting = {self._shooting}, passing = {self._passing}, dribbling = {self._dribbling}, defending = {self._defending}, physical = {self._physical}, finishing = {self._finishing}, reaction = {self._reaction}, international = {self._inter}'
        
    
    def overall(self):
        

            
        o_pace = self._pace * 0.15
        o_shooting = self._shooting * 0.2
        o_passing = self._passing * 0.15
        o_dribbling = self._dribbling * 0.2
        o_defending = self._defending * 0.005
        o_physical = self._physical * 0.05
        o_finishing = self._finishing * 0.2
        o_reaction = self._finishing * 0.045

        return round(o_pace + o_shooting + o_passing + o_dribbling + o_defending + o_physical + o_finishing + o_reaction + self._inter)
  
##############################################################################################################################################################################             

class Goalkeeper(Parent):

    def __init__(self, name, diving, handling, kicking, reflex, speed, positioning, inter):
        self._name = name

        self._inter = inter
        
        self._diving = diving
        self._handling = handling
        self._kicking = kicking
        self._reflex = reflex
        self._speed = speed
        self._positioning = positioning
        

    def __repr__(self):
        return f'Goalkeeper(name = {self._name}, diving = {self._diving}, handling = {self._handling}, kicking = {self._kicking}, speed = {self._speed}, positioning = {self._positioning}, international = {self._inter})'
        

    def __str__(self):
        return f'{self._name}, diving = {self._diving}, handling = {self._handling}, kicking = {self._kicking}, speed = {self._speed}, positioning = {self._positioning}, international = {self._inter}'


    def overall(self):

        
        o_diving = self._diving * 0.2
        o_handling = self._handling * 0.2
        o_kicking = self._kicking * 0.2
        o_reflex = self._reflex * 0.2
        o_speed = self._speed * 0.05
        o_positioning = self._positioning * 0.15

        return round(o_diving + o_handling + o_kicking + o_reflex + o_speed + o_positioning + self._inter)
     
#####################################################################################################################################################################################      

class Centreback(Parent):

    def __init__(self, name, standing_tackle, sliding_tackle, pace, defending, physical, marking, short_pass, reaction, inter):

        self._name = name

        self._inter = inter
        
        self._standingtackle = standing_tackle
        self._slidingtackle = sliding_tackle
        self._pace = pace
        self._defending = defending
        self._physical = physical
        self._marking = marking
        self._shortpass = short_pass
        self._reaction = reaction
        

    def __str__(self):
        return f'{self._name}, standing tackle = {self._standingtackle}, sliding tackle = {self._slidingtackle}, pace = {self._pace}, defending = {self._defending}, physical = {self._physical}, marking = {self._marking}, short pass = {self._shortpass}, reaction = {self._reaction}'
    
    def __repr__(self):
        return f'Centreback(name = {self._name}, standing tackle = {self._standingtackle}, sliding tackle = {self._slidingtackle}, pace = {self._pace}, defending = {self._defending}, physical = {self._physical}, marking = {self._marking}, short pass = {self._shortpass}, reaction = {self._reaction})'

    def overall(self):


        o_standingtackle = self._standingtackle * 0.3
        o_slidingtackle = self._slidingtackle * 0.2
        o_pace = self._pace * 0.1
        o_defending = self._defending * 0.1
        o_physical = self._physical * 0.1
        o_marking = self._marking * 0.1
        o_shortpass = self._shortpass * 0.1
        

        return round(o_standingtackle + o_slidingtackle + o_pace + o_defending + o_physical + o_marking + o_shortpass + self._inter)
    
######################################################################################################################################################################################
    
class Store:   
    
    def __init__(self):
        self._store = {'Striker': [], 'Goalkeeper': [], 'Centreback': []}

    def add_to_collection(self, other):
        if isinstance(other, Striker):
            self._store['Striker'].append(other)
                        
        elif isinstance(other, Goalkeeper):
            self._store['Goalkeeper'].append(other)

        elif isinstance(other, Centreback):
            self._store['Centreback'].append(other)

    def average_striker(self):
        total = 0
        count = 0
        for i in self._store['Striker']:
            total += i.overall()
            count += 1
        return round(total/count)

    def average_goalkeeper(self):
        total = 0
        count = 0
        for i in self._store['Goalkeeper']:
            total += i.overall()
            count += 1
        return round(total/count)

    def average_centreback(self):
        total = 0
        count = 0
        for i in self._store['Centreback']:
            total += i.overall()
            count += 1
        return round(total/count)

    def top_striker(self):

        temp = self._store['Striker']
        swapped = True
        index_of_last_unsorted_item = len(temp)
        
        while swapped:

            swapped = False
            
            for i in range(0, index_of_last_unsorted_item -1):
                if temp[i].overall() < temp[i+1].overall():
                    temp[i], temp[i+1] = temp[i+1], temp[i]


                    swapped = True

            index_of_last_unsorted_item -= 1
 
        return (temp[0:5])
        #changed return temp to print temp

    def top_goalkeeper(self):

        temp = self._store['Goalkeeper']
        swapped = True
        index_of_last_unsorted_item = len(temp)
        
        while swapped:

            swapped = False
            
            for i in range(0, index_of_last_unsorted_item -1):
                if temp[i].overall() < temp[i+1].overall():
                    temp[i], temp[i+1] = temp[i+1], temp[i]


                    swapped = True

            index_of_last_unsorted_item -= 1
 
        return temp[0:5]

    def top_centreback(self):

        temp = self._store['Centreback']
        swapped = True
        index_of_last_unsorted_item = len(temp)
        
        while swapped:

            swapped = False
            
            for i in range(0, index_of_last_unsorted_item -1):
                if temp[i].overall() < temp[i+1].overall():
                    temp[i], temp[i+1] = temp[i+1], temp[i]


                    swapped = True

            index_of_last_unsorted_item -= 1
 
        return temp[0:5]

    
    def get_stored(self):
        return self._store
                    
##################################################################################################################################################################################     

def main(filename):
    collection = Store()
    with open(filename, "r", encoding='utf-8', errors='ignore') as file_in:
        file_in.readline()
        reader = csv.reader(file_in)

        for key in reader:
            position = key[24]
            if position == "ST":

                name = key[3]
                
                inter = int(key[16])
                
                pace = int(key[31])
                shooting = int(key[32])
                passing = int(key[33])
                dribbling = int(key[34])
                defending = int(key[35])
                physical = int(key[36])
                finishing = int(key[45])
                reaction = int(key[57])

                newstriker = Striker(name, pace, shooting, passing, dribbling, defending, physical, finishing, reaction, inter)
                collection.add_to_collection(newstriker)

            elif position == "GK":
                name = key[3]

                inter = int(key[16])
                
                diving = int(key[37])
                handling = int(key[38])
                kicking = int(key[39])
                reflex = int(key[40])
                speed = int(key[41])
                positioning = int(key[41])

                newgoalkeeper = Goalkeeper(name, diving, handling, kicking, reflex, speed, positioning, inter)
                collection.add_to_collection(newgoalkeeper)
            
            elif position == "LCB" or position == "RCB" or position == "CB":

                name = key[3]

                inter = int(key[16])

                standing_tackle = int(key[71])
                sliding_tackle = int(key[72])
                if key[31] == '':
                    pace = 50
                else:
                    pace = int(key[31])
                if key[35] == '':
                    defending = 50
                else:
                    defending = int(key[35])
                if key[36] == '':
                    physical = 50
                else:
                    physical = int(key[36])
                marking = int(key[70])
                short_pass = int(key[47])
                reaction = int(key[57])
                
                

                newcentreback = Centreback(name, standing_tackle, sliding_tackle, pace, defending, physical, marking, short_pass, reaction, inter)
                collection.add_to_collection(newcentreback)


################################################################################################################################################################################################

main("players_20.csv")


    

        
    

    
            



    

    
    

            
        
        
            

        
    
    
