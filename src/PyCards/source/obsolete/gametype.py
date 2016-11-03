# game types
from src.PyCards.source.model.cardsets import CSI
from ..model.enum import Enum

def n_(msg):
    return msg

# ************************************************************************
# * constants
# ************************************************************************

# GameInfo constants
# ************************************************************************

# ************************************************************************
# * Game Types
# ************************************************************************


STYLE = Enum()
STYLE.addAll((
    'ONE_DECK_TYPE', 0,
    'TWO_DECK_TYPE', 1,
    'THREE_DECK_TYPE', 2,
    'FOUR_DECK_TYPE', 3,
    'BAKERS_DOZEN', 4,
    'BELEAGUERED_CASTLE', 5,
    'CANFIELD', 6,
    'DASHAVATARA_GANJIFA', 7,
    'FAN_TYPE', 8,
    'FORTY_THIEVES', 9,
    'FREECELL', 10,
    'GOLF', 11,
    'GYPSY', 12,
    'HANAFUDA', 13,
    'HEXADECK', 14,
    'KLONDIKE', 15,
    'MAHJONGG', 16,
    'MATRIX', 17,
    'MEMORY', 18,
    'MONTANA', 19,
    'MUGHAL_GANJIFA', 20,
    'NAPOLEON', 21,
    'NAVAGRAHA_GANJIFA', 22,
    'NUMERICA', 23,
    'PAIRING_TYPE', 24,
    'POKER_TYPE', 25,
    'PUZZLE_TYPE', 26,
    'RAGLAN', 27,
    'ROW_TYPE', 28,
    'SIMPLE_TYPE', 29,
    'SPIDER', 30,
    'TAROCK', 31,
    'TERRACE', 32,
    'YUKON', 33,
    'SHISEN_SHO', 34,
    'CUSTOM', 40,

    # extra flags
    'BETA', 1 << 12,  # beta version of game driver
    'CHILDREN', 1 << 13,  # *not used*
    'CONTRIB', 1 << 14,  # contributed games under the GNU GPL
    'HIDDEN', 1 << 15,  # not visible in menus, but games can be loaded
    'OPEN', 1 << 16,
    'ORIGINAL', 1 << 17,
    'POPULAR', 1 << 18,  # *not used*
    'RELAXED', 1 << 19,
    'SCORE', 1 << 20,  # game has some type of scoring
    'SEPARATE_DECKS', 1 << 21,
    'XORIGINAL', 1 << 22  # original games by other people, not playable

))

CATEGORY = Enum()
CATEGORY.addAll((
    'FRENCH', CSI.TYPE_FRENCH,
    'HANAFUDA', CSI.TYPE_HANAFUDA,
    'TAROCK', CSI.TYPE_TAROCK,
    'MAHJONGG', CSI.TYPE_MAHJONGG,
    'HEXADECK', CSI.TYPE_HEXADECK,
    'MUGHAL_GANJIFA', CSI.TYPE_MUGHAL_GANJIFA,
    'NAVAGRAHA_GANJIFA', CSI.TYPE_NAVAGRAHA_GANJIFA,
    'DASHAVATARA_GANJIFA', CSI.TYPE_DASHAVATARA_GANJIFA,
    'TRUMP_ONLY', CSI.TYPE_TRUMP_ONLY,
))

SKILL = Enum()
SKILL.addAll((
    'LUCK', 1,
    'MOSTLY_LUCK', 2,
    'BALANCED', 3,
    'MOSTLY_SKILL', 4,
    'SKILL', 5
))

# Typedef
FR_TYPES = {
    STYLE.BAKERS_DOZEN: n_("Baker's Dozen"),
    STYLE.BELEAGUERED_CASTLE: n_("Beleaguered Castle"),
    STYLE.CANFIELD: n_("Canfield"),
    STYLE.FAN_TYPE: n_("Fan"),
    STYLE.FORTY_THIEVES: n_("Forty Thieves"),
    STYLE.FREECELL: n_("FreeCell"),
    STYLE.GOLF: n_("Golf"),
    STYLE.GYPSY: n_("Gypsy"),
    STYLE.KLONDIKE: n_("Klondike"),
    STYLE.MONTANA: n_("Montana"),
    STYLE.NAPOLEON: n_("Napoleon"),
    STYLE.NUMERICA: n_("Numerica"),
    STYLE.PAIRING_TYPE: n_("Pairing"),
    STYLE.RAGLAN: n_("Raglan"),
    STYLE.SIMPLE_TYPE: n_("Simple games"),
    STYLE.SPIDER: n_("Spider"),
    STYLE.TERRACE: n_("Terrace"),
    STYLE.YUKON: n_("Yukon"),
    STYLE.ONE_DECK_TYPE: n_("One-Deck games"),
    STYLE.ONE_DECK_TYPE: n_("Two-Deck games"),
    STYLE.ONE_DECK_TYPE: n_("Three-Deck games"),
    STYLE.ONE_DECK_TYPE: n_("Four-Deck games"),
}

