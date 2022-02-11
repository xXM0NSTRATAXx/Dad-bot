import discord
import operator
from discord import activity
from discord.ext import commands
import random
from discord.flags import Intents

Token = '-----------> Token Goes here <----------'

#Stuff that bot needs to function properly
colours=[0xff80ed,0x5ac18e,0xffa500,0x990000,0x2acaea,0x0ff1ce,0xbada55,0xf7347a,0x0000ff,0xff6666,0xff7f50,0xb6fcd5]

emojis=['1️⃣','2️⃣','3️⃣','4️⃣','5️⃣','6️⃣']

responses=("It is certain.",
    "It is decidedly so.",
    "Without a doubt.",
    "Yes - definitely.",
    "You may rely on it.",
    "As I see it, yes.",
    "Most likely.",
    "Outlook good.",
    "Yes.",
    "Signs point to yes.",
    "Reply hazy, try again.",
    "Ask again later.",
    "Better not tell you now.",
    "Cannot predict now.",
    "Concentrate and ask again.",
    "Don't count on it.",
    "My reply is no.",
    "My sources say no.",
    "Outlook not so good.",
    "Very doubtful.")

bakas=("https://media1.tenor.com/images/856a34bc945f740b7c4f31dfec044620/tenor.gif?itemid=18059578",
    "https://media1.tenor.com/images/e6ee9ecaf46a515f833173860e4c550b/tenor.gif?itemid=13893185",
    "https://media1.tenor.com/images/06218cff28c7e691731bd5ac6284da18/tenor.gif?itemid=13265129",
    "https://media1.tenor.com/images/e32a01457c5db0e9424dea4de4a46585/tenor.gif?itemid=14364932",
    "https://media1.tenor.com/images/81b64932f764e44c0c2316c68703a46a/tenor.gif?itemid=5897515",
    "https://media1.tenor.com/images/88819a7e457c5dc3f124b9d6bb720edc/tenor.gif?itemid=5586968",
    "https://media1.tenor.com/images/2370a6a8ff4e6a9b881cda06c94b7847/tenor.gif?itemid=17941187",
    "https://media1.tenor.com/images/406ef128433bb6b0d62ba092ed5ec67d/tenor.gif?itemid=14954653",
    "https://media1.tenor.com/images/a3108070c1fe6b40a99e5add546e3423/tenor.gif?itemid=9441674",
    "https://media1.tenor.com/images/aa301f667fd42228343a5fcc60b1373c/tenor.gif?itemid=9694074",
    "https://c.tenor.com/4aBGKXpAzygAAAAC/ahagon-new-game.gif")

bites=("https://media1.tenor.com/images/89f6c275fb5cdf44c7b75c92306b8d66/tenor.gif?itemid=12652308",
    "https://media1.tenor.com/images/7ba6e66b663737212ae62ced08ec99e7/tenor.gif?itemid=17055139",
    "https://media1.tenor.com/images/e2c3b97c6bcf475ec0eed309c553d719/tenor.gif?itemid=18059464",
    "https://media1.tenor.com/images/6ab39603ef0dd6dbfc78ba20885b991f/tenor.gif?itemid=8220087",
    "https://media1.tenor.com/images/6b42070f19e228d7a4ed76d4b35672cd/tenor.gif?itemid=9051585",
    "https://media1.tenor.com/images/7afe518504b71a3ca71770f8ac58b73a/tenor.gif?itemid=12897780",
    "https://media1.tenor.com/images/f308e2fe3f1b3a41754727f8629e5b56/tenor.gif?itemid=12390216",
    "https://media1.tenor.com/images/8a853337af58ee7c16d05d6e7c5ce31d/tenor.gif?itemid=4966068",
    "https://media1.tenor.com/images/785facc91db815ae613926cddb899ed4/tenor.gif?itemid=17761094",
    "https://media1.tenor.com/images/432a41a6beb3c05953c769686e8c4ce9/tenor.gif?itemid=4704665",
    "https://i.nobuwu.dev/nyaa/bite/0.gif",
    "https://i.nobuwu.dev/nyaa/bite/3.gif",
    "https://i.nobuwu.dev/nyaa/bite/4.gif",
    "https://i.nobuwu.dev/nyaa/bite/5.gif",
    "https://i.nobuwu.dev/nyaa/bite/11.gif",
    "https://i.nobuwu.dev/nyaa/bite/14.gif",
    "https://i.nobuwu.dev/nyaa/bite/16.gif",
    "https://i.nobuwu.dev/nyaa/nom/15.gif")

blowkisses=("https://media1.tenor.com/images/74e1894ce5b90c47d54896d3c657d143/tenor.gif?itemid=17686659",
    "https://media1.tenor.com/images/f24035839104cad2d18246e99ab384a6/tenor.gif?itemid=15780174",
    "https://media1.tenor.com/images/e858678426357728038c277598871d6d/tenor.gif?itemid=9903014",
    "https://media1.tenor.com/images/f99327c0ac523c3311de3c5dab5e6af1/tenor.gif?itemid=16349463",
    "https://media1.tenor.com/images/54d5874399731360b520956a1352ba59/tenor.gif?itemid=17583339",
    "https://media1.tenor.com/images/7dd0ca2d6a37361aa8a7760aec8db364/tenor.gif?itemid=18504614",
    "https://media1.tenor.com/images/bfa0fbd263bb9f3e503ede07a5808143/tenor.gif?itemid=11539049",
    "https://media1.tenor.com/images/189f0c46c59826885b0053a8355d79bf/tenor.gif?itemid=17701920",
    "https://media1.tenor.com/images/63258f26e4500bab94c5f15665daa48b/tenor.gif?itemid=16231037",
    "https://media1.tenor.com/images/9fd866e042f3e7cc214d858ecddbf659/tenor.gif?itemid=17719284")

blushes=("https://media1.tenor.com/images/4c03573f06a1bd8841976abdafd16d26/tenor.gif?itemid=15711893",
    "https://media1.tenor.com/images/f72035e032125a5395883b8d68d9df5d/tenor.gif?itemid=16149781",
    "https://media1.tenor.com/images/84307582253a96e4552d20e3ecef3a33/tenor.gif?itemid=5531498",
    "https://media1.tenor.com/images/5ea40ca0d6544dbf9c0074542810e149/tenor.gif?itemid=14841901",
    "https://media1.tenor.com/images/71015cf10d2bc6ddc6c2dd0d7b294277/tenor.gif?itemid=9096269",
    "https://media1.tenor.com/images/aef3bb8700d90d89f26bfff1e9acb730/tenor.gif?itemid=20554069",
    "https://media1.tenor.com/images/5d26675f934b0df29bfe08c5ebfa113c/tenor.gif?itemid=20554121",
    "https://media1.tenor.com/images/0cf36fa0271f4318d1c372321d0398be/tenor.gif?itemid=20554208",
    "https://media1.tenor.com/images/51f92d00c1fe58f31a9c774a42bc9451/tenor.gif?itemid=20554243",
    "https://media1.tenor.com/images/684b987297d7352e93a5f3ed7f0ec2c6/tenor.gif?itemid=20554365",
    "https://i.nobuwu.dev/nyaa/blush/2.gif",
    "https://i.nobuwu.dev/nyaa/blush/3.gif",
    "https://i.nobuwu.dev/nyaa/blush/4.gif",
    "https://i.nobuwu.dev/nyaa/blush/5.gif",
    "https://i.nobuwu.dev/nyaa/blush/10.gif",
    "https://i.nobuwu.dev/nyaa/blush/11.gif",
    "https://i.nobuwu.dev/nyaa/blush/12.gif",
    "https://i.nobuwu.dev/nyaa/blush/13.gif",
    "https://i.nobuwu.dev/nyaa/blush/14.gif",
    "https://i.nobuwu.dev/nyaa/blush/15.gif",
    "https://i.nobuwu.dev/nyaa/blush/20.gif",
    "https://i.nobuwu.dev/nyaa/blush/21.gif",
    "https://i.nobuwu.dev/nyaa/blush/22.gif",
    "https://i.nobuwu.dev/nyaa/blush/25.gif",
    "https://i.nobuwu.dev/nyaa/blush/26.gif")

