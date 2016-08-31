# pylint: disable=c0302
import random
import json

import discord

import cacobot.base as base

@base.postcommand
async def woah(message, client):
    c = message.content.lower()
    send = None
    if message.author.id != client.user.id:
        if c == 'woah' or\
                c == 'woah.' or\
                c == 'whoa' or\
                 c == 'whoa.':
            send = 'Hey guys.'
        elif c == 'hey guys' or c == 'hey guys':
            send = 'Welcome to EB Games.'
        elif 'call of duty' in c or\
                'advanced warfare' in c or\
                'xbox one' in c:
            send = 'Copy that.'

    if send:
        if random.randint(1, 20) == 1:
            await client.send_message(message.channel, send)

@base.postcommand
async def wow(message, client):
    """
    c = message.content.lower()
    if message.author.id != client.user.id:
        if c == 'wow' or c == 'wow.':
            if random.randint(1, 20) == 1:
                await client.send_message(
                    message.channel,
                    'Ethan, great moves. Keep it up. I\'m proud of you.'
                    )
    """
suicides = [
    'Looks like Team %k is blasting off again!',
    '%k divided by 0.',
    '%k lost at Russian Roulette.',
    '%k applied for release.',
    '%k commited thoughtcrime.',
    '%k is ded.',
    '%k has died.',
    '%k has commited suicide.',
    '%k left it to the RNG.',
    '%k hugged Pyrope.',
    '%k had a whoopsie.',
    '%k failed at life.',
    '%k killed %hself.',
    '%k got too many student loans.',
    '%k is in debt.',
    '%k fell out of the world.',
    '%k had a bad time.',
    '%k had a bed tem.',
    '%k got dunked on.',
    '%k commited sudoku.',
    '%k commited seppuku.',
    '%k decided to end it once and for all.',
    '%k forgot to list a target\'s name.',
    '%k inched closer towards a black hole.',
    '%k discovers the secret to exploding your own brain.',
    '%k slits their own throat.',
    '%k bleeds out of a stab wound.',
    '%k died of dysentary.',
    '%k decided that %g had nothing left to live for.',
    '%k accidentally opened a letter bomb that had been returned to the sender.',
    '%k pulls the pin from a grenade without throwing it.',
    '%k ingested cyanide.',
    '%k looked down the barrel while firing.',
    '%k shot their chin.',
    '%k fired a blank to the head to prove that blanks are safe.',
    '%k "discovers middle earth" by jumping into a volcano.',
    '%k dies of lung cancer after smoking too much.',
    '%k starts smoking.',
    '%k dies from morbid obesity after eating so much.',
    '%k runs out of Psions after casting too many spells.',
    '%k falls into a strong river and drowns.',
    '%k gets ditched by Jerry.',
    '%k is murdered by a flower.',
    '%k accidentally wipes their save file.',
    '%k does not see a car coming and gets hit.',
    'A meteor falls from the sky and strikes %k, killing %h.',
    '%k finds some mercury and ingests it, leading to illness and death.',
    '%k decides to hug a bomb.',
    '%k steps into a bear trap and does not get rescued, being left to die alone.',
    '%k had the functions of every hole in %p face shuffled.',
    '%k was erradicated by Bill Cipher.',
    '%k discovers the joy of painting.',
    '%k could not think of anything.',
    '%k was contemplating what to do in life when a news feed item popped up, the contents of which gave %h an existential crisis. Not wanting to lose hope, %g continued to persevere, but to no avail. %k was seen standing at the top of a skyscraper, looking down at the city below. No other emotion besides sorrow for the universe was present as %g stepped off, before being rescued by a sudden shift in winds knocking %h back into a lower floor of the building. This did not stop %h as %g pulled out a gun and shot %hself in the head, ending it once and for all. Or so %g thought. The bullet had penetrated the brain but only caused %h to be in a vegetative state. The rest of %p sad life is now spent alone in a hospital with no family or friends, hooked up to machines and unable to do anything, before dying of old age and leaving this mortal coil forever.',
    'TODO: Death message for %k here.',
    'Original death message for %k here.',
    '%k was looking good until %g killed %hself!',
    '%k suicides.',
    '%k fell too far.',
    '%k was squished.',
    '%k tried to leave.',
    '%k can\'t swim.',
    '%k mutated.',
    "%k melted.",
    "%k went boom.",
    "%k stood in the wrong spot.",
    "%k should have stood back.",
    "%k should have stood back.",
    "%k killed %hself.",
    '%k was killed by the power of voodoo.',
    '%k was punched by a Revenant.',
    '%k was slashed by an Imp.',
    '%k got too close to a Cacodemon.',
    '%k was bit by a Demon.',
    '%k was eaten by a spectre.',
    '%k was ripped open by a Baron of Hell.',
    '%k was gutted by a Hell Knight.',
    "%k was killed by a zombieman.",
    "%k was shot by a sergeant.",
    "%k was incinerated by an archvile.",
    "%k couldn't evade a revenant's fireball.",
    "%k was squashed by a mancubus.",
    "%k was perforated by a chaingunner.",
    "%k was spooked by a lost soul.",
    "%k was burned by an imp.",
    "%k was smitten by a cacodemon.",
    "%k was bruised by a Baron of Hell.",
    "%k was splayed by a Hell Knight.",
    "%k stood in awe of the spider demon.",
    "%k let an arachnotron get %h.",
    "%k was splattered by a cyberdemon.",
    "%k was mauled by a dog.",
    "%k was pecked to death.",
    "%k was charred by a weredragon.",
    "%k was slashed by a sabreclaw.",
    "%k was scalded by D'Sparil's serpent.",
    "%k was chewed up by D'Sparil's serpent.",
    "%k was no match for D'Sparil.",
    "%k was smacked down by D'Sparil.",
    "%k was scarred by a gargoyle.",
    "%k was hacked by a gargoyle.",
    "%k was devastated by an ironlich.",
    "%k got up-close and personal with an ironlich.",
    "%k was axed by an undead warrior.",
    "%k was slain by an undead warrior.",
    "%k was smashed by a golem.",
    "%k was shrieked to death by a nitrogolem.",
    "%k was rattled by an ophidian.",
    "%k was cursed by a wizard.",
    "%k was palpated by a wizard.",
    "%k tasted an Afrit's fire.",
    "%k was scalded by a Serpent.",
    "%k was poisoned by a Serpent.",
    "%k was mashed by an Ettin.",
    "%k was cut up by a Centaur.",
    "%k was cut up by a Slaughtaur.",
    "%k was struck down by a Slaughtaur's fireball.",
    "%k succumbed to a Bishop's dark power.",
    "%k was frozen solid by a Wendigo.",
    "%k was mauled by a Stalker.",
    "%k was melted by a Stalker.",
    "%k was charred by a Reiver.",
    "%k had %p life stolen by a Reiver.",
    "%k was incinerated by the Death Wyvern.",
    "%k was swept from the board by Korax.",
    "%k was slain by Zedek.",
    "%k couldn't absorb Menelkir's Mana.",
    "%k was baptized by Traductus.",
    "%k had %p bones rolled by the Heresiarch.",
    "%k was zealously shot down by an Acolyte.",
    "%k should have never rebelled against Macil.",
    "%k was gunned down by a Rebel.",
    "%k was beaten to death by the poor.",
    "%k should have never picked a fight with a civilian.",
    "%k was struck down by the Spectre.",
    "%k felt the wrath of The One God.",
    "%k couldn't escape from the Lore Master's grasp.",
    "%k was deleted by the Programmer.",
    "%k was blown away by the Bishop.",
    "%k was shot down by a Sentinel.",
    "%k was swept away by a Crusader.",
    "%k was sentenced by an Inquisitor.",
    "%k was bugged by a Stalker.",
    "%k triggered the automatic defenses.",
    "%k was clawed by a Templar.",
    "%k was vaporized by a Templar.",
    "%k was sliced open by a Reaver.",
    "%k was shot down by a Reaver.",
    "%k was telefragged.",
    "%k checks %p glasses.",
    "%k was slimed by a flemoid.",
    "%k was slimed by a bipedicus.",
    "%k was slimed by an armored bipedicus.",
    "%k was slimed by a cycloptis.",
    "%k was defeated by the Flembrane.",
    '%k ascended.',
    '%k was lost in the matrix.',
    '%k was digitized to see the MCP.',
    'I\'m afraid I can\'t do that, %k.',
    '%k was petrified by elementary physics.',
    '%k was killed by elementary chemistry.',
    '%k failed the DPS check.',
    '%k drowned %hself.',
    '%k discovered the true nature of the electric fence.',
    '%k downed a bottle of aspirin in a bathtub full of water.',
    '%k fainted in a bathtub full of water.',
    '%k used the .kill command on %hself.',
    '%k joined the Tautology Club.',
    '%k made a deal with Bill Cipher.',
    '%k\'s aim did not get better.',
    '%k forgot %p timezone.',
    '%k was kidnapped by a madman in a police box.',
    '%k was kidnapped by a British guy in a phone booth.',
    '%k tried to bake a cake, but it got too `crazy`.',
    'Bravely bold Sir %k\nRode forth from Camelot\n%G was not afraid to die\nOh, brave Sir %k\n%G was not at all afraid\nTo be killed in nasty ways\nBrave, brave, brave, brave Sir %k\n\n%G was not in the least bit scared\nTo be mashed into a pulp\nOr to have %p eyes gouged out\nAnd %p elbows broken\nTo have %p kneecaps split\nAnd %p body burned away\nAnd %p limbs all hacked and mangled\nBrave Sir %k.', #"Sir" is defos gender neutral right?
    '%k lost %p creative juices.',
    'The author lost their creative juices to be able to write another death message for %k.',
    '%k was not 20% cooler.',
    '%k\'s eardrums were ruptured from excessive puffu-ing.',
    '%k tripped on a floppy disk.',
    '%k used too many pony memes.',
    'Actually, %k snaps in two. **Just kidding!**',
    '%k must\'ve been one swood guy.',
    '%k mistook hydrogen peroxide for water.',
    '%k played all the games and Bootleg Michael Jackson ascended them.',
    '%k took the red pill.',
    '%k took the blue pill.',
    '%k took both the red and the blue pills.',
    '%k threw away %p shot.',
    '%k will never be satisfied.',
    '%k\'s world turned upside down.',
    '%k couldn\'t say no to this.',
    '"Ah, Mister Secretary."\n"Mr. Burr, sir!"\n"Did you hear the news about good ol\' general %k, sir?"\n"No."\n"You know Clairmont street?"\n"Yeah?"\n"They renamed it after %h. The %k legacy is secure!"\n"Sure."\n"And all %g had to do was die."\n"That\'s a lot less work."\n"We oughta give it a try."',
    '%k didn\'t know %g was up against the SOUTHERN MOTHERFUCKING DEMOCRATIC-REPUBLICANS.',
    '%k thought %g was in the eye of a hurricane.',
    '%k doesn\'t die... %g must learn to live with the unimaginable instead.',
    'It\'s quiet uptown. %k never liked the quiet before.',
    '%k swallowed a fishbone.',
    '%k took an arrow to the knee.',
    '%k datched %hself',
    '%k squanched %hself',
    '%k\'s Kickstarter failed.',
    '%k didn\'t get the reference the author made in a death message.',
    '%k got Megaovania\'d',
    'Oh *maaaan*! %k forgot to bring an octagon! How embarrasing!',
    'Oh no! %k is inexplicably inflating again!',
    'Hello. look at %k, now back to me, now back at %k, now back to me. Sadly, %g is now dead. I\'m on a horse.',
    '%k did not know what a funyarinpa was.',
    '%k got @\u2060everyone pinged.',
    '%k was torn to shreds by an angry mob by pinging @\u2060everyone.\n\"To shreds, you say?\"',
    'Good news, everyone! %k has died!',
    r'%k was destroyed by a \*\*\*\*\*\*\*\*\*\*\*\*\* chainsaw! Wait, did I say chainsaw? What?',
    '%k got censored.',
    '%k ate an echo roll.',
    '%k had ████████████ done to %p █████████ while ██████ got a ███████████████ and decided ████████████ was an elephant version of █████████████████ candy.',
    '%k had a nosebleed. A deadly nosebleed.',
    'Subject D-%k was [DATA EXPUNGED]',
    '%k was found [REDACTED]',
    '%k\'s belt was set to W for Wumbo.',
    '%k felt the burn.',
    '%k felt the bern.',
    '%k got kawooshed by a Stargate.',
    '%k stepped through the wrong end of a Stargate.',
    '@\u2060%k: Urban Dictionary doesn\'t have that word.',
    '@\u2060%k: discord.errors.HTTPException: BAD REQUEST (status code: 400)',
    'Error 404 - Death message for %k not found.',
    '%k was lost to the ether.',
    '%k got stuck in the nether.',
    '%k didn\'t study for %p test tomorrow.',
    '%k inhaled neurotoxin. It\'s not deadly, you can put it in your cereal, run it in your eyes!',
    '%k was turned into a robot and sent back in time.',
    '%k discovered that the cake was in fact a lie.',
    '%k had a weighted companion cube dropped on %h.',
    '%k Hazzated %hself.',
    '%k downed a bottle of ground cinnamon.',
    '%k tried to eat a spoonful of ground cinnamon.',
    '%k died. Riphaghetti in Spaghetti, never forghetti,',
    '%k was portaled into space by GLaDOS.',
    '"Oh, %k! You came back! Didn\'t actually plan... for that. Can\'t actually reset the death trap. So. Ah. Could you jump into that pit, there? Would you just jump into that pit for me?"\n"Could you just jump into that pit? There. That deadly pit."\n"You\'re saying to yourself, why should I jump into the pit? I\'ll tell you why. Guess who\'s down there? Your parents! You\'re not adopted after all! It\'s your natural parents down there in the pit. Should have mentioned it before. But I didn\'t. So jump on down and reunite with mommy and daddy."\n"Oh I\'ll tell you what\'s also down there. Your parents and... There\'s also an escape elevator!. Down there. Funny. I should have mentioned it before. But so it\'s down there. So pop down. Jump down. You\'ve got your folks down there and an escape elevator"\n"And what else is down there... Tell you what, it\'s only a new jumpsuit. A very trendy designer jumpsuit from France. Down there. Which is exactly your size. And if it\'s a bit baggy, we got a tailor down there as well who can take it in for you"\n"And what\'s this, a lovely handbag? And the three portal device! It\'s all down there!"\n"Um. You\'ve got a yacht. And... Boys! Loads of fellas. Hunky guys down there. Possibly even a boyfriend! Who\'s to say at this stage. But, a lot of good looking fellas down there. And, ah, a boy band as well! That haven\'t seen a woman in years. And they\'re not picky at all. They don\'t care if you\'ve got a bit of brain damage. If you\'ve been running around sweating. And... A farm! A pony farm! And... Just jump down, would ya?"\n"Oh! Wow! Good! I didn\'t think that was going to work."',
    '%k shoulda rolled.',
    '%k tried to swooce right in.',
    '%k elected not to see The Strongman.',
    '%k got messed up by those Golden Rhino thugs!', # This one's for you, Ham.
    '%k likes hurting other people.',
    '%k HAS BEEN TAKEN INTO CUSTODY!',
    '%k was bleeding on the ground, but then a Texan yelled "Get the fuck up" to them and they got back up.',
    '%k was spooked solid.',
    '%k forgot a pair of bolt cutters.',
    '%k almost made it to Elysium, but plummeted back to Deponia instead.',
    '%k almost made it to Elysium, but plummeted back to the nondenominational Middle Eastern area instead.',
    '%k began development of "%k Forever".',
    '%k forgot how %p uncle\'s grappling device worked.',
    '%k saw the numbers and tasted the violence.',
    '%k is now half the man he used to be!',
    '%k was purged.',
    '%k was declared a heretic.',
    '%k was mashed by a bigger and stronger ork.'
    ]

