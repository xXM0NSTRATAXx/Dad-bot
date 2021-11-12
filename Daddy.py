import pickle
import discord
import random
from discord.flags import SystemChannelFlags

#TOKEN : CHANGE VALUE OF OBJECT TOKEN 
Token = 'ENTER'

client=discord.Client()

#Invite link to bot: https://discord.com/oauth2/authorize?client_id=776302115009462303&scope=bot

#some stuff that is needed by commands
colors=[0xff005a,0xffa500,0x00ffa5,0x005aff,0xdaff00,0x7ce47c,0x99ffff,0x0033ff,0x6666ff]


openportal=('<:glowstone:847025347555491842><:glowstone:847025347555491842><:glowstone:847025347555491842><:glowstone:847025347555491842><:glowstone:847025347555491842>\n<:glowstone:847025347555491842><:water:847025347623124992><:water:847025347623124992><:water:847025347623124992><:glowstone:847025347555491842>\n<:glowstone:847025347555491842><:water:847025347623124992><:water:847025347623124992><:water:847025347623124992><:glowstone:847025347555491842>\n<:glowstone:847025347555491842><:water:847025347623124992><:water:847025347623124992><:water:847025347623124992><:glowstone:847025347555491842>\n<:glowstone:847025347555491842><:water:847025347623124992><:water:847025347623124992><:water:847025347623124992><:glowstone:847025347555491842>\n<:glowstone:847025347555491842><:water:847025347623124992><:water:847025347623124992><:water:847025347623124992><:glowstone:847025347555491842>\n<:glowstone:847025347555491842><:glowstone:847025347555491842><:glowstone:847025347555491842><:glowstone:847025347555491842><:glowstone:847025347555491842>',
            '<:obsedian:847025346901704714><:obsedian:847025346901704714><:obsedian:847025346901704714><:obsedian:847025346901704714><:obsedian:847025346901704714>\n<:obsedian:847025346901704714><:portal:847025347731914813><:portal:847025347731914813><:portal:847025347731914813><:obsedian:847025346901704714>\n<:obsedian:847025346901704714><:portal:847025347731914813><:portal:847025347731914813><:portal:847025347731914813><:obsedian:847025346901704714>\n<:obsedian:847025346901704714><:portal:847025347731914813><:portal:847025347731914813><:portal:847025347731914813><:obsedian:847025346901704714>\n<:obsedian:847025346901704714><:portal:847025347731914813><:portal:847025347731914813><:portal:847025347731914813><:obsedian:847025346901704714>\n<:obsedian:847025346901704714><:portal:847025347731914813><:portal:847025347731914813><:portal:847025347731914813><:obsedian:847025346901704714>\n<:obsedian:847025346901704714><:obsedian:847025346901704714><:obsedian:847025346901704714><:obsedian:847025346901704714><:obsedian:847025346901704714>',
            '<:blank:847033164220071948><:endlu:847035144296595476><:endu:847035144351252500><:endru:847035143955808288>\n<:endl1:847035144274706461><:endp:847040470387261440><:endp:847040470387261440><:endp:847040470387261440><:endr1:847035893326807050>\n<:endl2:847035143969701890><:endp:847040470387261440><:endp:847040470387261440><:endp:847040470387261440><:endr2:847035893117485065>\n<:endl3:847036590895398973><:endp:847040470387261440><:endp:847040470387261440><:endp:847040470387261440><:endr3:847035893096251402>\n<:blank:847033164220071948><:endld:847036318264852530><:endd:847036318269440000><:endrd:847036318428561408>'
            )

spidermanimages=(' https://cdn.discordapp.com/attachments/655475477846425618/807957008350183474/9k.png',
                 ' https://cdn.discordapp.com/attachments/655475477846425618/807956968991752202/9k.png',
                 ' https://cdn.discordapp.com/attachments/655475477846425618/807957073530585118/2Q.png',
                 ' https://cdn.discordapp.com/attachments/655475477846425618/807957107890061342/images.png',
                 ' https://cdn.discordapp.com/attachments/655475477846425618/807957259446779954/images.png',
                 ' https://cdn.discordapp.com/attachments/655475477846425618/807957428242874368/images.png',

                 ' https://cdn.discordapp.com/attachments/655475477846425618/807957457560928306/images.png',
                 ' https://cdn.discordapp.com/attachments/655475477846425618/807957512425963530/images.png')