revs=('https://cdn.discordapp.com/attachments/889229807097880621/910597130413019146/1582340002773.jpg',
    'https://media.discordapp.net/attachments/889229807097880621/910597549042323546/888eae2b4b6ad5e2cdc822bdbfc96c4f.png?width=384&height=586',
    'https://media.discordapp.net/attachments/889229807097880621/910598134491664394/09382e372daa787e0a34942ec576dcd6.png?width=382&height=586',
    'https://cdn.discordapp.com/attachments/889229807097880621/910598223725465620/6e0ff3f1d054a39348a428f99b455e7d.png',
    'https://cdn.discordapp.com/attachments/889229807097880621/910598493956091914/8a650dbffd5d35fcfa81816bcff1bbf9.png',
    'https://cdn.discordapp.com/attachments/889229807097880621/910598542266097706/latest.png',
    'https://media.discordapp.net/attachments/889229807097880621/910598600390750268/flat750x075f-pad750x1000f8f8f8.png?width=439&height=585',
    'https://cdn.discordapp.com/attachments/889229807097880621/910598775733616691/dtncymd2b5y41.png',
    'https://cdn.discordapp.com/attachments/889229807097880621/910598833564684379/thumb_i-just-made-this-uno-reverse-card-for-cute-no-62618252.png',
    'https://cdn.discordapp.com/attachments/889229807097880621/910598892645679114/reverse-uno.png',
    'https://cdn.discordapp.com/attachments/889229807097880621/910599039521808434/39aa73cf65e0db99ff5468517a8575bf0f8ac554763a05e21a9433d3b3b3316a_1.png',
    'https://cdn.discordapp.com/attachments/889229807097880621/910599272729296906/keiuts0u62x31.png',
    'https://cdn.discordapp.com/attachments/844441699974381579/912417563483451412/xe1lgjqkxw501.png',
    'https://cdn.discordapp.com/attachments/844441699974381579/912417323430854736/image0-2-1.jpg',
    )

bonks=("https://media1.tenor.com/images/dc4329d27745a6707219cb658f5b2c46/tenor.gif?itemid=18191826",
    "https://media1.tenor.com/images/743f16f3d1233ce521e45d1d843b2779/tenor.gif?itemid=20598611",
    "https://media1.tenor.com/images/78d620fdf79cb1e8206f72a4de693fd3/tenor.gif?itemid=20598599",
    "https://media1.tenor.com/images/194c7b9dd6fdc1e1580afca803a26d3a/tenor.gif?itemid=16570141",
    "https://media1.tenor.com/images/bc8d9395166b82df05d590459f184f2d/tenor.gif?itemid=16061390",
    "https://media1.tenor.com/images/119ca32322ba24e4ffc4f0d84a6839f1/tenor.gif?itemid=17402810",
    "https://media1.tenor.com/images/c70e5c67f32b126e8d62bb1ee099aec4/tenor.gif?itemid=17872492",
    "https://media1.tenor.com/images/544fecdfc2d904cf9b1e36994d3a007d/tenor.gif?itemid=19740955",
    "https://media1.tenor.com/images/e140a5061bca97f0c8b9932f12b96a00/tenor.gif?itemid=20598630",
    "https://media1.tenor.com/images/7ef889cb06c3adca3ecfe9b536d95bde/tenor.gif?itemid=20598645",
    "https://i.nobuwu.dev/nyaa/slap/16.gif")

boreds=("https://media1.tenor.com/images/b353dcd4eb7b36ae6ce50e83824dc66e/tenor.gif?itemid=11579685",
    "https://media1.tenor.com/images/2ed5a360a233ad45bf7ec122476c0fe4/tenor.gif?itemid=15916939",
    "https://media1.tenor.com/images/a1d29d4e4181e563db8c07353ba90f6f/tenor.gif?itemid=13095377",
    "https://media1.tenor.com/images/edd5474d03a0756e45c8c42c2be08043/tenor.gif?itemid=15496297",
    "https://media1.tenor.com/images/fe42bcedb6118731aaf056e493556d3f/tenor.gif?itemid=4583775",
    "https://media1.tenor.com/images/d63e9b62702a9c8ff079c5a289a2ec19/tenor.gif?itemid=12518589",
    "https://media1.tenor.com/images/3687130d2490d4011c088e31ba38b4f4/tenor.gif?itemid=5897451",
    "https://media1.tenor.com/images/da89d9a8aeb28fd73f0c8d17c675bd30/tenor.gif?itemid=15021625",
    "https://media1.tenor.com/images/2771430a3bad24eae2a712ffe621a599/tenor.gif?itemid=17778357",
    "https://media1.tenor.com/images/717ec8721e21b9e0f989a1e205e4b5ba/tenor.gif?itemid=15963940")

byes=("https://media1.tenor.com/images/5ec19a5bfed4ac58ceb52e2fc265a3e3/tenor.gif?itemid=13701943",
    "https://media1.tenor.com/images/86a81a4a4e63afc759800f452b396787/tenor.gif?itemid=15151699",
    "https://media1.tenor.com/images/33fdd8dc7564b56d5905428484f5aee4/tenor.gif?itemid=5604313",
    "https://media1.tenor.com/images/6c8a17b6f1754975f6e1bff224bfcb58/tenor.gif?itemid=16222444",
    "https://media1.tenor.com/images/0f6922ce0e6bee7ddf0ecbab7cb4a053/tenor.gif?itemid=9214454",
    "https://media1.tenor.com/images/cddf900fe24300e30e162e4d1cbf0d7e/tenor.gif?itemid=17381662",
    "https://media1.tenor.com/images/7c3cbde624b0e7888fac8fa8c3412bb6/tenor.gif?itemid=18453580",
    "https://media1.tenor.com/images/49b1aa90b1a0b63ee3a89a651efdcd01/tenor.gif?itemid=14596996",
    "https://media1.tenor.com/images/8a87452b39aa0a394f19b42d8d2e790d/tenor.gif?itemid=12284917",
    "https://media1.tenor.com/images/4cdc75a9068ae855379fcf99c217e45f/tenor.gif?itemid=9434390",
    "https://i.nobuwu.dev/nyaa/greet/0.gif",
    "https://i.nobuwu.dev/nyaa/greet/7.gif")