FILTER = Enum()
FILTER.add('FRENCH',
           ((n_("Baker's Dozen type"), lambda gi, gt=STYLE.BAKERS_DOZEN: gi.game_type == gt),
            (n_("Beleaguered Castle type"), lambda gi, gt=STYLE.BELEAGUERED_CASTLE: gi.game_type == gt),
            (n_("Canfield type"), lambda gi, gt=STYLE.CANFIELD: gi.game_type == gt),
            (n_("Fan type"), lambda gi, gt=STYLE.FAN_TYPE: gi.game_type == gt),
            (n_("Forty Thieves type"), lambda gi, gt=STYLE.FORTY_THIEVES: gi.game_type == gt),
            (n_("FreeCell type"), lambda gi, gt=STYLE.FREECELL: gi.game_type == gt),
            (n_("Golf type"), lambda gi, gt=STYLE.GOLF: gi.game_type == gt),
            (n_("Gypsy type"), lambda gi, gt=STYLE.GYPSY: gi.game_type == gt),
            (n_("Klondike type"), lambda gi, gt=STYLE.KLONDIKE: gi.game_type == gt),
            (n_("Montana type"), lambda gi, gt=STYLE.MONTANA: gi.game_type == gt),
            (n_("Napoleon type"), lambda gi, gt=STYLE.NAPOLEON: gi.game_type == gt),
            (n_("Numerica type"), lambda gi, gt=STYLE.NUMERICA: gi.game_type == gt),
            (n_("Pairing type"), lambda gi, gt=STYLE.PAIRING_TYPE: gi.game_type == gt),
            (n_("Raglan type"), lambda gi, gt=STYLE.RAGLAN: gi.game_type == gt),
            (n_("Simple games"), lambda gi, gt=STYLE.SIMPLE_TYPE: gi.game_type == gt),
            (n_("Spider type"), lambda gi, gt=STYLE.SPIDER: gi.game_type == gt),
            (n_("Terrace type"), lambda gi, gt=STYLE.TERRACE: gi.game_type == gt),
            (n_("Yukon type"), lambda gi, gt=STYLE.YUKON: gi.game_type == gt),
            (n_("One-Deck games"), lambda gi, gt=STYLE.ONE_DECK_TYPE: gi.game_type == gt),
            (n_("Two-Deck games"), lambda gi, gt=STYLE.TWO_DECK_TYPE: gi.game_type == gt),
            (n_("Three-Deck games"), lambda gi, gt=STYLE.THREE_DECK_TYPE: gi.game_type == gt),
            (n_("Four-Deck games"), lambda gi, gt=STYLE.FOUR_DECK_TYPE: gi.game_type == gt))
           )

FILTER.add('ORIGINAL',
           ((n_("French type"), lambda gi, gf=STYLE.ORIGINAL, gt=(
               STYLE.HANAFUDA, STYLE.HEXADECK, STYLE.MUGHAL_GANJIFA, STYLE.NAVAGRAHA_GANJIFA, STYLE.DASHAVATARA_GANJIFA,
               STYLE.TAROCK,): gi.game_flags & gf and gi.game_type not in gt),
            (n_("Ganjifa type"), lambda gi, gf=STYLE.ORIGINAL, gt=(
                STYLE.MUGHAL_GANJIFA, STYLE.NAVAGRAHA_GANJIFA,
                STYLE.DASHAVATARA_GANJIFA,): gi.game_flags & gf and gi.game_type in gt),
            (n_("Hanafuda type"),
             lambda gi, gf=STYLE.ORIGINAL, gt=STYLE.HANAFUDA: gi.game_flags & gf and gi.game_type == gt),
            (n_("Hex A Deck type"),
             lambda gi, gf=STYLE.ORIGINAL, gt=STYLE.HEXADECK: gi.game_flags & gf and gi.game_type == gt),
            (n_("Tarock type"),
             lambda gi, gf=STYLE.ORIGINAL, gt=STYLE.TAROCK: gi.game_flags & gf and gi.game_type == gt))
           )

