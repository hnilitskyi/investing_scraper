Investing scraper

Project tracks indices from the Investing website, allowing users to specify which indices they want to monitor by setting the corresponding value to True in the indexes dictionary. Additionally, users need to provide their Telegram bot token and chat ID for receiving notifications. Instructions on how to obtain these are provided in the "How to Use" section below. The script checks for changes in the selected indices at specified time intervals and sends Telegram messages to notify the user of any updates.

     Features
Dynamic Index Tracking: The script dynamically scrapes the latest index data from the Investing website, focusing on the indices specified by the user.
Telegram Integration: Users can receive notifications about index changes via Telegram. They need to provide their Telegram bot token and chat ID for the script to send messages.
Automatic Updates: The script periodically checks for changes in the selected indices and sends Telegram messages to notify the user if any changes are detected.
     
     How to Use

Make sure to install:
BeautifulSoup4, requests, python-telegram-bot

Set Index Tracking: In the indexes dictionary, set the value to True for each index you want to track.
Telegram Bot Setup:
Create a Telegram bot using BotFather (https://core.telegram.org/bots#botfather).
Obtain the bot token provided by BotFather.
Find your chat ID by sending a message to your bot and visiting the following URL: https://api.telegram.org/botYourBotToken/getUpdates. Look for the "chat" section to find your chat ID.
Update Script Parameters:
Replace the 'token_for_chatbot' variable with your Telegram bot token.
Replace the 'id_for_chatbot' variable with your chat ID.
Specify the refresh time in seconds according to your preference.
Run the Script: Execute the Python script. It will start monitoring the specified indices and send Telegram notifications for any changes detected.
