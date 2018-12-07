import discord, time
from pathlib import Path

#####-CONSTANTS-#####
SECONDS_IN_DAY = 86400
SECONDS_IN_HOUR
CM = 'Common'
UNCM = 'Uncommon'
RARE = 'Rare'
LEG = 'Legendary'
UNI = 'Unique'


#####################

client = discord.Client()
players_in_session = []



@client.event
async def on_ready():
    print('Online.')
    
async def on_message(message):
    if message.author != client.user and message.author.id not in players_in_session:
        players_in_session.append(message.author.id)
        if message.content.startswith(';'):
            cmd = message.content[1:].lower()
            try:
                if   cmd in ['encounter', 'e', 'wild', 'w']:
                    await encounter_poke(message)
                elif cmd == 'join':
                    await join_member(message)
                elif cmd == 'help':
                    pass
                elif cmd in ['location', 'loc']:
                    await show_loc(message)
            except KeyboardInterrupt as k:
                raise k
            except Exception as e:
                #we catch this so it doesn't hang that user's session on error,
                #but we still want to see what went wrong so:
                print(traceback.format_exc())
        players_in_session.remove(message.author.id)  
    return
client.run('NTE3NTQ4ODMxNzY0NjQzODgw.DuD0tQ.HF2LnifglJACb6zGw3tOHqp3bHI')


async def register_user(message):
    
#Inventory: list of artifact instances
#Bank: dict of resource values    
class Player:
    def __init__(self, id, name, inventory, bank):
        self.id = id
        self.name = name
        self.inventory = inventory
        self.bank = bank
        
    def to_dict(self):
        output = {}
        output['id'] = self.id
        output['name'] = self.name
        output['inventory'] = [a.to_dict() for a in inventory]
        output['bank'] = self.bank
        return output
        
    def remove_artifact(self, art):
        
    def add_artifact():
    
    def add_resource(self, name, amount):
        self.bank[name] += amount
        
    def spend_resource(self, name, amount):
        self.bank[name] -= amount
        
def make_player_from_dict(dic):
    return Player(dic['id'])
    
    
def write_players(

#tradable object that can do things, passive or active
#subclass me!
#In subclasses:
#--Define passive and active
#--call super().__init__()
class Artifact:
    #call this to set up these variables. subclass should only include vars needed to 
    #reconstruct from dict
    def __init__(self, name, rarity, description):
        self.name = name
        self.rarity = rarity
        self.description = description
    #delete self from players inventory
    def destroy(self):
        owner.remove_artifact(self)
        
    #----Define everything below in subclass!---#
    
    #Acts like its being called continually, actually called only when viewed
    #if somthing is to be done every X seconds, store a "last_time" vars
    #and account for outages
    def passive(self, owner, T):
        pass
    #called on user command
    def active(self, owner, T):
        pass
    #create a new instance of self, with default values
    def make_new():
        pass
    def to_dict(self):
        #dict should contain any info needed to reconstruct artifact, and 
        #the 'type' field, containing the name of the artifact, all lowercase, no spaces
        pass
    #given an input dictionary, construct an instance
    def from_dict(dic):
        pass
        
#---------------Template:---------------
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
#############---Artifacts---#############

#once every 24 hours, generate an egg.
class EggMachine(Artifact):
    def __init__(self, last_use, uses, broken):
        self.last_use = last_use
        self.uses = uses
        self.broken = broken
        self.chance_to_break = 0.10
        super().__init__(name='Egg Machine', 
                         rarity=RARE,
                         description='Ah! Gatcha!')
        self.set_description()
    
    #set the correct description based on uses and broken status
    def set_description(self):
        if self.broken:
            self.description = f'Ah! Gatcha!\nUses Left: {self.uses} <BROKEN>'
        else:
            self.description = f'Ah! Gatcha!\nUses Left: {self.uses}'
            
    #generates uses, one every 24 hours.
    #small chance of breaking after producing an egg
    def passive(self, owner, T):
        if self.broken:
            return
        dt = T - self.last_use
        while dt > SECONDS_IN_DAY:
            dt -= SECONDS_IN_DAY
            uses += 1
            if random.random() < 0.10:
                self.broken = True
            self.last_use = time.time()
        self.set_description()
    
    #On activate, use a use if possible.
    def active(self, owner, T):
        if self.uses > 0:
            self.uses -= 1
            owner.add_artifact(Egg.make_new())
        if self.uses <= 0:
            self.destroy()
            return
        self.set_description()
        
    def make_new():
        return EggMachine(time.time(), 0, False)

    def to_dict(self):
        output = {}
        output['type'] = 'eggmachine'
        output['last_use'] = self.last_use
        output['uses'] = self.uses
        output['broken'] = self.broken
        return output
        
    def from_dict(dic):
        return EggMachine(dic['last_use', dic['uses'], dic['broken'])
        
#gacha egg. gives some money for now, TODO make it give other stuff     
class Egg(Artifact):
    def __init__(self):
        super().__init__(name='Egg',
                         rarity=UNCM,
                         description='What could be inside???')
                         
    #open the egg, get the reward, delete self
    def active(self, owner, T):
        owner.add_resource('money', random.randint(1, 1000))
        self.destroy()
    def make_new():
        return Egg()
    def to_dict(self):
        output = {}
        output['type'] = 'egg'
        return output
    def from_dict(dic):
        return Egg()
        
#gives the user 1 dollar per hour
class ShittyMoneySource(Artifact):
    def __init__(self, last_produce):
        self.last_produce = last_produce
        super.__init__(name='Shitty Money Source',
                       rarity=CM
                       description='...its better than nothing. Produces 1 dollar every hour')
           
    def passive(self, owner, T):
        dt = T - last_produce
        dmoney = 0
        while dt > SECONDS_IN_HOUR:
            dt -= SECONDS_IN_HOUR
            dmoney += 1
        if dmoney > 0:
            owner.add_resource('money', dmoney)
            self.last_produce = time.time()

    def make_new():
        return ShittyMoneySource(time.time())
        
    def to_dict(self):
        output = {}
        output['type'] = 'shittymoneysource'
        output['last_produce'] = self.last_produce
        
    def from_dict(dic):
        return ShittyMoneySource(dic['last_produce'])
        
        
#############---Upgrades---#############
class Upgrade:
    def __init__(self, name, description):
        pass