killmsgs = [
    '%k has the chainsaw! %k has the Murderbrawl chainsaw! Oh, and down goes %o!',
    '%k ganked %o.',
    '%k purged %o.',
    '%k declared %o a heretic.',
    '%k squished %o the grot.',
    '%k tied %o to the back of the truck and dragged %h through the streets of Stillwater.',
    '%o gets a regularly-affected-by-gravity ball upside his head. %k gains a point.',
    '%o gets an anti-gravity big ball upside his head. %k gains a point.',
    '%o gets an anti-gravity ball upside his head. %k gains a point.',
    '%k didn\'t realize this level gave him the option of sparing %o.',
    "%k put a bangin' donk on %o.",
    '%o was plastered by a B.O.S.C.O. round. %k gains Brozouf.'
    "%o was spoon fed by %k.",
    '%k got mashy-spike-plated by %o.',
    '%k tried PK Fire Ω!\n%o took mortal damage!',
    "%o was thouroughly mixed with %k's bootspork.",
    "%o was zorched by %k.",
    "%o was hit by %k's mega-zorcher.",
    "%o was rapid zorched by %k.",
    "%o was zorched by %k's propulsor.",
    "%o was hit by %k's propulsor.",
    "%o was phase zorched by %k.",
    "%o fell prey to %k's LAZ device.",
    "%o was lazzed by %k.",
    "%o chewed on %k's fist.",
    "%o was mowed over by %k's chainsaw.",
    "%o was tickled by %k's pea shooter.",
    "%o chewed on %k's boomstick.",
    "%o was splattered by %k's super shotgun.",
    "%o was mowed down by %k's chaingun.",
    "%o rode %k's rocket.",
    "%o almost dodged %k's rocket.",
    "%o was melted by %k's plasma gun.",
    "%o was splintered by %k's BFG.",
    "%o couldn't hide from %k's BFG.",
    "%o was telefragged by %k.",
    "%o was railed by %k.",
    "%o was burned by %k's BFG.",
    "%o got staffed by %k.",
    "%o got a shock from %k's gauntlets.",
    "%o waved goodbye to %k's elven wand.",
    "%o was pegged by %k's ethereal crossbow.",
    "%o was blasted a new one by %k's dragon claw.",
    "%o got sent down under by %k's hellstaff.",
    "%o was scorched to cinders by %k's phoenix rod.",
    "%o was bounced by %k's firemace.",
    "%o got clapped by %k's charged staff.",
    "%o was bled dry by %k's gauntlets.",
    "%o was assaulted by %k's elven wand.",
    "%o was shafted by %k's ethereal crossbow.",
    "%o was ripped apart by %k's dragon claw.",
    "%k poured %p hellstaff on %o.",
    "%o was burned down by %k's phoenix staff.",
    "%o was squished by %k's giant mace sphere.",
    "%o was beaten to a pulp by %k's bare fists.",
    "%o got the axe from %k.",
    "%o had %p head caved in by %k's hammer.",
    "%o's soul was forged anew by %k's hammer.",
    "%o was silenced by %k's mighty Quietus.",
    "%o got a mace to the face from %k.",
    "%o was bitten by %k's serpent staff.",
    "%o choked on %k's serpent staff.",
    "%o was lit up by %k's flames.",
    "%o was cleansed by %k's Wraithverge.",
    "%o took one too many sapphire beams from %k.",
    "%o was turned into a frosty fellow by %k.",
    "%o recieved a shocking revelation from %k.",
    "%o was wiped off the face of the universe by %k's Bloodscourge.",
    "%o was unwittingly backstabbed by %k.",
    "%o got bolted to the wall by %k.",
    "%o recieved a lethal dose of %k's wrath.",
    "%o was drilled full of holes by %k's assault gun.",
    "%o gulped down %k's missile.",
    "%o was inverted by %k's H-E grenade.",
    "%o took a flame bath in %k's phosphorous pyre.",
    "%o was barbecued by %k.",
    "%o was zapped by %k.",
    "%o was viciously vaporized by %k.",
    "%o bowed down to the sheer power of %k's Sigil.",
    'Looks like %k blasted off Team %o again!',
    '%k blasted off Team %o again!',
    '%k taught %o the Dewey Decimal System.',
    '%o was taught the Dewey Decimal System by %k.',
    '%o was doomed to fall by %k.',
    '%k unfollowed %o.',
    '%k unfriended %o.',
    '%k Obama\'d %o.',
    '%k took %o to court.',
    '%k #YOLO\'d %o.',
    '%k uninstalled %o.',
    '%k annoyed %o.',
    '%k beat %o at life.',
    '%k bid farewell to %o.',
    '%k bought out by %o.',
    '%k attacked %o.',
    '%k baked %o.',
    '%k Jason\'ed %o.',
    '%k touhou\'d %o.',
    '%k billed %o.',
    '%k slammed %o.',
    '%k jammed %o.',
    '%k audited %o.',
    '%k shot %o.',
    '%k bleached %o.',
    '%k blotted out %o.',
    '%k bashed %o.',
    '%k bashed in %o\'s skull.',
    '%k betrayed %o.',
    '%k crossed %o.',
    '%k crossed %o out.',
    '%k boxed %o.',
    '%k boxed %o in.',
    '%k crossbred %o.',
    '%k cut %o down.',
    '%k booked %o.',
    '%k burried %o.',
    '%k disproved %o.',
    '%k disproved %o\'s existance.',
    '%k took %o to the pool.',
    '%k busted %o.',
    '%k killed %o.',
    '%k calculated %o.',
    '%k carved %o.',
    '%k canvased over %o.',
    '%k drank %o.',
    '%k ate %o.',
    '%k roasted %o.',
    '%k classified %o.',
    '%k choked %o.',
    '%k chewed %o.',
    '%k concentrated %o.',
    '%k concatenated %o.',
    '%k crashed into %o.',
    '%k cracked %o.',
    '%k closed %o.',
    '%k clutched %o.',
    '%k collapsed %o.',
    '%k showed %o the ancient arts of Shaolin Kung Fu.',
    '%k concluded %o.',
    '%k defenestrated %o.',
    '%k decided %o.',
    '%k deserted %o.',
    '%k exposed horrors to %o.',
    '%k infected %o.',
    '%k divided %o.',
    '%k drained %o.',
    '%k dripped %o.',
    '%k dropped %o.',
    '%k disliked %o.',
    '%k downvoted %o.',
    '%k consecrated on %o.',
    '%k forbade %o.',
    '%k downloaded %o.',
    '%k uploaded %o.',
    '%k installed %o.',
    '%k consigned %o.',
    '%o lost to %k.',
    '%o lost to %k at a Xiaolin Showdown.',
    '%o lost to %k at a tennis match.',
    '%o lost to %k at a boxing match.',
    '%o lost to %k at Portal 2 Co-op.',
    '%k sued %o.',
    '%o lost a lawsuit against %k.',
    '%k won a lawsuit against %o.',
    '%k forgot about %o.',
    '%k educated %o.',
    '%k obfuscated %o.',
    '%k dusted %o.',
    '%k lasered %o.',
    '%k constituted %o.',
    '%k misconstrued %o.',
    '%k contradicted %o.',
    '%k grinded %o.',
    '%o was had by %k.',
    '%k hit %o.',
    '%k snapchatted %o.',
    '%k converged %o.',
    '%k cooked %o.',
    '%k expanded %o.',
    '%k exploded %o.',
    '%k converted %o.',
    '%k charged %o.',
    '%k stumped %o.',
    '%k Trumped %o.',
    '%k Drumpfed %o.',
    '%k cheesed %o.',
    '%k crushed %o.',
    '%k dealt with %o.',
    '%k erased %o.',
    '%k released %o.',
    '%k applied for %o\'s release.',
    '%k inlaid %o.',
    '%k mispelled %o.',
    '%k detached %o.',
    '%k unpersoned %o.',
    '%k smited %o.',
    '%k dedded %o.',
    '%o got MUDAMUDAMUDA\'d by %k.',
    '%k ORAORAORA\'d %o.',
    '%k turned %o into a bagel sandwich.',
    'Killed by %k, %o got.',
    '%o, %k killed.',
    '%k murdered %o.',
    '%k brutally murdered %o.',
    '%k interwove %o.',
    '%k forcechoked %o.',
    '%k took %o out to the ballgame.',
    '%k drilled %o.',
    '%k empowered %o.',
    '%k faxed %o.',
    '%k fooled %o.',
    '%k filed %o.',
    '%k AFK\'d %o.',
    '%k ragequitted %o.',
    '%k tormented %o.',
    '%k knitted %o.',
    '%k evaporated %o.',
    '%k fizzed %o.',
    '%k flapped %o.',
    '%k folded %o.',
    '%k verbed %o.',
    '%k knocked %o out.',
    '%k Zandatsu\'d %o.',
    '%k guacamole\'d %o.',
    '%k road rollered %o.',
    '%k butterfingered %o.',
    '%o was taken into %k\'s van.',
    '%k blew up %o.',
    '%k clagged %o.',
    '%k clubbed %o.',
    '%k spinjumped on %o.',
    '%k poofed %o.',
    '%k composed %o.',
    '%k decomposed %o.',
    '%k Urban Dictionaried %o.',
    '%k wallhacked %o.',
    '%k terroristed %o.',
    '%k hounded on %o.',
    '%k RIPped on %o.',
    '%k SUPERHOTted %o.',
    '%k made %o SUPERHOT.',
    '%k goomba\'d %o.',
    '%k Falcon Punched %o.',
    '%k blazed %o.',
    '%k Chaos Sabred %o.',
    '%k threw %o into the underground.',
    '%k splatted %o.',
    '%k released the Kraken upon %o.',
    '%o was defamed by %k.',
    '%k defamed %o.',
    '%k failed %o.',
    '%k Space Jammed %o.',
    '%k Shrek\'d %o.',
    '%k Shrekt %o.',
    '%k Silverhorn Trident\'ed %o.',
    '%k air punched %o.',
    '%k air fried %o.',
    '%k drillkicked %o.',
    '%k turned %o into a pachinko machine.',
    '%k made %o into a sequel.',
    '%k formatted %o.',
    '%k technologic\'d %o.',
    '%k monopolised %o.',
    '%k blunderbussed %o.',
    '%k taught %o the joy of debt.',
    '%k mach tornado\'d %o.',
    '%k final smashed %o.',
    '%k tore %o to pieces.',
    '%k webbed %o.',
    '%k heaven-piercing drilled %o.',
    '%k Shoryukened %o.',
    '%k Hadoukened %o.',
    '%k L-cancelled %o.',
    '%k trophied %o.',
    '%k Triforce Slashed %o.',
    '%k Aura Stormed %o.',
    '%k PK Starstormed %o.',
    '%k dunked on %o.',
    '%k Galaxia Darknessed %o.',
    '%k Volt Tackled %o.',
    '%k used splash on %o!\nIt was Super Effective!',
    '%k Omega Blitzed %o.',
    '%k Kiwi Blitzed %o.',
    '%k Primal Reverted %o.',
    '%k Hydro Cannoned %o.',
    '%k Stealth Rocked %o.',
    '%k corrupted by %o.',
    '%k ragdolled %o.',
    '%k traded %o in.',
    '%k balled %o up.',
    '%k marinated %o.',
    '%k simmered %o.',
    '%k deposited %o.',
    '%k withdrew %o.',
    '%k deported %o.',
    '%k slapped %o.',
    '%k Kamehameha\'d %o.',
    '%k fragged %o.',
    '%o was ended by %k.',
    '%k ended %o.',
    '%k Bing\'d %o.',
    '%k Googled %o.',
    '%k unsubscribed to %o.',
    '%k hacked %o.',
    '%k 4chan\'d %o.',
    '%k annihilated %o.',
    '%k decimated %o.',
    '%o was drowned by %k.',
    '%k drowned %o.',
    '%k hashtagged %o.',
    '%k whaled on %o.',
    '%k→%o %k→%o %k→%o %k→%o %k→%o %k→%o %k→%o %k→%o %k→%o ',
    '%k Hamon\'d %o.',
    '%k hammed on %o.',
    '%k denied %o.',
    '%k hung %o.',
    '%k eliminated %o.',
    '%k delimited %o.',
    '%k added %o to the file.',
    '%k 0x10c %o',
    '%k nidhogged %o.',
    '%k Steve\'d %o.',
    '%k dined on %o.',
    '%k elbowed %o.',
    '%k Tony Abboted %o.',
    '%k David Cameroned %o.',
    '%k Donald Trumped %o.',
    '%k Donald Drumpfed %o.',
    '%k pinged @\u2060%o.',
    '%k ended %o\'s streak.',
    '%k ended %o\'s game.',
    '%k charbroiled %o.',
    '%k despawned %o.',
    '%k bushwacked %o.',
    '%k sneezed on %o.',
    '%k heckled at %o.',
    '%k coughed at %o.',
    '%k signed out %o.',
    '%k sandwiched %o.',
    '%k swagged on %o.',
    '%k dank memed %o.',
    '%k evaluated %o.',
    '%k ignited %o.',
    '%k oppresed %o.',
    '%k operated %o.',
    '%k overflowed %o.',
    '%k pasted %o.',
    '%k pastad %o.',
    '%k spaghetti\'d %o.',
    '%k prescribed %o.',
    '%k denounced %o.',
    '%k took %o out to dinner.',
    '%k seperated %o.',
    '%k subtracted %o.',
    '%k taxed %o.',
    '%k terminated %o.',
    '%k puncutred %o.',
    '%k brewed %o into a delicious cup of coffee.',
    '%k taxidermied %o.',
    '%k slits %o\'s throat.',
    '%k stabbed %o.',
    '%k shanked %o.',
    '%k rekt %o.',
    '%k owned %o.',
    '%k pwned %o.',
    '%o\'s organs were ripped out by %k.',
    '%k ripped out the organs of %o.',
    '%k burned %o.',
    '%k launched %o out of a cannon into the sun.',
    '%k clocked %o on the head.',
    '%k pushed %o into a tarpit.',
    '%k trapped %o in quicksand.',
    '%k one-punched %o.',
    '%k punched %o.',
    '%k pasta machined %o.',
    '%k Aoshima\'d %o.',
    '%k Wabisuke\'d %o.',
    '%k Gear Seconded %o.',
    '%k typoed %o.',
    '%k Spirit Bombed %o.',
    '%k Who The Hell Do You Think I Am Kicked %o.',
    '%k Jim Sterlinged %o.',
    '%k Jim Fucking Sterling Sonned %o.',
    '%k entropied %o.',
    '%k demolished %o.',
    '%k turned %o into poutine.',
    '%k DENDRO\'d %o.',
    '%k Azusayumi\'d %o.',
    '%k Baryon Lanced %o.',
    '%k cast jammed %o.',
    '%k Niflheimed %o.',
    '%k Gram Demolitioned by %o.',
    '%k Lapised %o.',
    '%k Pluto\'d %o.',
    '%k Inferno\'d %o.',
    '%k Napstablocked %o.',
    '%o was slain by %k.',
    '%k bored %o to death.',
    '%k baked %o into a pizza.',
    '%k sniped %o.',
    '%k threw piss at %o.',
    '%k canned %o.',
    '%k disemboweled %o.',
    '%k sent %o to %p grave.',
    '%k gnocchi\'d %o.',
    '%k railway\'d %o.',
    '%k played a blank card for %o.',
    '%k oh\'d %o.',
    '%o\'s killing spree was ended by %k',
    '%k futurmedia\'d %o.',
    '%o imagines death so much it feels more like a memory. Is this where it gets %h? On %p feet... several feet ahead of %h. %G can see it coming. Should %g run, or fire %p gun, or let it be? *There is no beat, no melody.* %k, %p first friend and enemy... maybe the last face %g ever will see. *If %o throws away his shot, is this how %k remembers %h?* What if this bullet is %p legacy...\n***LEGACY...*** *what is a legacy?* It\'s planting seeds in a garden you never get to see. %G wrote some notes at the beginning of a song someone will sing for %h. America, you great unfinished symphony you sent for %h! You let %h make a difference! A place where even orphan immigrants can leave their fingerprints and\n***RISE UP.*** %G might be running out of time, %p *TIME\'S UP.* *WISE UP.* Eyes... *up.* %G catch a glimpse of the other side. Laurens leads a soldier\'s chorus on the other side. *%P son is on the other side! He\'s with %p mother on the other side!* ***Washington is watching from the other side! Teach them how to say goodbye~ RISE UP. RISE UP. RISE UP.*** __***ELIZA***__\n\n%o would love to take your time. %G\'ll see you on the other side.\n~~*Raise a glass, to freedom...*~~\n"**W** %G aims **A** their pistol **I** at the **T** sky!"\n\n%k strikes %h right between %p ribs.',
    '%o was kicked from the party by %k.',
    '%k kicked %o out of the party.',
    '%k banhammered %o.',
    '%k Ramza\'d %o.',
    '%k Oreganostrared %o.',
    '%k atomised %o.',
    '%k purified %o.',
    '%k anime\'d %o.',
    '%k animoo\'d %o.',
    '%k Objectioned %o.',
    '%k OBJECTIONED!!! %o.',
    '%k DNA\'d %o.',
    '%k Trinitrotoluene\'d %o.',
    '%k Spicy Meatballed %o.',
    '%k oxidaned %o.',
    '%k Dihydrogen Monoxided %o.',
    '%k ate %o\'s immortal soul.',
    '%k used the .kill command on %o.',
    '%k hoarded %o\'s tags.',
    '%k hoarded %o.',
    '%o discovered the author of the journals, %k.',
    '%k Zvarri\'d %o.',
    '%k Spacechemed %o.',
    '%k caked %o.',
    '%k Pheonix Wrighted %o.',
    '%o made a deal with %k.',
    '%k Gram Dispersioned %o.',
    '%k DW\'ed %o.',
    '%k spoilered %o.',
    '%k Shauned %o.',
    '%k Dippy Freshed %o.',
    '%k dipped %o.',
    '%k Flip-a-dip-dipped %o.',
    '%k double dipped %o.',
    '%k B& %o.',
    '%k Meseeked %o.',
    '%k Mr. Meseeked %o.',
    '%k Wubba-lubba-dub-dubbed %o.',
    '%k appostrophe\'d %o.',
    '%k escape charactered %o.',
    '%k Morty\'d %o.',
    '%k erased %o from time.',
    '%k Gamma Ray Filtered %o.',
    '%k Tardised %o.',
    '%k Lapissed on %o.',
    '%k got\nB L A Z E D\nL\nA\nZ\nE\nD\nby %o.',
    '%k sponged on %o.',
    '%k sponged %o.',
    '%k tabulated %o.',
    '%k Olive Gardened %o.',
    '%k breadsticked %o.',
    '%k threw away %o\'s shot.',
    '%k Jerry\'d %o.',
    '%k encapsulated %o.',
    '%k sondered %o.',
    '%k MURRICA\'d %o.',
    '%k sprited %o.',
    '%k salsa\'d %o.',
    '%k VLC\'d %o.',
    '%k Photoshopped %o.',
    '%k developed an app for %o before dopping support for it after a week.',
    '%k Space Unicorned %o.',
    '%k Neon Pegasus\'d %o.',
    '%k used an emoji on %o.',
    '%o felt the blast from %k\'s party cannon.',
    '%k tried to tell %o to be sensible, but %g didn\'t listen!',
    'Actually, %k snaps %o in two. **Just kidding!**',
    '%k fillered %o.',
    '%k showed %o a lethal Codepen.',
    '%o lost to %k at Cards Against Humanity.',
    '%k Oldbagged %o.',
    '%k took %o to the Mystery Shack.',
    '%k threw a combustible lemon at %o.',
    '%k diddly darn snapped %o\'s neck.',
    '%k called %o a "buddy chum pal friend buddy pal chum bud friend fella bruther amigo pal buddy friend chummy chum chum pal friend pal home slice bread slice dawg friend buddy chum friend chum pally pal chum friend friend buddy chum friend chum pally pal chum friend friendly friend friend pal friend buddy chum pally friend chum buddy"',
    '%o met all of %k\'s standards. Almost.',
    '%k wowza\'d %o.',
    '%k toffee\'d %o.',
    'When %o aimed at the sky %g may have been the first one to die, but %k\'s the one who paid for it.',
    '"%o, do you yield?"\n"%k shot %h in the chest, *yes* %g yields!"',
    '%k tore %o apart for speaking freely about the Continental Congress.',
    '%o looked into %k\'s eyes and was helpless- wait, that\'s `{}ship`, wrong command. Sorry.'.format(base.config['invoker']),
    '%o called %k "Son" one time too many.',
    '%k looks %o in the eye, aims no higher, summons all the courage that\'s required, then counts...\n*1, 2, 3, 4, 5, 6, 7, 8, 9...*\n***Number 10... paces! Fire!***',
    '%k blew %o the fuck out in a cabinet meeting.',
    '%k\'s retort to %o in the cabinet meeting was fucking lit.',
    '%o made such a blunder, sometimes it makes %h wonder why %k even brings the thunder.',
    '%o was unable to convice %k to help in the French Revolution.',
    'How does %o the short-tempered cronie and creator of the coast guard, founder of the New York Post ardently abuse %p cabinet post and destroy %p reputation? Welcome, folks, to the ***%k Administration!***',
    '%o aimed to the sky to be honorable, but %k fired on the count of 7, jerkass.',
    '%k decided the world wasn\'t wide enough for %o too.',
    '%k JOHN CENA\'D %o. 🎺🎺🎺🎺🎺',
    '%k forked %o.',
    '%k pull requested %o.',
    '%k supervises %o with a shitton of soldiers. And then %p security was downgraded to a ***fuck***ton of soldiers. *(Did I say downgrade? I meant upgrade.)*',
    'It is true that %k killed %o, and yet, is not %p murderer',
    '%k used Outburst!\nSensational!\n%o is dazed!',
    '%o 🔫 %k.',
    '%k 👞 %o.',
    '%k updated %o\'s firmware.',
    '%k Woomy\'d %o.',
    '%k delisted %o.',
    '%k unlisted %o.',
    '%k datched %o.',
    '%k squanched %o.',
    '%k Kickstartered %o.',
    '%k yee haw\'d %o.',
    '%k yee naw\'d %o.',
    '%k kekked %o.\ncake*',
    '%k caked %o.',
    '%k 86\'ed %o.',
    '%k DETERMINATED %o.',
    '%k Megalovania\'d %o.',
    '%k Rule Disordered %o.',
    '%k Coconut 56\'ed %o.',
    '%k Netflix\'ed %o.',
    '%k JiffyBot\'ed %o.',
    '%k funyarinpa\'d %o.',
    '%k Apollo\'d %o.',
    '%k Athena\'d %o.',
    '%k employed Gorilla Warfare against %o.',
    '%k censored %o.',
    '%k punched a hole in %o.',
    '%k ordered %o from SCP-294.',
    '%k bloodbent %o.',
    '%k sent %o the Bee Movie script.',
    '%k sent %o the Bee Movie script.\nAccording to all known laws of aviation, there is no way a bee should be able to fly. Its wings are too small to get its fat little body off the ground. The bee, of course, flies anyway because bees don’t care what humans think is impossible.'
    '%k flagged %o for copyright.',
    '%k sent %o to a small island off yhe Philippines.',
    '%o was last seen alive with %k.',
    '%k killed %o... like a feesh.',
    '%k killed %o. Jerry came too.',
    '%k and Cartoon Network UK leaked %o. We\'re still on hiatus, though.',
    '%o wasn\'t noticed by %k-senpai.',
    '%k SJW\'ed %o.',
    '%k told %o to check %p privilege.'
    '%k ayy lmao\'d %o.',
    '%k Jerry\'d %o.',
    '%k crushed %o with Balrog.\n~~Huzzah!~~ Oh Yeah!',
    '%k force-fed %o a mushroom.',
    '%k fed %o to a mammoth.',
    '%k Eric\'d %o.',
    '%k Tatsuya\'d by %o.',
    '%k Brindley\'d %o.',
    '%k Schwifty\'d %o.',
    '%k zozzled %o.',
    '%k xyzzy\'d %o.',
    '%k frotz\'d %o.'
    '%k Hazzated %o.',
    '%k 👉🔥 %o.',
    '%k dissolved %o.',
    '%k ripped %o apart.',
    '%k sawed off %o\'s head and other limbs.',
    '%k Shu Takumi\'d %o.',
    '%k jajajajaja\'d %o.',
    '%k wavedashed %o.',
    '%k destroyed %o.',
    '%k absolutely destroyed %o.',
    '%k deleted %o.',
    '%k made %o into a movie.\nIt wasn\'t as good as the book.',
    '%k randverbed %o.',
    '%k randomverbed %o.',
    '%k rate-limited %o.',
    '%o is banne by %k'
]