dudes=(' https://www.amwaycenter.com/assets/img/Dude-Perfect_Event-Image_Amway-Center_2020-13602b87ee.jpg',
       ' https://www.guinnessworldrecords.com/Images/Dude-Perfect-GWR-website-header-Nick_tcm25-569770.jpg',
       ' https://variety.com/wp-content/uploads/2019/04/dude-perfect-live-tour.jpg',
       ' https://dudeperfect.com/wp-content/uploads/2016/12/DPHQ2-Tour-Dude-Perfect.jpg',
       ' https://specials-images.forbesimg.com/imageserve/5e72a52f37d0440006bcde90/960x0.jpg?fit=scale',
       ' https://static.inspiremore.com/wp-content/uploads/2019/07/16110254/Liam-and-Nolan-Harm-with-Dude-Perfect-4.png',
       ' https://media.tenor.com/images/cb867b02ef6ad9c92a76db8df21672f2/tenor.gif')

nukes=(' https://media.npr.org/assets/img/2019/01/31/gettyimages-623841168_wide-b949880a7dda8647e88a4fd3f0c5cc5633fb734c.jpg',
       ' https://storage.googleapis.com/afs-prod/media/media:1f2476f8da914101b6ecc0676dfff701/3000.jpeg',
       ' https://foreignpolicy.com/wp-content/uploads/2019/07/GettyImages-75598466.jpg?w=800&h=532&quality=90',
       ' https://www.motherjones.com/wp-content/uploads/mushroom-cloud.gif?w=990',
       ' https://assets.bwbx.io/images/users/iqjWHBFdfxIU/ipk2a6Y376lM/v1/1000x-1.jpg')

getsuga_tensho=(' https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/c767ed37-086b-4387-8b2e-603384aea013/d5w234r-a0f35502-4aef-4938-8a1b-fda632ca1794.gif?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOiIsImlzcyI6InVybjphcHA6Iiwib2JqIjpbW3sicGF0aCI6IlwvZlwvYzc2N2VkMzctMDg2Yi00Mzg3LThiMmUtNjAzMzg0YWVhMDEzXC9kNXcyMzRyLWEwZjM1NTAyLTRhZWYtNDkzOC04YTFiLWZkYTYzMmNhMTc5NC5naWYifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6ZmlsZS5kb3dubG9hZCJdfQ.jdOAllVRCy8qx1pYwGoDZsiAlFIeNSXCrZftu_mj6YY',
                ' https://thumbs.gfycat.com/DentalAlarmedCoypu-max-1mb.gif',
                ' https://thumbs.gfycat.com/AdorableMediocreJunco-max-1mb.gif',
                ' https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/c767ed37-086b-4387-8b2e-603384aea013/d5w234r-a0f35502-4aef-4938-8a1b-fda632ca1794.gif?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOiIsImlzcyI6InVybjphcHA6Iiwib2JqIjpbW3sicGF0aCI6IlwvZlwvYzc2N2VkMzctMDg2Yi00Mzg3LThiMmUtNjAzMzg0YWVhMDEzXC9kNXcyMzRyLWEwZjM1NTAyLTRhZWYtNDkzOC04YTFiLWZkYTYzMmNhMTc5NC5naWYifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6ZmlsZS5kb3dubG9hZCJdfQ.jdOAllVRCy8qx1pYwGoDZsiAlFIeNSXCrZftu_mj6YY',
                ' https://i.postimg.cc/X7DfkHtX/ezgif-7-2e68f5f3ea0f.gif')

traps=(' https://sloanreview.mit.edu/wp-content/uploads/2014/08/FourTraps-1000-382x255.jpg',
       ' https://images-na.ssl-images-amazon.com/images/I/81M1RJkku3L._AC_SL1500_.jpg',
       ' https://hedgeconnection.com/blog/wp-content/uploads/2015/12/The-Self-Esteem-Trap.jpg',
       ' https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/mousetrap-with-hard-cheese-isolated-on-yellow-side-royalty-free-image-171303053-1564705834.jpg?crop=0.667xw:1.00xh;0.168xw,0&resize=640:*',
       ' https://374999-1254560-raikfcquaxqncofqfm.stackpathdns.com/wp-content/uploads/2019/11/top-6-chess-traps.jpg',
       ' https://assets.leevalley.com/Size4/10019/XM203-havahart-squirrel-trap-f-72.jpg',
       ' https://i.imgur.com/NqATS7C.png',
       ' https://wallpapercave.com/wp/wp6725199.jpg',
       'https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/i/0c0bd41e-4a87-4b78-b753-143f1a6b7f8a/dcg19ft-70e871f0-6d62-4721-886c-f4a4ff414a8f.jpg')

