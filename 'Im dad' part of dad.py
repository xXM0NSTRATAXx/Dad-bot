import discord
import random
colors=[0xff80ed,0x5ac18e,0xffa500,0x990000,0x2acaea,0x0ff1ce,0xbada55,0xf7347a,0x0000ff,0xff6666,0xff7f50,0xb6fcd5]
client=discord.Client()
@client.event
async def on_message(message):
  me=message.content.lower()
  if  me.startswith('i\'m'):
      guy=' '+me[3:]
      lnk=' https://cdn.discordapp.com/attachments/655475477846425618/806879604203061268/9k.png'
      m='hi ' + guy.replace('  ','')+', ' +'I\'m Dad!'
      if guy.strip()=='dad':
          e=discord.Embed(title='NO, I\'M THE DAD.',color=random.choice(colors))
          e.set_image(url=lnk)
          await message.channel.send(embed=e)
      else:
          await message.channel.send(m)
client.run('Nzc2MzAyMTE1MDA5NDYyMzAz.X6y5rw.nAIBnDnbjpEe3LuVlzy75EeIQ4o')