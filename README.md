# episodes_released_watched
With this script you can create a dataframe where you can see how many episodes have been released for each anime you haven't watched yet. It uses MyAnimeList API and scrapes gogoanime to view if the episodes have been uploaded there already

Before running make sure to replace the 'PUT YOUR ... HERE' with your actual things. For the client id go to https://myanimelist.net/clubs.php?cid=13727

To get your own list, you might need to use OAuth. Follow these steps:

1. Make a server using the python flash library and run it, I suggest using port 5000 as I did the same in the code

2. Get your OAuth link from the authlink classmethod in MyBot

3. Open the link in the browser and click allow. You'll be redirected to a link starting with 127.0.0.1/...

4. Change the link in the following way. Let's say you used port 8000 in the script for step 1, change the link into 127.0.0.1:8000/

5. Go back to the running server python script. A code will be printed with the state that was created in the bot's constructor. E.g. code=...&state=...

6. Copy the code

7. Make a post request to request the token using the get_token method in the bot class

8. give the authtoken classvariable the value of the token