tanks=(' https://cdn.discordapp.com/attachments/821405259460509716/823125977969852456/6-3.jpg',
       ' https://cdn.discordapp.com/attachments/821405259460509716/823125997540868157/2176947_original.jpg',
       ' https://cdn.discordapp.com/attachments/821405259460509716/823126074238042112/aa3fe9e.jpg',
       ' https://cdn.discordapp.com/attachments/821405259460509716/823126074509754368/427c3b6.jpg',
       ' https://cdn.discordapp.com/attachments/821405259460509716/823126074685784084/challenger-2-upgraded-with-a-130mm-smoothbore-main-gun-rheinmetall.jpg',
       ' https://cdn.discordapp.com/attachments/821405259460509716/823126075038629898/d552db0.png',
       ' https://cdn.discordapp.com/attachments/821405259460509716/823126075399733278/dbc9c5b.jpg',
       ' https://cdn.discordapp.com/attachments/821405259460509716/823126075663187968/17daed7.jpg',
       ' https://cdn.discordapp.com/attachments/821405259460509716/823126075847606302/908d6fa.png',
       ' https://cdn.discordapp.com/attachments/821405259460509716/823126202407452672/3df581a85b8f5b408ff5293a9cd6ecba.jpg',
       ' https://cdn.discordapp.com/attachments/821405259460509716/823126202612842566/The_Tank_Museum_2214.jpg',
       ' https://cdn.discordapp.com/attachments/821405259460509716/823126202746273792/0000.m38AlteredHalftrack.jpg',
       ' https://media.discordapp.net/attachments/844441699974381579/844508587514789888/IIH.gif')

dababy=(' https://i1.sndcdn.com/avatars-r2ARDGjU1QDFzXao-9YvMUA-t500x500.jpg',
        ' https://bucket.mn2s.com/wp-content/uploads/2018/06/22150041/Da-Baby-MN2S-.png',
        ' https://media1.tenor.com/images/64db52025442f157c960f521c0c050b8/tenor.gif',
        ' https://media1.tenor.com/images/212ae6ad1f6de4ed0bf5e449d6feed41/tenor.gif?itemid=15862612',
        ' https://media.tenor.com/images/2df2bdaba405753e82c688d32665a129/tenor.gif',
        ' https://media0.giphy.com/media/1BGPUWGTN9bMAbpxN6/giphy.gif?cid=790b7611880fd9d5c75b59c9ac4aed65d691010363fe0004&rid=giphy.gif&ct=g',
        ' https://i.ytimg.com/vi/DcRLTClL5YU/maxresdefault.jpg',
        ' https://external-preview.redd.it/vF-6JDVUTfZp9J30JqQyNrnpFK72RBypErIrhRDNDxk.jpg?auto=webp&s=7a6c3bfb1bbc7326a63832c71f2236875ce2451f',
        ' https://static1.srcdn.com/wordpress/wp-content/uploads/2021/04/Among-Us-DaBaby-Role-Mod.jpg',
        ' https://wallpapercave.com/wp/wp8964251.jpg',
        ' https://wallpapercave.com/wp/wp8964262.jpg',
        ' https://i.redd.it/3ujgd7wsc8n61.png',
        ' https://i.kym-cdn.com/photos/images/original/001/909/843/c04.png',
        ' https://img.ifunny.co/images/83f3bf775898ca91d726fd7cef4bd7f8472d8dca6b8ae4b79be35a682b558fc3_1.jpg',
        ' https://i.ytimg.com/vi/RdCMRZvbSB4/maxresdefault.jpg',
        ' https://media.tenor.com/images/065774a0e47c4f09f22797c6abb0c00a/tenor.gif',
        ' https://media.tenor.com/images/8814a1fde120eae38ffed4474ed3913d/tenor.gif',
        ' https://i.imgflip.com/546wbt.gif',
        ' https://media.tenor.com/images/bf9edc50b14b2dac5ce91f5baa7b59ab/tenor.gif')

