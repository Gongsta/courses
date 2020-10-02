import random
import sys
import pygame
from pygame.locals import *
import numpy
import matplotlib.pyplot as plt

SW = 280
SH = 511

# ['kokonorttf', 'stixintupbolotf', 'minionpromediumitotf', 'helveticattc', 'chaparralprolightitotf', 'microsoftsansserifttf', 'adobedevanagariregularotf', 'obelixprocyrttf', 'sfcompacttextitalicttf', 'bebasregularttf', 'kozgopr6nmediumotf', 'stixsizthreesymbolotf', 'papyrusttc', 'elitedangerexpanditalttf', 'minionprosemiboldotf', 'myriadprosemiboldotf', 'birchstdotf', 'poplarstdotf', 'charterttc', 'notoserifmyanmarttc', 'cooperblackstditalicotf', 'bradleyhandboldttf', 'georgiabolditalicttf', 'kozminpr6nregularotf', 'latothinitalicttf', 'gothamlightotf', 'stixnonunibolotf', 'lemonmilkbolditalicotf', 'myriadarabicbolditotf', 'minionprobolditotf', 'mesquitestdotf', 'tamilmnttc', 'ocrastdotf', 'couriernewitalicttf', 'elitedangersemiboldttf', 'elitedangerboldsuperitalttf', 'adobearabicitalicotf', 'euphemiacasttc', 'redemptionttf', 'sourcesansprobolditotf', 'bodoni72smallcapsbookttf', 'mshtakanttc', 'sourcesansproblackotf', 'kozminpr6nextralightotf', 'spartanmbregularotf', 'beyondthemountainsttf', 'stixintupsmbolotf', 'universltstdboldoblotf', 'stixsizfoursymregotf', 'kohinoorteluguttc', 'devanagarimtttc', 'lemonmilklightitalicotf', 'agaramondproregularotf', 'elitedangersemiboldconditalttf', 'sourcesansprosemiboldotf', 'arialroundedboldttf', 'ヒラキノ角コシックw3ttc', 'montserratthinitalicttf', 'impactttf', 'kozgoproboldotf', 'skiattf', 'munattc', 'elitedangerexpandttf', 'montserratsemiboldttf', 'chopinscriptotf', 'futuramediumbtttf', '22736otf', 'myriadprobolditotf', 'elitedangersemiboldcondttf', 'bigcaslonttf', 'kozminpr6nmediumotf', 'chalkboardsettc', 'applegothicttf', 'lucidagrandettc', 'andalemonottf', 'sfnsdisplaycondensedheavyotf', 'lemonmilkitalicotf', 'ヒラキノ明朝pronttc', 'kozminproheavyotf', 'sourcesansprolightitotf', 'futuraxblkbtttf', 'ヒラキノ丸コpronw4ttc', 'applemyungjottf', 'comicsansmsboldttf', 'adobedevanagariboldotf', 'sfnsitalicttf', 'signatrattf', 'tektonproboldcondotf', 'kefattc', 'zapfinottf', 'stixsizthreesymregotf', 'phosphatettc', 'tektonproboldoblotf', 'lemonmilkotf', 'optimusprincepssemiboldttf', 'latoregularttf', 'newyorkttf', 'theboldfontttf', 'mishafittf', 'montserratextraboldttf', 'avengeanceheroicavengerbittf', 'universlightnormalttf', 'adobenaskhmediumotf', 'stixsiztwosymbolotf', 'avenirnextcondensedttc', 'myriadproregularotf', 'khmersangammnttf', 'ptmonottc', 'nunitolightitalicttf', 'futuraboldfontttf', 'futuralightbtttf', 'tahomaboldttf', 'sfcompactdisplayttf', 'lastresortotf', 'malayalamsangammnttc', 'arabicuidisplayttc', 'myriadprocondotf', 'futurabookitalicfontttf', 'chalkdusterttf', 'sfnsdisplaycondensedboldotf', 'arialblackttf', 'nunitosemibolditalicttf', 'adobedevanagariitalicotf', 'trajanproboldotf', 'futuralightfontttf', 'minionproboldotf', 'arialnarrowttf', 'tektonproboldotf', 'ralewaymediumttf', 'trebuchetmsitalicttf', 'arialitalicttf', 'myriadproboldcondotf', 'acaslonproregularotf', 'ralewaylightttf', 'ヒラキノ角コシックw4ttc', 'montserratextrabolditalicttf', 'tahomattf', 'futurttf', 'laomnttc', 'kannadasangammnttc', 'elitedangersuperitalttf', 'kozgopr6nregularotf', 'rosewoodstdregularotf', 'myanmarmnttc', 'elitedangerttf', 'wingdings3ttf', 'sourcesansproextralightitotf', 'nunitosemiboldttf', 'trattatellottf', 'sfnsdisplaycondensedsemiboldotf', 'stixgeneralitalicotf', 'nunitoextralightttf', 'stixnonuniitaotf', 'stheitilightttc', 'billionthinepersonaluseonlyttf', 'sfnsroundedttf', 'nadeemttc', 'kohinoorgujaratittc', 'sfnstextcondensedregularotf', 'adobehebrewitalicotf', '22741otf', 'universltstdboldotf', 'elitedangeroutttf', 'kozgoproregularotf', 'nuevastdboldcondotf', 'bignoodletitlingobliquettf', 'ralewayextrabolditalicttf', 'timesnewromanbolditalicttf', 'trebuchetmsboldttf', 'hobostdotf', 'kozgoproheavyotf', 'aquakanattc', 'lettergothicstdboldslantedotf', 'elitedangersemitalttf', 'gujaratimtttc', 'kozgopr6nlightotf', 'futurattc', 'stixsizonesymbolotf', 'wingdingsttf', 'lemonmilkboldotf', 'elitedangersemiboldexpandttf', 'stixintupdbolotf', 'ralewayextralightitalicttf', 'caviardreamsttf', '16036otf', 'elitedangersemiboldexpanditalttf', 'nunitoboldttf', 'arialbolditalicttf', 'sfnstextcondensedmediumotf', 'kohinoorbanglattc', '28909otf', 'copperplatettc', 'baskervillettc', 'banglamnttc', 'ralewaythinitalicttf', 'stixintsmregotf', 'latoblackttf', 'nuevastditalicotf', 'itfdevanagarittc', 'latothinttf', 'applechanceryttf', 'minionproregularotf', 'ralewayboldttf', 'verdanaboldttf', 'acaslonprosemibolditalicotf', 'georgiaboldttf', 'kozminpromediumotf', 'sanattc', 'obelixprobcyrttf', 'sfnstextcondensedlightotf', 'agaramondproitalicotf', 'elitedangerconditalttf', 'stixgeneralbolotf', 'montserratregularttf', 'ヒラキノ角コシックw5ttc', 'chaparralprobolditotf', 'myriadproconditotf', 'sfcompactroundedttf', 'sourcesansprolightotf', 'elitedangerboldttf', 'kozminpr6nheavyotf', 'elitedangergraditalttf', 'minionpromediumotf', 'montserratblackttf', 'futuraextrablackfontttf', 'newyorkitalicttf', 'adobearabicboldotf', 'albayanttc', 'montserratboldttf', 'sfnsdisplaycondensedmediumotf', 'elitedangerboldexpandttf', 'stixsizfoursymbolotf', 'stixintupregotf', 'stixintupsmregotf', 'applesymbolsttf', 'sfnsmonoitalicttf', 'myriadarabicregularotf', 'helveticaneuedeskinterfacettc', 'notosansmyanmarttc', 'timesnewromanitalicttf', 'trajanpro3regularotf', 'zapfdingbatsttf', 'timesttc', 'helveticaneuettc', 'stixnonunibolitaotf', 'nunitobolditalicttf', 'sfnstextcondensedheavyotf', 'luminarittf', 'kohinoorttc', 'notosanskannadattc', 'elitedangeroutitalttf', 'lemonmilklightotf', 'sanchezregularotf', 'elitedangerboldexpanditalttf', 'montserratlightttf', 'kozgopr6nextralightotf', 'kozminpr6nlightotf', 'nuevastdboldconditalicotf', 'ptsansttc', 'ralewayblackitalicttf', 'chaparralproboldotf', 'avenirnextttc', 'ralewayregularttf', 'gurmukhimnttc', 'ralewayextraboldttf', 'lithosproblackotf', 'geezaprottc', 'avengeanceheroicavengeratttf', 'gurmukhittf', 'notosansjavaneseregularotf', 'blackoakstdotf', 'signatraotf', 'ralewaysemibolditalicttf', 'mishafigoldttf', 'sfnstextcondensedboldotf', 'montserratregularitalicttf', 'shree714ttc', 'futurabookfontttf', 'hiraginosansgbttc', 'loraregularitalicttf', 'montserratmediumttf', 'sourcesansproregularotf', 'sfnsdisplaycondensedlightotf', 'timesnewromanttf', 'elitedangersemiboldsuperitalttf', 'adobesongstdlightotf', 'latolightttf', 'montserratsemibolditalicttf', 'kozgoproextralightotf', 'myriadhebrewitotf', 'applesdgothicneottc', 'elitedangercondttf', 'nuevastdcondotf', 'stixsizfivesymregotf', 'lettergothicstdotf', 'chaparralproitalicotf', 'captureitttf', 'montserratblackitalicttf', 'vcrosdmono1001ttf', 'chalkboardttc', 'adobearabicregularotf', 'ヒラキノ角コシックw6ttc', 'keyboardttf', 'kozgopromediumotf', 'waseemttc', 'khmermnttc', 'elitedangersemiboldsemitalttf', 'adobefangsongstdregularotf', 'symbolttf', 'latobolditalicttf', 'acaslonproitalicotf', 'sfnsdisplaycondensedthinotf', 'stixgeneralotf', 'alnilettc', 'elitedangerleftttf', 'nunitoregularitalicttf', 'beirutttc', 'adobehebrewbolditalicotf', 'decotypenaskhttc', 'loraregularttf', 'nunitoextralightitalicttf', 'adobefanheitistdboldotf', 'elitedangerbolditalttf', 'ralewaythinttf', 'diverplatettf', 'arialnarrowitalicttf', 'ralewaylightitalicttf', 'georgiattf', 'sfnsdisplaycondensedregularotf', 'stixnonuniotf', 'myriadhebrewregularotf', 'adobehebrewregularotf', 'prestigeelitestdbdotf', 'ralewaymediumitalicttf', 'trajanproregularotf', 'arialhbttc', 'ralewayitalicttf', 'elitedangersemibolditalttf', 'futuralightitalicfontttf', 'sfnsttf', 'kozminprolightotf', 'adobearabicbolditalicotf', 'bodoni72osttc', 'webdingsttf', 'herculanumttf', 'stencilstdotf', 'futuraheavyfontttf', 'sfnsdisplaycondensedblackotf', 'sfnsmonottf', 'stixvarotf', 'elitedanger3ditalttf', 'angellinademootf', 'tektonproboldextotf', 'rockwellttc', 'sukhumvitsetttc', 'diwanthuluthttf', 'oratorstdslantedotf', 'sinhalamnttc', 'ptserifcaptionttc', 'chaparralproregularotf', 'bodoniornamentsttf', 'elitedangergradttf', 'oratorstdotf', 'adobedevanagaribolditalicotf', 'kozminproregularotf', 'applecoloremojittc', 'crackersbrusherotf', 'nunitolightttf', 'universltstdotf', 'montserratlightitalicttf', 'stixintdbolotf', '9664otf', 'myriadarabicboldotf', 'trajanpro3boldotf', 'fabianattf', 'obelixprobitcyrttf', 'kozgoprolightotf', 'voguettf', 'stixsizonesymregotf', 'elitedangertitlettf', 'savoyeletttc', 'bebasneueregularttf', 'elitedanger3dttf', 'bignoodletitlingttf', 'gurmukhisangammnttc', 'ヒラキノ角コシックw7ttc', 'stixvarbolotf', 'arialttf', 'myriadprosemibolditotf', 'devanagarisangammnttc', 'kozminpr6nboldotf', 'sfnsdisplaycondensedultralightotf', 'arialnarrowboldttf', 'stixsiztwosymregotf', 'waltographuittf', 'nuevastdboldotf', 'muktamaheettc', 'trebuchetmsbolditalicttf', 'dincondensedboldttf', 'sinhalasangammnttc', 'latolightitalicttf', 'signpainterttc', 'acaslonproboldotf', 'acaslonprosemiboldotf', 'comicsansmsttf', 'ヒラキノ角コシックw0ttc', 'adobekaitistdregularotf', 'historeademottf', 'trebuchetmsttf', 'acaslonprobolditalicotf', 'bodoni72ttc', 'myriadproboldotf', 'sfcompacttextttf', 'kailasattc', 'sfnstextcondensedsemiboldotf', 'futuramediumitalicfontttf', 'baghdadttc', 'montserratthinttf', 'minionproboldcnotf', 'ptserifttc', 'lorabolditalicttf', 'raananattc', 'sourcesansproblackitotf', 'ralewaysemiboldttf', 'americantypewriterttc', 'wingdings2ttf', 'elitedangerboldcondttf', 'nunitoblackitalicttf', 'charlemagnestdboldotf', 'verdanattf', 'minionproboldcnitotf', 'timesnewromanboldttf', 'spartanmbsemiboldotf', 'snellroundhandttc', 'krungthepttf', 'altarikhttc', 'hoeflertextttc', 'bebasregularotf', 'sourcesansproboldotf', 'futuraheavyitalicfontttf', 'silomttf', 'montserratextralightitalicttf', 'spartanmbthinotf', 'applebraillepinpoint6dotttf', 'couriernewttf', 'avenirttc', 'myriadproboldconditotf', 'applebraillepinpoint8dotttf', 'laosangammnttf', 'futuramediumcondensedbtttf', 'sourcesansproextralightotf', 'telugusangammnttc', 'adobeheitistdregularotf', 'lithosproregularotf', 'ヒラキノ角コシックw8ttc', 'banglasangammnttc', 'adobemyungjostdmediumotf', 'myanmarsangammnttc', 'verdanaitalicttf', 'applebraillettf', 'damascusttc', 'agaramondprobolditalicotf', 'arialnarrowbolditalicttf', 'elitedangertitleitalttf', 'couriernewbolditalicttf', 'adobehebrewboldotf', 'oriyamnttc', 'avengeanceheroicavengerbdttf', 'menlottc', 'avengeanceheroicavengerttf', 'waltograph42otf', 'montserratextralightttf', 'adobegurmukhiregularotf', 'nunitoblackttf', 'cooperblackstdotf', 'stixintsmbolotf', 'cochinttc', 'ralewayextralightttf', 'nunitoextraboldttf', 'dinalternateboldttf', 'latoblackitalicttf', 'sourcesansproitotf', 'ヒラキノ角コシックw1ttc', 'couriernewboldttf', 'sanchezregularitaotf', 'blackswordotf', 'applebrailleoutline6dotttf', 'caviardreamsbolditalicttf', 'loraboldttf', 'palatinottc', 'arabicuitextttc', 'hoeflertextornamentsttf', 'giddyupstdotf', 'arialunicodettf', 'minionprosemibolditotf', 'tamilsangammnttc', 'spartanmbblackotf', 'montserratbolditalicttf', 'newpeninimmtttc', 'noteworthyttc', 'brushscriptstdotf', 'minionproitotf', 'caviardreamsboldttf', 'farisittf', 'oriyasangammnttc', 'ayudishafreeversionttf', 'verdanabolditalicttf', 'kozgopr6nheavyotf', 'futurabolditalicfontttf', 'stixintdregotf', 'notonastaliqttc', 'kozminproboldotf', 'nisc18030ttf', 'telugumnttc', 'goodbrushotf', 'myriadhebrewboldotf', 'corsivattc', 'gillsansttc', 'agaramondproboldotf', 'spartanmblightotf', 'obelixproitcyrttf', 'notosansoriyattc', 'spartanmbboldotf', 'adobegothicstdboldotf', 'stheitimediumttc', 'elitedangerboldsemitalttf', 'inaimathimnttc', 'ヒラキノ角コシックw9ttc', 'lettergothicstdslantedotf', 'nunitoextrabolditalicttf', 'ralewaybolditalicttf', 'plantagenetcherokeettf', 'applebrailleoutline8dotttf', 'spartanmbextraboldotf', 'markerfeltttc', 'myriadproitotf', 'latoboldttf', 'kozgopr6nboldotf', 'sathuttf', 'caviardreamsitalicttf', 'georgiaitalicttf', 'goodbrushttf', 'brushscriptttf', 'nuevastdconditalicotf', 'elitedangeritalttf', 'latoitalicttf', 'universltstdoblotf', 'lettergothicstdboldotf', 'stixgeneralbolitaotf', 'pingfangttc', 'songtittc', 'sourcesansprosemibolditotf', 'bellerosettf', 'diwankufittc', 'didotttc', 'malayalammnttc', 'ヒラキノ角コシックw2ttc', 'thonburittc', 'adobegurmukhiboldotf', 'myriadhebrewbolditotf', 'myriadarabicitotf', 'kozminproextralightotf', 'kannadamnttc', 'farahttc', 'optimattc', 'galvjittc', 'montserratmediumitalicttf', 'gujaratisangammnttc', 'kufistandardgkttc', '28908otf', 'adobemingstdlightotf', 'elitedangerboldconditalttf', 'optimusprincepsttf', 'arialboldttf', 'nunitoregularttf', 'ayuthayattf', 'stixintupdregotf']