def postify(phrase, message, pronouns, suicide=False, *args):
    w = phrase

    if suicide is True:
        if message.mentions:
            w = w.replace(
                '%k', message.mentions[0].name
                )
        elif len(message.content.split()) > 1:
            w = w.replace(
                '%k', message.content.split(None, 1)[1]
            )

    #lower case
    w = w.replace(
        '%k', message.author.display_name
        ).replace(
            '%g', pronouns['%g']
            ).replace(
                '%h', pronouns['%h']
                ).replace(
                    '%p', pronouns['%p']
                    )

    #capitals
    w = w.replace(
        '%G', pronouns['%g'].capitalize()
        ).replace(
            '%H', pronouns['%h'].capitalize()
            ).replace(
                '%P', pronouns['%p'].capitalize()
                )

    if args:
        print(args)
        w = phrase.replace(
            '%v', args[0]['%g']
            ).replace(
                '%b', args[0]['%h']
                ).replace(
                    '%l', args[0]['%p']
                    ).replace(
                        '%V', args[0]['%g'].capitalize()
                        ).replace(
                            '%B', args[0]['%h'].capitalize()
                            ).replace(
                                '%L', args[0]['%p'].capitalize()
                                )


    if message.mentions:
        w = w.replace(
            '%o', message.mentions[0].name
            )
    elif len(message.content.split()) > 1:
        w = w.replace(
            '%o', message.content.split(None, 1)[1]
        )

    return w