calculations=['+','-','/','*']

count=0

message=0

#help menu
menuem=discord.Embed(title='🎎\t\t\t\t\t\t\t\t\t\t🌌 Commands 🌌\t\t\t\t\t\t\t\t\t\t🏮',color=0x6633ff)
menuem.add_field(name='💫 FUN',value='1)please predict: \n2)dad say: \n3)rate [name] pp\n4)borgor\n5)weebsdie\n6)thanostwerk\n7)senko\n8)open portal',inline=True)
menuem.add_field(name='👻 GIFS / IMAGES',value='1)Send nudes\n2)Send nukes\n3)Send dudes\n4)Send traps\n5)Send tanks\n6)Monki Flip\n7)Sus\n8)Getsuga Tensho\n9)joe biden be careful!\n10)Dababy\n11)im horny',inline=True)
menuem.add_field(name='🍀 INCLUDE IN SENTENCE ',value='1)fuck\n2)party\n3)pog\n4)fast\n5)sick beats\n6)im vibing\n7)respect_F\n8)yay\n9)haha\n10)crying\n11)sexy dance\n12)lool\n13)stop pinging me\n14)wtf',inline=True)
menuem.add_field(name='💯 MATH',value='1)random number\n2)calculate:\n3)split text: TEXT\n4)rolldie(numberofdie)\n5)flipcoins(numberofcoins) \n\n',inline=True)
menuem.add_field(name='👾 MISC ',value='1)dad.addchannel.channelid\n**messages in channel when online**\n2)dad.removechannel.channelid\n**discontinue online message in channel**')
menuem.add_field(name='🚀 Invite Dad to your server :)',value='[Click me!](https://discord.com/oauth2/authorize?client_id=776302115009462303&scope=bot)',inline=False)

channels=[]

@client.event
async def on_ready():
    global channels
    with open('channels.txt','r') as chan:
        channels=eval(chan.read())
    print('=========================================================\n\t\t   DADDY IS ONLNE\n=========================================================')
    print('Sending on_ready messages in channels:')
    for channeln in channels:
        channeln=eval(channeln)
        await channeln.send('Hello children!, papa\'s back in {} :)'.format(channeln.guild))
        print('sent in [{} : #{}]'.format(channeln.guild,channeln.name))
    print('All done :)')
    botavatar=client.user.avatar_url    
    menuem.set_footer(text='Dad-bot coded by Monstrata#0782 ',icon_url=botavatar)
#   menuem.set_thumbnail(url=botavatar)
    

@client.event
async def on_message(message):

#IMP TRAITS 
    #prevents bot from making its own input
    if message.author==client.user:
        return
    me=message.content
    me=me.lower()

    #help command
    if me =='dad help':
        await message.channel.send(embed=menuem)
    
    #online check
    if me=='are you online dad?':
        await message.channel.send('yes homie im online')

    #main dad idea
    if me.startswith('im ') or me.startswith('i\'m'):
        guy=' '+me[3:]
        lnk=' https://cdn.discordapp.com/attachments/655475477846425618/806879604203061268/9k.png'
        m='hi ' + guy.replace('  ','')+',' +'Im Dad!'
        if guy.strip()=='dad':
            e=discord.Embed(title='NO IM THE DAD',color=random.choice(colors))
            e.set_image(url=lnk)
            await message.channel.send(embed=e)
        else:
            await message.channel.send(m)

