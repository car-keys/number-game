from number_game import *

'''
class <Name>(Artifact):
    def __init__(self, name, rarity, description):
    
        super().__init__(name='<name>', 
                         rarity=<rarity>,
                         description='<desc>')
                         
    def passive(self, owner, T):
        <fill>
    
    def active(self, owner, T):
        <fill>
    
    def make_new():
        <fill>
    def to_dict(self):
        <fill>
    def from_dict(dic):
        <fill>
'''
########---Common Artifact Methods---########

#generates a set amount of resource every amount of seconds
class PassiveGenerator:
    def __init__(self, resource, delay, amount, last_gen=None):
        if last_gen is None:
            self.last_gen = time.time()
        else:
            self.last_gen = last_gen
        self.resource = resource
        self.delay = delay
        self.amount = amount
    
    #generates resource. Optimised for long periods of no checking
    def generate(owner, T):
        dt = T - self.last_gen
        resourcechange = 0
        while dt > self.delay:
            dt -= self.delay
            resourcechange += self.amount
        if resourcechange > 0:
            owner.add_resource(self.resource, resourcechange)
            self.last_gen = time.time()
            
#spawns apples every few days
class AppleTree(Artifact):
    def __init__(self, last_gen):
        self.generator = PassiveGenerator('apples', SECONDS_IN_DAY*3, 30, last_gen=last_gen(
        super().__init__(name='Apple Tree', 
                         rarity=RARE,
                         description='Produces Apples every few days.\nOwO')
                         
    def passive(self, owner, T):
        self.generator.generate(owner, T)
        
    def make_new():
        return AppleTree(time.time())
    def to_dict(self):
        output = {}
        output['type'] = 'appletree'
        output['last_gen'] = self.generator.last_gen
        return output
    def from_dict(dic):
        return AppleTree(dic['last_gen'])

#plant to make a sapling, that makes the tree
class ApppleSeed(Artifact):
    def __init__(self, plant_time):
        super().__init__(name='Apple Seed',
                         rarity=UNCM
                         description='You dont need to be told what this turns in to.'
    
    def active(self, owner, T):
        owner.add_artifact(AppleSapling.make_new())
        self.destroy(owner)
        
    def make_new():
        return AppleSeed()
    def to_dict(self):
        output = {}
        output['type'] = 'appleseed'
        return output
    def from_dict(dic):
        return AppleSeed.make_new()