@base.cacofunc
async def kill(message, client):
    '''
    **{0}kill** [ mention | string ]
    **{0}kill** [ optin ] [ he/she/they ] [ him/her/them ] [ his/her/their ]
    **{0}kill** [ optin ] [ check ]
    Prints an obituary for the mentioned party as though you had killed it. By default, will use "They" pronouns. You can do `{0}kill optin 1 2 3` to opt into replacing your pronouns with 3 of your choice. The syntax is posted above. This is agnostic: You can use any word you want for a pronoun.
    *Examples: `{0}kill @BooBot`, `{0}kill optin schlee schlim schleir`*
    '''

    try:
        with open('configs/pronouns.json') as datastream:
            optin = json.load(datastream)
    except FileNotFoundError:
        with open('configs/pronouns.json', 'w') as datastream:
            datastream.write('{}')
        optin = {}

    params = message.content.split()
    name = message.content.split(None, 1)
    if len(name) > 1:
        name = name[1]

    pronouns = {'%g':'they', '%h':'them', '%p': 'their'}
    killerpronouns = {'%g':'they', '%h':'them', '%p': 'their'}

    if message.content.lower() == '{}kill la kill'.format(base.config['invoker']):
        await client.send_message(message.channel, '{} tried to make a shitty anime joke and was victimized because of it.'.format(message.author.display_name))
        return

    if message.content.lower() == '{}kill the noise'.format(base.config['invoker']):
        await client.send_message(message.channel, '{} did that shit.'.format(message.author.display_name))
        return

    if message.content.lower() == '{}kill your heroes'.format(base.config['invoker']):
        await client.send_message(message.channel, 'No need to worry, {}, because everybody will die.'.format(message.author.display_name))
        return

    if message.mentions and message.mentions[0].id in optin:
        pronouns = optin[message.mentions[0].id]
    else:
        if len(params) > 1:

            name2member = None

            names = [x for x in message.server.members if x.name == name]
            displaynames = [x for x in message.server.members if x.display_name == name]

            if names:
                name2member = names[0]
            elif displaynames:
                name2member = displaynames[0]

            if name2member and name2member.id in optin:
                pronouns = optin[name2member.id]
        elif message.author.id in optin:
            pronouns = optin[message.author.id]

    if message.author.id in optin:
        killerpronouns = optin[message.author.id]

    if len(params) < 2:
        await client.send_message(message.channel, postify(random.choice(suicides), message, pronouns))
        return

    if message.mentions and message.mentions[0] == message.author:
        await client.send_message(message.channel, postify(random.choice(suicides), message, pronouns))
        return

    if message.mentions:
        await client.send_message(message.channel, postify(random.choice(killmsgs), message, pronouns, killerpronouns))
        return

    if params[1] == 'optin':
        if len(params) == 3 and params[2] == 'check':
            await client.send_message(
                message.channel,
                'Your pronouns are set to:\nHe/She/They: {}\nHim/Her/Them: {}\nHis/Her/Their: {}.'.format(
                    optin[message.author.id]['%g'],
                    optin[message.author.id]['%h'],
                    optin[message.author.id]['%p']
                    )
                )
            return

        try:
            optin[message.author.id] = {
                '%g' : params[2],
                '%h' : params[3],
                '%p' : params[4]
            }

            with open('configs/pronouns.json', 'w') as datastream:
                json.dump(optin, datastream, indent=4)

            await client.send_message(message.channel, '{}: I have successfully updated your pronouns to {}/{}/{}.'.format(
                message.author.display_name,
                params[2],
                params[3],
                params[4]
                ))

        except IndexError:
            await client.send_message(message.channel, '{}: You must provide 3 pronouns as an analogue to "he/she/they", "him/her/them", and "his/her/their", in that order.'.format(message.author.display_name))

        return

    if name.lower() == message.author.display_name.lower() or name.lower() == message.author.name.lower() or name.lower() in ['me', 'myself', 'i']:
        await client.send_message(message.channel, postify(random.choice(suicides), message, pronouns))
        return

    if name.lower() in ['us', 'everyone']:
        await client.send_message(message.channel, postify(random.choice(suicides), 'Everyone', pronouns))

    if name.lower() in ['you', 'yourself']:
        await client.send_message(message.channel, postify(random.choice(suicides, message.server.me.display_name, pronouns)))

    if '@everyone' in message.content or '@here' in message.content:
        await client.send_message(message.channel, '{}: **Do not use this command to circumvent everyone mention restrictions.**'.format(message.author.display_name))
        return

    await client.send_message(message.channel, postify(random.choice(killmsgs), message, pronouns, killerpronouns))