cheers=("https://media1.tenor.com/images/f9a825b7d614cedda3fb2676a4ca0b68/tenor.gif?itemid=16127538",
    "https://media1.tenor.com/images/a0ca54410e089e1f1f9d92084c4f4e87/tenor.gif?itemid=14409900",
    "https://media1.tenor.com/images/f42beb68f170e9da11aa5da10c1be9cd/tenor.gif?itemid=14754210",
    "https://media1.tenor.com/images/937cae0b3dbac58f7d4454f387fa5905/tenor.gif?itemid=10919823",
    "https://media1.tenor.com/images/3d03d6f865e6bfbf996f44764e51cfef/tenor.gif?itemid=4215383",
    "https://media1.tenor.com/images/6a0fb78a7d171e4457c090b3325398f4/tenor.gif?itemid=20554526",
    "https://media1.tenor.com/images/2ea934ab954c6709ae8a60fbb9fdd6b5/tenor.gif?itemid=20554541",
    "https://media1.tenor.com/images/9679d019929d180c2f30ba8b03b8e3af/tenor.gif?itemid=20554580",
    "https://media1.tenor.com/images/25beb4cad311177edecb1cbcfe4b73b6/tenor.gif?itemid=4731159",
    "https://media1.tenor.com/images/ced439774fac81102c490f321eb23ceb/tenor.gif?itemid=20554624")

confusions=("https://media1.tenor.com/images/89d55748e5ae70caa2828b3768112c09/tenor.gif?itemid=10196393",
    "https://media1.tenor.com/images/e057e7ac06b7e6c1735d9244a1c9d5c0/tenor.gif?itemid=18857176",
    "https://media1.tenor.com/images/a91c492a6af5eeec80379484538d998a/tenor.gif?itemid=4838969",
    "https://media1.tenor.com/images/649c1a33b3950ed26b0b38c6f75bb97b/tenor.gif?itemid=19368852",
    "https://media1.tenor.com/images/aea2b3b7a199c1d5de88f71e7f5a3a95/tenor.gif?itemid=15453847",
    "https://media1.tenor.com/images/676287309b99573cbbcaaf633cd9e1c8/tenor.gif?itemid=16142378",
    "https://media1.tenor.com/images/db761c3b514b85e0bae38d88383714c8/tenor.gif?itemid=13129993",
    "https://media1.tenor.com/images/e765e06eb21f7bdd41eb6605222c4f60/tenor.gif?itemid=6014356",
    "https://media1.tenor.com/images/88d015a1213cd2f65a469db5ca0c51e7/tenor.gif?itemid=16694798",
    "https://media1.tenor.com/images/eacde875b7c910facce71e92f4ede7b5/tenor.gif?itemid=13945306")

cries=("https://media1.tenor.com/images/ce52606293142a2bd11cda1d3f0dc12c/tenor.gif?itemid=5184314",
    "https://media1.tenor.com/images/de730b51400ed4dfb66d04141ea79a2d/tenor.gif?itemid=7353410",
    "https://media1.tenor.com/images/0436bfc9861b4b57ffffda82d3adad6e/tenor.gif?itemid=15550145",
    "https://media1.tenor.com/images/26e7564bfb4408f9f7ff9518d4f87308/tenor.gif?itemid=8199739",
    "https://media1.tenor.com/images/1e0c5617f4136bc195eabc2f9d39ef00/tenor.gif?itemid=14926648",
    "https://media1.tenor.com/images/f55c36ad4aa6a47513442a333d002046/tenor.gif?itemid=20554669",
    "https://media1.tenor.com/images/25647818b7bfecc954afffb5ecec6d09/tenor.gif?itemid=20554681",
    "https://media1.tenor.com/images/28e3877988b83bdef1cc81121524c9e8/tenor.gif?itemid=20554716",
    "https://media1.tenor.com/images/ae226179b3e70f8eb8180e590bb1bcfa/tenor.gif?itemid=20554747",
    "https://media1.tenor.com/images/e310ec151b85c9e479d5213ae9e88d7e/tenor.gif?itemid=20554751",
    "https://media1.tenor.com/images/179858dabefd75f7c001db7c3ec6f311/tenor.gif?itemid=13452863",
    "https://media1.tenor.com/images/7119d3e4881081ea574e9229540545db/tenor.gif?itemid=17088760",
    "https://i.nobuwu.dev/nyaa/cry/0.gif",
    "https://i.nobuwu.dev/nyaa/cry/1.gif",
    "https://i.nobuwu.dev/nyaa/cry/2.gif",
    "https://i.nobuwu.dev/nyaa/cry/3.gif",
    "https://i.nobuwu.dev/nyaa/cry/4.gif",
    "https://i.nobuwu.dev/nyaa/cry/5.gif",
    "https://i.nobuwu.dev/nyaa/cry/6.gif",
    "https://i.nobuwu.dev/nyaa/cry/7.gif",
    "https://i.nobuwu.dev/nyaa/cry/8.gif",
    "https://i.nobuwu.dev/nyaa/cry/9.gif",
    "https://i.nobuwu.dev/nyaa/cry/12.gif",
    "https://i.nobuwu.dev/nyaa/cry/13.gif",
    "https://i.nobuwu.dev/nyaa/cry/14.gif",
    "https://i.nobuwu.dev/nyaa/cry/15.gif",
    "https://i.nobuwu.dev/nyaa/cry/17.gif",
    "https://i.nobuwu.dev/nyaa/cry/18.gif",
    "https://i.nobuwu.dev/nyaa/cry/19.gif",
    "https://i.nobuwu.dev/nyaa/cry/20.gif",
    "https://i.nobuwu.dev/nyaa/cry/21.gif",
    "https://i.nobuwu.dev/nyaa/cry/23.gif")

dabs=("https://media1.tenor.com/images/033a2e811f625be20008eed617734d40/tenor.gif?itemid=13628207",
    "https://media1.tenor.com/images/d13c16a8853e3b309db0ec7e573c4c94/tenor.gif?itemid=10617637",
    "https://media1.tenor.com/images/dddd0236ad6d889e54df034f18383871/tenor.gif?itemid=5774497",
    "https://media1.tenor.com/images/59983e51f744411fd00c2e50b1399fc5/tenor.gif?itemid=12789689",
    "https://media1.tenor.com/images/bae5efed4c47dc74a4d892c430352a99/tenor.gif?itemid=19091109",
    "https://media1.tenor.com/images/b5dc3c3ce37cb98c4889b5c0c8260f00/tenor.gif?itemid=18411004",
    "https://media1.tenor.com/images/c9970c95b5290b6e51a546daf3b7e87e/tenor.gif?itemid=11805837",
    "https://media1.tenor.com/images/7787254cb6c8aeff5aea752474b10fb6/tenor.gif?itemid=17224535",
    "https://media1.tenor.com/images/7eebe12c2c235074c06708dd2b8d8c86/tenor.gif?itemid=17492683",
    "https://media1.tenor.com/images/ec046024d77f537ce993c56d11e799a8/tenor.gif?itemid=19198584")