FILTER.add('CONTRIBUTED',
           ((n_("French type"), lambda gi, gf=STYLE.CONTRIB, gt=(
               STYLE.HANAFUDA, STYLE.HEXADECK, STYLE.MUGHAL_GANJIFA, STYLE.NAVAGRAHA_GANJIFA, STYLE.DASHAVATARA_GANJIFA,
               STYLE.TAROCK,): gi.game_flags & gf and gi.game_type not in gt),
            (n_("Ganjifa type"), lambda gi, gf=STYLE.CONTRIB, gt=(
                STYLE.MUGHAL_GANJIFA, STYLE.NAVAGRAHA_GANJIFA,
                STYLE.DASHAVATARA_GANJIFA,): gi.game_flags & gf and gi.game_type in gt),
            (n_("Hanafuda type"),
             lambda gi, gf=STYLE.CONTRIB, gt=STYLE.HANAFUDA: gi.game_flags & gf and gi.game_type == gt),
            (n_("Hex A Deck type"),
             lambda gi, gf=STYLE.CONTRIB, gt=STYLE.HEXADECK: gi.game_flags & gf and gi.game_type == gt),
            (n_("Tarock type"),
             lambda gi, gf=STYLE.CONTRIB, gt=STYLE.TAROCK: gi.game_flags & gf and gi.game_type == gt))
           )

FILTER.add('ORIENTAL',
           ((n_("Dashavatara Ganjifa type"), lambda gi, gt=STYLE.DASHAVATARA_GANJIFA: gi.game_type == gt),
            (n_("Ganjifa type"), lambda gi, gt=(
            STYLE.MUGHAL_GANJIFA, STYLE.NAVAGRAHA_GANJIFA, STYLE.DASHAVATARA_GANJIFA,): gi.game_type in gt),
            (n_("Hanafuda type"), lambda gi, gt=STYLE.HANAFUDA: gi.game_type == gt),
            (n_("Mughal Ganjifa type"), lambda gi, gt=STYLE.MUGHAL_GANJIFA: gi.game_type == gt),
            (n_("Navagraha Ganjifa type"), lambda gi, gt=STYLE.NAVAGRAHA_GANJIFA: gi.game_type == gt))
           )

FILTER.add('SPECIAL',
           ((n_("Shisen-Sho"), lambda gi, gt=STYLE.SHISEN_SHO: gi.game_type == gt),
            (n_("Hex A Deck type"), lambda gi, gt=STYLE.HEXADECK: gi.game_type == gt),
            (n_("Matrix type"), lambda gi, gt=STYLE.MATRIX: gi.game_type == gt),
            (n_("Memory type"), lambda gi, gt=STYLE.MEMORY: gi.game_type == gt),
            (n_("Poker type"), lambda gi, gt=STYLE.POKER_TYPE: gi.game_type == gt),
            (n_("Puzzle type"), lambda gi, gt=STYLE.PUZZLE_TYPE: gi.game_type == gt),
            (n_("Tarock type"), lambda gi, gt=STYLE.TAROCK: gi.game_type == gt))
           )

# These obsolete gameids have been used in previous versions of
# PySol and are no longer supported because of internal changes
# (mainly rule changes). The game has been assigned a new id.
PROTECTED_GAMES = {
    22: 106,  # Double Canfield
    32: 901,  # La Belle Lucie (Midnight Oil)
    52: 903,  # Aces Up
    72: 115,  # Little Forty
    75: 126,  # Red and Black
    82: 901,  # La Belle Lucie (Midnight Oil)
    ##        155: 5034,              # Mahjongg - Flying Dragon
    ##        156: 5035,              # Mahjongg - Fortress Towers
    262: 105,  # Canfield
    902: 88,  # Trefoil
    904: 68,  # Lexington Harp
    297: 631,  # Alternation/Alternations
}

