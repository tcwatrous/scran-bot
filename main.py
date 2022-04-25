import discord
import os
#import tweepy
import random


listOfTweetURLs = [
  'best_brekkie/status/1518159953202139136', 'best_brekkie/status/1516411767391465487', 'footyscran/status/1517789255724113920', 'pubgrub_/status/1516067144634703877', 'footyscran/status/1516482099037016071', 'footyscran/status/1516844460453285894', 'footyscran/status/1516495763676798978', 'sportscran/status/1515758688526643206', 'footyscran/status/1515002465141370880', 'footyscran/status/1518255209201475584', 'footyscran/status/1516151067033100300', 'footyscran/status/1517430658431389697', 'footyscran/status/1518305926729580547', 'footybevs/status/1516400882551775236', 'best_brekkie/status/1517419830986649601', 'footyscran/status/1515978051733053440', 'pubgrub_/status/1516733420168175625', 'footyscran/status/1517479087345917960', 'footyscran/status/1515323786580705287', 'pubgrub_/status/1515976078313070596', 'footyscran/status/1516701151743385608', 'footyscran/status/1515117154051444737', 'pubgrub_/status/1515009772612984834', 'footyscran/status/1517171881660538880', 'footyscran/status/1516334030291181568', 'pubgrub_/status/1517122733854896128', 'footyscran/status/1516112258560151552', 'footyscran/status/1516812047899676682', 'footyscran/status/1514961478788526085', 'footyscran/status/1516455830429872142', 'footyscran/status/1517812740206825475', 'footybevs/status/1517156972327440384', 'pubgrub_/status/1515234122750476293', 'footyscran/status/1518285404121743361', 'footyscran/status/1517917461697466368', 'sportscran/status/1517767886433132544', 'footyscran/status/1515744506024448000', 'footyscran/status/1517843190149230592', 'pubgrub_/status/1515693191390978061', 'best_brekkie/status/1516688596543102976', 'footyscran/status/1518231704690905088', 'footyscran/status/1516876321783267328', 'footyscran/status/1515241051589648386', 'best_brekkie/status/1517838047173394432', 'best_brekkie/status/1515599111680147456', 'pubgrub_/status/1518242274295046147', 'footyscran/status/1517111671835308033', 'footyscran/status/1515692995068284928', 'pubgrub_/status/1515775492602961939', 'footyscran/status/1515642724283789316', 'pubgrub_/status/1516372212575518720', 'cricteas/status/1515263140811972610', 'footyscran/status/1518158883625312256', 'footyscran/status/1517550876696719363', 'pubgrub_/status/1516794775093100550', 'pubgrub_/status/1515630611293216770', 'best_brekkie/status/1515283949106475008', 'footyscran/status/1517208828395540480', 'pubgrub_/status/1517874245853982721', 'pubgrub_/status/1517911406284513280', 'footyscran/status/1516060023373320201', 'footyscran/status/1515046085676437520', 'footyscran/status/1516131071506599938', 'footyscran/status/1516013941461245952', 'footyscran/status/1516076159007612938', 'footyscran/status/1515667255815720964', 'best_brekkie/status/1514890199637139458', 'footyscran/status/1515802525554909191', 'footyscran/status/1514982118576775173', 'best_brekkie/status/1515954167747072001', 'pubgrub_/status/1514886399656407046', 'footyscran/status/1516749511867121669', 'footyscran/status/1515722362255204356', 'footyscran/status/1518333759292071942', 'footyscran/status/1515285851147808775', 'footybevs/status/1516832639524683783', 'pubgrub_/status/1517225678147567616', 'best_brekkie/status/1517078731914895360', 'footyscran/status/1517234756009738240', 'footyscran/status/1515027212453531658', 'footyscran/status/1514891734341373961', 'footyscran/status/1517879669823086593', 'footyscran/status/1515782344187207686', 'footyscran/status/1514942167525072908', 'footyscran/status/1517261961037238275', 'pubgrub_/status/1516517602050424834', 'footyscran/status/1515013423813251078', 'footyscran/status/1515071762542833666', 'footyscran/status/1516093467725910024', 'footyscran/status/1517066119345025024', 'footyscran/status/1516193396678922253', 'footyscran/status/1518199174193463297', 'footyscran/status/1515351751452409863', 'footyscran/status/1515762585806807047', 'footyscran/status/1516387385197711368' ]
