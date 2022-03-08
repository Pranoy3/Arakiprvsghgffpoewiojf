import nextcord
from nextcord.ext import commands
from nextcord import ButtonStyle
from nextcord.ui import Button, View
import config
from config import *

class Invite(commands.Cog):
  def __init__ (self, client):
    self.client = client

  @commands.command()
  async def Invite(self, ctx):
    support = Button(label='Suport server', url=support_link)
    invite = Button(label='Invite Me', url=invite_link)
    embed = nextcord.Embed(title='Links', color=0x303136)
    embed.add_field(name='My Invite Link', value='[Invite Me](https://discord.com/api/oauth2/authorize?client_id=943145043944960110&permissions=8&scope=bot%20applications.commands)', inline=True)
    embed.add_field(name='My Support Server Link', value='[Support Server](https://discord.com/api/oauth2/authorize?client_id=943145043944960110&permissions=8&scope=bot%20applications.commands)', inline=True)
    embed.set_footer(text='Made by Pranoy#0140')
    embed.set_thumbnail(url=ctx.author.avatar.url)
    myView = View()
    myView.add_item(support)
    myView.add_item(invite)
    await ctx.reply(embed=embed, view=myView)

def setup(client):
  client.add_cog(Invite(client))