#💫 FUN COMMANDS 

    #please predict:
    if 'please predict:' in me:
        m=random.choice(['no' ,'no','yes','yes','yes','no','yes','wait a sec lemme ask your mom'])
        await message.channel.send(m)
    
    
    #dad say:
    if me.startswith('dad say:'):
        send=me[8:]
        m=send
        await message.channel.send(send,tts=True)
        #await message.delete()
    
    #rate pp
    if me.startswith('rate')and 'pp' in me:
        k=random.choice(range(0,21))
        namen=me.lower()[4:-2] 
        m='8' + k*'=' + 'D'
        m=namen+'\n'+m+'\n'+str(k)+' inches long'
        penis=discord.Embed(title='Penis Length Detector',color=random.choice(colors))
        penis.add_field(name='Length of Penis Belonging to :',value=m)
        await message.channel.send(embed=penis)
    
    #borgor
    if me=='borgor':
        m='<a:borgor1:841589811110084658><a:borgor2:841589810623807498><a:borgor3:841589810611224587><a:borgor4:841589810530746389>'
        await message.channel.send(m)
    
    #weebsdie
    if me=='weebsdie':
        m='<:weebsdie1:841592379411791873><:weebsdie2:841592378069614612><a:weebsdie3:841592378129121290><a:weebsdie4:841592378254032896>'
        await message.channel.send(m)
    
    #thanostwerk
    if me=='thanostwerk':
        m='''<a:thanostwerk1:841594358121889876><a:thanostwerk2:841594365225861140><a:thanostwerk3:841594358897967134>\n<a:thanostwerk4:841594364819669012><a:thanostwerk5:841594366044143616><a:thanostwerk6:841594651412791317>\n<a:thanostwerk7:841594364365897758><a:thanostwerk8:841594366111383572><a:thanostwerk9:841594364924002314>\n<a:thanostwerk10:841594364630401064><a:thanostwerk11:841594363804909579><a:thanostwerk12:841594365931290624>'''
        await message.channel.send(m)   

    #senko
    if me=='senko':
        m='<a:senko1:841596766150590474><a:senko2:841596767056953344><a:senko3:841596766301978655>\n<a:senko4:841596766209703956><a:senko5:841596766834393130><a:senko6:841596767212142602>\n<a:senko7:841596766629789726><a:senko8:841596767132581898><a:senko9:841596766969004063>'
        await message.channel.send(m)
    
    #portal
    if me=='open portal':
        m=random.choice(openportal)
        await message.channel.send(m)

#👻 GIFS / IMAGES COMMANDS

    #send nudes
    if 'send nudes' in me:
        e=discord.Embed(title='Some hot nudes!',color=random.choice(colors))
        m=random.choice(spidermanimages)
        e.set_image(url=m)
        await message.channel.send(embed=e)
    
    #send nukes
    if me== 'send nukes':
        m=random.choice(nukes)
        e=discord.Embed(title='RUN FOR YOUR LIVES!',color=random.choice(colors))
        e.set_image(url=m)
        await message.channel.send(embed=e)
    
    #send dudes
    if me =='send dudes':
        m=random.choice(dudes)
        e=discord.Embed(title='Some dudes that would go along with you!',color=random.choice(colors))
        e.set_image(url=m)
        await message.channel.send(embed=e)

    #send traps
    if 'send traps' in me:
        m=random.choice(traps)
        e=discord.Embed(title='Dont fall for the trap',color=random.choice(colors))
        e.set_image(url=m)
        await message.channel.send(embed=e)

    #send tanks    
    if me=='send tanks':
        m=random.choice(tanks)
        e=discord.Embed(title='Heres your tank homie',color=random.choice(colors))
        e.set_image(url=m)
        await message.channel.send(embed=e)

    #Monki flip
    if 'Monki Flip' in me.title():
        m=' https://media.tenor.com/images/ceb26be382e116a9431548f178e66ba2/tenor.gif'
        e=discord.Embed(title='MONKI FLIP',color=random.choice(colors))
        e.set_image(url=m)
        await message.channel.send(embed=e)
    
    #sus
    if me.startswith('sus') :
        m=' https://i.kym-cdn.com/photos/images/masonry/001/948/851/b69.png'
        e=discord.Embed(title='WHEN THE IMPOSTER IS SUS !! ',color=0xff0000)
        e.set_image(url=m)
        await message.channel.send(embed=e)
    
    #getsuga tensho
    if me=='getsuga tensho':
        m=random.choice(getsuga_tensho)
        e=discord.Embed(title='GETSUGA TENSHO',color=0x0000ff)
        e.set_image(url=m)
        await message.channel.send(embed=e)
    
    #joe biden 
    if me=='joe biden be careful!':
        m=' https://www.thesun.co.uk/wp-content/uploads/2021/03/Joe-Biden-Fall-Gif-1-1.gif?strip=all&w=300&h=192&crop=1'
        e=discord.Embed(title='SLip Slip Slip',color=random.choice(colors))
        e.set_image(url=m)
        await message.channel.send(embed=e)
    
    #dababy
    if me=='dababy':
        e=discord.Embed(title='DABABY LESSGOOOO',color=random.choice(colors))
        e.set_image(url=random.choice(dababy))
        await message.channel.send(embed=e)
    
    #im horny
    if 'im' in me and 'horny' in me:
        m=client.get_emoji(776790610681397259)
        await message.add_reaction(m)
        e=discord.Embed(title='STOP BEING HORNY!',description='GO TO HORNY JAIL!',color=random.choice(colors))
        m=' https://i.imgur.com/WjWhGTg.gif'
        e.set_image(url=m)
        await message.channel.send(embed=e)