BASEY = SH *0.8
IMAGES = {}
pygame.font.init()
WINDOW = pygame.display.set_mode((SW,SH))
Font = pygame.font.SysFont("latoregularttf",16)
BIRD = 'imgs/bird1.png'
BG = 'imgs/bg.png'
PIPE = 'imgs/pipe.png'
Q=numpy.zeros((7,21,2),dtype = float)
FPS = 32
def static():
	birdxpos = int(SW/5)
	birdypos = int((SH - IMAGES['bird'].get_height())/2)
	basex = 0
	while (True):
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()

			elif event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
				return
			else :
				WINDOW.blit(IMAGES['background'],(0,0))
				WINDOW.blit(IMAGES['bird'],(birdxpos,birdypos))
				WINDOW.blit(IMAGES['base'],(basex,BASEY))
				text1 = Font.render("Press Space",1,(255,255,255))
				text2 = Font.render("Flappy Bird: AI",1,(255,255,255))
				WINDOW.blit(text1,(SW/2 ,SH/2))
				WINDOW.blit(text2,(10,50))
				pygame.display.update()
				FPSCLOCK.tick(FPS)

def game_start(generation,x,y):
	score = 0
	birdxpos = int(SW/5)
	birdypos = int(SH/2)
	basex1 = 0
	basex2 = SW

	bgx1=0
	bgx2 = IMAGES['background'].get_width()

	newPipe1 = get_new_pipe()
	newPipe2 = get_new_pipe()

	up_pipes = [
	{'x':SW +200,'y': newPipe1[0]['y']},
	{'x':SW +500 ,'y': newPipe2[0]['y']}
	]

	bttm_pipes = [
	{'x':SW+200,'y':newPipe1[1]['y']},
	{'x':SW +500 ,'y': newPipe2[1]['y']}
	]

	pipeVelx = -4

	birdyvel = -9
	birdymaxvel = 10
	birdyvelmin = -8
	birdyacc = 1

	playerFlapAccv = -8
	playerFlapped =False
	
	while(True):
		
		x_prev,y_prev = convert(birdxpos,birdypos,bttm_pipes)
		jump = ai_play(x_prev,y_prev)

		for event in pygame.event.get():
			if event.type == QUIT:
				plt.scatter(x,y)
				plt.xlabel("GENERATION/Number of Trials")
				plt.ylabel("SCORE")
				plt.title("Flappy Birds AI")
				plt.show()
				pygame.quit()
				sys.exit()
				

		if jump:
			if birdypos>0:
				birdyvel = playerFlapAccv
				playerFlapped = True

		

		
		
		playerMidPos= birdxpos + IMAGES['bird'].get_width()/2
		for pipe in up_pipes:
			pipeMidPos = pipe ['x'] +IMAGES['pipe'][0].get_width()/2
			if pipeMidPos <= playerMidPos < pipeMidPos +4 :
				score += 1


		if birdyvel < birdymaxvel and not playerFlapped:
			birdyvel += birdyacc


		if playerFlapped:
			playerFlapped = False

		playerHeight = IMAGES['bird'].get_height()

		birdypos = birdypos + min (birdyvel, BASEY - birdypos -playerHeight)

		for upperPipe,lowerPipe in zip(up_pipes,bttm_pipes):
			upperPipe['x'] += pipeVelx
			lowerPipe['x'] += pipeVelx

		if (0<up_pipes[0]['x']<5):
			newPipe = get_new_pipe()
			up_pipes.append(newPipe[0])
			bttm_pipes.append(newPipe[1])

		if(up_pipes[0]['x'] < -IMAGES['pipe'][0].get_width() ):
			up_pipes.pop(0)
			bttm_pipes.pop(0)
		basex1-=4
		basex2-=4
		if(basex1 <= -IMAGES['base'].get_width()):
			basex1 = basex2
			basex2 = basex1 + IMAGES['base'].get_width()

		bgx1-=2
		bgx2-=2
		if(bgx1 <= -IMAGES['background'].get_width()):
			bgx1 = bgx2
			bgx2 = bgx1 + IMAGES['background'].get_width()
		crashTest = Collision(birdxpos,birdypos,up_pipes,bttm_pipes)
		x_new,y_new = convert(birdxpos,birdypos,bttm_pipes)
		if crashTest:
			reward = -1000
			text1 = Font.render("Horizontal Distance from Pipe: "+ str(x_prev),1,(255,255,255))
			text2 = Font.render("Vertical Distance from Pipe: "+ str(y_prev),1,(255,255,255))

			text3 = Font.render("Reward: "+ str(reward),1,(255,255,255))

			text4 = Font.render("Generation: "+ str(generation),1,(255,255,255))
			text5 = Font.render("Score: "+ str(score),1,(255,255,255))
			# print(f"x: {x_prev}, y:{y_prev}, reward:{reward}, score:{score}, generation: {generation}")
			print(f"x: {x_prev}, y:{y_prev}, reward:{reward}")

			WINDOW.blit(text1,(7,10))
			WINDOW.blit(text2,(7,30))
			WINDOW.blit(text3,(7,60))
			WINDOW.blit(text4,(SW - 10 -text4.get_width(),SH-60))
			WINDOW.blit(text5,(7, SH-60))



			Q_update(x_prev,y_prev,jump,reward,x_new,y_new)
			return score

		reward = 15

		Q_update(x_prev,y_prev,jump,reward,x_new,y_new)

		WINDOW.blit(IMAGES['background'],(bgx1,0))
		WINDOW.blit(IMAGES['background'],(bgx2,0))
		for upperPipe,lowerPipe in zip(up_pipes,bttm_pipes):
			WINDOW.blit(IMAGES['pipe'][0],(upperPipe['x'],upperPipe['y']))
			WINDOW.blit(IMAGES['pipe'][1],(lowerPipe['x'],lowerPipe['y']))
		WINDOW.blit(IMAGES['base'],(basex1,BASEY))
		WINDOW.blit(IMAGES['base'],(basex2,BASEY))
		
		text1 = Font.render("Horizontal Distance from Pipe: "+ str(x_prev),1,(255,255,255))
		text2 = Font.render("Vertical Distance from Pipe: "+ str(y_prev),1,(255,255,255))

		text3 = Font.render("Reward: "+ str(reward),1,(255,255,255))

		text4 = Font.render("Generation: "+ str(generation),1,(255,255,255))
		text5 = Font.render("Score: "+ str(score),1,(255,255,255))
		# print(f"x: {x_prev}, y:{y_prev}, reward:{reward}, score:{score}, generation: {generation}")
		print(f"x: {x_prev}, y:{y_prev}, reward:{reward}")

		WINDOW.blit(text1,(7,10))
		WINDOW.blit(text2,(7,30))
		WINDOW.blit(text3,(7,60))
		WINDOW.blit(text4,(SW - 10 -text4.get_width(),SH-60))
		WINDOW.blit(text5,(7, SH-60))




		WINDOW.blit(IMAGES['bird'],(birdxpos,birdypos))

		pygame.display.update()
		FPSCLOCK.tick()