deads=("https://media1.tenor.com/images/24f2f1015aa273303e15f48a69c78260/tenor.gif?itemid=6373002",
    "https://media1.tenor.com/images/663b353a3ff20b0aca9b64667ea2d7e8/tenor.gif?itemid=7689712",
    "https://media1.tenor.com/images/bf1e5ee94ccd13576d3520d60d692317/tenor.gif?itemid=5384592",
    "https://media1.tenor.com/images/c2c9b32059b5abe04b7fd7c859905e8a/tenor.gif?itemid=15934339",
    "https://media1.tenor.com/images/7072d8d4cc68d68994b5c10924e3ee01/tenor.gif?itemid=8803836",
    "https://media1.tenor.com/images/bc95277aeee35ff93253789e9d68e13f/tenor.gif?itemid=11385161",
    "https://media1.tenor.com/images/e716262ed9bf96633cd7cb7df23f2c64/tenor.gif?itemid=15759504",
    "https://media1.tenor.com/images/79f1a0dd1bfc67b44c2d7ce4404c2a66/tenor.gif?itemid=5417340",
    "https://media1.tenor.com/images/25a5b0faa2044db0b1e5e3ab2fb8d4f0/tenor.gif?itemid=15157935",
    "https://media1.tenor.com/images/4b8a20e7dbd56575f1af27d9d26ff5e5/tenor.gif?itemid=3893716")

eats=("https://media1.tenor.com/images/0de27657daa673ccd7a60cf6919084d9/tenor.gif?itemid=4848690",
    "https://media1.tenor.com/images/5d6baa94cd7a02d0751779c851c598b9/tenor.gif?itemid=7889888",
    "https://media1.tenor.com/images/960151a0c15fefd51e008e45e59486f9/tenor.gif?itemid=14108963",
    "https://media1.tenor.com/images/5aaf1a7f1b7fc56c5f8ee50425efeefd/tenor.gif?itemid=17362621",
    "https://media1.tenor.com/images/995c722f20a9154a47149157832dc861/tenor.gif?itemid=6184631",
    "https://media1.tenor.com/images/f5123483b1c80afa0312ee9c5545e336/tenor.gif?itemid=20554757",
    "https://media1.tenor.com/images/c8a1aad9a386a7d6fbf7e3cb5cb81719/tenor.gif?itemid=20554766",
    "https://media1.tenor.com/images/4dff8890948087dac40f3fc080fc2d8f/tenor.gif?itemid=20554775",
    "https://media1.tenor.com/images/653a3dfc763415659750c95b47ad024c/tenor.gif?itemid=20554784",
    "https://media1.tenor.com/images/4ef4cb754505361b01bea930d292aa07/tenor.gif?itemid=20554789",
    "https://i.nobuwu.dev/nyaa/nom/0.gif",
    "https://i.nobuwu.dev/nyaa/nom/3.gif",
    "https://i.nobuwu.dev/nyaa/nom/5.gif",
    "https://i.nobuwu.dev/nyaa/nom/6.gif",
    "https://i.nobuwu.dev/nyaa/nom/8.gif",
    "https://i.nobuwu.dev/nyaa/nom/9.gif",
    "https://i.nobuwu.dev/nyaa/nom/13.gif",
    "https://i.nobuwu.dev/nyaa/nom/14.gif",
    "https://i.nobuwu.dev/nyaa/nom/16.gif",
    "https://i.nobuwu.dev/nyaa/nom/17.gif",
    "https://i.nobuwu.dev/nyaa/nom/19.gif",
    "https://i.nobuwu.dev/nyaa/nom/20.gif",
    "https://i.nobuwu.dev/nyaa/nom/21.gif",
    "https://i.nobuwu.dev/nyaa/nom/22.gif",
    "https://i.nobuwu.dev/nyaa/nom/23.gif",
    "https://i.nobuwu.dev/nyaa/nom/24.gif",
    "https://i.nobuwu.dev/nyaa/nom/26.gif",
    "https://i.nobuwu.dev/nyaa/nom/27.gif",
    "https://i.nobuwu.dev/nyaa/nom/30.gif",
    "https://media1.tenor.com/images/6f7436accef81dbb2cb1a8b3af2637fa/tenor.gif?itemid=16770961")

facepalms=("https://media1.tenor.com/images/9d30a11e7978ea3b404d5e48c5966c6b/tenor.gif?itemid=5015289",
    "https://media1.tenor.com/images/9a269d284388ae4906983f5dfbb15c64/tenor.gif?itemid=17106384",
    "https://media1.tenor.com/images/375754f9ccdf8ac94146381c06755c09/tenor.gif?itemid=5015299",
    "https://media1.tenor.com/images/f241523f9f179308e13ba8867feacdee/tenor.gif?itemid=10110823",
    "https://media1.tenor.com/images/d8d29f0d56957f209f42105baa4e00f1/tenor.gif?itemid=17236628",
    "https://media1.tenor.com/images/a29e11bc1132181031ed66ee2a4747fb/tenor.gif?itemid=19368854",
    "https://media1.tenor.com/images/76d2ec47ec76fa36b2fce913331ba7e3/tenor.gif?itemid=5533025",
    "https://media1.tenor.com/images/bc3f3842afb1edcba095f9bf766405b2/tenor.gif?itemid=17778269",
    "https://media1.tenor.com/images/142d74bbd13fc305aed5a4894c0c3f7f/tenor.gif?itemid=16642818",
    "https://media1.tenor.com/images/1985087041eb8f0e86899c6e3aa36614/tenor.gif?itemid=16187738")

good_mornings=("https://media1.tenor.com/images/11fdefc3cf323a47af3f665f018c2c77/tenor.gif?itemid=5634607",
    "https://media1.tenor.com/images/8aaa6365f75ef28ac4764e8a73f417d1/tenor.gif?itemid=11800129",
    "https://media1.tenor.com/images/12867253c66f18ce17121c716bd720e3/tenor.gif?itemid=7445458",
    "https://media1.tenor.com/images/52bf1afef19876cdaec8906952254802/tenor.gif?itemid=12348565",
    "https://media1.tenor.com/images/efb3c1fc454f0bd0c70cb3e3fc0f5e75/tenor.gif?itemid=13820235",
    "https://media1.tenor.com/images/a35527737a7cea9a682257eab848ef9a/tenor.gif?itemid=5118522",
    "https://media1.tenor.com/images/0a36f8dd96c3a61bd8926c3658920414/tenor.gif?itemid=16843917",
    "https://media1.tenor.com/images/c9bdd59ad0a38e3700d6cbd50fe79d8c/tenor.gif?itemid=17322803",
    "https://media1.tenor.com/images/d9b20916892ebd106b080711158c8735/tenor.gif?itemid=17666740",
    "https://media1.tenor.com/images/8aaa6365f75ef28ac4764e8a73f417d1/tenor.gif?itemid=11800129")

