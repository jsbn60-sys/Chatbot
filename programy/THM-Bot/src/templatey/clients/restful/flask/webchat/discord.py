from programy.clients.embed.basic import EmbeddedBasicBot
files = {'aiml': ['Chatbot/Easybot/storage/categories']}
my_bot = EmbeddedDataFileBot(files, defaults=True)
print("Response = %s" % my_bot.ask_question("Hello"))
