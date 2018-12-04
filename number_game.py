import discord
from pathlib import Path
client = discord.Client()
players_in_session = []

@client.event
async def on_ready():
    
    
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
    
    
class Player:
    def __init__(self, id):
        self.id = id
        self.upgrades = upgrades
        self.artifacts = artifacts
        
    def to_dict(self):
        output = {}
        output['id'] = self.id
        output['upgrades'] = 
def make_player_from_dict(dic):
    return Player(dic['id'])
    
    
def write_players(

#tradable object that can do things, passive or active
class Artifact:
    def __init__(self, name, ):
        
        