hi_fives=("https://media1.tenor.com/images/744dccb53da9e3847b4efa724975546c/tenor.gif?itemid=20379656",
    "https://media1.tenor.com/images/7b1f06eac73c36721912edcaacddf666/tenor.gif?itemid=10559431",
    "https://media1.tenor.com/images/b714d7680f8b49d69b07bc2f1e052e72/tenor.gif?itemid=13400356",
    "https://media1.tenor.com/images/e553e6d366ab4db4590bacc2ac9a4910/tenor.gif?itemid=16059180",
    "https://media1.tenor.com/images/c3263b8196afc25ddc1d53a4224347cd/tenor.gif?itemid=9443275",
    "https://media1.tenor.com/images/459842c03431f2c533dff985ac116f25/tenor.gif?itemid=19803970",
    "https://media1.tenor.com/images/ad22432b945ea3676ffb16ea2989b41b/tenor.gif?itemid=19685271",
    "https://media1.tenor.com/images/0c23b320822afd5b1ce3faf01c2b9b69/tenor.gif?itemid=14137078",
    "https://media1.tenor.com/images/16267f3a34efb42598bd822effaccd11/tenor.gif?itemid=14137081",
    "https://media1.tenor.com/images/564aac614e91983dcbef052742d2bb3a/tenor.gif?itemid=16059185",
    "https://i.nobuwu.dev/nyaa/highfive/2.gif",
    "https://i.nobuwu.dev/nyaa/highfive/4.gif",
    "https://i.nobuwu.dev/nyaa/highfive/5.gif",
    "https://i.nobuwu.dev/nyaa/highfive/6.gif",
    "https://i.nobuwu.dev/nyaa/highfive/7.gif",
    "https://i.nobuwu.dev/nyaa/highfive/8.gif",
    "https://i.nobuwu.dev/nyaa/highfive/9.gif")

hugs=("https://media1.tenor.com/images/4d89d7f963b41a416ec8a55230dab31b/tenor.gif?itemid=5166500",
    "https://media1.tenor.com/images/f5df55943b64922b6b16aa63d43243a6/tenor.gif?itemid=9375012",
    "https://media1.tenor.com/images/506aa95bbb0a71351bcaa753eaa2a45c/tenor.gif?itemid=7552075",
    "https://media1.tenor.com/images/16f4ef8659534c88264670265e2a1626/tenor.gif?itemid=14903944",
    "https://media1.tenor.com/images/e9d7da26f8b2adbb8aa99cfd48c58c3e/tenor.gif?itemid=14721541",
    "https://media1.tenor.com/images/3b14c13b07ae95649ffef7d855a2f5d1/tenor.gif?itemid=20556765",
    "https://media1.tenor.com/images/4db3a7f7a8c6f97bf1711c1752e766af/tenor.gif?itemid=20556781",
    "https://media1.tenor.com/images/33534833bb4a81dcd1b7a3540b069ca3/tenor.gif?itemid=20556797",
    "https://media1.tenor.com/images/a211f33e4ff688f9101a46ed95f2fb21/tenor.gif?itemid=20556812",
    "https://media1.tenor.com/images/249e80e40c76b60ae91a4a29d669e54b/tenor.gif?itemid=20556829",
    "https://media1.tenor.com/images/bd7554e3cc115e9851d836fe6c555f64/tenor.gif?itemid=20379697",
    "https://media1.tenor.com/images/0022315b49ced4bb72114011a4932580/tenor.gif?itemid=12480522",
    "https://i.nobuwu.dev/nyaa/hug/0.gif",
    "https://i.nobuwu.dev/nyaa/hug/1.gif",
    "https://i.nobuwu.dev/nyaa/hug/2.gif",
    "https://i.nobuwu.dev/nyaa/hug/3.gif",
    "https://i.nobuwu.dev/nyaa/hug/4.gif",
    "https://i.nobuwu.dev/nyaa/hug/5.gif",
    "https://i.nobuwu.dev/nyaa/hug/6.gif",
    "https://i.nobuwu.dev/nyaa/hug/8.gif",
    "https://i.nobuwu.dev/nyaa/hug/9.gif",
    "https://i.nobuwu.dev/nyaa/hug/10.gif",
    "https://i.nobuwu.dev/nyaa/hug/11.gif",
    "https://i.nobuwu.dev/nyaa/hug/12.gif",
    "https://i.nobuwu.dev/nyaa/hug/16.gif",
    "https://i.nobuwu.dev/nyaa/hug/18.gif",
    "https://i.nobuwu.dev/nyaa/hug/19.gif",
    "https://i.nobuwu.dev/nyaa/hug/20.gif",
    "https://i.nobuwu.dev/nyaa/hug/21.gif",
    "https://i.nobuwu.dev/nyaa/hug/23.gif",
    "https://i.nobuwu.dev/nyaa/hug/25.gif",
    "https://i.nobuwu.dev/nyaa/hug/26.gif",
    "https://i.nobuwu.dev/nyaa/hug/27.gif",
    "https://i.nobuwu.dev/nyaa/cuddle/0.gif",
    "https://i.nobuwu.dev/nyaa/cuddle/3.gif",
    "https://i.nobuwu.dev/nyaa/cuddle/5.gif",
    "https://i.nobuwu.dev/nyaa/cuddle/6.gif",
    "https://i.nobuwu.dev/nyaa/cuddle/7.gif",
    "https://i.nobuwu.dev/nyaa/cuddle/14.gif",
    "https://i.nobuwu.dev/nyaa/cuddle/15.gif",
    "https://i.nobuwu.dev/nyaa/cuddle/16.gif")

kills=("https://media1.tenor.com/images/bb4b7a7559c709ffa26c5301150e07e4/tenor.gif?itemid=9955653",
    "https://media1.tenor.com/images/0cead32a049a3e0e0803315c388725b0/tenor.gif?itemid=12818133",
    "https://media1.tenor.com/images/8dce634d2223474c4a9459f01bb57193/tenor.gif?itemid=17815150",
    "https://media1.tenor.com/images/0917e9f68e7d277135a9f885f953888b/tenor.gif?itemid=17763115",
    "https://media1.tenor.com/images/a80b2bf31635899ac0900ea6281a41f6/tenor.gif?itemid=5535365",
    "https://media1.tenor.com/images/1acb7c8c86f469dc558462631ac2f59e/tenor.gif?itemid=20556963",
    "https://media1.tenor.com/images/367ae5ad3b697a728b624cff0c33ec07/tenor.gif?itemid=20556976",
    "https://media1.tenor.com/images/cb2ef8d741462719e5eedd538df46ced/tenor.gif?itemid=20556983",
    "https://media1.tenor.com/images/b18fdc3fe3f78afcc037e96eff79de12/tenor.gif?itemid=20556992",
    "https://media1.tenor.com/images/b2a6648bf41f899ef3abbfde95c70b00/tenor.gif?itemid=20557007",
    "https://media1.tenor.com/images/c271a7d9500a77b79c47a1c0cca21d7d/tenor.gif?itemid=5062704",
    "https://media1.tenor.com/images/0bccc455e6793a4bfe0d1b27fef3e661/tenor.gif?itemid=17608658",
    "https://i.nobuwu.dev/nyaa/punch/5.gif",
    "https://i.nobuwu.dev/nyaa/punch/10.gif",
    "https://i.nobuwu.dev/nyaa/slap/26.gif")