def Collision(birdxpos,birdypos,up_pipes,bttm_pipes):
	if (birdypos >= BASEY - IMAGES['bird'].get_height() or birdypos < 0):
		return True
	for pipe in up_pipes:
		pipeHeight = IMAGES['pipe'][0].get_height()
		if(birdypos < pipeHeight + pipe['y'] and abs(birdxpos - pipe['x']) < IMAGES['pipe'][0].get_width()):
			return True

	for pipe in bttm_pipes:
		if (birdypos + IMAGES['bird'].get_height() > pipe['y'] and abs(birdxpos - pipe['x']) < IMAGES['pipe'][0].get_width()):
			return True
	return False


def get_new_pipe():

	pipeHeight = IMAGES['pipe'][1].get_height()
	gap = int(SH/4)
	y2 = int(gap + random.randrange(0,int(SH - IMAGES['base'].get_height() - 1.2*gap)))
	pipex = int(SW+300 )
	y1 = int(pipeHeight -y2 +gap)

	pipe = [
	{'x':pipex,'y':-y1},
	{'x':pipex,'y':y2}
	]
	return pipe

def ai_play(x,y):
	max=0
	jump = False
	
	
	if(Q[x][y][1]>Q[x][y][0]):
		max = Q[x][y][1]
		jump =True

	return jump

