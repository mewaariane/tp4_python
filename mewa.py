import discord
import logging


class DiscordClient(discord.Client):
    def __init__(self):
        default_intents = discord.Intents.default()
        default_intents.members = True
        super().__init__(intents=default_intents)

    async def on_ready(self):
        print("Le bot est prêt !")
        logging.warning("Le bot s'est connecté")
        
    async def on_message(self, message):
        print(message.content)
        
        if message.content == "Ping":
            await message.channel.send("Pong")     
        if message.content.startswith("!del"):
            number = int(message.content.split()[1])
            messages = await message.channel.history(limit=number + 1).flatten()
            for each_message in messages:
                await each_message.delete() 
    
    async def on_member_join(self, member):
        print(f"L'utilisateur {member.display_name} a rejoint le serveur !")
        general_channel = self.get_channel(966758039141105788)
        general_channel.send(f"Bienvenue sur le serveur {member.display_name} !")
              