"""
listOfTweetURLs = [
'footyscran/status/1517234756009738240',
'footyscran/status/1517208828395540480',
'footyscran/status/1517171881660538880',
'footyscran/status/1517111671835308033',
'footyscran/status/1517066119345025024',
'footyscran/status/1516876321783267328',
'footyscran/status/1516844460453285894',
'footyscran/status/1516812047899676682',
'footyscran/status/1516749511867121669',
'footyscran/status/1516701151743385608',
'footyscran/status/1516495763676798978',
'footyscran/status/1516482099037016071',
'footyscran/status/1516455830429872142',
'footyscran/status/1516387385197711368',
'footyscran/status/1516334030291181568',
'footyscran/status/1516193396678922253',
'footyscran/status/1516151067033100300',
'footyscran/status/1516131071506599938',
'footyscran/status/1516112258560151552',
'footyscran/status/1516093467725910024',
'footyscran/status/1516076159007612938',
'footyscran/status/1516060023373320201',
'footyscran/status/1516013941461245952',
'footyscran/status/1515978051733053440',
'footyscran/status/1515802525554909191',
'footyscran/status/1515782344187207686',
'footyscran/status/1515762585806807047',
'footyscran/status/1515744506024448000',
'footyscran/status/1515722362255204356',
'footyscran/status/1515692995068284928',
'footyscran/status/1515667255815720964',
'footyscran/status/1515642724283789316',
'footyscran/status/1515351751452409863',
'footyscran/status/1515323786580705287',
'footyscran/status/1515285851147808775',
'footyscran/status/1515241051589648386',
'footyscran/status/1515117154051444737',
'footyscran/status/1515071762542833666',
'footyscran/status/1515046085676437520',
'footyscran/status/1515027212453531658',
'footyscran/status/1515013423813251078',
'footyscran/status/1515002465141370880',
'footyscran/status/1514982118576775173',
'footyscran/status/1514961478788526085',
'footyscran/status/1514942167525072908',
'footyscran/status/1514891734341373961',
'sportscran/status/1515758688526643206',
'cricteas/status/1515263140811972610',
'footybevs/status/1517156972327440384',
'footybevs/status/1516832639524683783',
'footybevs/status/1516400882551775236',
'best_brekkie/status/1517078731914895360',
'best_brekkie/status/1516688596543102976',
'best_brekkie/status/1516411767391465487',
'best_brekkie/status/1515954167747072001',
'best_brekkie/status/1515599111680147456',
'best_brekkie/status/1515283949106475008',
'best_brekkie/status/1514890199637139458',
'pubgrub_/status/1517225678147567616',
'pubgrub_/status/1517122733854896128',
'pubgrub_/status/1516794775093100550',
'pubgrub_/status/1516733420168175625',
'pubgrub_/status/1516517602050424834',
'pubgrub_/status/1516372212575518720',
'pubgrub_/status/1516067144634703877',
'pubgrub_/status/1515976078313070596',
'pubgrub_/status/1515775492602961939',
'pubgrub_/status/1515693191390978061',
'pubgrub_/status/1515630611293216770',
'pubgrub_/status/1515234122750476293',
'pubgrub_/status/1515009772612984834',
'pubgrub_/status/1514886399656407046'
]
"""
client = discord.Client()




@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower()=='fs':
      await message.channel.send("Flip sucks!")
    if message.content.startswith('$scran'):
      await message.channel.send("its .scran you ding dong")
    if message.content.startswith('.moretweets'):
      await message.channel.send("send new tweets you want added to cav with the following format ```'[account]/status/[id]',```")
    if message.content.startswith('.scran'):
      random_index = random.randint(0,len(listOfTweetURLs)-1)
      await message.channel.send('https://twitter.com/'+listOfTweetURLs[random_index])

client.run(os.environ['TOKEN'])


#1514616897911676937
#api.get_status(1514616897911676937)
#tw = tweepy.Client(os.environ['BEARER_TOKEN'])

#tweets = tw.get_users_tweets(id = 1320495373769723904, exclude = 'replies,retweets', max_results = 100, tweet_fields='id')

#print(tweets.data)
#print(tweets.data[0].id)
#for tweet in tweets.data:
#  print(str(tweet.id) + ",")

#random_index_test = random.randint(0,len(listOfTweetIds)-1)
#print(listOfTweetIds[random_index_test])