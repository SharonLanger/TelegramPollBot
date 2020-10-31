# Smart polls telegram bot

![](https://core.telegram.org/file/811140763/1/PihKNbjT8UE/03b57814e13713da37)

## Connecting your bot to smart polls:
In the properties file fill the two properties needed:
- URL to the smart-polls-backend
- Your bot TOKEN.

### Getting telegram bot TOKEN:

A bot TOKEN is the bot secret key with it you will change your bot code.
You get it when creating a new bot.
How to create a new bot?
Well, telegram have a bot for that. Just talk to BotFather.

All you need to do is:
- Go to the BotFather(look him up in telegram)
- Create a new bot: /newbot
- Give it a name
- Give it a user_name(must end with the word bot)
- Copy the HTTP API the bot gave you
- enable inline for your bot: /setinline (Our bot needs it to display the polls options)

That is it 

If you want more info, please follow one of the two:
- https://docs.microsoft.com/en-us/azure/bot-service/bot-service-channel-connect-telegram?view=azure-bot-service-4.0
- https://www.process.st/telegram-bot/

Create a new bot, give it a name, add a photo and a bunch more w/o even writing a code.
And, in the end save the token of your bot in order to access his HTTP API.
You will need to access the HTTP API so you can send your bot commands via REST.

If you want to experement with the bot you can do so by sending requests to your bot URL.
The prefix of any telegram bot is: 
- https://api.telegram.org/bot

So the full prefix of your bot will be: 
- https://api.telegram.org/bot + {{TOKEN}}

Note: The HTTP API token is also needed for the properties file in the backend microservice.

### Misc

I recommend using the python-telegram-bot library: 
- https://github.com/python-telegram-bot/python-telegram-bot

Please see the examples folder to see some basic use of the API and bots.  