#💯 MATH

    #random number
    if (('random' in me) and ('number' in me)):
        m=random.choice(range(-100,100))
        await message.channel.send(m)

    #caculate:
    if me.startswith('calculate:'):
        m=''
        p=len(me)
        mel=list(me)
        for i in range (10,p):
            m=m+mel[i]
        await message.channel.send(eval(m))
    
    #split text:
    if me.startswith('split text:'):
        me=me[11:]
        me=me+' '
        me=me.split()
        e=discord.Embed(title='Your text splitted:',color=random.choice(colors))
        for i in me:
            e.add_field(name='{}'.format(i),value='===============',inline=False)
        await message.channel.send(embed=e)
    
    #Roll a die
    emojis=['1️⃣','2️⃣','3️⃣','4️⃣','5️⃣','6️⃣']
    if me.startswith('rolldie('):
        if me[8:-1].isdigit() and me[-1]==')': 
            num=int(me[8:-1])
            d={}
            if num <= 70:
                m='| 🎲 | ROLLING {} DIE  | 🎲 |\n'.format(num)
                for roller in range(num):
                    rolled=random.randint(1,6)
                    m=m+'\nRolled {} on die {} 🎲.'.format(emojis[rolled-1],str(roller+1))
                    if rolled not in d:
                        d[rolled]=1
                    else:
                        d[rolled]+=1
                su='\n| 🎲 | SUMMARY | 🎲 |'
                for i in d:
                    su=su+'\n {} appeared {} times'.format(emojis[i-1],d[i])
                m=m+'\n{}'.format(su)
                await message.channel.send(m)
            else:
                await message.channel.send('Max limit of dice is 70.')
        else:
            await message.channel.send('Enter valid number of die.')
    
    #Flip Coins
    poss=['Heads','Tails']
    k={'Heads':'🤯','Tails':'🍤'}
    if me.startswith('flipcoins('):
        if me[10:-1].isdigit() and me[-1]==')':
            num=int(me[10:-1])
            if num <=75:
                d={}
                m='| 🔴 | FLIPPING {} COINS | 🔴 |'.format(num)
                for flipper in range(num):
                    flipped=random.choice(poss)
                    m=m+'\nFLipped {} on coin {}'.format(flipped,flipper+1)
                    if flipped=='Heads':
                        m=m+'🤯'
                    else:
                        m=m+'🍤'
                    if flipped not in d:
                        d[flipped]=1
                    else:
                        d[flipped]+=1
                su='\n| 🔴 | SUMMARY | 🔴 |'
                for i in d:
                    su=su+'\n {} {} was flipped {} times'.format(i,k[i],str(d[i]))
                m=m+'\n{}'.format(su)
                await message.channel.send(m)
            else:
                await message.channel.send('You can only flip 75 coins at a time.')
        else:
            await message.channel.send('Enter valid number of coins')