kisses=("https://media1.tenor.com/images/d307db89f181813e0d05937b5feb4254/tenor.gif?itemid=16371489",
    "https://media1.tenor.com/images/bc5e143ab33084961904240f431ca0b1/tenor.gif?itemid=9838409",
    "https://media1.tenor.com/images/4b5d5afd747fe053ed79317628aac106/tenor.gif?itemid=5649376",
    "https://media1.tenor.com/images/105a7ad7edbe74e5ca834348025cc650/tenor.gif?itemid=9158317",
    "https://media1.tenor.com/images/ea9a07318bd8400fbfbd658e9f5ecd5d/tenor.gif?itemid=12612515",
    "https://media1.tenor.com/images/78095c007974aceb72b91aeb7ee54a71/tenor.gif?itemid=5095865",
    "https://media1.tenor.com/images/7fd98defeb5fd901afe6ace0dffce96e/tenor.gif?itemid=9670722",
    "https://media1.tenor.com/images/f5167c56b1cca2814f9eca99c4f4fab8/tenor.gif?itemid=6155657",
    "https://media1.tenor.com/images/1306732d3351afe642c9a7f6d46f548e/tenor.gif?itemid=6155670",
    "https://media1.tenor.com/images/a390476cc2773898ae75090429fb1d3b/tenor.gif?itemid=12837192",
    "https://media1.tenor.com/images/b303e0f83f852e649011b9c277d89f1e/tenor.gif?itemid=15827699",
    "https://media1.tenor.com/images/5118fdccd96ff77207d9b109af14ffd9/tenor.gif?itemid=12861943",
    "https://i.nobuwu.dev/nyaa/kiss/0.gif",
    "https://i.nobuwu.dev/nyaa/kiss/2.gif",
    "https://i.nobuwu.dev/nyaa/kiss/4.gif",
    "https://i.nobuwu.dev/nyaa/kiss/5.gif",
    "https://i.nobuwu.dev/nyaa/kiss/6.gif",
    "https://i.nobuwu.dev/nyaa/kiss/9.gif",
    "https://i.nobuwu.dev/nyaa/kiss/11.gif",
    "https://i.nobuwu.dev/nyaa/kiss/12.gif",
    "https://i.nobuwu.dev/nyaa/kiss/13.gif",
    "https://i.nobuwu.dev/nyaa/kiss/14.gif",
    "https://i.nobuwu.dev/nyaa/kiss/15.gif",
    "https://i.nobuwu.dev/nyaa/kiss/16.gif",
    "https://i.nobuwu.dev/nyaa/kiss/17.gif",
    "https://i.nobuwu.dev/nyaa/kiss/18.gif",
    "https://i.nobuwu.dev/nyaa/kiss/20.gif",
    "https://i.nobuwu.dev/nyaa/kiss/22.gif",
    "https://i.nobuwu.dev/nyaa/kiss/23.gif",
    "https://i.nobuwu.dev/nyaa/kiss/24.gif",
    "https://i.nobuwu.dev/nyaa/kiss/25.gif",
    "https://i.nobuwu.dev/nyaa/kiss/26.gif")

#Main
dad_activity=discord.Game(name='Hide and Seek with my children after getting milk from the store :).')
client=commands.Bot(command_prefix='>',intents=discord.Intents.all(),activity=dad_activity)
client.remove_command('help')

@client.event
async def on_ready():
    print('>>>Bot hosted successfully ')
    for i in client.guilds:
        print(i.name)
spacesd='⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀'
#spacesd=''
@client.command(aliases=['menu','Menu','help'])
async def commands(ctx):
    menuem=discord.Embed(title='__**Command List**__',color=0xffa500,url='https://youtu.be/PgaSGAeoz9w')
    menuem.set_author(icon_url=client.user.avatar_url,name='{}'.format(client.user))
    #menuem.add_field(name='⠀',value='⠀',inline=True)
    menuem.add_field(name='__*💫 - Fun*__',value='`8ball [question]`    {} '.format(spacesd),inline=False)
    menuem.add_field(name='__*👻 - Reactions*__',value='`send_reversecard`, `Understandable`, `Baka`, `Bite`, `Blowkiss`, `Blush`, `Bonk`, `Bye`, `Cheer`, `Confused`, `Cry`, `Dab`, `Dead`, `Eat`, `Facepalm`, `good_morning`, `high_five`, `hug`, `kill`, `kiss`     {} '.format(spacesd),inline=False)
    menuem.add_field(name='__*💯 - Math*__',value='`rolldice [numbeer_of_dice]`, `flipcoins [number_of_coins]`, `calculate [expression to solve]`    {} '.format(spacesd),inline=False)
    menuem.add_field(name='__*👾 - Miscellaneous*__',value='`avatar [ping(user)]`, `choose [value1,value2....valuen]`    {} '.format(spacesd),inline=False)
    menuem.add_field(name='*🚀 __Invite Dad to your server__ :)*',value='[Click me!](https://discord.com/oauth2/authorize?client_id=776302115009462303&scope=bot){}'.format(spacesd),inline=False)
    menuem.set_footer(text='Dad-bot - created by: Ty1er#0555 .')
    await ctx.send(embed=menuem)

#💫 FUN

##8ball prediction
@client.command(aliases=['8b','8ball','is','Is'])
async def randball(ctx,*,question):
    await ctx.send('{} : {}'.format(question,str(random.choice(responses))))


#👻 REACTIONS

##Send a reverse card
@client.command(aliases=['send_rev','reverse','send_reversecard','no_u','uno'])
async def send_reverse(ctx,*,message=''):
    try:
        usr=client.get_user(int(str(message).strip('<>!@')))
        e=discord.Embed(title='{} reverses {}'.format(ctx.author,usr),color=random.choice(colours))
        e.set_image(url=random.choice(revs))
    except:
        e=discord.Embed(title='{} reverses {}'.format(ctx.author,message),color=random.choice(colours))
        e.set_image(url=random.choice(revs))
    await ctx.send(embed=e)

##Understandable 
@client.command(aliases=['understandable_have_a_great_day'])
async def understandable(ctx,*,message=''):
    try:
        usr=client.get_user(int(str(message).strip('<>!@')))
    except:
        usr=''
    if usr != '':
        if usr != ctx.author:
            e=discord.Embed(title='@{} Understands and says @{} to have a great day!'.format(ctx.author,usr),color=random.choice(colours))
        else:
            e=discord.Embed(title='@{} understand themselves ( hopefully they\'ll have a good day too ). What an introspector!'.format(ctx.author),color=random.choice(colours))
    else:
        e=discord.Embed(title='Understandable, Have a great day',color=random.choice(colours))
    e.set_image(url='https://c.tenor.com/Z6uHH2k0_vEAAAAd/understandable-have-nice-day.gif')
    await ctx.send(embed=e)

##Baka
@client.command(aliases=['Baka','Idiot','idiot'])
async def baka(ctx,*,message=''):
    try:
        usr=client.get_user(int(str(message).strip('<>!@')))
    except:
        usr=''
    if usr != '':
        if usr != ctx.author:
            e=discord.Embed(title='@{} calls @{} a baka.'.format(ctx.author,usr),color=random.choice(colours))
        else:
            e=discord.Embed(title='@{} is a baka. 🤦'.format(ctx.author),color=random.choice(colours))
    else:
        e=discord.Embed(title='@{} is a baka. 🤦'.format(ctx.author),color=random.choice(colours))
    e.set_image(url=random.choice(bakas))
    await ctx.send(embed=e)

