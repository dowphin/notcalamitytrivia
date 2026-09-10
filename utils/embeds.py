from discord import Embed, Color

def build_mystic_embed(title, description):
    embed = Embed(title=title, description=description, color=Color.fuchsia())
    embed.set_author(name="Mystic Slime", icon_url="https://terraria.wiki.gg/images/Mystic_Slime.png?ba659a")
    return embed

def build_nerdy_embed(title, description):
    embed = Embed(title=title, description=description, color=Color.blue())
    embed.set_author(name="Nerdy Slime", icon_url="https://terraria.wiki.gg/images/Nerdy_Slime.png?846f41")
    return embed

def build_diva_embed(title, description):
    embed = Embed(title=title, description=description, color=Color.from_rgb(245, 171, 224))
    embed.set_author(name="Diva Slime", icon_url="https://terraria.wiki.gg/images/Diva_Slime.gif?fec9c4")
    return embed

def build_cool_embed(title, description):
    embed = Embed(title=title, description=description, color=Color.from_rgb(0, 255, 0))
    embed.set_author(name="Cool Slime", icon_url="https://terraria.wiki.gg/images/Cool_Slime.png?799de9")
    return embed

def build_surly_embed(title, description, footer=""):
    embed = Embed(title=title, description=description, color=Color.from_rgb(247, 124, 198))
    embed.set_author(name="Surly Slime", icon_url="https://terraria.wiki.gg/images/Surly_Slime.png?9dbe7d")
    return embed