#🍀 INCLUDE IN SENTENCE

    #Ratz    
    if me.startswith('ratz'):
        m=client.get_emoji(786491091801079828)
        await message.channel.send(m)

    #oof 
    if me=='oof':
        m='oof'
        await message.channel.send(m,tts=False)
    
    #wtf
    if 'wtf' in me:
        m=client.get_emoji(776322820010410004)
        await message.add_reaction(m)
        m=client.get_emoji(776322194812174386)
        await message.add_reaction(m)
        m=client.get_emoji(776322273635860480)
        await message.add_reaction(m)
    
    #boost me
    if 'boost me' in me:
        m=client.get_emoji(776721847470260254)
        await message.channel.send(m)
        await message.channel.send('you have been boosted')

    #party
    if 'party' in me:
        m=client.get_emoji(776725030439485470)
        await message.channel.send(m)

    #pog
    if  me=='pog' :
        cho=random.choice([775589415313080330,775588995337158686,775589580828049428,775589581235159091,775587533295058985])
        
        m=client.get_emoji(cho)
        await message.channel.send(m)

    #fast    
    if 'fast' in me :
        m=client.get_emoji(776726842623262730)
        await message.channel.send(m)

    #sick beats
    if 'sick' in me and 'beats' in me :         
        m=client.get_emoji(776727674353483788)
        await message.channel.send(m)

    #im vibing     
    if 'im vibing' in me :
        m=client.get_emoji(776729064261812224)
        await message.channel.send(m)
    
    #respect_f
    if 'respect_f' in me :
        m=client.get_emoji(776731039895781386)
        await message.channel.send(m)

    #yay
    if 'yay' in me :
        m=client.get_emoji(776732470640246814)
        await message.channel.send(m)

    #haha
    if 'haha' in me :
        m=client.get_emoji(776734063389573120)
        await message.channel.send(m)

    #crying
    if 'crying' in me:
        m=client.get_emoji(776734778921451530)
        await message.channel.send(m)

    #sexy dance
    if 'sexy dance' in me :
        m=client.get_emoji(776735811890708490)
        await message.channel.send(m)

    #lool
    if 'lool' in me:
        m=client.get_emoji(776737080276942849)
        await message.channel.send(m)

    #stop pinging me
    if (('stop' in me) and ('pinging' in me) and ('me' in me)):
        m=client.get_emoji(776738477672103957)
        await message.channel.send(m)

#👾 MISC COMMANDS

    #dad.addchannel.channelid
    if me.startswith('dad.addchannel.') :
        if (message.author.guild_permissions.manage_channels):
            id=me[15:]
            try:
                global channels
                id=int(id)
                x=client.get_channel(id)
                if x:
                    with open('channels.txt','r+') as chan:
                        channels=eval(chan.read())
                        if ('client.get_channel({})'.format(id) not in channels):
                            channels.append('client.get_channel({})'.format(id))
                            with open('channels.txt','w') as chan:
                                chan.write(str(channels))
                                await message.channel.send('Channel [{}:#{}] addedd successfully'.format(client.get_channel(id).guild,client.get_channel(id).name))
                                print('Channel [{}:#{}] addedd successfully'.format(client.get_channel(id).guild,client.get_channel(id).name))
                                await x.send('Added channel [{}:#{}] to updation : by user[@{}]'.format(client.get_channel(id).guild,client.get_channel(id).name,message.author))
                        else:
                            await message.channel.send('Channel [{}:#{}] already exists in updation list! '.format(client.get_channel(id).guild,client.get_channel(id).name))
                else:
                    await message.channel.send('invalid id :( [channeltype=None]')
            except:
                await message.channel.send('invalid id :( [exept]')
        else:
            await message.channel.send('Missing permission [message.author.guild_permissions.manage_channels]')

    #dad.removechannel.channelid
    if me.startswith('dad.removechannel.'):
        if (message.author.guild_permissions.manage_channels):
            id=me[18:]
            try:
                id=int(id)
                x=client.get_channel(id)
                if x:
                    with open('channels.txt','r+') as chan:
                        channels=eval(chan.read())
                        if ('client.get_channel({})'.format(id) in channels):
                            channels.remove('client.get_channel({})'.format(id))
                            with open('channels.txt','w') as chan:
                                chan.write(str(channels))
                            await message.channel.send('Channel [{}:#{}] removed from updation successfully!'.format(client.get_channel(id).guild,client.get_channel(id).name))
                            print('Channel [{}:#{}] removed successfully'.format(client.get_channel(id).guild,client.get_channel(id).name))
                            await x.send('Removed channel [{}:#{}] from updation : by user[@{}]'.format(client.get_channel(id).guild,client.get_channel(id).name,message.author))
                        else:
                            await message.channel.send('Channel [{}:#{}] does not exists in updation list! '.format(client.get_channel(id).guild,client.get_channel(id).name))
                else:
                    await message.channel,send('invalid id :(')
            except:
                await message.channel.send('invalid id :(')
        else:
            await message.channel.send('Missing permission [message.author.guild_permissions.manage_channels]')

#CLIENT TOKEN 
client.run(Token)