##Bite
@client.command(aliases=['Bite','nom','chew'])
async def bite(ctx,*,message=''):
    try:
        usr=client.get_user(int(str(message).strip('<>!@')))
    except:
        usr=''
    if usr != '':
        if usr != ctx.author:
            e=discord.Embed(title='@{} Bites @{}.'.format(ctx.author,usr),color=random.choice(colours))
        else:
            e=discord.Embed(title='@{} turn 180* and bites themselves.'.format(ctx.author),color=random.choice(colours))
    else:
        e=discord.Embed(title='@{} turn 180* and bites themselves.'.format(ctx.author),color=random.choice(colours))
    e.set_image(url=random.choice(bites))
    await ctx.send(embed=e)

##Blowkiss
@client.command(aliases=['Blowkiss'])
async def blowkiss(ctx,*,message=''):
    try:
        usr=client.get_user(int(str(message).strip('<>!@')))
    except:
        usr=''
    if usr != '':
        if usr != ctx.author:
            e=discord.Embed(title='@{} blows a kiss  😘  to @{}.'.format(ctx.author,usr),color=random.choice(colours))
        else:
            e=discord.Embed(title='@{} wants to be kissed.'.format(ctx.author),color=random.choice(colours))
    else:
        e=discord.Embed(title='@{} wants to be kissed.'.format(ctx.author),color=random.choice(colours))
    e.set_image(url=random.choice(blowkisses))
    await ctx.send(embed=e)

##Blush
@client.command(aliases=['Blush'])
async def blush(ctx):
    e=discord.Embed(title='@{} is blushing   😳 .'.format(ctx.author),color=random.choice(colours))
    e.set_image(url=random.choice(blushes))
    await ctx.send(embed=e)

##Bonk
@client.command(aliases=['Bonk','homerun','no_horny'])
async def bonk(ctx,*,message=''):
    try:
        usr=client.get_user(int(str(message).strip('<>!@')))
    except:
        usr=''
    if usr != '':
        if usr != ctx.author:
            e=discord.Embed(title='@{} Bonks @{}.'.format(ctx.author,usr),color=random.choice(colours))
        else:
            e=discord.Embed(title='@{} Are you a masaochist?'.format(ctx.author),color=random.choice(colours))
    else:
        e=discord.Embed(title='@{} bonks a ghost 👻 . '.format(ctx.author),color=random.choice(colours))
    e.set_image(url=random.choice(bonks))
    await ctx.send(embed=e)

##Bored
@client.command(aliases=['Bored'])
async def bored(ctx):
    e=discord.Embed(title='@{} is bored  🥱  .'.format(ctx.author),color=random.choice(colours))
    e.set_image(url=random.choice(boreds))
    await ctx.send(embed=e)

##Bye
@client.command(aliases=['Bye','cya','byebye','tata'])
async def bye(ctx,*,message=''):
    try:
        usr=client.get_user(int(str(message).strip('<>!@')))
    except:
        usr=''
    if usr != '':
        if usr != ctx.author:
            e=discord.Embed(title='@{} waves bye  👋  to @{}.'.format(ctx.author,usr),color=random.choice(colours))
        else:
            e=discord.Embed(title='Bye 👋 @{}. : ) Dad is proud of you.'.format(ctx.author),color=random.choice(colours))
    else:
        e=discord.Embed(title='@{} waves bye to a ghost 👻 .'.format(ctx.author),color=random.choice(colours))
    e.set_image(url=random.choice(byes))
    await ctx.send(embed=e)

##Cheer
@client.command(aliases=['cheer_up','Cheer'])
async def cheer(ctx,*,message=''):
    try:
        usr=client.get_user(int(str(message).strip('<>!@')))
    except:
        usr=''
    if usr != '':
        if usr != ctx.author:
            e=discord.Embed(title='@{} cheers @{}.'.format(ctx.author,usr),color=random.choice(colours))
        else:
            e=discord.Embed(title='@{} cheer up :) something good will definetly happen'.format(ctx.author),color=random.choice(colours))
    else:
        e=discord.Embed(title='@{} cheers a ghost 👻 .Hope they make a new friend today.'.format(ctx.author),color=random.choice(colours))
    e.set_image(url=random.choice(cheers))
    await ctx.send(embed=e)

##Confused
@client.command(aliases=['Confused','dilema','confusion'])
async def confused(ctx):
    e=discord.Embed(title='@{} is confused 😕 .'.format(ctx.author),color=random.choice(colours))
    e.set_image(url=random.choice(confusions))
    await ctx.send(embed=e)

##Cry
@client.command(aliases=['Cry'])
async def cry(ctx):
    e=discord.Embed(title='@{} is crying 😢  .'.format(ctx.author),color=random.choice(colours))
    e.set_image(url=random.choice(cries))
    await ctx.send(embed=e)

##Dab
@client.command(aliases=['Dab'])
async def dab(ctx):
    e=discord.Embed(title='@{} is DABBING .'.format(ctx.author),color=random.choice(colours))
    e.set_image(url=random.choice(dabs))
    await ctx.send(embed=e)

##Dead
@client.command(aliases=['Dead'])
async def dead(ctx):
    e=discord.Embed(title='@{} is Dead 😵 .'.format(ctx.author),color=random.choice(colours))
    e.set_image(url=random.choice(deads))
    await ctx.send(embed=e)

##Eat
@client.command(aliases=['Eat'])
async def eat(ctx):
    e=discord.Embed(title='@{} is eating.'.format(ctx.author),color=random.choice(colours))
    e.set_image(url=random.choice(eats))
    await ctx.send(embed=e)

##facepalm
@client.command(aliases=['Facepalm','Bruh','bruh'])
async def facepalm(ctx,*,message=''):
    try:
        usr=client.get_user(int(str(message).strip('<>!@')))
    except:
        usr=''
    if usr != '':
        if usr != ctx.author:
            e=discord.Embed(title='@{} is facepalming due to @{}\'s stupidity.'.format(ctx.author,usr),color=random.choice(colours))
        else:
            e=discord.Embed(title='@{} is facepalming 🤦  .'.format(ctx.author),color=random.choice(colours))
    else:
        e=discord.Embed(title='@{} is facaplming 🤦  .'.format(ctx.author),color=random.choice(colours))
    e.set_image(url=random.choice(facepalms))
    await ctx.send(embed=e)

##Good morning
@client.command(aliases=['gooodmorning','Goodmorning','Ohayo','ohayo'])
async def good_morning(ctx,*,message=''):
    try:
        usr=client.get_user(int(str(message).strip('<>!@')))
    except:
        usr=''
    if usr != '':
        if usr != ctx.author:
            e=discord.Embed(title='@{} wishes @{} to have a good morning.'.format(ctx.author,usr),color=random.choice(colours))
        else:
            e=discord.Embed(title='Good morning @{}'.format(ctx.author),color=random.choice(colours))
    else:
        e=discord.Embed(title='Good morning @{}'.format(ctx.author),color=random.choice(colours))
    e.set_image(url=random.choice(good_mornings))
    await ctx.send(embed=e)

