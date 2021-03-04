# Google-Cloud-Dialog-Flow
Google Cloud Dialog Flow with Python client


1.Create new agent-->testbot

2.Activate smart talk for fun.

3.Lets create intent and entities if needed.
      
      intents--> anything which you want to train the bot.
      fulfillment-->we connect our bot to backend flask with the help of fulfillment.
      integrations--> integrate the bot with telegram,webpaage,skype etc.

4.Create intents for the interaction purposes and then we can connect with backend flask.

5.Lets connect the dialogflow with the flask backend.

6.First of all we need to understand that.we run our flask code on the local server...if we want to run it on the globally then we need to use public ip and expose the ports ....which is not a ideal way for security purposes.

7.For the testing purposes..we are using ngrok here.
    steps to install ngrok:
        
        1.download ngrok from official website
        for linux-> https://ngrok.com/download
        2.connect ngrok with flask port with command--> ./ngrok http 5000

8.Copy the ngrok link and paste it into the fulfillment webhook url and enable the webhook.
    thats done....in this way we can work with  dialogflow with flask as a backend.
