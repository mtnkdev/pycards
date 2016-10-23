#!/usr/bin/env python

class Game:
	#For statistics
	U_PLAY		=  0
	U_WON		= -2
	U_LOST		= -3
	U_PERFECT	= -4
	
	#For state
	S_INIT		= 0x00
	S_DEAL		= 0x10
	S_FILL		= 0x20
	S_RESTORE	= 0x30
	S_PLAY		= 0x40
	S_UNDO		= 0x50
	S_REDO		= 0x60
	
	# for saving and loading (subclasses should override if the save format is different)
	# also see canLoadGame ()
	GAME_VERSION = 1
	
	#preliminary constructor
	def __init__(self,gameInfo):
		self.preview = 0
		self.random = None
		self.gameInfo = gameInfo
		self.id = gameInfo.ID
		assert self.id > 0
		self.busy = 0
		self.pause = False
		self.finished = False
		self.version = VERSION
		self.version_tuple = VERSION_TUPLE
		self.cards = []
		self.stackmap = {}	# dictionary with (x,y) tuples as key
		self.stacks = []
		self.snGroups = []	#snapshot groups (list of similar stacks)
		self.snapshots = []
		self.failedSnapshots = []
		self.stackDescList = []
		self.demoLogo = None
		self.pauseLogo = None
		
		#stacks
		self.s_talon = None
		self.s_waste = None
		self.s_foundations = []
		self.s_rows = []
		self.s_reserves = []
		self.s_internals = []
		
		#Stack groups
		self.sg_openstacks = []		#used for getClosestStack(): list of stacks the player can place a card on
		self.sg_talonstacks = []	#for Hint
		self.sg_dropstacks = []		#for Hint and getAutoStacks()
		self.sg_reservestacks = []	#for Hint
		self.sg_hpStacks = []		#for getHighlightPileStacks()
		
		#for getClosestStack()- set by optimizeRegions()
		self.regions_info = []		#list of tuples (stacks,rect)
		self.regions_remaining = []	#list of stacks in no region
		self.region_data			#raw data
		
		self.eventhandled = False 	#if click event handled by Stack
		self.reset()
		
	#main constructor
	def create (self, app):
		self.sg_openstacks = [s for s in self.sg_openstacks if s.maxAccept >= s.minAccept]
		self.sg_hpStacks = [s for s in self.sg_dropstacks if s.maxMove >= 2]
		self.createSnGroups()
		
		#apperently using tuples improves speed
		self.stacks = tuple (self.stacks)
		self.s_foundations = tuple (self.s_foundations)
		self.s_rows = tuple(self.s_rows)
		self.s_reserves = tuple(self.s_reserves)
        self.s_internals = tuple(self.s_internals)
        self.sg_openstacks = tuple(self.sg_openstacks)
        self.sg_talonstacks = tuple(self.sg_talonstacks)
        self.sg_dropstacks = tuple(self.sg_dropstacks)
        self.sg_reservestacks = tuple(self.sg_reservestacks)
        self.sg_hpStacks = tuple(self.sg_hpStacks)
		
		self.optimizeRegions
		#create cards
		if not self.cards:
			self.cards = self.createCards(progress = app.intro.progress)
		self.initBindings()
		
		