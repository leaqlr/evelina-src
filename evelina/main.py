import discord
import datetime
import signal
import sys
import asyncio
import time
from loguru import logger

from modules.evelinabot import EvelinaContext, Evelina

bot = Evelina()

@bot.event
async def on_command(ctx: EvelinaContext):
    if not ctx.bot.is_ready():
        return
    start_time = time.time()
    try:
        full_command_name = ctx.command.qualified_name
        invoked_with = ctx.invoked_with
        command_start_index = len(ctx.prefix) + ctx.message.content[len(ctx.prefix):].find(invoked_with)
        command_length = command_start_index + len(invoked_with)
        arguments = ctx.message.content[command_length:].strip()
        server_id = ctx.guild.id if ctx.guild else None
        user_id = ctx.author.id
        channel_id = ctx.channel.id
        timestamp = datetime.datetime.now(datetime.timezone.utc).timestamp()
        
        # await ctx.bot.db.execute(
        #     "INSERT INTO command_history (command, arguments, server_id, user_id, channel_id, timestamp) VALUES ($1, $2, $3, $4, $5, $6)",
        #     full_command_name, arguments, server_id, user_id, channel_id, timestamp
        # )
        
        execution_time = round((time.time() - start_time) * 1000, 2)
        await ctx.bot.db.execute(
            "INSERT INTO command_stats (command, user_id, guild_id, channel_id, execution_time, timestamp) VALUES ($1, $2, $3, $4, $5, $6)",
            full_command_name,
            user_id,
            server_id,
            channel_id,
            execution_time,
            datetime.datetime.now()
        )
        
        check = await ctx.bot.db.fetchrow("SELECT * FROM avatar_privacy WHERE user_id = $1", user_id)
        if ctx.guild is not None and not ctx.guild.chunked:
            await ctx.guild.chunk(cache=True)
        if not check:
            await ctx.bot.db.execute("INSERT INTO avatar_privacy (user_id, status) VALUES ($1, $2) ON CONFLICT (user_id) DO UPDATE SET status = EXCLUDED.status", user_id, True)
            
        logger.info(f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [INFO    ] command: {full_command_name} | guild: {ctx.guild.name if ctx.guild else 'DM'} | channel: {ctx.channel.name if isinstance(ctx.channel, discord.TextChannel) else 'DM'} | user: {ctx.author} | time: {execution_time / 1000:.2f}s")
    except Exception as e:
        logger.error(f"Error logging command: {str(e)}")

@bot.event
async def on_interaction(interaction: discord.Interaction):
    if not interaction.client.is_ready():
        return
    if interaction.type == discord.InteractionType.application_command:
        if interaction.command is None:
            return
        full_command_name = interaction.command.qualified_name
        arguments = ' '.join([f"{option['name']}: {option['value']}" if 'value' in option else option['name'] for option in interaction.data.get('options', [])])
        server_id = interaction.guild.id if interaction.guild else None
        user_id = interaction.user.id
        channel_id = interaction.channel_id
        timestamp = datetime.datetime.now(datetime.timezone.utc).timestamp()
        await interaction.client.db.execute(
            "INSERT INTO command_history (command, arguments, server_id, user_id, channel_id, timestamp) VALUES ($1, $2, $3, $4, $5, $6)",
            full_command_name, arguments, server_id, user_id, channel_id, timestamp
        )

def handle_exit(*args):
    asyncio.create_task(bot.close())
    sys.exit(0)

signal.signal(signal.SIGINT, handle_exit)
signal.signal(signal.SIGTERM, handle_exit)

try:
    bot.run()
except KeyboardInterrupt:
    asyncio.run(bot.close())
except Exception as e:
    print(f"Error: {e}")
    asyncio.run(bot.close())