def convert(birdxpos,birdypos,bttm_pipes):
	x = min(280, bttm_pipes[0]['x'])
	y = bttm_pipes[0]['y']-birdypos
	if(y<0):
		y=abs(y)+408
	return int(x/40-1),int(y/40)


def Q_update(x_prev,y_prev,jump,reward,x_new,y_new):


	if jump:
		Q[x_prev][y_prev][1] = 0.4 * Q[x_prev][y_prev][1] + (0.6)*(reward+max(Q[x_new][y_new][0],Q[x_new][y_new][1]))
	else :
		Q[x_prev][y_prev][0] = 0.4 * Q[x_prev][y_prev][0] + (0.6)*(reward+max(Q[x_new][y_new][0],Q[x_new][y_new][1]))



if __name__=="__main__":

	pygame.init()
	FPSCLOCK = pygame.time.Clock()
	pygame.display.set_caption("Flappy Bird AI")

	IMAGES['base'] = pygame.image.load('imgs/base.png').convert_alpha()
	IMAGES['pipe'] = ( pygame.transform.rotate(pygame.image.load(PIPE).convert_alpha(),180) , pygame.image.load(PIPE).convert_alpha())
	IMAGES['background']= pygame.image.load(BG).convert()
	IMAGES['bird'] = pygame.image.load(BIRD).convert_alpha()
	generation = 1
	static()
	x=[]
	y=[]
	while(True):
		score = game_start(generation,x,y)
		if (score==-1):
			break
		x.append(generation)
		y.append(score)
		generation+=1
	
		
	print(generation)