##High five
@client.command(aliases=['Hi5','higfive'])
async def high_five(ctx,*,message=''):
    try:
        usr=client.get_user(int(str(message).strip('<>!@')))
    except:
        usr=''
    if usr != '':
        if usr != ctx.author:
            e=discord.Embed(title='@{} highfives @{}.'.format(ctx.author,usr),color=random.choice(colours))
        else:
            e=discord.Embed(title='@{} wants to high-five someone.'.format(ctx.author),color=random.choice(colours))
    else:
        e=discord.Embed(title='@{} gets high-fived by a ghost 👻 .'.format(ctx.author),color=random.choice(colours))
    e.set_image(url=random.choice(hi_fives))
    await ctx.send(embed=e)

##Hug
@client.command(aliases=['Hug'])
async def hug(ctx,*,message=''):
    try:
        usr=client.get_user(int(str(message).strip('<>!@')))
    except:
        usr=''
    if usr != '':
        if usr != ctx.author:
            e=discord.Embed(title='@{} hugs @{} 🫂 .'.format(ctx.author,usr),color=random.choice(colours))
        else:
            e=discord.Embed(title='@{} wants a hug 🫂 . '.format(ctx.author),color=random.choice(colours))
    else:
        e=discord.Embed(title='@{} hugs a ghost 👻 .'.format(ctx.author),color=random.choice(colours))
    e.set_image(url=random.choice(hugs))
    await ctx.send(embed=e)

##Kill
@client.command(aliases=['Kill','murder','Murder'])
async def kill(ctx,*,message=''):
    try:
        usr=client.get_user(int(str(message).strip('<>!@')))
    except:
        usr=''
    if usr != '':
        if usr != ctx.author:
            e=discord.Embed(title='@{} kills @{} . RIP.'.format(ctx.author,usr),color=random.choice(colours))
        else:
            e=discord.Embed(title='@{} dont be suicidal.... '.format(ctx.author),color=random.choice(colours))
    else:
        e=discord.Embed(title='@{} was klled by a ghost 👻 .'.format(ctx.author),color=random.choice(colours))
    e.set_image(url=random.choice(kills))
    await ctx.send(embed=e)

##Kiss
@client.command(aliases=['Smooch','smooch','Kiss'])
async def kiss(ctx,*,message=''):
    try:
        usr=client.get_user(int(str(message).strip('<>!@')))
    except:
        usr=''
    if usr != '':
        if usr != ctx.author:
            e=discord.Embed(title='@{} kisses 😘  @{}  .'.format(ctx.author,usr),color=random.choice(colours))
        else:
            e=discord.Embed(title='@{} kisses a mirror 😘 . '.format(ctx.author),color=random.choice(colours))
    else:
        e=discord.Embed(title='@{} kisses a ghost 👻 .'.format(ctx.author),color=random.choice(colours))
    e.set_image(url=random.choice(kisses))
    await ctx.send(embed=e)


#💯 MATH

##roll n dice
@client.command(aliases=['roll','rolldices','Roll','Rolldie','rolldie'])
async def rolldice(ctx,*,number=1):
    number=str(number)
    if number.isdigit():
        num=int(number)
        d={}
        if num <= 50 and num >0:
            m='| 🎲 | ROLLING {} DICE  | 🎲 |\n'.format(num)
            for roller in range(num):
                rolled=random.randint(1,6)
                m=m+'\n{:<8}{:^7}{:^8}{:^3}{:^3}.'.format('Rolled',emojis[rolled-1],'On Die',str(roller+1),'🎲')
                if rolled not in d:
                    d[rolled]=1
                else:
                    d[rolled]+=1
                d = dict( sorted(d.items(), key=operator.itemgetter(1),reverse=True))
            if num > 1:
                su='\n| 🎲 | SUMMARY | 🎲 |'
                for i in d:
                    su=su+'\n {} appeared {} times'.format(emojis[i-1],d[i])
                m=m+'\n{}'.format(su)
            await ctx.send(m)
        else:
            await ctx.send('Enter number between 0 and 50')
    else:
        await ctx.send('Enter number between 0 and 50')

##Flip n coins
@client.command(aliases=['flipcoins','flip'])
async def flipcoin(ctx,*,number=1):
    poss=['Heads','Tails']
    k={'Heads':'🤯','Tails':'🍤'}
    num=str(number)
    if num.isdigit():
        num=int(num)
        if num >0 and num <=75:
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
            d = dict( sorted(d.items(), key=operator.itemgetter(1),reverse=True))
            if num >1:
                su='\n| 🔴 | SUMMARY | 🔴 |'
                for i in d:
                    su=su+'\n {} {} was flipped {} times'.format(i,k[i],str(d[i]))
                m=m+'\n{}'.format(su)
            await ctx.send(m)
        else:
            await ctx.send('Please enter a number between 0 and 75')
    else:
        await ctx.send('Please enter a number between 0 and 75')

##Calculate 
@client.command(aliases=['calc','whatis','solve'])
async def calculate(ctx,*,message=''):
        try:
            messagen=str(message).replace('x','*')
            messagen=messagen.replace('^','**')
            e=discord.Embed(title='Calculated Successfully!',colour=random.choice(colours))
            try:
                emessage=eval(messagen)
            except:
                emessage=messagen
            e.add_field(value=str(message)+' = '+str(emessage),name='Result:')
            e.set_author(icon_url=client.user.avatar_url,name='{}'.format(client.user))
            e.set_footer(text='Dad-bot - created by: Ty1er#0555 .',icon_url=client.user.avatar_url)
            await ctx.send(embed=e)
        except:
            await ctx.send('This is taking too long for me to calculate... :( please go a litte easier on your dad.')

##Choose
@client.command(aliases=['random','Choose','return'])
async def choose(ctx,*,message):
    ch=message.split(',')
    r=random.choice(ch)
    r='Chose {} randomly'.format(r)
    e=discord.Embed(title='Random choice',color=random.choice(colours))
    e.add_field(name='Choices : |'+message+'|',value='**{}**'.format(r))
    e.set_footer(text='Dad-bot - created by: Ty1er#0555 .',icon_url=client.user.avatar_url)
    await ctx.send(embed=e)


#👾 MISC COMMANDS

##Avatar
@client.command(aliases=['pfp','picture','image','profilepicture'])
async def avatar(ctx,member=''):
    try:
        usr=client.get_user(int(str(member).strip('<>!@')))
    except:
        usr=ctx.author
    mem=ctx.guild.get_member(usr.id)
    e=discord.Embed(title='',color=mem.top_role.color)
    e.set_author(icon_url=usr.avatar_url,name='{}'.format(client.user))
    e.set_footer(text='Dad-bot - created by: Ty1er#0555 .',icon_url=client.user.avatar_url)
    e.set_image(url=usr.avatar_url)
    e.add_field(name='Avatar belonging to @{}'.format(usr),value='[__**Download Image**__]({})'.format(usr.avatar_url),inline=True)
    await ctx.send(embed=e)



client.run(Token)
