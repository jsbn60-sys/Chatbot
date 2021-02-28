from programy.clients.embed.basic import EmbeddedBasicBot
from programy.clients.embed.basic import EmbeddedDataFileBot
files = {'aiml': ['Easybot/storage/categories']}
my_bot = EmbeddedDataFileBot(files, defaults=True)
print("Response = %s" % my_bot.ask_question("Hi"))