GAMES_BY_COMPATIBILITY = (
    # Atari ST Patience game v2.13 (we have 10 out of 10 games)
    ("Atari ST Patience", (1, 3, 4, 7, 12, 14, 15, 16, 17, 39,)),

    ## Gnome AisleRiot 1.0.51 (we have 28 out of 32 games)
    ##   still missing: Camelot, Clock, Thieves, Thirteen
    ##("Gnome AisleRiot 1.0.51", (
    ##    2, 8, 11, 19, 27, 29, 33, 34, 35, 40,
    ##    41, 42, 43, 58, 59, 92, 93, 94, 95, 96,
    ##    100, 105, 111, 112, 113, 130, 200, 201,
    ##)),
    ## Gnome AisleRiot 1.4.0.1 (we have XX out of XX games)
    ##("Gnome AisleRiot", (
    ##    1, 2, 8, 11, 19, 27, 29, 33, 34, 35, 40,
    ##    41, 42, 43, 58, 59, 92, 93, 94, 95, 96,
    ##    100, 105, 111, 112, 113, 130, 200, 201,
    ##)),
    # Gnome AisleRiot 2.2.0 (we have 61 out of 70 games)
    #   still missing:
    #         Gay gordons, Helsinki,
    #         Isabel, Labyrinth, Quatorze, Thieves,
    #         Treize, Valentine, Yeld.
    ("Gnome AisleRiot", (
        1, 2, 8, 9, 11, 12, 19, 24, 27, 29, 31, 33, 34, 35, 36, 40,
        41, 42, 43, 45, 48, 58, 59, 67, 89, 91, 92, 93, 94, 95, 96,
        100, 105, 111, 112, 113, 130, 139, 144, 146, 147, 148, 200,
        201, 206, 224, 225, 229, 230, 233, 257, 258, 280, 281, 282,
        283, 284, 551, 552, 553, 737,
    )),

    ## KDE Patience 0.7.3 from KDE 1.1.2 (we have 6 out of 9 games)
    ##("KDE Patience 0.7.3", (2, 7, 8, 18, 256, 903,)),
    ## KDE Patience 2.0 from KDE 2.1.2 (we have 11 out of 13 games)
    ##("KDE Patience", (1, 2, 7, 8, 18, 19, 23, 50, 256, 261, 903,)),
    ## KDE Patience 2.0 from KDE 2.2beta1 (we have 12 out of 14 games)
    ##("KDE Patience", (1, 2, 7, 8, 18, 19, 23, 36, 50, 256, 261, 903,)),
    # KDE Patience 2.0 from KDE 3.1.1 (we have 15 out of 15 games)
    ("KDE Patience", (1, 2, 7, 8, 18, 19, 23, 36, 50,
                      256, 261, 277, 278, 279, 903,)),

    # xpat2 1.06 (we have 14 out of 16 games)
    #   still missing: Michael's Fantasy, modCanfield
    ("xpat2", (
        1, 2, 8, 9, 11, 31, 54, 63, 89, 105, 901, 256, 345, 903,
    )),
)

GAMES_BY_INVENTORS = (
    ("Paul Alfille", (8,)),
    ("C.L. Baker", (45,)),
    ("David Bernazzani", (314,)),
    ("Gordon Bower", (763,)),
    ("Art Cabral", (9,)),
    ("Robert Harbin", (381,)),
    ("Robert Hogue", (22216,)),
    ("Charles Jewell", (220, 309,)),
    ("Michael Keller", (592,)),
    ("Fred Lunde", (459,)),
    ("Albert Morehead and Geoffrey Mott-Smith", (25, 42, 48, 173, 282,
                                                 303, 362, 547, 738)),
    ("David Parlett", (64, 98, 294, 338, 654, 674,)),
    ("Randy Rasa", (187, 190, 191, 192,)),
    ("Captain Jeffrey T. Spaulding", (400,)),
    ("Adam Selene", (366,)),
    ("John Stoneham", (201,)),
    ("Bryan Stout", (655,)),
    ("Bill Taylor", (349,)),
    ("Thomas Warfield", (189, 264, 300, 320, 336, 337, 359,
                         415, 427, 458, 495, 496, 497, 508,)),
)

