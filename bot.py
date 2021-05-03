import discord
from discord.ext import commands
import pyfiglet
import hashlib
import random
from colorama import Fore, Back, Style
import time
import colorama

client = discord.Client()

defaultToken = 'ODM4Njg0ODE2MTg5OTQ3OTA1.YI-sGg.2vkmcR-bJReTOPidilztNhzqw7U'
version = '2.1.5b'
year = '2021'
versionandyear = f'{version}#{year}'
github = 'http://www.github.com/IkonoDim-App-Factory/SpamBot'
owner = 'IkonoDim'
auth = hashlib.md5(str(random.randint(100, 9999)).encode()).hexdigest()
command = f'{Fore.LIGHTGREEN_EX}.verify {versionandyear}{auth} {Style.RESET_ALL}'
commandondc = '.verify {versionandyear}{auth}'
fullauth = f'{versionandyear}{auth}'

print(pyfiglet.print_figlet('SpamBot'))
print(f'version {version} ({year})')
print(f'made with :heart: by {owner}')
print('for new version look on github:')
print(github)
print(' ')

token = input("Bot's Token: ")
bot = commands.Bot('.')

if token == 'default':
    token = defaultToken

else:
    pass

print(f'Please enter the following command into your Server:')
print('')
print(command)
print('')


@bot.command()
async def verify(ctx, token1):
    input(f'{Fore.LIGHTGREEN_EX}Command detected.{Style.RESET_ALL} Please press enter')
    global commandondc

    if token1 == fullauth:
        while 1:
            print(' ')
            print(f'{Fore.LIGHTRED_EX}spam:{Style.RESET_ALL}{Style.BRIGHT} send a message many times \r\n {Style.RESET_ALL}'
                           f'{Fore.CYAN}del:{Style.RESET_ALL}{Style.BRIGHT} delete all channels in the Server{Style.RESET_ALL}')
            choice = input(f'{Fore.LIGHTYELLOW_EX}Choice:{Style.RESET_ALL} ')

            if choice == 'spam':
                times = int(input('How many times to send message: '))
                message = input('Please enter your Message: ')
                for i in range(1, times + 1):
                    await ctx.send(message)

            if choice == 'create':
                channel =  await guild.create_text_channel('cool-channel')
                channel


            if choice == 'del':
                for c in ctx.guild.channels:
                    await c.delete()
                    print(' ')
                    print(f'{Fore.LIGHTRED_EX}Deleted {Style.BRIGHT}{Fore.LIGHTYELLOW_EX}{c}{Style.RESET_ALL}')
    else:
        print(f'\r\n {Fore.LIGHTRED_EX}{Style.BRIGHT}ERROR:{Fore.RED} wrong auth{Style.RESET_ALL}')
        print(f'{Fore.LIGHTGREEN_EX}{Style.BRIGHT}please try again{Style.RESET_ALL}')
        print(' ')
        print(f'Command:')
        print(command)


bot.run(token)