@base.cacofunc
async def rip(message, client):
    '''
    **{0}rip** [ mention | string ]
    Prints an obituary for the mentioned party as though they had died from either their own means or an outside party. Pronouns are taken from the `{0}kill` command. See it's help file for more information.
    *Example: `{0}rip @42`*
    '''

    try:
        with open('configs/pronouns.json') as datastream:
            optin = json.load(datastream)
    except FileNotFoundError:
        with open('configs/pronouns.json', 'w') as datastream:
            datastream.write('{}')
        optin = {}

    params = message.content.split()
    name = message.content.split(None, 1)
    if len(name) > 1:
        name = name[1]

    pronouns = {'%g':'they', '%h':'them', '%p': 'their'}

    if message.mentions and message.mentions[0].id in optin:
        pronouns = optin[message.mentions[0].id]
    else:
        if len(message.content.split()) > 1:
            name2member = discord.utils.get(message.server.members, name=name)
            if name2member and name2member.id in optin:
                pronouns = optin[name2member.id]
        elif message.author.id in optin:
            pronouns = optin[message.author.id]

    if len(params) < 2:
        await client.send_message(message.channel, postify(random.choice(suicides), message, pronouns))
        return

    if message.mentions and message.mentions[0] == message.author:
        await client.send_message(message.channel, postify(random.choice(suicides), message, pronouns))
        return

    if message.mentions:
        await client.send_message(message.channel, postify(random.choice(suicides), message, pronouns, suicide=True))
        return

    if name.lower() == message.author.display_name.lower() or name.lower() == message.author.name.lower() or name.lower() in ['me', 'myself', 'i']:
        await client.send_message(message.channel, postify(random.choice(suicides), message, pronouns))
        return

    if name.lower() in ['us', 'everyone']:
        await client.send_message(message.channel, postify(random.choice(suicides), 'Everyone', pronouns))

    if name.lower() in ['you', 'yourself']:
        await client.send_message(message.channel, postify(random.choice(suicides, message.server.me.display_name, pronouns)))

    if '@everyone' in message.content or '@here' in message.content:
        await client.send_message(message.channel, '{}: **Do not use this command to circumvent everyone mention restrictions.**'.format(message.author.display_name))
        return

    await client.send_message(message.channel, postify(random.choice(suicides), message, pronouns, suicide=True))