GAMES_BY_PYSOL_VERSION = (
    ("1.00", (1, 2, 3, 4)),
    ("1.01", (5, 6)),
    ("1.02", (7, 8, 9)),
    ("1.03", (10, 11, 12, 13)),
    ("1.10", (14,)),
    ("1.11", (15, 16, 17)),
    ("2.00", (256, 257)),
    ("2.01", (258, 259, 260, 261)),
    ("2.02", (105,)),
    ("2.90", (18, 19, 20, 21, 106, 23, 24, 25, 26, 27,
              28, 29, 30, 31, 901, 33, 34, 35, 36)),
    ("2.99", (37,)),
    ("3.00", (38, 39,
              40, 41, 42, 43, 45, 46, 47, 48, 49,
              50, 51, 903, 53, 54, 55, 56, 57, 58, 59,
              60, 61, 62, 63, 64, 65, 66, 67, 68, 69,
              70, 71, 115, 73, 74, 126, 76, 77, 78, 79,
              80, 81, 83, 84, 85, 86, 87, 88, 89,
              90, 91, 92, 93, 94, 95, 96, 97, 98, 99,
              100, 101, 102, 103, 104, 107, 108,)),
    ("3.10", (109, 110, 111, 112, 113, 114, 116, 117, 118, 119,
              120, 121, 122, 123, 124, 125, 127)),
    ("3.20", (128, 129, 130, 131, 132, 133, 134, 135, 136, 137,
              138, 139, 140, 141, 142,
              12345, 12346, 12347, 12348, 12349, 12350, 12351, 12352)),
    ("3.21", (143, 144)),
    ("3.30", (145, 146, 147, 148, 149, 150, 151)),
    ("3.40", (152, 153, 154)),
    ("4.00", (157, 158, 159, 160, 161, 162, 163, 164)),
    ("4.20", (165, 166, 167, 168, 169, 170, 171, 172, 173, 174,
              175, 176, 177, 178)),
    ("4.30", (179, 180, 181, 182, 183, 184)),
    ("4.41", (185, 186, 187, 188, 189, 190, 191, 192, 193, 194,
              195, 196, 197, 198, 199)),
    ("4.60", (200, 201, 202, 203, 204, 205,
              206, 207, 208, 209,
              210, 211, 212, 213, 214, 215, 216, 217, 218, 219,
              220, 221, 222, 223, 224, 225, 226, 227, 228, 229,
              230, 231, 232, 233, 234, 235, 236)),
    ("4.70", (237,)),
    ('fc-0.5.0', (  # moved from Ultrasol
        # 121, 122, 187, 188, 189, 190, 191, 192, 194, 197, 198,
        5301, 5302, 9011, 11001, 11002, 11003, 11004, 11005,
        11006, 12353, 12354, 12355, 12356, 12357, 12358, 12359,
        12360, 12361, 12362, 12363, 12364, 12365, 12366, 12367,
        12368, 12369, 12370, 12371, 12372, 12373, 12374, 12375,
        12376, 12377, 12378, 12379, 12380, 12381, 12382, 12383,
        12384, 12385, 13001, 13002, 13003, 13004, 13005, 13006,
        13007, 13008, 13009, 13010, 13011, 13012, 13013, 13014,
        13163, 13164, 13165, 13166, 13167, 14401, 14402, 14403,
        14404, 14405, 14406, 14407, 14408, 14409, 14410, 14411,
        14412, 14413, 15406, 15407, 15408, 15409, 15410, 15411,
        15412, 15413, 15414, 15415, 15416, 15417, 15418, 15419,
        15420, 15421, 15422, 16000, 16001, 16002, 16003, 16004,
        16666, 16667, 16668, 16669, 16670, 16671, 16672, 16673,
        16674, 16675, 16676, 16677, 16678, 16679, 16680, 22216,
        22223, 22224, 22225, 22226, 22227, 22228, 22229, 22230,
        22231, 22232,)),
    ('fc-0.8.0', tuple(range(263, 323))),  # exclude 297
    ('fc-0.9.0', tuple(range(323, 421))),
    ('fc-0.9.1', tuple(range(421, 441))),
    ('fc-0.9.2', tuple(range(441, 466))),
    ('fc-0.9.3', tuple(range(466, 661))),
    ('fc-0.9.4', tuple(range(661, 671))),
    ('fc-1.0', tuple(range(671, 711))),
    ('fc-1.1', tuple(range(711, 759))),
    ('fc-2.0', tuple(range(11011, 11014)) + tuple(range(759, 767))),
)

_CHILDREN_GAMES = [16, 33, 55, 90, 91, 96, 97, 176, 903, ]

_OPEN_GAMES = []

_POPULAR_GAMES = [
    1,  # Gypsy
    2,  # Klondike
    7,  # Picture Galary
    8,  # FreeCell
    9,  # Seahaven Towers
    11,  # Spider
    12,  # Braid
    13,  # Forty Thieves
    14,  # Grounds for a Divorce
    19,  # Yukon
    31,  # Baker's Dozen
    36,  # Golf
    38,  # Pyramid
    105,  # Canfield
    158,  # Imperial Trumps
    279,  # Kings
    903,  # Ace Up
    5034,  # Mahjongg Flying Dragon
    5401,  # Mahjongg Taipei
    12345,  # Oonsoo
]
