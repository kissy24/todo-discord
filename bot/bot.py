import discord
import requests
import toml
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

# Discordボットの設定
bot = commands.Bot(command_prefix="!", intents=intents)


# ボットの起動時の処理
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")


@bot.command()
async def add_todo(ctx, *, title: str):
    """コマンド：!add_todo [内容]"""
    # Todoを追加する処理
    response = requests.post("http://127.0.0.1:8000/tasks", json={"title": title})
    if response.status_code == 200:
        await ctx.send("Todo added successfully")
    else:
        await ctx.send("Failed to add todo")


@bot.command()
async def delete_todo(ctx, task_id: int):
    """コマンド：!delete_todo [番号]"""
    # Todoを削除する処理
    response = requests.delete(f"http://127.0.0.1:8000/tasks/{task_id}/")
    if response.status_code == 200:
        await ctx.send("Todo deleted successfully")
    else:
        await ctx.send("Failed to delete todo")


# Discordボットを起動
config = toml.load(open("token.toml"))
bot.run(config["tool"]["discord"]["bot_token"])
