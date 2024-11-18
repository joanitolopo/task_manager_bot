import discord
from discord.ext import commands
from database import init_database, add_task_db, delete_task_db, show_tasks_db, complete_task_db, check_task_exists, check_tasks_exist_noid

# initialize database
init_database()

# init bot discord
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def add_task(ctx, description: str):
    "adds a task with a  description <description>"
    
    if check_tasks_exist_noid():
        await ctx.send("There are already tasks created!")
    else:
        # If no tasks exist, proceed to add the new task
        info = add_task_db(description=description)
        await ctx.send(f"Task added: {description}")

@bot.command()
async def delete_task(ctx, task_id: int):
    "deletes task with the <task_id> identifier"
    
    # Check if the task_id exists in the database
    task_exists = check_task_exists(task_id)
    if not task_exists:
        await ctx.send(f"Task with ID {task_id} not found. Please check the task ID.")
        return
    
    info = delete_task_db(task_id)
    await ctx.send(info)

@bot.command()
async def show_tasks(ctx):
    "shows a list of all tasks"
    tasks = show_tasks_db()
    # print(tasks)

    template = "ID: {ID}\nTask: {task}\nStatus: {status}\n"
    # parse list of task
    for task in tasks:
        info = template.format(ID=task["ID"], task=task["Description"], status=task["Status"])
        if task["ID"] == "unavailable":
            info = info + "Please add new task"
            await ctx.send(info)
        else:
            await ctx.send(info)
        

@bot.command()
async def complete_task(ctx, task_id: int):
    "marks the task with the <task_id> identifier"
    
    # Check if the task_id exists in the database
    task_exists = check_task_exists(task_id)
    if not task_exists:
        await ctx.send(f"Task with ID {task_id} not found. Please check the task ID.")
        return
    
    info = complete_task_db(task_id=task_id)
    await ctx.send(info)


# get token from txt
with open("token.txt", "r") as f:
    token = f.read()

bot.run(token)