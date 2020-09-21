# Swiping Bot semi-automatic

Requieres python interpreter and selenium package.

This script allows you to automate the swiping process on the dating platform okcupid.com. Anyway you have to manually create an account and verify using your phone number. After you type in your email address and password in swipingbot.py start the script using 

`~$ python3 -i swipingbot.py`

This will load all imports and definitions and start the python interpreter.
Create new bot:
`>>> bot = OKCBot()`

Login:
`bot.login()`

You may enter a security code sent to your smartphone manually. 

In the past the criterium for like / dislike was the percantge of common interests shown by the website. It doesn't appear in this version but may come back in future versions.
The criterium changed the keyword vegan (here non case-sensitive). If the keyword is content of the biography displayed, the bot will hit like. You can search and decide using
`>>> bot.testmatch()`

To make 1000 decisions use
`>>> bot.testmatchloop()`


Please notice, that there are so many steps you have to take manually, because this api is UNSTABLE. Most common error is that the bot cannot find the button to click. From my experience the xpath may change from time to time and you will have to replace the path in the code.

Creative Commons
You may change, remix and share this content for non commercial purpose without reciting theta-computing.net.
