#!/usr/bin/env python

class Game:
    # For statistics
    U_PLAY        =  0
    U_WON        = -2
    U_LOST        = -3
    U_PERFECT    = -4
    
    # For state
    S_INIT        = 0x00
    S_DEAL        = 0x10
    S_FILL        = 0x20
    S_RESTORE    = 0x30
    S_PLAY        = 0x40
    S_UNDO        = 0x50
    S_REDO        = 0x60
    
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
        self.stackmap = {}    # dictionary with (x,y) tuples as key
        self.stacks = []
        self.snGroups = []    #snapshot groups (list of similar stacks)
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
        self.sg_openstacks = []        #used for getClosestStack(): list of stacks the player can place a card on
        self.sg_talonstacks = []    #for Hint
        self.sg_dropstacks = []        #for Hint and getAutoStacks()
        self.sg_reservestacks = []    #for Hint
        self.sg_hpStacks = []        #for getHighlightPileStacks()
        
        #for getClosestStack()- set by optimizeRegions()
        self.regions_info = []        #list of tuples (stacks,rect)
        self.regions_remaining = []    #list of stacks in no region
        self.region_data            #raw data
        
        self.eventhandled = False     #if click event handled by Stack
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
        
    def __createCommon(self,app):
        self.busy = 1
        self.app = app
        self.filename = ""
        
        self.drag_event = None
        self.drag_timer = None
        self.drag_startX = 0
        self.drag_startY = 0
        self.drag_stack = None
        self.drag_cards = []
        self.drag_index = -1
        self.drag_shados = []
        self.drag_shadeStack = None
        self.drag_shadeIMG = None
        self.drag_canShadeStack = []
        self.drag_noShadeStack = []
        if self.gstats_startPlayer is None:
            self.gstats_startPlayer = self.app.opt.player
        
    def destruct (self):
        for obj in self.cards:
            destruct(obj)
        for obj in self.stacks:
            obj.destruct()
            destruct(obj)
            
    
        
    def reset (self,restart = 0):
        self.filename=""
        self.demo=None
        self.solver = None
        self.hints_list = None
        self.hint_index = -1
        self.hint_level = -1
        self.saveinfo = []
        self.loadinfo_stacks = None
        self.loadinfo_talonRound = 1
        self.loadinfo_ncards = 0
        self.snapshots = []
        self.failed_snapshots = []
        self.stats_hints = 0
        self.stats_highlightPiles = 0
        self.stats_highlightCards = 0
        self.stats_highlightsamerank = 0
        self.stats_undoMoves = 0
        self.stats_redoMoves = 0
        self.stats_totalMoves = 0
        self.stats_playerMoves = 0
        self.stats_demoMoves = 0
        self.stats_autoplayMoves = 0
        self.stats_quickplayMoves = 0
        self.stats_gotoBookmarkMoves = 0
        self.stats_shuffleMoves = 0
        self.stats_demoUpdated = 0
        self.stats_updateTime = time.time()
        self.stats_elapsedTime = 0
        self.stats_pauseStartTime = 0
        
        self.startMoves()
        if restart:
            return
            
        #global stats survive game restart
        self.gstats_bookmarks = {}
        self.gstats_comment = ""
        
        self.winAnimation_timer = None
        self.winAnimation_images = []
        self.winAnimation_tkImages = []
        self.winAnimation_savedImages = {}
        self.winAnimation_canvasImages = []
        self.winAnimation_frameNum = 0
        self.winAnimation_width = 0
        self.winAnimation_height = 0
        
    def getTitleName(self):
        return self.app.getGameTitleName(self.id)
        
    def getGameNumber(self,format):
        s = str(self.random)
        if format: return "#" + s
        return s
        
    def setSize(self,w,h):
        self.width, self.height = int(round(w)),int(round(h))
        
    def setCursor(self,cursor):
        if self.canvas:
            self.cancas.config(sursor=cursor)
            
    def newGame (self, random = None, restart = 0, autoplay=1):
        self.finished = False
        old_busy, self.busy = self.busy, 1
        self.setCursor (cursor = CURSOR_WATCH)
        self.stopWinAnimation()
        self.disableMenus()
        self.redealAnimation()
        self.restart(restart=restart)
        self.resetGame()
        self.createRandom(random)
        self.shuffle()
        assert len(self.s.talon.cards) == self.gameInfo.numcards
        for stack in self.stacks:
            stack.updateText()
        self.updateText()
        self.updateStatus