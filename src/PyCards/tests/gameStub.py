from source.gamedb import registerGame, GameInfo
from source.stack import *
from source.hint import *
from source.gametype import STYLE, SKILL, CATEGORY

class Game:
    def __init__(self):
        pass

## mahjongg util
def comp_cardset(ncards):
    # calc decks, ranks & trumps
    assert ncards % 4 == 0
    assert 0 < ncards <= 288 # ???
    decks = 1
    cards = ncards/4
    if ncards > 144:
        assert ncards % 8 == 0
        decks = 2
        cards = cards/2
    ranks, trumps = divmod(cards, 3)
    if ranks > 10:
        trumps += (ranks-10)*3
        ranks = 10
    if trumps > 4:
        trumps = 4+(trumps-4)*4
    assert 0 <= ranks <= 10 and 0 <= trumps <= 12
    return decks, ranks, trumps

class AcesUp_Foundation(AbstractFoundationStack):
    pass
class AcesUp_RowStack(BasicRowStack):
    pass
class AcesUp(Game):
    pass
class Fortunes(AcesUp):
    pass
class RussianAces_Talon(DealRowTalonStack):
    pass
class RussianAces(AcesUp):
    pass
class PerpetualMotion_Talon(DealRowTalonStack):
    pass
class PerpetualMotion_Foundation(AbstractFoundationStack):
    pass
class PerpetualMotion_RowStack(RK_RowStack):
    pass
class PerpetualMotion(Game):
    pass
class AcesUp5(AcesUp):
    pass
class MonteCarlo_RowStack(BasicRowStack):
    pass
class Cover_RowStack(MonteCarlo_RowStack):
    pass
class Cover(AcesUp):
    pass
class Deck(Cover):
    pass
class FiringSquad_Foundation(AcesUp_Foundation):
    pass
class FiringSquad(AcesUp):
    pass
class TabbyCatStack(RK_RowStack):
    pass
class TabbyCat(Game):
    pass
class Manx(TabbyCat):
    pass
class MaineCoon(TabbyCat):
    pass
class Carthage_Talon(DealRowTalonStack):
    pass
class Carthage(Game):
    pass
class AlgerianPatience(Carthage):
    pass
class AlgerianPatience3(Carthage):
    pass
class TamOShanter(Game):
    pass
class AuldLangSyne(TamOShanter):
    pass
class Strategy_Foundation(SS_FoundationStack):
    pass
class Strategy_RowStack(BasicRowStack):
    pass
class Strategy(Game):
    pass
class StrategyPlus(Strategy):
    pass
class Interregnum_Foundation(RK_FoundationStack):
    pass
class Interregnum(Game):
    pass
class Primrose_Talon(DealRowTalonStack):
    pass
class Primrose(Interregnum):
    pass
class Colorado_RowStack(OpenStack):
    pass
class Colorado(Game):
    pass
class Amazons_Talon(RedealTalonStack):
    pass
class Amazons_Foundation(AbstractFoundationStack):
    pass
class Amazons(AuldLangSyne):
    pass
class Scuffle_Talon(RedealTalonStack):
    pass
class Scuffle(AuldLangSyne):
    pass
class Acquaintance_Talon(Scuffle_Talon):
    pass
class Acquaintance(AuldLangSyne):
    pass
class DoubleAcquaintance(AuldLangSyne):
    pass
class Formic_Foundation(AbstractFoundationStack):
    pass
class Formic(TamOShanter):
    pass
class CastlesInSpain(Game):
    pass
class Martha_RowStack(AC_RowStack):
    pass
class Martha(CastlesInSpain):
    pass
class BakersDozen(CastlesInSpain):
    pass
class SpanishPatience(BakersDozen):
    pass
class PortugueseSolitaire(BakersDozen):
    pass
class SpanishPatienceII(PortugueseSolitaire):
    pass
class GoodMeasure(BakersDozen):
    pass
class Cruel_Talon(TalonStack):
    pass
class Cruel(CastlesInSpain):
    pass
class RoyalFamily(Cruel):
    pass
class Indefatigable(Cruel):
    pass
class Perseverance(Cruel, BakersDozen):
    pass
class RippleFan(CastlesInSpain):
    pass
class BakersGame(Game):
    pass
class KingOnlyBakersGame(BakersGame):
    pass
class EightOff(KingOnlyBakersGame):
    pass
class SeahavenTowers(KingOnlyBakersGame):
    pass
class RelaxedSeahavenTowers(SeahavenTowers):
    pass
class Tuxedo(Game):
    pass
class Penguin(Tuxedo):
    pass
class Opus(Penguin):
    pass
class Flipper_Row(AC_RowStack):
    pass
class Flipper(Tuxedo):
    pass
class BeleagueredCastleType_Hint(CautiousDefaultHint):
    pass
class StreetsAndAlleys(Game):
    pass
class BeleagueredCastle(StreetsAndAlleys):
    pass
class Citadel(StreetsAndAlleys):
    pass
class ExiledKings(Citadel):
    pass
class Fortress(Game):
    pass
class Bastion(Game):
    pass
class TenByOne(Bastion):
    pass
class CastlesEnd_Foundation(SS_FoundationStack):
    pass
class CastlesEnd_StackMethods:
    pass
class CastlesEnd_RowStack(CastlesEnd_StackMethods, UD_AC_RowStack):
    pass
class CastlesEnd_Reserve(CastlesEnd_StackMethods, OpenStack):
    pass
class CastlesEnd(Bastion):
    pass
class Chessboard_Foundation(SS_FoundationStack):
    pass
class Chessboard_RowStack(UD_SS_RowStack):
    pass
class Chessboard(Fortress):
    pass
class Stronghold(StreetsAndAlleys):
    pass
class Fastness(StreetsAndAlleys):
    pass
class Zerline_ReserveStack(ReserveStack):
    pass
class Zerline(Game):
    pass
class Zerline3Decks(Zerline):
    pass
class Chequers(Fortress):
    pass
class CastleOfIndolence(Game):
    pass
class Rittenhouse_Foundation(RK_FoundationStack):
    pass
class Rittenhouse(Game):
    pass
class Lightweight(StreetsAndAlleys):
    pass
class CastleMount(Lightweight):
    pass
class SelectiveCastle_RowStack(RK_RowStack):
    pass
class SelectiveCastle(StreetsAndAlleys, Chessboard):
    pass
class Soother(Game):
    pass
class PenelopesWeb(StreetsAndAlleys):
    pass
class Bisley(Game):
    pass
class DoubleBisley(Bisley):
    pass
class Gloria(Game):
    pass
class Realm(Game):
    pass
class Mancunian(Realm):
    pass
class HospitalPatience(Game):
    pass
class BoardPatience(Game):
    pass
class Cringle(Game):
    pass
class Braid_Hint(DefaultHint):
    pass
class Braid_Foundation(AbstractFoundationStack):
    pass
class Braid_BraidStack(OpenStack):
    pass
class Braid_RowStack(ReserveStack):
    pass
class Braid_ReserveStack(ReserveStack):
    pass
class Braid(Game):
    pass
class LongBraid(Braid):
    pass
class Fort(Braid):
    pass
class Backbone_BraidStack(OpenStack):
    pass
class Backbone(Game):
    pass
class BackbonePlus(Backbone):
    pass
class BigBraid(Braid):
    pass
class Casket_Hint(CautiousDefaultHint):
    pass
class JewelsStack(OpenStack):
    pass
class Casket_RowStack(SS_RowStack):
    pass
class Casket_Reserve(ReserveStack):
    pass
class Casket(Game):
    pass
class Well_TalonStack(DealRowRedealTalonStack):
    pass
class Well(Game):
    pass
class Bristol_Hint(CautiousDefaultHint):
    pass
class Bristol_Talon(TalonStack):
    pass
class Bristol(Game):
    pass
class Belvedere(Bristol):
    pass
class Dover_RowStack(RK_RowStack):
    pass
class Dover(Bristol):
    pass
class NewYork_Hint(CautiousDefaultHint):
    pass
class NewYork_Talon(OpenTalonStack):
    pass
class NewYork_ReserveStack(ReserveStack):
    pass
class NewYork_RowStack(AC_RowStack):
    pass
class NewYork(Dover):
    pass
class Spike(Dover):
    pass
class Gotham_RowStack(RK_RowStack):
    pass
class Gotham(NewYork):
    pass
class Interment_Hint(CautiousDefaultHint):
    pass
class Interment_Talon(OpenTalonStack):
    pass
class Interment_Reserve(OpenStack):
    pass
class Interment_Waste(ReserveStack):
    pass
class Interment(Game):
    pass
class BuffaloBill(Game):
    pass
class LittleBillie(BuffaloBill):
    pass
class Calculation_Hint(DefaultHint):
    pass
class BetsyRoss_Foundation(RK_FoundationStack):
    pass
class Calculation_Foundation(BetsyRoss_Foundation):
    pass
class Calculation_RowStack(BasicRowStack):
    pass
class Calculation(Game):
    pass
class Hopscotch(Calculation):
    pass
class BetsyRoss(Calculation):
    pass
class One234_Foundation(BetsyRoss_Foundation):
    pass
class One234_RowStack(BasicRowStack):
    pass
class One234(Calculation):
    pass
class SeniorWrangler_Talon(DealRowTalonStack):
    pass
class SeniorWrangler_RowStack(BasicRowStack):
    pass
class SeniorWrangler(Game):
    pass
class SPatience(Game):
    pass
class Camelot_Hint(AbstractHint):
    pass
class Camelot_RowStack(ReserveStack):
    pass
class Camelot_Foundation(AbstractFoundationStack):
    pass
class Camelot_Talon(OpenTalonStack):
    pass
class Camelot(Game):
    pass
class SlyFox_Foundation(SS_FoundationStack):
    pass
class SlyFox_Talon(OpenTalonStack):
    pass
class SlyFox_RowStack(ReserveStack):
    pass
class SlyFox(Game):
    pass
class OpenSlyFox(SlyFox):
    pass
class PrincessPatience_RowStack(SS_RowStack):
    pass
class PrincessPatience(Game):
    pass
class GrandmammasPatience_Talon(OpenTalonStack):
    pass
class GrandmammasPatience_RowStack(BasicRowStack):
    pass
class GrandmammasPatience(Game):
    pass
class DoubleLine_RowStack(BasicRowStack):
    pass
class DoubleLine(Game):
    pass
class Canfield_Hint(CautiousDefaultHint):
    pass
class Canfield_AC_RowStack(AC_RowStack):
    pass
class Canfield_SS_RowStack(SS_RowStack):
    pass
class Canfield_RK_RowStack(RK_RowStack):
    pass
class Canfield(Game):
    pass
class SuperiorCanfield(Canfield):
    pass
class Rainfall(Canfield):
    pass
class Rainbow(Canfield):
    pass
class Storehouse(Canfield):
    pass
class Chameleon(Canfield):
    pass
class DoubleCanfield(Canfield):
    pass
class AmericanToad(Canfield):
    pass
class VariegatedCanfield(Canfield):
    pass
class EagleWing_ReserveStack(OpenStack):
    pass
class EagleWing(Canfield):
    pass
class Gate(Game):
    pass
class LittleGate(Gate):
    pass
class Doorway(LittleGate):
    pass
class Minerva(Canfield):
    pass
class Munger(Minerva):
    pass
class Mystique(Munger):
    pass
class TripleCanfield(Canfield):
    pass
class Acme(Canfield):
    pass
class Duke(Game):
    pass
class Demon(Canfield):
    pass
class CanfieldRush_Talon(WasteTalonStack):
    pass
class CanfieldRush(Canfield):
    pass
class Skippy(Canfield):
    pass
class Lafayette(Game):
    pass
class Capricieuse(Game):
    pass
class Nationale(Capricieuse):
    pass
class Strata(Game):
    pass
class Fifteen(Capricieuse):
    pass
class Choice_Foundation(RK_FoundationStack):
    pass
class Choice(Game):
    pass
class CurdsAndWhey_RowStack(BasicRowStack):
    pass
class CurdsAndWhey(Game):
    pass
class MissMuffet(CurdsAndWhey):
    pass
class Nordic(MissMuffet):
    pass
class Dumfries_TalonStack(OpenTalonStack):
    pass
class Dumfries_RowStack(BasicRowStack):
    pass
class Dumfries(Game):
    pass
class Galloway(Dumfries):
    pass
class Robin(Dumfries):
    pass
class Arachnida_RowStack(BasicRowStack):
    pass
class Arachnida(CurdsAndWhey):
    pass
class Harvestman(Arachnida):
    pass
class GermanPatience(Game):
    pass
class BavarianPatience(GermanPatience):
    pass
class TrustyTwelve_Hint(AbstractHint):
    pass
class TrustyTwelve(Game):
    pass
class KnottyNines(TrustyTwelve):
    pass
class SweetSixteen(TrustyTwelve):
    pass
class Glacier(Game):
    pass
class EightPacks(Game):
    pass
class FourPacks_RowStack(SS_RowStack):
    pass
class FourPacks(EightPacks):
    pass
class DieBoeseSieben(Game):
    pass
class Diplomat(Game):
    pass
class LadyPalk(Diplomat):
    pass
class Congress(Diplomat):
    pass
class Parliament(Congress):
    pass
class Wheatsheaf(Congress):
    pass
class RowsOfFour(Diplomat):
    pass
class Dieppe(Diplomat):
    pass
class LittleNapoleon(Diplomat):
    pass
class TwinQueens(Congress):
    pass
class Doublets_Foundation(AbstractFoundationStack):
    pass
class Doublets(Game):
    pass
class EiffelTower_RowStack(OpenStack):
    pass
class EiffelTower(Game):
    pass
class StrictEiffelTower(EiffelTower):
    pass
class Fan_Hint(CautiousDefaultHint):
    pass
class Fan(Game):
    pass
class FanGame(Fan):
    pass
class ScotchPatience(Fan):
    pass
class Shamrocks(Fan):
    pass
class ShamrocksII(Shamrocks):
    pass
class LaBelleLucie_Talon(TalonStack):
    pass
class LaBelleLucie(Fan):
    pass
class SuperFlowerGarden(LaBelleLucie):
    pass
class ThreeShufflesAndADraw_RowStack(SS_RowStack):
    pass
class ThreeShufflesAndADraw_ReserveStack(ReserveStack):
    pass
class ThreeShufflesAndADraw(LaBelleLucie):
    pass
class Trefoil(LaBelleLucie):
    pass
class Intelligence_Talon(LaBelleLucie_Talon):
    pass
class Intelligence_RowStack(UD_SS_RowStack):
    pass
class Intelligence_ReserveStack(ReserveStack, DealRow_StackMethods):
    pass
class Intelligence(Fan):
    pass
class IntelligencePlus(Intelligence):
    pass
class HouseInTheWood(Fan):
    pass
class HouseOnTheHill(HouseInTheWood):
    pass
class CloverLeaf_RowStack(UD_SS_RowStack):
    pass
class CloverLeaf(Game):
    pass
class FreeFan(Fan):
    pass
class BoxFan(Fan):
    pass
class Troika(Fan):
    pass
class Quads_RowStack(RK_RowStack):
    pass
class Quads(Troika):
    pass
class QuadsPlus(Quads):
    pass
class FascinationFan_Talon(RedealTalonStack):
    pass
class FascinationFan(Fan):
    pass
class Crescent_Talon(RedealTalonStack):
    pass
class Crescent(Game):
    pass
class School(Fan):
    pass
class ForestGlade_Talon(DealRowRedealTalonStack):
    pass
class ForestGlade(Game):
    pass
class FortyThieves_Hint(CautiousDefaultHint):
    pass
class FortyThieves(Game):
    pass
class BusyAces(FortyThieves):
    pass
class Limited(BusyAces):
    pass
class Courtyard(BusyAces):
    pass
class WaningMoon(FortyThieves):
    pass
class Lucas(WaningMoon):
    pass
class NapoleonsSquare(FortyThieves):
    pass
class CarreNapoleon(FortyThieves):
    pass
class Josephine(FortyThieves):
    pass
class MarieRose(Josephine):
    pass
class BigCourtyard(Courtyard):
    pass
class Express(Limited):
    pass
class Carnation(Limited):
    pass
class SanJuanHill(FortyThieves):
    pass
class FamousFifty(FortyThieves):
    pass
class Deuces(FortyThieves):
    pass
class Corona(FortyThieves):
    pass
class Quadrangle(Corona):
    pass
class FortyAndEight(FortyThieves):
    pass
class LittleForty(FortyThieves):
    pass
class Streets(FortyThieves):
    pass
class Maria(Streets):
    pass
class NumberTen(Streets):
    pass
class RankAndFile(Streets):
    pass
class Emperor(Streets):
    pass
class TripleLine(Streets):
    pass
class BigStreets(Streets):
    pass
class NumberTwelve(NumberTen):
    pass
class Roosevelt(Streets):
    pass
class RedAndBlack(Streets):
    pass
class Zebra(RedAndBlack):
    pass
class Indian(FortyThieves):
    pass
class Midshipman(Indian):
    pass
class Mumbai(Indian):
    pass
class NapoleonsExile(FortyThieves):
    pass
class DoubleRail(NapoleonsExile):
    pass
class SingleRail(DoubleRail):
    pass
class FinalBattle(DoubleRail):
    pass
class Octave_Talon(WasteTalonStack):
    pass
class Octave_Waste(WasteStack):
    pass
class Octave(Game):
    pass
class FortunesFavor(Game):
    pass
class Octagon(Game):
    pass
class Squadron(FortyThieves):
    pass
class Waterloo(FortyThieves):
    pass
class Junction(Game):
    pass
class Crossroads(Junction):
    pass
class TheSpark_Talon(TalonStack):
    pass
class TheSpark(Game):
    pass
class DoubleGoldMine_RowStack(AC_RowStack):
    pass
class DoubleGoldMine(Streets):
    pass
class Interchange(FortyThieves):
    pass
class Unlimited(Interchange):
    pass
class Breakwater(Interchange):
    pass
class FortyNine_RowStack(AC_RowStack):
    pass
class FortyNine(Interchange):
    pass
class Alternation(Interchange):
    pass
class TripleInterchange(Interchange):
    pass
class IndianPatience_RowStack(BO_RowStack):
    pass
class IndianPatience(Indian):
    pass
class Floradora(Game):
    pass
class BlindPatience_Hint(DefaultHint):
    pass
class BlindPatience_RowStack(AC_RowStack):
    pass
class BlindPatience(FortyThieves):
    pass
class Foothold(FortyThieves):
    pass
class FreeCell(Game):
    pass
class RelaxedFreeCell(FreeCell):
    pass
class ForeCell(FreeCell):
    pass
class ChallengeFreeCell(FreeCell):
    pass
class SuperChallengeFreeCell(ChallengeFreeCell):
    pass
class Stalactites(FreeCell):
    pass
class DoubleFreecell(FreeCell):
    pass
class TripleFreecell(FreeCell):
    pass
class Cell11(TripleFreecell):
    pass
class BigCell(TripleFreecell):
    pass
class Spidercells_RowStack(SuperMoveAC_RowStack):
    pass
class Spidercells(FreeCell):
    pass
class SevenByFour(FreeCell):
    pass
class SevenByFive(SevenByFour):
    pass
class Bath(FreeCell):
    pass
class Clink(FreeCell):
    pass
class Repair(FreeCell):
    pass
class FourColours_RowStack(AC_RowStack):
    pass
class FourColours(FreeCell):
    pass
class GermanFreeCell_Reserve(ReserveStack):
    pass
class GermanFreeCell(SevenByFour):
    pass
class OceanTowers(TripleFreecell):
    pass
class KingCell(FreeCell):
    pass
class Headquarters_Reserve(ReserveStack):
    pass
class Headquarters(Game):
    pass
class CanCan(FreeCell):
    pass
class Limpopo(Game):
    pass
class Glenwood_Talon(WasteTalonStack):
    pass
class Glenwood_Foundation(AbstractFoundationStack):
    pass
class Glenwood_RowStack(AC_RowStack):
    pass
class Glenwood_ReserveStack(OpenStack):
    pass
class Glenwood(Game):
    pass
class DoubleFives_Talon(RedealTalonStack):
    pass
class DoubleFives_RowStack(SS_RowStack):
    pass
class DoubleFives_WasteStack(WasteStack):
    pass
class DoubleFives_Stock(WasteStack):
    pass
class DoubleFives(Glenwood):
    pass
class Golf_Hint(AbstractHint):
    pass
class Golf_Talon(WasteTalonStack):
    pass
class Golf_Waste(WasteStack):
    pass
class Golf_RowStack(BasicRowStack):
    pass
class Golf(Game):
    pass
class DeadKingGolf(Golf):
    pass
class RelaxedGolf(Golf):
    pass
class Elevator_RowStack(Golf_RowStack):
    pass
class Elevator(RelaxedGolf):
    pass
class Escalator(Elevator):
    pass
class BlackHole_Foundation(AbstractFoundationStack):
    pass
class BlackHole_RowStack(ReserveStack):
    pass
class BlackHole(Game):
    pass
class FourLeafClovers_Foundation(AbstractFoundationStack):
    pass
class FourLeafClovers(Game):
    pass
class AllInARow(BlackHole):
    pass
class Robert(Game):
    pass
class Wasatch(Robert):
    pass
class DiamondMine_RowStack(RK_RowStack):
    pass
class DiamondMine(Game):
    pass
class Dolphin(Game):
    pass
class DoubleDolphin(Dolphin):
    pass
class Waterfall_Foundation(AbstractFoundationStack):
    pass
class Waterfall(Game):
    pass
class Vague_RowStack(BasicRowStack):
    pass
class Vague(Game):
    pass
class ThirtyTwoCards(Vague):
    pass
class DevilsSolitaire_Foundation(RK_FoundationStack):
    pass
class DevilsSolitaire_WasteStack(WasteStack):
    pass
class DevilsSolitaire(Game):
    pass
class ThreeFirTrees_RowStack(Golf_RowStack):
    pass
class FirTree_GameMethods:
    pass
class ThreeFirTrees(Golf, FirTree_GameMethods):
    pass
class RelaxedThreeFirTrees(ThreeFirTrees):
    pass
class NapoleonTakesMoscow(Game, FirTree_GameMethods):
    pass
class NapoleonLeavesMoscow(NapoleonTakesMoscow):
    pass
class Flake(Game):
    pass
class Flake2Decks(Flake):
    pass
class Beacon(Game):
    pass
class GrandDuchess_Talon(RedealTalonStack):
    pass
class GrandDuchess_Reserve(ArbitraryStack):
    pass
class GrandDuchess(Game):
    pass
class Parisienne(GrandDuchess):
    pass
class GrandDuchessPlus(GrandDuchess):
    pass
class GrandfathersClock_Hint(CautiousDefaultHint):
    pass
class GrandfathersClock(Game):
    pass
class Dial(Game):
    pass
class Hemispheres_Hint(DefaultHint):
    pass
class Hemispheres_RowStack(SC_RowStack):
    pass
class Hemispheres(Game):
    pass
class BigBen_Talon(DealRowTalonStack):
    pass
class BigBen_RowStack(SS_RowStack):
    pass
class BigBen(Game):
    pass
class Clock_RowStack(RK_RowStack):
    pass
class Clock(Game):
    pass
class Gypsy(Game):
    pass
class Giant_Foundation(SS_FoundationStack):
    pass
class Giant(Gypsy):
    pass
class Irmgard_Talon(TalonStack):
    pass
class Irmgard(Gypsy):
    pass
class DieKoenigsbergerin_Talon(DealRowTalonStack):
    pass
class DieKoenigsbergerin(Gypsy):
    pass
class DieRussische_Foundation(AbstractFoundationStack):
    pass
class DieRussische_RowStack(AC_RowStack):
    pass
class DieRussische(Gypsy):
    pass
class MissMilligan_ReserveStack(AC_RowStack):
    pass
class MissMilligan(Gypsy):
    pass
class ImperialGuards(MissMilligan):
    pass
class Nomad(MissMilligan):
    pass
class MilliganCell(MissMilligan):
    pass
class MilliganHarp(Gypsy):
    pass
class Carlton(MilliganHarp):
    pass
class Steve(Carlton):
    pass
class LexingtonHarp(MilliganHarp):
    pass
class Brunswick(LexingtonHarp):
    pass
class Mississippi(LexingtonHarp):
    pass
class Griffon(Mississippi):
    pass
class Blockade(Gypsy):
    pass
class PhantomBlockade(Gypsy):
    pass
class Cone_Talon(DealRowTalonStack):
    pass
class Cone(Gypsy):
    pass
class Surprise_ReserveStack(ReserveStack):
    pass
class Surprise(Gypsy):
    pass
class Elba(Gypsy):
    pass
class Millie(Gypsy):
    pass
class Hypotenuse(Gypsy):
    pass
class EternalTriangle(Hypotenuse):
    pass
class RightTriangle_Talon(OpenStack, DealRowTalonStack):
    pass
class RightTriangle(Hypotenuse):
    pass
class Trapdoor_Talon(DealRowTalonStack):
    pass
class Trapdoor(Gypsy):
    pass

class TrapdoorSpider(Trapdoor):
    pass
class Flamenco(Gypsy):
    pass
class Eclipse(Gypsy):
    pass
class BrazilianPatience(Gypsy):
    pass
class Leprechaun_Reserve(OpenStack):
    pass
class Leprechaun(Game):
    pass
class LockedCards_Reserve(OpenStack):
    pass
class LockedCards_Foundation(SS_FoundationStack):
    pass
class LockedCards(Game):
    pass
class TopsyTurvyQueens(LockedCards):
    pass
class Thirty_RowStack(BasicRowStack):
    pass
class Thirty(Game):
    pass
class DoubleKlondike(Game):
    pass
class DoubleKlondikeByThrees(DoubleKlondike):
    pass
class Gargantua(DoubleKlondike):
    pass
class Pantagruel(DoubleKlondike):
    pass
class BigHarp(DoubleKlondike):
    pass
class Steps(DoubleKlondike):
    pass
class TripleKlondike(DoubleKlondike):
    pass
class TripleKlondikeByThrees(DoubleKlondike):
    pass
class ChineseKlondike(DoubleKlondike):
    pass
class LadyJane(DoubleKlondike):
    pass
class Inquisitor(DoubleKlondike):
    pass
class Arabella(DoubleKlondike):
    pass
class BigDeal(DoubleKlondike):
    pass
class Delivery(BigDeal):
    pass
class DoubleKingsley(DoubleKlondike):
    pass
class ThievesOfEgypt(DoubleKlondike):
    pass
class Brush(DoubleKlondike):
    pass
class HeadsAndTails_Reserve(OpenStack):
    pass
class HeadsAndTails(Game):
    pass
class Barrier_ReserveStack(OpenStack):
    pass
class Barrier(Game):
    pass
class DerKatzenschwanz_Hint(FreeCellType_Hint):
    pass
class DerKatzenschwanz(Game):
    pass
class DieSchlange(DerKatzenschwanz):
    pass
class Kings(DerKatzenschwanz):
    pass
class Retinue(DieSchlange, Kings):
    pass
class SalicLaw_Hint(CautiousDefaultHint):
    pass
class SalicLaw_Talon(TalonStack):
    pass
class SalicLaw_Talon_2(SalicLaw_Talon):
    pass
class SalicLaw_RowStack(OpenStack):
    pass
class SalicLaw_Foundation(RK_FoundationStack):
    pass
class SalicLaw(DerKatzenschwanz):
    pass
class Deep(DerKatzenschwanz):
    pass
class FaerieQueen_RowStack(RK_RowStack):
    pass
class FaerieQueen(SalicLaw):
    pass
class Intrigue_RowStack(OpenStack):
    pass
class Intrigue(SalicLaw):
    pass
class LaggardLady_Foundation(RK_FoundationStack):
    pass
class LaggardLady(Intrigue):
    pass
class Glencoe_Foundation(RK_FoundationStack):
    pass
class Glencoe(Intrigue):
    pass
class StepUp_Foundation(SS_FoundationStack):
    pass
class StepUp_Talon(WasteTalonStack):
    pass
class StepUp_RowStack(AC_RowStack):
    pass
class StepUp(Game):
    pass
class Kentish(Kings):
    pass
class Klondike(Game):
    pass
class VegasKlondike(Klondike):
    pass
class CasinoKlondike(VegasKlondike):
    pass
class KlondikeByThrees(Klondike):
    pass
class ThumbAndPouch(Klondike):
    pass
class Chinaman(ThumbAndPouch):
    pass
class Whitehead_RowStack(SS_RowStack):
    pass
class Whitehead(Klondike):
    pass
class SmallHarp(Klondike):
    pass
class Eastcliff(Klondike):
    pass
class Easthaven(Eastcliff):
    pass
class DoubleEasthaven(Easthaven):
    pass
class TripleEasthaven(Easthaven):
    pass
class Westcliff(Eastcliff):
    pass
class Westhaven(Westcliff):
    pass
class PasSeul(Eastcliff):
    pass
class BlindAlleys(Eastcliff):
    pass
class Somerset(Klondike):
    pass
class Morehead(Somerset):
    pass
class Usk(Somerset):
    pass
class AmericanCanister(Klondike):
    pass
class Canister(AmericanCanister):
    pass
class BritishCanister(AmericanCanister):
    pass
class AgnesSorel(Klondike):
    pass
class EightTimesEight(Klondike):
    pass
class AchtmalAcht(EightTimesEight):
    pass
class EightByEight_RowStack(RK_RowStack):
    pass
class EightByEight(EightTimesEight):
    pass
class Batsford_ReserveStack(ReserveStack):
    pass
class Batsford(Klondike):
    pass
class BatsfordAgain(Batsford):
    pass
class Jumbo(Klondike):
    pass
class OpenJumbo(Jumbo):
    pass
class Stonewall(Klondike):
    pass
class FlowerGarden(Stonewall):
    pass
class KingAlbert(Klondike):
    pass
class Raglan(KingAlbert):
    pass
class Brigade(Raglan):
    pass
class QueenVictoria(KingAlbert):
    pass
class Jane_Talon(OpenTalonStack):
    pass
class Jane(Klondike):
    pass
class AgnesBernauer_Talon(DealRowTalonStack):
    pass
class AgnesBernauer(Jane):
    pass
class Senate(Jane):
    pass
class SenatePlus(Senate):
    pass
class Phoenix(Klondike):
    pass
class Arizona(Phoenix):
    pass
class Lanes(Klondike):
    pass
class ThirtySix(Klondike):
    pass
class Q_C_(Klondike):
    pass
class NorthwestTerritory(KingAlbert):
    pass
class ArticGarden(NorthwestTerritory):
    pass
class AuntMary(Klondike):
    pass
class DoubleDot(Klondike):
    pass
class SevenDevils_RowStack(AC_RowStack):
    pass
class SevenDevils(Klondike):
    pass
class MovingLeft(Klondike):
    pass
class Souter(MovingLeft):
    pass
class BigForty(Klondike):
    pass
class AliBaba(BigForty):
    pass
class Cassim(AliBaba):
    pass
class Saratoga(Klondike):
    pass
class Whitehorse(Klondike):
    pass
class Boost(Klondike):
    pass
class GoldRush(Klondike):
    pass
class GoldMine_RowStack(AC_RowStack):
    pass
class GoldMine(Klondike):
    pass
class LuckyThirteen(Game):
    pass
class LuckyPiles(LuckyThirteen):
    pass
class Legion(Klondike):
    pass
class BigBertha(Game):
    pass
class Athena(Klondike):
    pass
class Kingsley(Klondike):
    pass
class Scarp(Klondike):
    pass
class EightSages_Row(AC_RowStack):
    pass
class EightSages(Klondike):
    pass
class Labyrinth_Talon(DealRowTalonStack):
    pass
class Labyrinth_RowStack(BasicRowStack):
    pass
class Labyrinth(Game):
    pass
class LarasGame_Hint(CautiousDefaultHint):
    pass
class LarasGame_Talon(WasteTalonStack):
    pass
class LarasGame_RowStack(OpenStack):
    pass
class LarasGame_ReserveStack(OpenStack):
    pass
class LarasGame_Reserve(OpenStack):
    pass
class LarasGame(Game):
    pass
class RelaxedLarasGame(LarasGame):
    pass
class DoubleLarasGame(RelaxedLarasGame):
    pass
class Matriarchy_Waste(WasteStack):
    pass
class Matriarchy_Talon(WasteTalonStack):
    pass
class Matriarchy_UpRowStack(SS_RowStack):
    pass
class Matriarchy_DownRowStack(SS_RowStack):
    pass
class Matriarchy(Game):
    pass
class Montana_Hint(DefaultHint):
    pass
class Montana_Talon(TalonStack):
    pass
class Montana_RowStack(BasicRowStack):
    pass
class Montana(Game):
    pass
class Spaces_Talon(Montana_Talon):
    pass
class Spaces(Montana):
    pass
class BlueMoon(Montana):
    pass
class RedMoon(BlueMoon):
    pass
class Galary_Hint(Montana_Hint):
    pass
class Galary_RowStack(Montana_RowStack):
    pass
class Galary(RedMoon):
    pass
class Moonlight(Montana):
    pass
class Jungle_RowStack(Montana_RowStack):
    pass
class Jungle(BlueMoon):
    pass
class SpacesAndAces_RowStack(Montana_RowStack):
    pass
class SpacesAndAces(BlueMoon):
    pass
class Paganini_Talon(Montana_Talon):
    pass
class Paganini_RowStack(Montana_RowStack):
    pass
class Paganini(BlueMoon):
    pass
class Spoilt_RowStack(BasicRowStack):
    pass
class Spoilt_Waste(WasteStack):
    pass
class Spoilt(Game):
    pass
class DoubleMontana(Montana):
    pass
class MonteCarlo_Hint(DefaultHint):
    pass
class MonteCarlo_Talon(TalonStack):
    pass
class MonteCarlo(Game):
    pass
class MonteCarlo2Decks(MonteCarlo):
    pass
class Weddings_Talon(MonteCarlo_Talon):
    pass
class Weddings(MonteCarlo):
    pass
class SimpleCarlo(MonteCarlo):
    pass
class SimplePairs(MonteCarlo):
    pass
class Neighbour_Foundation(AbstractFoundationStack):
    pass
class Neighbour_RowStack(MonteCarlo_RowStack):
    pass
class Neighbour(MonteCarlo):
    pass
class Fourteen_RowStack(MonteCarlo_RowStack):
    pass
class Fourteen(Game):
    pass
class Nestor_RowStack(MonteCarlo_RowStack):
    pass
class Nestor(Game):
    pass
class Vertical(Nestor):
    pass
class TheWish(Game):
    pass
class TheWishOpen(TheWish):
    pass
class DerLetzteMonarch_Foundation(SS_FoundationStack):
    pass
class DerLetzteMonarch_RowStack(ReserveStack):
    pass
class DerLetzteMonarch_ReserveStack(ReserveStack):
    pass
class DerLetzteMonarch(Game):
    pass
class TheLastMonarchII(DerLetzteMonarch):
    pass
class DoubletsII(Game):
    pass
class RightAndLeft_Talon(DealRowRedealTalonStack):
    pass
class RightAndLeft(Game):
    pass
class Napoleon_RowStack(UD_SS_RowStack):
    pass
class Napoleon_ReserveStack(BasicRowStack):
    pass
class Napoleon_SingleFreeCell(ReserveStack):
    pass
class Napoleon_FreeCell(ReserveStack):
    pass
class DerKleineNapoleon(Game):
    pass
class DerFreieNapoleon(DerKleineNapoleon):
    pass
class Napoleon(DerKleineNapoleon):
    pass
class FreeNapoleon(DerFreieNapoleon):
    pass
class Master(DerFreieNapoleon):
    pass
class TheLittleCorporal_RowStack(UD_SS_RowStack):
    pass
class TheLittleCorporal(DerFreieNapoleon):
    pass
class Bonaparte(TheLittleCorporal):
    pass
class BusyCards_FreeCell(ReserveStack):
    pass
class BusyCards(Game):
    pass
class Needle(Game):
    pass
class Haystack(Needle):
    pass
class Pitchfork(Needle):
    pass
class Numerica_Hint(DefaultHint):
    pass
class Numerica_RowStack(BasicRowStack):
    pass
class Numerica(Game):
    pass
class Numerica2Decks(Numerica):
    pass
class LadyBetty(Numerica):
    pass
class LastChance_RowStack(Numerica_RowStack):
    pass
class LastChance_Reserve(OpenStack):
    pass
class LastChance(LadyBetty):
    pass
class PussInTheCorner_Talon(OpenTalonStack):
    pass
class PussInTheCorner_Foundation(SS_FoundationStack):
    pass
class PussInTheCorner_RowStack(BasicRowStack):
    pass
class PussInTheCorner(Numerica):
    pass
class Frog(Game):
    pass
class Fly(Frog):
    pass
class Fanny(Frog):
    pass
class Gnat(Game):
    pass
class Gloaming_Hint(Numerica_Hint):
    pass
class Gloaming_RowStack(Numerica_RowStack):
    pass
class Gloaming(Game):
    pass
class Chamberlain(Gloaming):
    pass
class Toad_TalonStack(DealRowTalonStack):
    pass
class Toad(Game):
    pass
class Shifting_Hint(Numerica_Hint):
    pass
class Shifting_RowStack(Numerica_RowStack):
    pass
class Shifting(Numerica):
    pass
class Strategerie_Talon(OpenTalonStack):
    pass
class Strategerie_RowStack(BasicRowStack):
    pass
class Strategerie_ReserveStack(ReserveStack):
    pass
class Strategerie(Game):
    pass
class Assembly_RowStack(RK_RowStack):
    pass
class Assembly(Numerica):
    pass
class AnnoDomini_Hint(DefaultHint):
    pass
class AnnoDomini(Numerica):
    pass
class CircleNine_RowStack(BasicRowStack):
    pass
class CircleNine(Game):
    pass
class Measure(CircleNine):
    pass
class DoubleMeasure(Measure):
    pass
class Amphibian(Game):
    pass
class Aglet(Game):
    pass
class Osmosis_Foundation(AbstractFoundationStack):
    pass
class Osmosis(Game):
    pass
class Peek(Osmosis):
    pass
class OsmosisII_Foundation(AbstractFoundationStack):
    pass
class OsmosisII(Osmosis):
    pass
class PeekII(OsmosisII):
    pass
class OpenPeek(Game):
    pass
class Genesis(Game):
    pass
class GenesisPlus(Genesis):
    pass
class Bridesmaids(Game):
    pass
class Parallels_RowStack(BasicRowStack):
    pass
class Parallels_TalonStack(DealRowTalonStack):
    pass
class Parallels(Game):
    pass
class BritishBlockade(Parallels):
    pass
class PasDeDeux_Hint(AbstractHint):
    pass
class PasDeDeux_Waste(WasteStack):
    pass
class PasDeDeux_RowStack(ReserveStack):
    pass
class PasDeDeux(Game):
    pass
class PictureGallery_Hint(AbstractHint):
    pass
class PictureGallery_Foundation(RK_FoundationStack):
    pass
class PictureGallery_TableauStack(SS_RowStack):
    pass
class PictureGallery_RowStack(BasicRowStack):
    pass
class PictureGallery(Game):
    pass
class GreatWheel_Hint(PictureGallery_Hint):
    pass
class GreatWheel_Foundation(PictureGallery_Foundation):
    pass
class GreatWheel_RowStack(BasicRowStack):
    pass
class GreatWheel(PictureGallery):
    pass
class MountOlympus_Foundation(SS_FoundationStack):
    pass
class MountOlympus_RowStack(SS_RowStack):
    pass
class MountOlympus(Game):
    pass
class Zeus_RowStack(MountOlympus_RowStack):
    pass
class Zeus(MountOlympus):
    pass
class RoyalParade_TableauStack(PictureGallery_TableauStack):
    pass
class RoyalParade(PictureGallery):
    pass
class VirginiaReel_Talon(DealRowTalonStack):
    pass
class VirginiaReel(RoyalParade):
    pass
class PileOn_RowStack(RK_RowStack):
    pass
class PileOn(Game):
    pass
class SmallPileOn(PileOn):
    pass
## class PileOn2Decks(PileOn):
    pass
class Foursome(Game):
    pass
class Quartets(Foursome):
    pass
class FourByFour_Hint(DefaultHint):
    pass
class FourByFour_Foundation(AbstractFoundationStack):
    pass
class FourByFour(Game):
    pass
class Footling(FourByFour):
    pass
class DoubleFootling(Footling):
    pass
class PushPin_Hint(AbstractHint):
    pass
class PushPin_Foundation(AbstractFoundationStack):
    pass
class PushPin_Talon(DealRowTalonStack):
    pass
class PushPin_RowStack(ReserveStack):
    pass
class PushPin(Game):
    pass
class RoyalMarriage(PushPin):
    pass
class Queens(PushPin):
    pass
class Accordion_Hint(AbstractHint):
    pass
class Accordion_RowStack(PushPin_RowStack):
    pass
class Accordion(PushPin):
    pass
class Pyramid_Hint(DefaultHint):
    pass
class Pyramid_StackMethods:
    pass
class Pyramid_Foundation(AbstractFoundationStack):
    pass
class Pyramid_Talon(Pyramid_StackMethods, FaceUpWasteTalonStack):
    pass
class Pyramid_Waste(Pyramid_StackMethods, WasteStack):
    pass
class Pyramid_RowStack(Pyramid_StackMethods, OpenStack):
    pass
class Pyramid(Game):
    pass
class RelaxedPyramid(Pyramid):
    pass
class Giza_Reserve(Pyramid_StackMethods, OpenStack):
    pass
class Giza(Pyramid):
    pass
class Thirteen(Pyramid):
    pass
class Thirteens(Pyramid):
    pass
class Elevens_RowStack(Giza_Reserve):
    pass
class Elevens_Reserve(ReserveStack):
    pass
class Elevens(Pyramid):
    pass
class ElevensToo(Elevens):
    pass
class SuitElevens_RowStack(Elevens_RowStack):
    pass
class SuitElevens_Reserve(Elevens_Reserve):
    pass
class SuitElevens(Elevens):
    pass
class Fifteens_RowStack(Elevens_RowStack):
    pass
class Fifteens_Reserve(ReserveStack):
    pass
class Fifteens(Elevens):
    pass
class TripleAlliance_Reserve(ReserveStack):
    pass
class TripleAlliance(Game):
    pass
class Pharaohs(Pyramid):
    pass
class Baroness_Talon(DealRowTalonStack):
    pass
class Baroness_RowStack(Giza_Reserve):
    pass
class Baroness(Pyramid):
    pass
class Apophis_Hint(Pyramid_Hint):
    pass
class Apophis_RowStack(Pyramid_RowStack):
    pass
class Apophis(Pharaohs):
    pass
class Cheops_StackMethods(Pyramid_StackMethods):
    pass
class Cheops_Talon(Cheops_StackMethods, Pyramid_Talon):
    pass
class Cheops_Waste(Cheops_StackMethods, Pyramid_Waste):
    pass
class Cheops_RowStack(Cheops_StackMethods, Pyramid_RowStack):
    pass
class Cheops(Pyramid):
    pass
class Exit_RowStack(Elevens_RowStack):
    pass
class Exit(Game):
    pass
class TwoPyramids(Pyramid):
    pass
class KingTut(RelaxedPyramid):
    pass
class DoublePyramid(Pyramid):
    pass
class Triangle(Pyramid):
    pass
class UpAndDown(Pyramid):
    pass
class Hurricane_Hint(DefaultHint):
    pass
class Hurricane_StackMethods(Pyramid_StackMethods):
    pass
class Hurricane_RowStack(Hurricane_StackMethods, BasicRowStack):
    pass
class Hurricane_Reserve(Hurricane_StackMethods, OpenStack):
    pass
class Hurricane(Pyramid):
    pass
class RoyalCotillion_Foundation(SS_FoundationStack):
    pass
class RoyalCotillion(Game):
    pass
class OddAndEven(RoyalCotillion):
    pass
class Kingdom(RoyalCotillion):
    pass
class Alhambra_Hint(CautiousDefaultHint):
    pass
class Alhambra_RowStack(UD_SS_RowStack):
    pass
class Alhambra_Talon(DealRowTalonStack):
    pass
class Alhambra(Game):
    pass
class Granada(Alhambra):
    pass
class Reserves_RowStack(UD_RK_RowStack):
    pass
class Reserves(Alhambra):
    pass
class GrantsReinforcement(Reserves):
    pass
class Carpet(Game):
    pass
class BritishConstitution_RowStackMethods:
    pass
class BritishConstitution_RowStack(BritishConstitution_RowStackMethods, AC_RowStack):
    pass
class NewBritishConstitution_RowStack(BritishConstitution_RowStackMethods, RK_RowStack):
    pass
class BritishConstitution_Foundation(SS_FoundationStack):
    pass
class BritishConstitution(Game):
    pass
class NewBritishConstitution(BritishConstitution):
    pass
class Twenty_RowStack(BasicRowStack):
    pass
class Twenty(Game):
    pass
class ThreePirates_Talon(DealRowTalonStack):
    pass
class ThreePirates(Game):
    pass
class Frames_Hint(CautiousDefaultHint):
    pass
class UnionSquare_Foundation(AbstractFoundationStack):
    pass
class Frames_Foundation(UnionSquare_Foundation):
    pass
class Frames_RowStack(UD_SS_RowStack):
    pass
class Frames(Game):
    pass
class RoyalRendezvous(Game):
    pass
class ShadyLanes_Hint(CautiousDefaultHint):
    pass
class ShadyLanes_Foundation(AbstractFoundationStack):
    pass
class ShadyLanes_RowStack(AC_RowStack):
    pass
class ShadyLanes(Game):
    pass
class FourWinds(Game):
    pass
class BoxingTheCompass(FourWinds):
    pass
class Colonel_Hint(DefaultHint):
    pass
class Colonel_RowStack(SS_RowStack):
    pass
class Colonel(Game):
    pass
class TheRedAndTheBlack_Foundation(AC_FoundationStack):
    pass
class TheRedAndTheBlack_Reserve(ReserveStack):
    pass
class TheRedAndTheBlack(Game):
    pass
class TwilightZone_Foundation(AC_FoundationStack):
    pass
class TwilightZone_Talon(OpenTalonStack, WasteTalonStack):
    pass
class TwilightZone_RowStack(AC_RowStack):
    pass
class TwilightZone_Waste(WasteStack):
    pass
class TwilightZone(Game):
    pass
class RoyalEast(Game):
    pass
class Sanibel(Gypsy):
    pass
class SiebenBisAs_Hint(CautiousDefaultHint):
    pass
class SiebenBisAs_Foundation(SS_FoundationStack):
    pass
class SiebenBisAs_RowStack(BasicRowStack):
    pass
class SiebenBisAs(Game):
    pass
class Maze_Hint(SiebenBisAs_Hint):
    pass
class Maze_RowStack(BasicRowStack):
    pass
class Maze(Game):
    pass
class Simplex_Foundation(AbstractFoundationStack):
    pass
class Simplex_RowStack(SequenceRowStack):
    pass
class Simplex(Game):
    pass
class Spider_Hint(SpiderType_Hint):
    pass
class Spider_RowStack(Spider_SS_RowStack):
    pass
class SuperMoveSpider_RowStack(SuperMoveStack_StackMethods, Spider_RowStack):
    pass
class RelaxedSpider(Game):
    pass
class Spider(RelaxedSpider):
    pass
class Spider1Suit(Spider):
    pass
class Spider2Suits(Spider):
    pass
class OpenSpider(Spider):
    pass
class BlackWidow_RowStack(RK_RowStack, Spider_RowStack):
    pass
class BlackWidow(Spider):
    pass
class GroundsForADivorce_Talon(TalonStack):
    pass
class GroundsForADivorce(RelaxedSpider):
    pass
class GrandmothersGame(RelaxedSpider):
    pass
class Spiderette(Spider):
    pass
class BabySpiderette(Spiderette):
    pass
class WillOTheWisp(Spiderette):
    pass
class SimpleSimon(Spider):
    pass
class SimpleSimonII(SimpleSimon):
    pass
class Rachel(RelaxedSpider):
    pass
class Scorpion_RowStack(Yukon_SS_RowStack, Spider_RowStack):
    pass
class Scorpion(RelaxedSpider):
    pass
class ScorpionTail_RowStack(Yukon_AC_RowStack, Spider_RowStack):
    pass
class ScorpionTail(Scorpion):
    pass
class DoubleScorpion(Scorpion):
    pass
class TripleScorpion(Scorpion):
    pass
class Wasp(Scorpion):
    pass
class ThreeBlindMice(Scorpion):
    pass
class FarmersWife(ThreeBlindMice):
    pass
class HowTheyRun(ThreeBlindMice):
    pass
class RougeEtNoir_RowStack(KingAC_RowStack):
    pass
class RougeEtNoir(Game):
    pass
class MrsMop(RelaxedSpider):
    pass
class Cicely_Talon(DealRowTalonStack):
    pass
class Cicely(Game):
    pass
class Trillium(Game):
    pass
class Lily(Trillium):
    pass
class WakeRobin(Trillium):
    pass
class TripleWakeRobin(WakeRobin):
    pass
class Chelicera_RowStack(Yukon_SS_RowStack):
    pass
class Chelicera(Game):
    pass
class ScorpionHead(Scorpion):
    pass
class SpiderWeb(RelaxedSpider):
    pass
class SimonJester(Spider):
    pass
class Applegate(Game):
    pass
class BigSpider(Spider):
    pass
class BigSpider1Suit(BigSpider):
    pass
class BigSpider2Suits(BigSpider):
    pass
class Spider3x3(BigSpider):
    pass
class GroundsForADivorce3Decks(BigSpider):
    pass
class Spider4Decks(BigSpider):
    pass
class GroundsForADivorce4Decks(Spider4Decks):
    pass
class ChineseSpider(Spider):
    pass
class York(RelaxedSpider):
    pass
class BigYork(York):
    pass
class Spidike(RelaxedSpider):
    pass
class FredsSpider(Spidike):
    pass
class FredsSpider3Decks(FredsSpider):
    pass
class LongTail(RelaxedSpider):
    pass
class ShortTail(LongTail):
    pass
class Incompatibility(Spidike):
    pass
class ScorpionII(Scorpion):
    pass
class Tarantula_RowStack(Spider_RowStack):
    pass
class Tarantula(Spider):
    pass
class FechtersGame_Talon(TalonStack):
    pass
class FechtersGame_RowStack(AC_RowStack):
    pass
class FechtersGame(RelaxedSpider):
    pass
class Bebop(Game):
    pass
class TheJollyRoger_Foundation(AbstractFoundationStack):
    pass
class TheJollyRoger_RowStack(BasicRowStack):
    pass
class TheJollyRoger(Game):
    pass
class StHelena_Talon(TalonStack):
    pass
class StHelena_FoundationStack(SS_FoundationStack):
    pass
class StHelena(Game):
    pass
class BoxKite(StHelena):
    pass
class LesQuatreCoins_RowStack(UD_RK_RowStack):
    pass
class LesQuatreCoins_Talon(RedealTalonStack):
    pass
class LesQuatreCoins_Foundation(SS_FoundationStack):
    pass
class LesQuatreCoins(Game):
    pass
class RegalFamily_RowStack(UD_SS_RowStack):
    pass
class RegalFamily(Game):
    pass
class Sultan(Game):
    pass
class SultanPlus(Sultan):
    pass
class Boudoir(Game):
    pass
class CaptiveQueens(Game):
    pass
class Contradance(Game):
    pass
class IdleAces_AceFoundation(AbstractFoundationStack):
    pass
class IdleAces(Game):
    pass
class LadyOfTheManor_RowStack(BasicRowStack):
    pass
class LadyOfTheManor_Reserve(OpenStack):
    pass
class LadyOfTheManor(Game):
    pass
class Matrimony_Talon(DealRowTalonStack):
    pass
class Matrimony(Game):
    pass
class PicturePatience(Game):
    pass
class Patriarchs(PicturePatience):
    pass
class SixesAndSevens(Game):
    pass
class TwoRings(Game):
    pass
class CornerSuite_RowStack(RK_RowStack):
    pass
class CornerSuite(Game):
    pass
class Marshal_Hint(CautiousDefaultHint):
    pass
class Marshal(Game):
    pass
class RoyalAids(Game):
    pass
class CircleEight(Game):
    pass
class Adela_Foundation(SS_FoundationStack):
    pass
class Adela(Game):
    pass
class Toni(Game):
    pass
class Khedive(Game):
    pass
class Phalanx(Game):
    pass
class Grandee(Game):
    pass
class Turncoats(Grandee):
    pass
class Voracious(Grandee):
    pass
class DesertIsland(Game):
    pass
class CatherineTheGreat(Game):
    pass
class TakeAway_Foundation(AbstractFoundationStack):
    pass
class TakeAway(Game):
    pass
class FourStacks_RowStack(AC_RowStack):
    pass
class FourStacks(Game):
    pass
class Striptease_RowStack(UD_RK_RowStack):
    pass
class Striptease_Reserve(OpenStack):
    pass
class Striptease(TakeAway):
    pass
class Terrace_Talon(WasteTalonStack):
    pass
class Terrace_AC_Foundation(AC_FoundationStack):
    pass
class Terrace_SS_Foundation(SS_FoundationStack):
    pass
class Terrace_RowStack(AC_RowStack):
    pass
class Terrace(Game):
    pass
class QueenOfItaly(Terrace):
    pass
class GeneralsPatience(Terrace):
    pass
class BlondesAndBrunettes(Terrace):
    pass
class FallingStar(BlondesAndBrunettes):
    pass
class Wood_RowStack(AC_RowStack):
    pass
class Wood(BlondesAndBrunettes):
    pass
class Signora(Terrace):
    pass
class Madame(Terrace):
    pass
class MamySusan_RowStack(AC_RowStack):
    pass
class MamySusan(Terrace):
    pass
class BastilleDay_BastilleStack(Stack):
    pass
class BastilleDay(Game):
    pass
class ThreePeaks_TalonStack(WasteTalonStack):
    pass
class ThreePeaks_RowStack(OpenStack):
    pass
class ThreePeaks(Game):
    pass
class ThreePeaksNoScore(ThreePeaks):
    pass
class Tournament_Talon(DealRowRedealTalonStack):
    pass
class Tournament(Game):
    pass
class LaNivernaise(Tournament):
    pass
class KingsdownEights_Talon(DealRowTalonStack):
    pass
class KingsdownEights(Game):
    pass
class Saxony_Reserve(SS_RowStack):
    pass
class Saxony_Talon(DealRowTalonStack):
    pass
class Saxony(Game):
    pass
class LadiesBattle_RowStack(AC_RowStack):
    pass
class LadiesBattle(Game):
    pass
class UnionSquare_RowStack(OpenStack):
    pass
class UnionSquare(Game):
    pass
class SolidSquare(UnionSquare):
    pass
class Boomerang_Foundation(AbstractFoundationStack):
    pass
class Boomerang(UnionSquare):
    pass
class WaveMotion(Game):
    pass
class Flourish(WaveMotion):
    pass
class Windmill_Foundation(RK_FoundationStack):
    pass
class Windmill_RowStack(ReserveStack):
    pass
class Windmill(Game):
    pass
class DutchSolitaire_RowStack(UD_RK_RowStack):
    pass
class DutchSolitaire(Windmill):
    pass
class NapoleonsTomb(Game):
    pass
class Corners(Game):
    pass
class Czarina_RowStack(RK_RowStack):
    pass
class Czarina(Corners):
    pass
class FourSeasons(Czarina):
    pass
class FlorentinePatience(FourSeasons):
    pass
class Simplicity(Game):
    pass
class Yukon(Game):
    pass
class RussianSolitaire(Yukon):
    pass
class Moosehide_RowStack(Yukon_AC_RowStack):
    pass
class Moosehide(Yukon):
    pass
class Odessa(RussianSolitaire):
    pass
class Grandfather_Talon(RedealTalonStack):
    pass
class Grandfather(RussianSolitaire):
    pass
class Alaska_RowStack(Yukon_SS_RowStack):
    pass
class Alaska(RussianSolitaire):
    pass
class Roslin_RowStack(Yukon_AC_RowStack):
    pass
class Roslin(Yukon):
    pass
class ChineseDiscipline(Yukon):
    pass
class ChineseSolitaire(ChineseDiscipline):
    pass
class Queenie(Yukon):
    pass
class Rushdike(RussianSolitaire):
    pass
class RussianPoint(Rushdike):
    pass
class Abacus_Foundation(SS_FoundationStack):
    pass
class Abacus_RowStack(Yukon_SS_RowStack):
    pass
class Abacus(Rushdike):
    pass
class DoubleYukon(Yukon):
    pass
class DoubleRussianSolitaire(DoubleYukon):
    pass
class TripleYukon(Yukon):
    pass
class TripleRussianSolitaire(TripleYukon):
    pass
class TenAcross(Yukon):
    pass
class Panopticon(TenAcross):
    pass
class AustralianPatience(RussianSolitaire):
    pass
class RawPrawn(AustralianPatience):
    pass
class BimBom(AustralianPatience):
    pass
class Geoffrey(Yukon):
    pass
class Queensland(Yukon):
    pass
class OutbackPatience(Yukon):
    pass
class RussianSpider_RowStack(Yukon_SS_RowStack): #Spider_SS_RowStack
    pass
class RussianSpider(RussianSolitaire):
    pass
class DoubleRussianSpider(RussianSpider, DoubleRussianSolitaire):
    pass
class Brisbane_RowStack(Yukon_AC_RowStack):
    pass
class Brisbane(Yukon):
    pass
class Hawaiian(Game):
    pass
class WaveTalon(DealRowTalonStack):
    pass
class Wave(Game):
    pass
class Zodiac_Foundation(SS_FoundationStack):
    pass
class Zodiac_RowStack(UD_SS_RowStack):
    pass
class Zodiac_ReserveStack(ReserveStack):
    pass
class Zodiac(Game):
    pass
class TwelveSleepingMaids_Reserve(OpenStack):
    pass
class TwelveSleepingMaids(Game):
    pass
class Mahjongg_Hint(AbstractHint):
    pass
#class Mahjongg_Foundation(AbstractFoundationStack):
    pass
class Mahjongg_Foundation(OpenStack):
    pass
class Mahjongg_RowStack(OpenStack):
    pass
class AbstractMahjonggGame(Game):
    NCARDS = 144
class Shisen_Hint(AbstractHint):
    pass
class NotShisen_Hint(Shisen_Hint):
    pass
class Shisen_Foundation(AbstractFoundationStack):
    pass
class Shisen_RowStack(Mahjongg_RowStack):
    pass
class AbstractShisenGame(AbstractMahjonggGame):
    pass
class Shisen_18x8(AbstractShisenGame):
    L = (18, 8)
class Shisen_14x6(AbstractShisenGame):
    L = (14, 6)
    NCARDS = 84
class Shisen_24x12(AbstractShisenGame):
    L = (24, 12)
    NCARDS = 288
class Shisen_18x8_NoGravity(AbstractShisenGame):
    L = (18, 8)
    GRAVITY = False
class Shisen_14x6_NoGravity(AbstractShisenGame):
    L = (14, 6)
    NCARDS = 84
    GRAVITY = False
class Shisen_24x12_NoGravity(AbstractShisenGame):
    L = (24, 12)
    NCARDS = 288
    GRAVITY = False
class NotShisen_RowStack(Shisen_RowStack):
    pass
class NotShisen_14x6(AbstractShisenGame):
    Hint_Class = NotShisen_Hint
    RowStack_Class = NotShisen_RowStack
    L = (14, 6)
    NCARDS = 84
class NotShisen_18x8(AbstractShisenGame):
    Hint_Class = NotShisen_Hint
    RowStack_Class = NotShisen_RowStack
    L = (18, 8)
class NotShisen_24x12(AbstractShisenGame):
    Hint_Class = NotShisen_Hint
    RowStack_Class = NotShisen_RowStack
    L = (24, 12)
    NCARDS = 288
class TowerOfHanoy_Hint(CautiousDefaultHint):
    pass
class TowerOfHanoy_RowStack(BasicRowStack):
    pass
class TowerOfHanoy(Game):
    pass
class HanoiPuzzle_RowStack(TowerOfHanoy_RowStack):
    pass
class HanoiPuzzle4(TowerOfHanoy):
    pass
class HanoiPuzzle5(HanoiPuzzle4):
    pass
class HanoiPuzzle6(HanoiPuzzle4):
    pass
class Memory_RowStack(OpenStack):
    pass
class Memory24(Game):
    pass
class Memory30(Memory24):
    pass
class Memory40(Memory24):
    pass
class Concentration_RowStack(Memory_RowStack):
    pass
class Concentration(Memory24):
    pass
class Pegged_Hint(AbstractHint):
    pass
class Pegged_RowStack(ReserveStack):
    pass
class Pegged(Game):
    Hint_Class = Pegged_Hint
    STEPS = ((-4, 0), (4, 0), (0, -4), (0, 4))
    ROWS = (3, 5, 7, 7, 7, 5, 3)
    EMPTY_STACK_ID = -1
class PeggedCross1(Pegged):
    ROWS = (3, 3, 7, 7, 7, 3, 3)
class PeggedCross2(Pegged):
    ROWS = (3, 3, 3, 9, 9, 9, 3, 3, 3)
class Pegged6x6(Pegged):
    EMPTY_STACK_ID = 14
    ROWS = (6, 6, 6, 6, 6, 6)
class Pegged7x7(Pegged):
    ROWS = (7, 7, 7, 7, 7, 7, 7)
class PeggedTriangle1(Pegged):
    STEPS = ((-2, -4), (-2, 4), (-4, 0), (4, 0), (2, -4), (2, 4))
    ROWS = (1, 2, 3, 4, 5)
    EMPTY_STACK_ID = 4
class PeggedTriangle2(PeggedTriangle1):
    ROWS = (1, 2, 3, 4, 5, 6)
class PokerSquare_RowStack(ReserveStack):
    pass
class PokerSquare(Game):
    pass
class PokerShuffle_RowStack(ReserveStack):
    pass
class PokerShuffle(PokerSquare):
    pass
class Wicked_Talon(Cruel_Talon):
    pass
class ImperialTrump_Foundation(SS_FoundationStack):
    pass
class Ponytail_Foundation(Braid_Foundation):
    pass
class Tarock_OpenStack(OpenStack):
    pass
class Tarock_AC_RowStack(Tarock_OpenStack):
    pass
class Skiz_RowStack(RK_RowStack):
    pass
class Pagat_RowStack(RK_RowStack):
    pass
class TrumpWild_RowStack(Tarock_OpenStack):
    pass
class TrumpOnly_RowStack(Tarock_OpenStack):
    pass
class Excuse_RowStack(Tarock_OpenStack):
    pass
class WheelOfFortune_RowStack(Tarock_OpenStack):
    pass
class Ponytail_PonytailStack(Braid_BraidStack):
    pass
class Ponytail_RowStack(Braid_RowStack):
    pass
class Ponytail_ReserveStack(Braid_ReserveStack):
    pass
class Cavalier_RowStack(Tarock_AC_RowStack):
    pass
class Nasty_RowStack(SS_RowStack):
    pass
class Tarock_GameMethods:
    pass
class AbstractTarockGame(Tarock_GameMethods, Game):
    pass
class WheelOfFortune(AbstractTarockGame):
    pass
class ImperialTrumps(AbstractTarockGame):
    pass
class Pagat(AbstractTarockGame):
    pass
class Skiz(AbstractTarockGame):
    pass
class FifteenPlus(AbstractTarockGame):
    pass
class Excuse(AbstractTarockGame):
    pass
class Grasshopper(AbstractTarockGame):
    pass
class DoubleGrasshopper(Grasshopper):
    pass
class Ponytail(Tarock_GameMethods, Braid):
    pass
class Cavalier(AbstractTarockGame):
    pass
class FiveAces(Cavalier):
    pass
class Wicked(FiveAces):
    pass
class Nasty(Wicked):
    pass
class Dashavatara_FoundationStack(AbstractFoundationStack):
    pass
class Journey_Foundation(AbstractFoundationStack):
    pass
class AppachansWaterfall_Foundation(AbstractFoundationStack):
    pass
class Dashavatara_OpenStack(OpenStack):
    pass
class Dashavatara_AC_RowStack(Dashavatara_OpenStack):
    pass
class Dashavatara_AF_RowStack(Dashavatara_OpenStack):
    pass
class Dashavatara_RK_RowStack(Dashavatara_OpenStack):
    pass
class Dashavatara_SS_RowStack(Dashavatara_OpenStack):
    pass
class Circles_RowStack(SS_RowStack):
    pass
class Journey_BraidStack(OpenStack):
    pass
class Journey_StrongStack(ReserveStack):
    pass
class Journey_WeakStack(ReserveStack):
    pass
class Journey_ReserveStack(ReserveStack):
    pass
class AppachansWaterfall_RowStack(RK_RowStack):
    pass
class Dashavatara_TableauStack(Dashavatara_OpenStack):
    pass
class Dashavatara_ReserveStack(ReserveStack):
    pass
class Dashavatara_RowStack(BasicRowStack):
    pass
class AbstractDashavataraGame(Game):
    pass
class Journey_Hint(DefaultHint):
    pass
class DashavataraCircles(AbstractDashavataraGame):
    pass
class TenAvatars(AbstractDashavataraGame):
    pass
class Balarama(AbstractDashavataraGame):
    pass
class Hayagriva(Balarama):
    pass
class Shanka(Balarama):
    pass
class Surukh(Balarama):
    pass
class Matsya(AbstractDashavataraGame):
    pass
class Kurma(Matsya):
    pass
class Varaha(Matsya):
    pass
class Narasimha(Matsya):
    pass
class Vamana(Matsya):
    pass
class Parashurama(Matsya):
    pass
class Journey(AbstractDashavataraGame):
    pass
class LongJourney(Journey):
    pass
class AppachansWaterfall(AbstractDashavataraGame):
    pass
class Hiranyaksha(AbstractDashavataraGame):
    pass
class Dashavatara_Hint(AbstractHint):
    pass
class Dashavatara(Game):
    pass
class AbstractFlowerGame(Game):
    pass
class Flower_OpenStack(OpenStack):
    pass
class FlowerClock(AbstractFlowerGame):
    pass
class Gaji(AbstractFlowerGame):
    pass
class Oonsoo(AbstractFlowerGame):
    pass
class OonsooToo(Oonsoo):
    pass
class OonsooStrict(Oonsoo):
    pass
class OonsooOpen(Oonsoo):
    pass
class OonsooTimesTwo(Oonsoo):
    pass
class Pagoda(AbstractFlowerGame):
    pass
class MatsuKiri(AbstractFlowerGame):
    pass
class MatsuKiriStrict(MatsuKiri):
    pass
class GreatWall(AbstractFlowerGame):
    pass
class FourWinds(AbstractFlowerGame):
    pass
class Sumo(AbstractFlowerGame):
    pass
class BigSumo(AbstractFlowerGame):
    pass
class Samuri(AbstractFlowerGame):
    pass
class DoubleSamuri(Samuri):
    pass
class SuperSamuri(DoubleSamuri):
    pass
class LittleEasy(AbstractFlowerGame):
    pass
class EasyX1(LittleEasy):
    pass
class Relax(EasyX1):
    pass
class BigEasy(LittleEasy):
    pass
class EasySupreme(LittleEasy):
    pass
class JustForFun(AbstractFlowerGame):
    pass
class DoubleYourFun(JustForFun):
    pass
class Firecracker(JustForFun):
    pass
class CherryBomb(Firecracker):
    pass
class Paulownia(AbstractFlowerGame):
    pass
class Paulownia(AbstractFlowerGame):
    pass
class Pine(Paulownia):
    pass
class Eularia(Paulownia):
    pass
class Peony(Eularia):
    pass
class Iris(Peony):
    pass
class LesserQueue(AbstractFlowerGame):
    pass
class GreaterQueue(LesserQueue):
    pass
class JapaneseGarden(AbstractFlowerGame):
    pass
class JapaneseGardenII(JapaneseGarden):
    pass
class JapaneseGardenIII(JapaneseGardenII):
    pass
class SixSages(JapaneseGarden):
    pass
class SixTengus(SixSages):
    pass
class HanafudaFourSeasons(AbstractFlowerGame):
    pass
class Wisteria(AbstractFlowerGame):
    pass
class FlowerArrangement_Hint(AbstractHint):
    pass
class FlowerArrangement_TableauStack(Flower_OpenStack):
    pass
class FlowerArrangement_RowStack(BasicRowStack):
    pass
class FlowerArrangement(Game):
    pass
class Queue_Hint(DefaultHint):
    pass
class Flower_FoundationStack(AbstractFoundationStack):
    pass
class Hanafuda_SS_FoundationStack(Flower_FoundationStack):
    pass
class FlowerClock_Foundation(Flower_FoundationStack):
    pass
class Gaji_Foundation(Flower_FoundationStack):
    pass
class Pagoda_Foundation(Flower_FoundationStack):
    pass
class MatsuKiri_Foundation(Flower_FoundationStack):
    pass
class GreatWall_FoundationStack(Flower_FoundationStack):
    pass
class FourWinds_Foundation(Flower_FoundationStack):
    pass
class Queue_Foundation(AbstractFoundationStack):
    pass
class Hanafuda_SequenceStack(Flower_OpenStack):
    pass
class Oonsoo_SequenceStack(Flower_OpenStack):
    pass
class FlowerClock_RowStack(Flower_OpenStack):
    pass
class Gaji_RowStack(Flower_OpenStack):
    pass
class Matsukiri_RowStack(Flower_OpenStack):
    pass
class Samuri_RowStack(Flower_OpenStack):
    pass
class GreatWall_RowStack(Flower_OpenStack):
    pass
class FourWinds_RowStack(Flower_OpenStack):
    pass
class Queue_BraidStack(OpenStack):
    pass
class Queue_RowStack(ReserveStack):
    pass
class Queue_ReserveStack(ReserveStack):
    pass
class JapaneseGarden_RowStack(Flower_OpenStack):
    pass
class HanafudaRK_RowStack(Flower_OpenStack):
    pass
class HexADeck_FoundationStack(SS_FoundationStack):
    pass
class HexATrump_Foundation(HexADeck_FoundationStack):
    pass
class Merlins_Foundation(AbstractFoundationStack):
    pass
class HexADeck_OpenStack(OpenStack):
    pass
class HexADeck_RK_RowStack(HexADeck_OpenStack):
    pass
class HexADeck_AC_RowStack(HexADeck_OpenStack):
    pass
class HexADeck_SS_RowStack(HexADeck_OpenStack):
    pass
class Bits_RowStack(ReserveStack):
    pass
class Bytes_RowStack(ReserveStack):
    pass
class HexAKlon_RowStack(AC_RowStack):
    pass
class HexADeck_ACRowStack(AC_RowStack):
    pass
class Familiar_ReserveStack(ReserveStack):
    pass
class Merlins_BraidStack(OpenStack):
    pass
class Merlins_RowStack(ReserveStack):
    pass
class Merlins_ReserveStack(ReserveStack):
    pass
class AbstractHexADeckGame(Game):
    pass
class Merlins_Hint(DefaultHint):
    pass
class BitsNBytes(Game):
    pass
class HexAKlon(Game):
    pass
class HexAKlonByThrees(Game):
    pass
class KingOnlyHexAKlon(Game):
    pass
class KlondikePlus16(Game):
    pass
class TheFamiliar(Game):
    pass
class TwoFamiliars(Game):
    pass
class TenByEight(Game):
    pass
class Drawbridge(Game):
    pass
class DoubleDrawbridge(Game):
    pass
class HiddenPassages(Game):
    pass
class CluitjarsLair(Game):
    pass
class MerlinsMeander(AbstractHexADeckGame):
    pass
class MagesGame(Game):
    pass
class Convolution(AbstractHexADeckGame):
    pass
class Labyrinth(Convolution):
    pass
class Snakestone(Convolution):
    pass
class DojoujisGame_Talon(LarasGame_Talon):
    pass
class DoubleKalisGame_Talon(LarasGame_Talon):
    pass
class BridgetsGame_Reserve(OpenStack):
    pass
class KatrinasGame(LarasGame):
    pass
class RelaxedKatrinasGame(KatrinasGame):
    pass
class DoubleKatrinasGame(RelaxedKatrinasGame):
    pass
class BridgetsGame(LarasGame):
    pass
class DoubleBridgetsGame(BridgetsGame):
    pass
class FatimehsGame(LarasGame):
    pass
class RelaxedFatimehsGame(FatimehsGame):
    pass
class KalisGame(FatimehsGame):
    pass
class RelaxedKalisGame(KalisGame):
    pass
class DoubleKalisGame(RelaxedKalisGame):
    pass
class DojoujisGame(LarasGame):
    pass
class DoubleDojoujisGame(DojoujisGame):
    pass
class Matrix_RowStack(OpenStack):
    pass
class Matrix3(Game):
    pass
class Matrix4(Matrix3):
    pass
class Matrix5(Matrix3):
    pass
class Matrix6(Matrix3):
    pass
class Matrix7(Matrix3):
    pass
class Matrix8(Matrix3):
    pass
class Matrix9(Matrix3):
    pass
class Matrix10(Matrix3):
    pass
class Matrix20(Matrix3):
    pass
class Mughal_FoundationStack(AbstractFoundationStack):
    pass
class Triumph_Foundation(AbstractFoundationStack):
    pass
class Mughal_OpenStack(OpenStack):
    pass
class Mughal_AC_RowStack(Mughal_OpenStack):
    pass
class Mughal_AF_RowStack(Mughal_OpenStack):
    pass
class Mughal_RK_RowStack(Mughal_OpenStack):
    pass
class Mughal_SS_RowStack(Mughal_OpenStack):
    pass
class Circles_RowStack(SS_RowStack):
    pass
class Triumph_BraidStack(OpenStack):
    pass
class Triumph_StrongStack(ReserveStack):
    pass
class Triumph_WeakStack(ReserveStack):
    pass
class Triumph_ReserveStack(ReserveStack):
    pass
class AbstractMughalGame(Game):
    pass
class Triumph_Hint(DefaultHint):
    pass
class MughalCircles(AbstractMughalGame):
    pass
class EightLegions(AbstractMughalGame):
    pass
class Shamsher(AbstractMughalGame):
    pass
class Ashrafi(Shamsher):
    pass
class Ghulam(Shamsher):
    pass
class Tipati(AbstractMughalGame):
    pass
class Ashwapati(Tipati):
    pass
class Gajapati(Tipati):
    pass
class Narpati(Tipati):
    pass
class Garhpati(Tipati):
    pass
class Dhanpati(Tipati):
    pass
class AkbarsTriumph(AbstractMughalGame):
    pass
class AkbarsConquest(AkbarsTriumph):
    pass
class Vajra(AbstractMughalGame):
    pass
class Danda(Vajra):
    pass
class Khadga(Vajra):
    pass
class Makara(Vajra):
    pass
class Dikapala_TableauStack(Mughal_OpenStack):
    pass
class Dikapala_ReserveStack(ReserveStack):
    pass
class Dikapala_RowStack(BasicRowStack):
    pass
class Dikapala_Hint(AbstractHint):
    pass
class AshtaDikapala(Game):
    pass
class Tarock_OpenStack(OpenStack):
    pass
class Tarock_RK_RowStack(Tarock_OpenStack):
    pass
class Tarock_SS_RowStack(Tarock_OpenStack):
    pass
class Tarock_AC_RowStack(Tarock_OpenStack):
    pass
class Cockroach(Grasshopper):
    pass
class DoubleCockroach(Grasshopper):
    pass
class Corkscrew(AbstractTarockGame):
    pass
class Serpent(Corkscrew):
    pass
class Rambling(Corkscrew):
    pass
class LeGrandeTeton(ThreePeaksNoScore):
    pass


def registerAll():
    
    registerGame(GameInfo(903, AcesUp, "Aces Up",                   # was: 52
                          STYLE.ONE_DECK_TYPE, 1, 0, SKILL.LUCK, altnames=("Aces High", "Drivel") ))
    registerGame(GameInfo(206, Fortunes, "Fortunes",
                          STYLE.ONE_DECK_TYPE, 1, 0, SKILL.LUCK))
    registerGame(GameInfo(213, RussianAces, "Russian Aces",
                          STYLE.ONE_DECK_TYPE, 1, 0, SKILL.LUCK))
    registerGame(GameInfo(130, PerpetualMotion, "Perpetual Motion",
                          STYLE.ONE_DECK_TYPE, 1, -1, SKILL.MOSTLY_LUCK,
                          altnames="First Law"))
    registerGame(GameInfo(353, AcesUp5, "Aces Up 5",
                          STYLE.ONE_DECK_TYPE, 1, 0, SKILL.LUCK))
    registerGame(GameInfo(552, Cover, "Cover",
                          STYLE.ONE_DECK_TYPE, 1, 0, SKILL.LUCK))
    registerGame(GameInfo(583, FiringSquad, "Firing Squad",
                          STYLE.ONE_DECK_TYPE, 1, 0, SKILL.BALANCED))
    registerGame(GameInfo(684, Deck, "Deck",
                          STYLE.ONE_DECK_TYPE, 1, 0, SKILL.LUCK))
    registerGame(GameInfo(756, TabbyCat, "Tabby Cat",
                          STYLE.ONE_DECK_TYPE, 1, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(757, Manx, "Manx",
                          STYLE.ONE_DECK_TYPE, 1, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(758, MaineCoon, "Maine Coon",
                          STYLE.TWO_DECK_TYPE, 2, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(321, Carthage, "Carthage",
                          STYLE.TWO_DECK_TYPE, 2, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(322, AlgerianPatience, "Algerian Patience",
                          STYLE.TWO_DECK_TYPE, 2, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(457, AlgerianPatience3, "Algerian Patience (3 decks)",
                          STYLE.THREE_DECK_TYPE | STYLE.ORIGINAL, 3, 0, SKILL.MOSTLY_SKILL))

    registerGame(GameInfo(172, TamOShanter, "Tam O'Shanter",
                          STYLE.NUMERICA, 1, 0, SKILL.LUCK))
    registerGame(GameInfo(95, AuldLangSyne, "Auld Lang Syne",
                          STYLE.NUMERICA, 1, 0, SKILL.LUCK,
                          altnames=("Patience",) ))
    registerGame(GameInfo(173, Strategy, "Strategy",
                          STYLE.NUMERICA, 1, 0, SKILL.SKILL))
    registerGame(GameInfo(123, Interregnum, "Interregnum",
                          STYLE.NUMERICA, 2, 0, SKILL.BALANCED))
    registerGame(GameInfo(296, Colorado, "Colorado",
                          STYLE.NUMERICA, 2, 0, SKILL.BALANCED))
    registerGame(GameInfo(406, Amazons, "Amazons",
                          STYLE.NUMERICA, 1, -1, SKILL.LUCK,
                          ranks=(0, 6, 7, 8, 9, 10, 11),
                          ))
    registerGame(GameInfo(490, Acquaintance, "Acquaintance",
                          STYLE.NUMERICA, 1, 2, SKILL.BALANCED))
    registerGame(GameInfo(553, Scuffle, "Scuffle",
                          STYLE.NUMERICA, 1, 2, SKILL.MOSTLY_LUCK))
    registerGame(GameInfo(560, DoubleAcquaintance, "Double Acquaintance",
                          STYLE.NUMERICA, 2, 2, SKILL.BALANCED))
    registerGame(GameInfo(569, Primrose, "Primrose",
                          STYLE.NUMERICA, 2, 8, SKILL.BALANCED))
    registerGame(GameInfo(636, StrategyPlus, "Strategy +",
                          STYLE.NUMERICA, 1, 0, SKILL.SKILL))
    registerGame(GameInfo(688, Formic, "Formic",
                          STYLE.NUMERICA, 1, 0, SKILL.MOSTLY_SKILL))

    registerGame(GameInfo(83, CastlesInSpain, "Castles in Spain",
                          STYLE.BAKERS_DOZEN, 1, 0, SKILL.BALANCED))
    registerGame(GameInfo(84, Martha, "Martha",
                          STYLE.BAKERS_DOZEN, 1, 0, SKILL.BALANCED))
    registerGame(GameInfo(31, BakersDozen, "Baker's Dozen",
                          STYLE.BAKERS_DOZEN | STYLE.OPEN, 1, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(85, SpanishPatience, "Spanish Patience",
                          STYLE.BAKERS_DOZEN | STYLE.OPEN, 1, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(86, GoodMeasure, "Good Measure",
                          STYLE.BAKERS_DOZEN | STYLE.OPEN, 1, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(104, Cruel, "Cruel",
                          STYLE.BAKERS_DOZEN | STYLE.OPEN, 1, -1, SKILL.BALANCED))
    registerGame(GameInfo(291, RoyalFamily, "Royal Family",
                          STYLE.BAKERS_DOZEN | STYLE.OPEN, 1, 1, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(308, PortugueseSolitaire, "Portuguese Solitaire",
                          STYLE.BAKERS_DOZEN | STYLE.OPEN, 1, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(404, Perseverance, "Perseverance",
                          STYLE.BAKERS_DOZEN | STYLE.OPEN, 1, 2, SKILL.BALANCED))
    registerGame(GameInfo(369, RippleFan, "Ripple Fan",
                          STYLE.BAKERS_DOZEN, 1, -1, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(515, Indefatigable, "Indefatigable",
                          STYLE.BAKERS_DOZEN | STYLE.OPEN, 1, 2, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(664, SpanishPatienceII, "Spanish Patience II",
                          STYLE.BAKERS_DOZEN | STYLE.OPEN, 1, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(45, BakersGame, "Baker's Game",
                          STYLE.FREECELL | STYLE.OPEN, 1, 0, SKILL.SKILL))
    registerGame(GameInfo(26, KingOnlyBakersGame, "King Only Baker's Game",
                          STYLE.FREECELL | STYLE.OPEN, 1, 0, SKILL.SKILL))
    registerGame(GameInfo(258, EightOff, "Eight Off",
                          STYLE.FREECELL | STYLE.OPEN, 1, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(9, SeahavenTowers, "Seahaven Towers",
                          STYLE.FREECELL | STYLE.OPEN, 1, 0, SKILL.SKILL,
                          altnames=("Sea Towers", "Towers") ))
    registerGame(GameInfo(6, RelaxedSeahavenTowers, "Relaxed Seahaven Towers",
                          STYLE.FREECELL | STYLE.RELAXED | STYLE.OPEN, 1, 0, SKILL.SKILL))
    registerGame(GameInfo(64, Penguin, "Penguin",
                          STYLE.FREECELL | STYLE.OPEN, 1, 0, SKILL.MOSTLY_SKILL,
                          altnames=("Beak and Flipper",) ))
    registerGame(GameInfo(427, Opus, "Opus",
                          STYLE.FREECELL | STYLE.OPEN, 1, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(629, Tuxedo, "Tuxedo",
                          STYLE.FREECELL | STYLE.OPEN, 1, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(713, Flipper, "Flipper",
                          STYLE.FREECELL | STYLE.ORIGINAL, 1, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(146, StreetsAndAlleys, "Streets and Alleys",
                          STYLE.BELEAGUERED_CASTLE | STYLE.OPEN, 1, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(34, BeleagueredCastle, "Beleaguered Castle",
                          STYLE.BELEAGUERED_CASTLE | STYLE.OPEN, 1, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(145, Citadel, "Citadel",
                          STYLE.BELEAGUERED_CASTLE | STYLE.OPEN, 1, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(147, Fortress, "Fortress",
                          STYLE.BELEAGUERED_CASTLE | STYLE.OPEN, 1, 0, SKILL.SKILL))
    registerGame(GameInfo(148, Chessboard, "Chessboard",
                          STYLE.BELEAGUERED_CASTLE | STYLE.OPEN, 1, 0, SKILL.SKILL))
    registerGame(GameInfo(300, Stronghold, "Stronghold",
                          STYLE.BELEAGUERED_CASTLE | STYLE.OPEN, 1, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(301, Fastness, "Fastness",
                          STYLE.BELEAGUERED_CASTLE | STYLE.OPEN | STYLE.ORIGINAL, 1, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(306, Zerline, "Zerline",
                          STYLE.BELEAGUERED_CASTLE, 2, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(324, Bastion, "Bastion",
                          STYLE.BELEAGUERED_CASTLE | STYLE.OPEN, 1, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(325, TenByOne, "Ten by One",
                          STYLE.BELEAGUERED_CASTLE | STYLE.OPEN, 1, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(351, Chequers, "Chequers",
                          STYLE.BELEAGUERED_CASTLE, 2, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(393, CastleOfIndolence, "Castle of Indolence",
                          STYLE.BELEAGUERED_CASTLE, 2, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(395, Zerline3Decks, "Zerline (3 decks)",
                          STYLE.BELEAGUERED_CASTLE | STYLE.ORIGINAL, 3, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(400, Rittenhouse, "Rittenhouse",
                          STYLE.BELEAGUERED_CASTLE | STYLE.OPEN, 2, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(507, Lightweight, "Lightweight",
                          STYLE.BELEAGUERED_CASTLE | STYLE.OPEN | STYLE.ORIGINAL, 2, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(508, CastleMount, "Castle Mount",
                          STYLE.BELEAGUERED_CASTLE | STYLE.OPEN, 3, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(524, SelectiveCastle, "Selective Castle",
                          STYLE.BELEAGUERED_CASTLE | STYLE.OPEN, 1, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(535, ExiledKings, "Exiled Kings",
                          STYLE.BELEAGUERED_CASTLE | STYLE.OPEN, 1, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(626, Soother, "Soother",
                          STYLE.FOUR_DECK_TYPE | STYLE.ORIGINAL, 4, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(650, CastlesEnd, "Castles End",
                          STYLE.BELEAGUERED_CASTLE | STYLE.OPEN, 1, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(665, PenelopesWeb, "Penelope's Web",
                          STYLE.BELEAGUERED_CASTLE | STYLE.OPEN, 1, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(290, Bisley, "Bisley",
                          STYLE.ONE_DECK_TYPE | STYLE.OPEN, 1, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(372, DoubleBisley, "Double Bisley",
                          STYLE.TWO_DECK_TYPE | STYLE.OPEN | STYLE.ORIGINAL, 2, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(373, Gloria, "Gloria",
                          STYLE.TWO_DECK_TYPE | STYLE.OPEN | STYLE.ORIGINAL, 2, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(374, Realm, "Realm",
                          STYLE.ONE_DECK_TYPE | STYLE.OPEN | STYLE.ORIGINAL, 1, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(375, Mancunian, "Mancunian",
                          STYLE.ONE_DECK_TYPE | STYLE.OPEN | STYLE.ORIGINAL, 1, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(686, HospitalPatience, "Hospital Patience",
                          STYLE.ONE_DECK_TYPE, 1, -1, SKILL.MOSTLY_LUCK))
    registerGame(GameInfo(692, BoardPatience, "Board Patience",
                          STYLE.ONE_DECK_TYPE | STYLE.OPEN, 1, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(747, Cringle, "Cringle",
                          STYLE.TWO_DECK_TYPE | STYLE.ORIGINAL, 2, 0, SKILL.BALANCED))

    registerGame(GameInfo(12, Braid, "Braid",
                          STYLE.NAPOLEON, 2, 2, SKILL.BALANCED,
                          altnames=("Der Zopf", "Plait", "Pigtail") ))
    registerGame(GameInfo(175, LongBraid, "Long Braid",
                          STYLE.NAPOLEON, 2, 2, SKILL.BALANCED,
                          altnames=("Der lange Zopf",) ))
    registerGame(GameInfo(358, Fort, "Fort",
                          STYLE.NAPOLEON, 2, 2, SKILL.BALANCED))
    registerGame(GameInfo(376, Backbone, "Backbone",
                          STYLE.NAPOLEON, 2, 0, SKILL.BALANCED))
    registerGame(GameInfo(377, BackbonePlus, "Backbone +",
                          STYLE.NAPOLEON, 2, 0, SKILL.BALANCED))
    registerGame(GameInfo(510, BigBraid, "Big Braid",
                          STYLE.NAPOLEON | STYLE.ORIGINAL, 3, 2, SKILL.BALANCED))
    registerGame(GameInfo(694, Casket, "Casket",
                          STYLE.TWO_DECK_TYPE, 2, 0, SKILL.BALANCED))
    registerGame(GameInfo(717, Well, "Well",
                          STYLE.TWO_DECK_TYPE, 2, 4, SKILL.BALANCED))
    registerGame(GameInfo(42, Bristol, "Bristol",
                          STYLE.FAN_TYPE, 1, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(214, Belvedere, "Belvedere",
                          STYLE.FAN_TYPE, 1, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(266, Dover, "Dover",
                          STYLE.FAN_TYPE, 2, 0, SKILL.BALANCED))
    registerGame(GameInfo(425, NewYork, "New York",
                          STYLE.FAN_TYPE, 2, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(468, Spike, "Spike",
                          STYLE.KLONDIKE, 1, 0, SKILL.BALANCED))
    registerGame(GameInfo(519, Gotham, "Gotham",
                          STYLE.FAN_TYPE, 2, 0, SKILL.BALANCED))
    registerGame(GameInfo(604, Interment, "Interment",
                          STYLE.FAN_TYPE, 2, 0, SKILL.BALANCED))

    registerGame(GameInfo(338, BuffaloBill, "Buffalo Bill",
                          STYLE.TWO_DECK_TYPE, 2, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(421, LittleBillie, "Little Billie",
                          STYLE.TWO_DECK_TYPE, 2, 0, SKILL.MOSTLY_SKILL))


    registerGame(GameInfo(256, Calculation, "Calculation",
                          STYLE.ONE_DECK_TYPE, 1, 0, SKILL.MOSTLY_SKILL,
                          altnames=("Progression",) ))
    registerGame(GameInfo(94, Hopscotch, "Hopscotch",
                          STYLE.ONE_DECK_TYPE, 1, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(134, BetsyRoss, "Betsy Ross",
                          STYLE.ONE_DECK_TYPE, 1, 2, SKILL.MOSTLY_LUCK,
                          altnames=("Fairest", "Four Kings", "Musical Patience",
                                    "Quadruple Alliance", "Plus Belle") ))
    registerGame(GameInfo(550, One234, "One234",
                          STYLE.ONE_DECK_TYPE | STYLE.OPEN, 1, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(653, SeniorWrangler, "Senior Wrangler",
                          STYLE.TWO_DECK_TYPE, 2, 8, SKILL.BALANCED))
    registerGame(GameInfo(704, SPatience, "S Patience",
                          STYLE.TWO_DECK_TYPE, 2, 0, SKILL.BALANCED))

    registerGame(GameInfo(280, Camelot, "Camelot",
                          STYLE.ONE_DECK_TYPE, 1, 0, SKILL.BALANCED))
    registerGame(GameInfo(610, SlyFox, "Sly Fox",
                          STYLE.NUMERICA, 2, 0, SKILL.BALANCED))
    registerGame(GameInfo(614, OpenSlyFox, "Open Sly Fox",
                          STYLE.NUMERICA | STYLE.ORIGINAL, 2, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(623, PrincessPatience, "Princess Patience",
                          STYLE.TWO_DECK_TYPE, 2, 0, SKILL.BALANCED))
    registerGame(GameInfo(622, GrandmammasPatience, "Grandmamma's Patience",
                          STYLE.NUMERICA, 2, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(702, DoubleLine, "Double Line",
                          STYLE.NUMERICA, 2, 0, SKILL.BALANCED))


    registerGame(GameInfo(105, Canfield, "Canfield",                # was: 262
                          STYLE.CANFIELD | STYLE.CONTRIB, 1, -1, SKILL.BALANCED))
    registerGame(GameInfo(101, SuperiorCanfield, "Superior Canfield",
                          STYLE.CANFIELD, 1, -1, SKILL.BALANCED))
    registerGame(GameInfo(99, Rainfall, "Rainfall",
                          STYLE.CANFIELD | STYLE.ORIGINAL, 1, 2, SKILL.BALANCED))
    registerGame(GameInfo(108, Rainbow, "Rainbow",
                          STYLE.CANFIELD, 1, 0, SKILL.BALANCED))
    registerGame(GameInfo(100, Storehouse, "Storehouse",
                          STYLE.CANFIELD, 1, 2, SKILL.BALANCED,
                          altnames=("Provisions", "Straight Up", "Thirteen Up") ))
    registerGame(GameInfo(43, Chameleon, "Chameleon",
                          STYLE.CANFIELD, 1, 0, SKILL.BALANCED,
                          altnames="Kansas"))
    registerGame(GameInfo(106, DoubleCanfield, "Double Canfield",   # was: 22
                          STYLE.CANFIELD, 2, -1, SKILL.BALANCED))
    registerGame(GameInfo(103, AmericanToad, "American Toad",
                          STYLE.CANFIELD, 2, 1, SKILL.BALANCED))
    registerGame(GameInfo(102, VariegatedCanfield, "Variegated Canfield",
                          STYLE.CANFIELD, 2, 2, SKILL.BALANCED))
    registerGame(GameInfo(112, EagleWing, "Eagle Wing",
                          STYLE.CANFIELD, 1, 2, SKILL.BALANCED))
    registerGame(GameInfo(315, Gate, "Gate",
                          STYLE.CANFIELD, 1, 0, SKILL.BALANCED))
    registerGame(GameInfo(316, LittleGate, "Little Gate",
                          STYLE.CANFIELD, 1, 0, SKILL.BALANCED))
    registerGame(GameInfo(360, Munger, "Munger",
                          STYLE.CANFIELD, 1, 0, SKILL.BALANCED))
    registerGame(GameInfo(396, TripleCanfield, "Triple Canfield",
                          STYLE.CANFIELD, 3, -1, SKILL.BALANCED))
    registerGame(GameInfo(403, Acme, "Acme",
                          STYLE.CANFIELD, 1, 1, SKILL.BALANCED))
    registerGame(GameInfo(413, Duke, "Duke",
                          STYLE.CANFIELD, 1, 2, SKILL.BALANCED))
    registerGame(GameInfo(422, Minerva, "Minerva",
                          STYLE.CANFIELD, 1, 1, SKILL.BALANCED))
    registerGame(GameInfo(476, Demon, "Demon",
                          STYLE.CANFIELD, 2, -1, SKILL.BALANCED))
    registerGame(GameInfo(494, Mystique, "Mystique",
                          STYLE.CANFIELD, 1, 0, SKILL.BALANCED))
    registerGame(GameInfo(521, CanfieldRush, "Canfield Rush",
                          STYLE.CANFIELD, 1, 2, SKILL.BALANCED))
    registerGame(GameInfo(527, Doorway, "Doorway",
                          STYLE.KLONDIKE, 1, 0, SKILL.BALANCED,
                          altnames=('Solstice',) ))
    registerGame(GameInfo(605, Skippy, "Skippy",
                          STYLE.FAN_TYPE, 2, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(642, Lafayette, "Lafayette",
                          STYLE.CANFIELD, 1, -1, SKILL.BALANCED))

    registerGame(GameInfo(292, Capricieuse, "Capricieuse",
                          STYLE.BAKERS_DOZEN | STYLE.OPEN, 2, 2, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(293, Nationale, "Nationale",
                          STYLE.BAKERS_DOZEN | STYLE.OPEN, 2, 0, SKILL.MOSTLY_SKILL,
                          altnames=('Zigzag Course',) ))
    registerGame(GameInfo(606, Strata, "Strata",
                          STYLE.BAKERS_DOZEN | STYLE.OPEN, 2, 2, SKILL.MOSTLY_SKILL,
                          ranks=(0, 6, 7, 8, 9, 10, 11, 12),
                          altnames=('Persian Patience',) ))
    registerGame(GameInfo(673, Fifteen, "Fifteen",
                          STYLE.BAKERS_DOZEN | STYLE.OPEN, 2, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(755, Choice, "Choice",
                          STYLE.THREE_DECK_TYPE | STYLE.OPEN | STYLE.ORIGINAL, 3, 0, SKILL.MOSTLY_SKILL,
                          ranks=(5, 6, 7, 8, 9, 10, 11, 12) ))

    registerGame(GameInfo(294, CurdsAndWhey, "Curds and Whey",
                          STYLE.SPIDER | STYLE.OPEN, 1, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(311, Dumfries, "Dumfries",
                          STYLE.ONE_DECK_TYPE, 1, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(312, Galloway, "Galloway",
                          STYLE.ONE_DECK_TYPE, 1, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(313, Robin, "Robin",
                          STYLE.TWO_DECK_TYPE | STYLE.ORIGINAL, 2, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(348, Arachnida, "Arachnida",
                          STYLE.SPIDER, 2, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(349, MissMuffet, "Miss Muffet",
                          STYLE.SPIDER | STYLE.OPEN, 1, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(352, Nordic, "Nordic",
                          STYLE.SPIDER | STYLE.OPEN | STYLE.ORIGINAL, 1, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(414, GermanPatience, "German Patience",
                          STYLE.TWO_DECK_TYPE, 2, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(415, BavarianPatience, "Bavarian Patience",
                          STYLE.TWO_DECK_TYPE, 2, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(480, TrustyTwelve, "Trusty Twelve",
                          STYLE.ONE_DECK_TYPE, 1, 0, SKILL.BALANCED))
    registerGame(GameInfo(481, KnottyNines, "Knotty Nines",
                          STYLE.ONE_DECK_TYPE, 1, 0, SKILL.BALANCED))
    registerGame(GameInfo(482, SweetSixteen, "Sweet Sixteen",
                          STYLE.ONE_DECK_TYPE, 1, 0, SKILL.BALANCED))
    registerGame(GameInfo(534, Harvestman, "Harvestman",
                          STYLE.SPIDER | STYLE.ORIGINAL, 2, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(687, Glacier, "Glacier",
                          STYLE.TWO_DECK_TYPE, 2, 0, SKILL.BALANCED))
    registerGame(GameInfo(724, EightPacks, "Eight Packs",
                          STYLE.TWO_DECK_TYPE | STYLE.ORIGINAL, 2, 2, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(762, FourPacks, "Four Packs",
                          STYLE.TWO_DECK_TYPE, 2, 1, SKILL.MOSTLY_SKILL))


    registerGame(GameInfo(120, DieBoeseSieben, "Bad Seven",
                          STYLE.TWO_DECK_TYPE, 2, 1, SKILL.MOSTLY_LUCK,
                          ranks=(0, 6, 7, 8, 9, 10, 11, 12),
                          altnames=("Die boese Sieben",) ))

    registerGame(GameInfo(149, Diplomat, "Diplomat",
                          STYLE.FORTY_THIEVES, 2, 0, SKILL.BALANCED))
    registerGame(GameInfo(151, LadyPalk, "Lady Palk",
                          STYLE.FORTY_THIEVES, 2, 0, SKILL.BALANCED))
    registerGame(GameInfo(150, Congress, "Congress",
                          STYLE.FORTY_THIEVES, 2, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(433, RowsOfFour, "Rows of Four",
                          STYLE.FORTY_THIEVES, 2, 2, SKILL.BALANCED))
    registerGame(GameInfo(485, Dieppe, "Dieppe",
                          STYLE.FORTY_THIEVES, 2, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(489, LittleNapoleon, "Little Napoleon",
                          STYLE.FORTY_THIEVES, 2, 0, SKILL.BALANCED))
    registerGame(GameInfo(548, Parliament, "Parliament",
                          STYLE.FORTY_THIEVES, 2, 0, SKILL.BALANCED))
    registerGame(GameInfo(549, Wheatsheaf, "Wheatsheaf",
                          STYLE.FORTY_THIEVES, 2, 0, SKILL.BALANCED))
    registerGame(GameInfo(563, TwinQueens, "Twin Queens",
                          STYLE.FORTY_THIEVES, 2, 1, SKILL.MOSTLY_SKILL))

    registerGame(GameInfo(111, Doublets, "Doublets",
                          STYLE.ONE_DECK_TYPE, 1, 2, SKILL.MOSTLY_LUCK,
                          altnames=('Double or Quits',) ))

    registerGame(GameInfo(16, EiffelTower, "Eiffel Tower",
                          STYLE.PAIRING_TYPE, 2, 0, SKILL.MOSTLY_LUCK))
    ##registerGame(GameInfo(801, StrictEiffelTower, "Strict Eiffel Tower",
    ##                      STYLE.PAIRING_TYPE, 2, 0))

    registerGame(GameInfo(56, FanGame, "Fan",
                          STYLE.FAN_TYPE | STYLE.OPEN, 1, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(87, ScotchPatience, "Scotch Patience",
                          STYLE.FAN_TYPE | STYLE.OPEN, 1, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(57, Shamrocks, "Shamrocks",
                          STYLE.FAN_TYPE | STYLE.OPEN, 1, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(901, LaBelleLucie, "La Belle Lucie",      # was: 32, 82
                          STYLE.FAN_TYPE | STYLE.OPEN, 1, 2, SKILL.MOSTLY_SKILL,
                          altnames=("Fair Lucy", "Midnight Oil") ))
    registerGame(GameInfo(132, SuperFlowerGarden, "Super Flower Garden",
                          STYLE.FAN_TYPE | STYLE.OPEN, 1, 2, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(128, ThreeShufflesAndADraw, "Three Shuffles and a Draw",
                          STYLE.FAN_TYPE | STYLE.OPEN, 1, 2, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(88, Trefoil, "Trefoil",
                          STYLE.FAN_TYPE | STYLE.OPEN, 1, 2, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(227, Intelligence, "Intelligence",
                          STYLE.FAN_TYPE, 2, 2, SKILL.BALANCED))
    registerGame(GameInfo(340, IntelligencePlus, "Intelligence +",
                          STYLE.FAN_TYPE, 2, 2, SKILL.BALANCED))
    registerGame(GameInfo(268, HouseInTheWood, "House in the Wood",
                          STYLE.FAN_TYPE | STYLE.OPEN, 2, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(317, HouseOnTheHill, "House on the Hill",
                          STYLE.FAN_TYPE | STYLE.OPEN, 2, 0, SKILL.MOSTLY_SKILL,
                          rules_filename='houseinthewood.html'))
    registerGame(GameInfo(320, CloverLeaf, "Clover Leaf",
                          STYLE.FAN_TYPE | STYLE.OPEN, 1, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(347, FreeFan, "Free Fan",
                          STYLE.FAN_TYPE | STYLE.OPEN, 1, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(385, BoxFan, "Box Fan",
                          STYLE.FAN_TYPE | STYLE.OPEN, 1, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(516, Troika, "Troika",
                          STYLE.FAN_TYPE | STYLE.OPEN, 1, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(517, Quads, "Quads",
                          STYLE.FAN_TYPE | STYLE.OPEN | STYLE.ORIGINAL, 1, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(625, FascinationFan, "Fascination Fan",
                          STYLE.FAN_TYPE, 1, 6, SKILL.BALANCED,
                          altnames=('Demon Fan',) ))
    registerGame(GameInfo(647, Crescent, "Crescent",
                          STYLE.FAN_TYPE, 2, 3, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(714, ShamrocksII, "Shamrocks II",
                          STYLE.FAN_TYPE | STYLE.OPEN, 1, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(719, School, "School",
                          STYLE.FAN_TYPE, 1, 2, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(739, ForestGlade, "Forest Glade",
                          STYLE.FAN_TYPE, 2, 2, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(767, QuadsPlus, "Quads +",
                          STYLE.FAN_TYPE | STYLE.OPEN | STYLE.ORIGINAL, 1, 0, SKILL.MOSTLY_SKILL))

    registerGame(GameInfo(13, FortyThieves, "Forty Thieves",
                          STYLE.FORTY_THIEVES, 2, 0, SKILL.MOSTLY_SKILL,
                          altnames=("Napoleon at St.Helena",
                                    "Le Cadran")))
    registerGame(GameInfo(80, BusyAces, "Busy Aces",
                          STYLE.FORTY_THIEVES, 2, 0, SKILL.BALANCED))
    registerGame(GameInfo(228, Limited, "Limited",
                          STYLE.FORTY_THIEVES, 2, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(79, WaningMoon, "Waning Moon",
                          STYLE.FORTY_THIEVES, 2, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(125, Lucas, "Lucas",
                          STYLE.FORTY_THIEVES, 2, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(109, Deuces, "Deuces",
                          STYLE.FORTY_THIEVES, 2, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(196, Corona, "Corona",
                          STYLE.FORTY_THIEVES, 2, 0, SKILL.BALANCED))
    registerGame(GameInfo(195, Quadrangle, "Quadrangle",
                          STYLE.FORTY_THIEVES, 2, 0, SKILL.BALANCED))
    registerGame(GameInfo(110, Courtyard, "Courtyard",
                          STYLE.FORTY_THIEVES, 2, 0, SKILL.BALANCED))
    registerGame(GameInfo(23, FortyAndEight, "Forty and Eight",
                          STYLE.FORTY_THIEVES, 2, 1, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(115, LittleForty, "Little Forty",         # was: 72
                          STYLE.FORTY_THIEVES, 2, 3, SKILL.BALANCED))
    registerGame(GameInfo(76, Streets, "Streets",
                          STYLE.FORTY_THIEVES, 2, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(73, Maria, "Maria",
                          STYLE.FORTY_THIEVES, 2, 0, SKILL.BALANCED,
                          altnames=("Maria Luisa",) ))
    registerGame(GameInfo(70, NumberTen, "Number Ten",
                          STYLE.FORTY_THIEVES, 2, 0, SKILL.BALANCED))
    registerGame(GameInfo(71, RankAndFile, "Rank and File",
                          STYLE.FORTY_THIEVES, 2, 0, SKILL.BALANCED,
                          altnames=("Dress Parade") ))
    registerGame(GameInfo(197, TripleLine, "Triple Line",
                          STYLE.FORTY_THIEVES | STYLE.XORIGINAL, 2, 1, SKILL.BALANCED))
    registerGame(GameInfo(126, RedAndBlack, "Red and Black",        # was: 75
                          STYLE.FORTY_THIEVES, 2, 0, SKILL.BALANCED))
    registerGame(GameInfo(113, Zebra, "Zebra",
                          STYLE.FORTY_THIEVES, 2, 1, SKILL.BALANCED))
    registerGame(GameInfo(69, Indian, "Indian",
                          STYLE.FORTY_THIEVES, 2, 0, SKILL.BALANCED))
    registerGame(GameInfo(74, Midshipman, "Midshipman",
                          STYLE.FORTY_THIEVES, 2, 0, SKILL.BALANCED))
    registerGame(GameInfo(198, NapoleonsExile, "Napoleon's Exile",
                          STYLE.FORTY_THIEVES | STYLE.XORIGINAL, 2, 0, SKILL.BALANCED))
    registerGame(GameInfo(131, DoubleRail, "Double Rail",
                          STYLE.FORTY_THIEVES, 2, 0, SKILL.BALANCED))
    registerGame(GameInfo(199, SingleRail, "Single Rail",
                          STYLE.FORTY_THIEVES, 1, 0, SKILL.MOSTLY_LUCK))
    registerGame(GameInfo(295, NapoleonsSquare, "Napoleon's Square",
                          STYLE.FORTY_THIEVES, 2, 0, SKILL.BALANCED))
    registerGame(GameInfo(310, Emperor, "Emperor",
                          STYLE.FORTY_THIEVES, 2, 0, SKILL.BALANCED))
    registerGame(GameInfo(323, Octave, "Octave",
                          STYLE.FORTY_THIEVES, 2, 1, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(332, Mumbai, "Mumbai",
                          STYLE.FORTY_THIEVES, 3, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(411, CarreNapoleon, "Carre Napoleon",
                          STYLE.FORTY_THIEVES, 2, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(416, FortunesFavor, "Fortune's Favor",
                          STYLE.FORTY_THIEVES, 1, 0, SKILL.LUCK))
    registerGame(GameInfo(426, Octagon, "Octagon",
                          STYLE.FORTY_THIEVES, 2, 3, SKILL.BALANCED))
    registerGame(GameInfo(440, Squadron, "Squadron",
                          STYLE.FORTY_THIEVES, 2, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(462, Josephine, "Josephine",
                          STYLE.FORTY_THIEVES, 2, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(493, MarieRose, "Marie Rose",
                          STYLE.FORTY_THIEVES, 3, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(503, BigStreets, "Big Streets",
                          STYLE.FORTY_THIEVES | STYLE.ORIGINAL, 3, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(504, NumberTwelve, "Number Twelve",
                          STYLE.FORTY_THIEVES | STYLE.ORIGINAL, 3, 0, SKILL.BALANCED))
    registerGame(GameInfo(505, BigCourtyard, "Big Courtyard",
                          STYLE.FORTY_THIEVES | STYLE.ORIGINAL, 3, 0, SKILL.BALANCED))
    registerGame(GameInfo(506, Express, "Express",
                          STYLE.FORTY_THIEVES | STYLE.ORIGINAL, 3, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(514, Carnation, "Carnation",
                          STYLE.FORTY_THIEVES | STYLE.ORIGINAL, 4, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(528, FinalBattle, "Final Battle",
                          STYLE.FORTY_THIEVES, 2, 0, SKILL.BALANCED))
    registerGame(GameInfo(529, SanJuanHill, "San Juan Hill",
                          STYLE.FORTY_THIEVES, 2, 0, SKILL.BALANCED))
    registerGame(GameInfo(540, Waterloo, "Waterloo",
                          STYLE.FORTY_THIEVES, 2, 0, SKILL.BALANCED))
    registerGame(GameInfo(556, Junction, "Junction",
                          STYLE.FORTY_THIEVES, 4, 0, SKILL.MOSTLY_SKILL,
                          ranks=(0, 6, 7, 8, 9, 10, 11, 12) ))
    registerGame(GameInfo(564, TheSpark, "The Spark",
                          STYLE.FORTY_THIEVES, 2, 0, SKILL.MOSTLY_LUCK))
    registerGame(GameInfo(573, DoubleGoldMine, "Double Gold Mine",
                          STYLE.NUMERICA | STYLE.ORIGINAL, 2, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(574, Interchange, "Interchange",
                          STYLE.FORTY_THIEVES, 2, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(575, Unlimited, "Unlimited",
                          STYLE.FORTY_THIEVES, 2, -1, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(576, Breakwater, "Breakwater",
                          STYLE.FORTY_THIEVES, 2, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(577, FortyNine, "Forty Nine",
                          STYLE.FORTY_THIEVES, 2, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(578, IndianPatience, "Indian Patience",
                          STYLE.FORTY_THIEVES, 2, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(588, Roosevelt, "Roosevelt",
                          STYLE.FORTY_THIEVES, 2, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(628, Crossroads, "Crossroads",
                          STYLE.FORTY_THIEVES, 4, 0, SKILL.BALANCED))
    registerGame(GameInfo(631, Alternation, "Alternation",
                          STYLE.FORTY_THIEVES, 2, 0, SKILL.BALANCED))
    registerGame(GameInfo(632, Floradora, "Floradora",
                          STYLE.FORTY_THIEVES, 2, 0, SKILL.MOSTLY_LUCK))
    registerGame(GameInfo(679, TripleInterchange, "Triple Interchange",
                          STYLE.FORTY_THIEVES, 3, -1, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(683, FamousFifty, "Famous Fifty",
                          STYLE.FORTY_THIEVES, 2, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(751, BlindPatience, "Blind Patience",
                          STYLE.FORTY_THIEVES, 2, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(765, Foothold, "Foothold",
                          STYLE.FORTY_THIEVES | STYLE.ORIGINAL, 2, 0, SKILL.MOSTLY_SKILL))

    registerGame(GameInfo(5, RelaxedFreeCell, "Relaxed FreeCell",
                          STYLE.FREECELL | STYLE.RELAXED | STYLE.OPEN, 1, 0, SKILL.SKILL))
    registerGame(GameInfo(8, FreeCell, "FreeCell",
                          STYLE.FREECELL | STYLE.OPEN, 1, 0, SKILL.SKILL))
    registerGame(GameInfo(46, ForeCell, "ForeCell",
                          STYLE.FREECELL | STYLE.OPEN, 1, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(77, Stalactites, "Stalactites",
                          STYLE.FREECELL | STYLE.OPEN, 1, 0, SKILL.MOSTLY_SKILL,
                          altnames=("Grampus", "Old Mole") ))
    registerGame(GameInfo(264, DoubleFreecell, "Double FreeCell",
                          STYLE.FREECELL | STYLE.OPEN, 2, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(265, TripleFreecell, "Triple FreeCell",
                          STYLE.FREECELL | STYLE.OPEN, 3, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(336, ChallengeFreeCell, "Challenge FreeCell",
                          STYLE.FREECELL | STYLE.OPEN, 1, 0, SKILL.SKILL,
                          rules_filename='freecell.html'))
    registerGame(GameInfo(337, SuperChallengeFreeCell, "Super Challenge FreeCell",
                          STYLE.FREECELL | STYLE.OPEN, 1, 0, SKILL.SKILL))
    registerGame(GameInfo(363, Spidercells, "Spidercells",
                          STYLE.SPIDER | STYLE.OPEN, 1, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(364, SevenByFour, "Seven by Four",
                          STYLE.FREECELL | STYLE.OPEN, 1, 0, SKILL.SKILL))
    registerGame(GameInfo(365, SevenByFive, "Seven by Five",
                          STYLE.FREECELL | STYLE.OPEN, 1, 0, SKILL.SKILL))
    registerGame(GameInfo(383, Bath, "Bath",
                          STYLE.FREECELL | STYLE.OPEN, 1, 0, SKILL.SKILL))
    registerGame(GameInfo(394, Clink, "Clink",
                          STYLE.FREECELL | STYLE.OPEN | STYLE.ORIGINAL, 1, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(448, Repair, "Repair",
                          STYLE.FREECELL | STYLE.OPEN, 2, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(451, Cell11, "Cell 11",
                          STYLE.FREECELL | STYLE.OPEN, 3, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(464, FourColours, "Four Colours",
                          STYLE.FREECELL | STYLE.OPEN, 1, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(509, BigCell, "Big Cell",
                          STYLE.FREECELL | STYLE.OPEN | STYLE.ORIGINAL, 3, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(513, OceanTowers, "Ocean Towers",
                          STYLE.FREECELL | STYLE.OPEN | STYLE.ORIGINAL, 2, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(520, GermanFreeCell, "German FreeCell",
                          STYLE.FREECELL | STYLE.OPEN, 1, 0, SKILL.SKILL))
    registerGame(GameInfo(542, KingCell, "KingCell",
                          STYLE.FREECELL | STYLE.OPEN, 1, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(648, Headquarters, "Headquarters",
                          STYLE.FREECELL | STYLE.OPEN | STYLE.ORIGINAL, 2, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(698, CanCan, "Can Can",
                          STYLE.RAGLAN | STYLE.OPEN, 1, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(746, Limpopo, "Limpopo",
                          STYLE.FREECELL | STYLE.ORIGINAL, 2, 0, SKILL.MOSTLY_SKILL))

    registerGame(GameInfo(282, Glenwood, "Dutchess",
                          STYLE.CANFIELD, 1, 1, SKILL.BALANCED,
                          altnames=("Duchess", "Glenwood",) ))
    registerGame(GameInfo(587, DoubleFives, "Double Fives",
                          STYLE.TWO_DECK_TYPE, 2, 1, SKILL.BALANCED))

    registerGame(GameInfo(36, Golf, "Golf",
                          STYLE.GOLF, 1, 0, SKILL.BALANCED))
    registerGame(GameInfo(259, DeadKingGolf, "Dead King Golf",
                          STYLE.GOLF, 1, 0, SKILL.BALANCED))
    registerGame(GameInfo(260, RelaxedGolf, "Relaxed Golf",
                          STYLE.GOLF | STYLE.RELAXED, 1, 0, SKILL.BALANCED,
                          altnames=("Putt Putt",) ))
    registerGame(GameInfo(40, Elevator, "Elevator",
                          STYLE.GOLF, 1, 0, SKILL.BALANCED,
                          altnames=("Egyptian Solitaire", "Pyramid Golf") ))
    registerGame(GameInfo(98, BlackHole, "Black Hole",
                          STYLE.GOLF | STYLE.OPEN, 1, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(267, FourLeafClovers, "Four Leaf Clovers",
                          STYLE.GOLF | STYLE.OPEN, 1, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(281, Escalator, "Escalator",
                          STYLE.GOLF, 1, 0, SKILL.BALANCED))
    registerGame(GameInfo(405, AllInARow, "All in a Row",
                          STYLE.GOLF | STYLE.OPEN, 1, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(432, Robert, "Robert",
                          STYLE.GOLF, 1, 2, SKILL.LUCK))
    registerGame(GameInfo(551, DiamondMine, "Diamond Mine",
                          STYLE.ONE_DECK_TYPE, 1, 0, SKILL.BALANCED))
    registerGame(GameInfo(661, Dolphin, "Dolphin",
                          STYLE.GOLF | STYLE.ORIGINAL, 1, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(662, DoubleDolphin, "Double Dolphin",
                          STYLE.GOLF | STYLE.ORIGINAL, 2, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(709, Waterfall, "Waterfall",
                          STYLE.TWO_DECK_TYPE | STYLE.ORIGINAL, 2, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(720, Vague, "Vague",
                          STYLE.ONE_DECK_TYPE, 1, 0, SKILL.MOSTLY_LUCK))
    registerGame(GameInfo(723, DevilsSolitaire, "Devil's Solitaire",
                          STYLE.TWO_DECK_TYPE, 2, 2, SKILL.BALANCED,
                          altnames=('Banner',) ))
    registerGame(GameInfo(728, ThirtyTwoCards, "Thirty Two Cards",
                          STYLE.TWO_DECK_TYPE, 2, 0, SKILL.LUCK))
    registerGame(GameInfo(731, ThreeFirTrees, "Three Fir-trees",
                          STYLE.GOLF, 2, 0, SKILL.BALANCED))
    registerGame(GameInfo(733, NapoleonTakesMoscow, "Napoleon Takes Moscow",
                          STYLE.TWO_DECK_TYPE, 2, 2, SKILL.BALANCED))
    registerGame(GameInfo(734, NapoleonLeavesMoscow, "Napoleon Leaves Moscow",
                          STYLE.TWO_DECK_TYPE, 2, 2, SKILL.BALANCED))
    registerGame(GameInfo(749, Flake, "Flake",
                          STYLE.GOLF | STYLE.OPEN | STYLE.ORIGINAL,
                          1, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(750, Flake2Decks, "Flake (2 decks)",
                          STYLE.GOLF | STYLE.OPEN | STYLE.ORIGINAL,
                          2, 0, SKILL.MOSTLY_SKILL))

    UNLIMITED_REDEALS = None

    registerGame(GameInfo(763, Wasatch, "Wasatch",
                          STYLE.ONE_DECK_TYPE, 1, UNLIMITED_REDEALS, SKILL.MOSTLY_LUCK))
    registerGame(GameInfo(764, Beacon, "Beacon",
                          STYLE.ONE_DECK_TYPE | STYLE.ORIGINAL, 1, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(768, RelaxedThreeFirTrees, "Relaxed Three Fir-trees",
                          STYLE.GOLF, 2, 0, SKILL.BALANCED))

    registerGame(GameInfo(557, GrandDuchess, "Grand Duchess",
                          STYLE.TWO_DECK_TYPE, 2, 3))
    registerGame(GameInfo(617, Parisienne, "Parisienne",
                          STYLE.TWO_DECK_TYPE, 2, 3,
                          rules_filename='grandduchess.html',
                          altnames=('La Parisienne', 'Parisian') ))
    registerGame(GameInfo(618, GrandDuchessPlus, "Grand Duchess +",
                          STYLE.TWO_DECK_TYPE, 2, 3))

    registerGame(GameInfo(261, GrandfathersClock, "Grandfather's Clock",
                          STYLE.ONE_DECK_TYPE | STYLE.OPEN, 1, 0, SKILL.BALANCED))
    registerGame(GameInfo(682, Dial, "Dial",
                          STYLE.ONE_DECK_TYPE, 1, 1, SKILL.LUCK))
    registerGame(GameInfo(690, Hemispheres, "Hemispheres",
                          STYLE.TWO_DECK_TYPE, 2, 0, SKILL.BALANCED,
                          altnames=("The Four Continents",) ))
    registerGame(GameInfo(697, BigBen, "Big Ben",
                          STYLE.TWO_DECK_TYPE, 2, 0, SKILL.BALANCED))
    registerGame(GameInfo(737, Clock, "Clock",
                          STYLE.ONE_DECK_TYPE, 1, 0, SKILL.LUCK,
                          altnames=("Travellers",) ))

    registerGame(GameInfo(1, Gypsy, "Gypsy",
                          STYLE.GYPSY, 2, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(65, Giant, "Giant",
                          STYLE.GYPSY, 2, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(3, Irmgard, "Irmgard",
                          STYLE.GYPSY, 2, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(119, DieKoenigsbergerin, "Die Koenigsbergerin",
                          STYLE.GYPSY, 2, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(174, DieRussische, "Russian Patience",
                          STYLE.TWO_DECK_TYPE | STYLE.OPEN, 2, 0, SKILL.MOSTLY_SKILL,
                          ranks=(0, 6, 7, 8, 9, 10, 11, 12),
                          altnames=("Die Russische",) ))
    registerGame(GameInfo(62, MissMilligan, "Miss Milligan",
                          STYLE.GYPSY, 2, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(200, Nomad, "Nomad",
                          STYLE.GYPSY | STYLE.CONTRIB | STYLE.ORIGINAL, 2, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(78, MilliganCell, "Milligan Cell",
                          STYLE.GYPSY, 2, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(217, MilliganHarp, "Milligan Harp",
                          STYLE.GYPSY, 2, 0, SKILL.BALANCED))
    registerGame(GameInfo(218, Carlton, "Carlton",
                          STYLE.GYPSY, 2, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(68, LexingtonHarp, "Lexington Harp",
                          STYLE.YUKON, 2, 0, SKILL.BALANCED))
    registerGame(GameInfo(154, Brunswick, "Brunswick",
                          STYLE.YUKON, 2, 0, SKILL.BALANCED))
    registerGame(GameInfo(121, Mississippi, "Mississippi",
                          STYLE.YUKON | STYLE.XORIGINAL, 2, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(122, Griffon, "Griffon",
                          STYLE.YUKON | STYLE.XORIGINAL, 2, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(226, Blockade, "Blockade",
                          STYLE.GYPSY, 2, 0, SKILL.BALANCED))
    registerGame(GameInfo(412, Cone, "Cone",
                          STYLE.GYPSY, 2, 0, SKILL.BALANCED))
    registerGame(GameInfo(463, Surprise, "Surprise",
                          STYLE.GYPSY, 2, 0, SKILL.BALANCED))
    registerGame(GameInfo(469, PhantomBlockade, "Phantom Blockade",
                          STYLE.GYPSY, 2, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(478, Elba, "Elba",
                          STYLE.GYPSY, 2, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(486, ImperialGuards, "Imperial Guards",
                          STYLE.GYPSY, 2, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(487, Millie, "Millie",
                          STYLE.GYPSY, 2, 0, SKILL.BALANCED))
    registerGame(GameInfo(498, Steve, "Steve",
                          STYLE.GYPSY, 2, 0, SKILL.BALANCED))
    registerGame(GameInfo(566, Hypotenuse, "Hypotenuse",
                          STYLE.GYPSY, 2, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(567, EternalTriangle, "Eternal Triangle",
                          STYLE.GYPSY, 2, 0, SKILL.MOSTLY_SKILL,
                          altnames=('Lobachevsky',) ))
    registerGame(GameInfo(568, RightTriangle, "Right Triangle",
                          STYLE.GYPSY, 2, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(580, Trapdoor, "Trapdoor",
                          STYLE.GYPSY | STYLE.ORIGINAL, 2, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(581, Flamenco, "Flamenco",
                          STYLE.GYPSY | STYLE.ORIGINAL, 2, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(584, Eclipse, "Eclipse",
                          STYLE.GYPSY, 2, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(640, BrazilianPatience, "Brazilian Patience",
                          STYLE.GYPSY, 2, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(666, TrapdoorSpider, "Trapdoor Spider",
                          STYLE.SPIDER | STYLE.ORIGINAL, 2, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(712, Leprechaun, "Leprechaun",
                          STYLE.GYPSY | STYLE.ORIGINAL, 2, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(718, LockedCards, "Locked Cards",
                          STYLE.TWO_DECK_TYPE, 2, 2, SKILL.BALANCED))
    registerGame(GameInfo(721, Thirty, "Thirty",
                          STYLE.ONE_DECK_TYPE | STYLE.OPEN, 1, 0, SKILL.MOSTLY_SKILL,
                          ranks=(0, 6, 7, 8, 9, 10, 11, 12)))
    registerGame(GameInfo(725, TopsyTurvyQueens, "Topsy-Turvy Queens",
                          STYLE.TWO_DECK_TYPE, 2, 2, SKILL.BALANCED))
    registerGame(GameInfo(21, DoubleKlondike, "Double Klondike",
                          STYLE.KLONDIKE, 2, -1, SKILL.BALANCED))
    registerGame(GameInfo(28, DoubleKlondikeByThrees, "Double Klondike by Threes",
                          STYLE.KLONDIKE, 2, -1, SKILL.MOSTLY_LUCK))
    registerGame(GameInfo(25, Gargantua, "Gargantua",
                          STYLE.KLONDIKE, 2, 1, SKILL.BALANCED))
    registerGame(GameInfo(15, BigHarp, "Big Harp",
                          STYLE.KLONDIKE, 2, 0, SKILL.BALANCED))
    registerGame(GameInfo(51, Steps, "Steps",
                          STYLE.KLONDIKE, 2, 1, SKILL.BALANCED))
    registerGame(GameInfo(273, TripleKlondike, "Triple Klondike",
                          STYLE.KLONDIKE, 3, -1, SKILL.BALANCED))
    registerGame(GameInfo(274, TripleKlondikeByThrees, "Triple Klondike by Threes",
                          STYLE.KLONDIKE, 3, -1, SKILL.MOSTLY_LUCK))
    registerGame(GameInfo(495, LadyJane, "Lady Jane",
                          STYLE.KLONDIKE, 2, 1, SKILL.BALANCED))
    registerGame(GameInfo(496, Inquisitor, "Inquisitor",
                          STYLE.KLONDIKE, 2, 2, SKILL.BALANCED))
    registerGame(GameInfo(497, Arabella, "Arabella",
                          STYLE.KLONDIKE, 3, 0, SKILL.BALANCED))
    registerGame(GameInfo(545, BigDeal, "Big Deal",
                          STYLE.KLONDIKE | STYLE.ORIGINAL, 4, 1, SKILL.BALANCED))
    registerGame(GameInfo(562, Delivery, "Delivery",
                          STYLE.FORTY_THIEVES | STYLE.ORIGINAL, 4, 0, SKILL.BALANCED))
    registerGame(GameInfo(590, ChineseKlondike, "Chinese Klondike",
                          STYLE.KLONDIKE, 3, -1, SKILL.BALANCED,
                          suits=(0, 1, 2) ))
    registerGame(GameInfo(591, Pantagruel, "Pantagruel",
                          STYLE.KLONDIKE, 2, 0, SKILL.BALANCED))
    registerGame(GameInfo(668, DoubleKingsley, "Double Kingsley",
                          STYLE.KLONDIKE, 2, 0, SKILL.BALANCED))
    registerGame(GameInfo(678, ThievesOfEgypt, "Thieves of Egypt",
                          STYLE.KLONDIKE, 2, 1, SKILL.BALANCED))
    registerGame(GameInfo(689, Brush, "Brush",
                          STYLE.TWO_DECK_TYPE | STYLE.ORIGINAL, 2, 0, SKILL.MOSTLY_SKILL))

    registerGame(GameInfo(307, HeadsAndTails, "Heads and Tails",
                          STYLE.TWO_DECK_TYPE, 2, 0, SKILL.BALANCED))
    registerGame(GameInfo(708, Barrier, "Barrier",
                          STYLE.TWO_DECK_TYPE | STYLE.ORIGINAL, 2, 0, SKILL.BALANCED))

    registerGame(GameInfo(141, DerKatzenschwanz, "Cat's Tail",
                          STYLE.FREECELL | STYLE.OPEN, 2, 0, SKILL.MOSTLY_SKILL,
                          altnames=("Der Katzenschwanz",) ))
    registerGame(GameInfo(142, DieSchlange, "Snake",
                          STYLE.FREECELL | STYLE.OPEN, 2, 0, SKILL.MOSTLY_SKILL,
                          altnames=("Die Schlange",) ))
    registerGame(GameInfo(279, Kings, "Kings",
                          STYLE.FREECELL | STYLE.OPEN, 2, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(286, Retinue, "Retinue",
                          STYLE.FREECELL | STYLE.OPEN | STYLE.ORIGINAL, 2, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(299, SalicLaw, "Salic Law",
                          STYLE.TWO_DECK_TYPE, 2, 0, SKILL.MOSTLY_LUCK))
    registerGame(GameInfo(442, Deep, "Deep",
                          STYLE.FREECELL | STYLE.OPEN | STYLE.ORIGINAL, 2, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(523, Intrigue, "Intrigue",
                          STYLE.TWO_DECK_TYPE, 2, 0, SKILL.BALANCED))
    registerGame(GameInfo(611, FaerieQueen, "Faerie Queen",
                          STYLE.TWO_DECK_TYPE, 2, 0, SKILL.BALANCED))
    registerGame(GameInfo(612, Glencoe, "Glencoe",
                          STYLE.TWO_DECK_TYPE, 2, 0, SKILL.BALANCED,
                          rules_filename="intrigue.html"))
    registerGame(GameInfo(616, LaggardLady, "Laggard Lady",
                          STYLE.TWO_DECK_TYPE, 2, 0, SKILL.BALANCED,
                          rules_filename="intrigue.html"))
    registerGame(GameInfo(624, StepUp, "Step-Up",
                          STYLE.TWO_DECK_TYPE, 2, 0, SKILL.BALANCED))
    registerGame(GameInfo(766, Kentish, "Kentish",
                          STYLE.TWO_DECK_TYPE | STYLE.OPEN | STYLE.ORIGINAL, 2, 0, SKILL.MOSTLY_SKILL))



    registerGame(GameInfo(2, Klondike, "Klondike",
                          STYLE.KLONDIKE, 1, -1, SKILL.BALANCED))
    registerGame(GameInfo(61, CasinoKlondike, "Casino Klondike",
                          STYLE.KLONDIKE | STYLE.SCORE, 1, 2, SKILL.BALANCED))
    registerGame(GameInfo(129, VegasKlondike, "Vegas Klondike",
                          STYLE.KLONDIKE | STYLE.SCORE, 1, 0, SKILL.BALANCED))
    registerGame(GameInfo(18, KlondikeByThrees, "Klondike by Threes",
                          STYLE.KLONDIKE, 1, -1, SKILL.MOSTLY_LUCK))
    registerGame(GameInfo(58, ThumbAndPouch, "Thumb and Pouch",
                          STYLE.KLONDIKE, 1, 0, SKILL.MOSTLY_LUCK))
    registerGame(GameInfo(67, Whitehead, "Whitehead",
                          STYLE.KLONDIKE, 1, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(39, SmallHarp, "Small Harp",
                          STYLE.KLONDIKE, 1, -1, SKILL.BALANCED,
                          altnames=("Die kleine Harfe",) ))
    registerGame(GameInfo(66, Eastcliff, "Eastcliff",
                          STYLE.KLONDIKE, 1, 0, SKILL.BALANCED))
    registerGame(GameInfo(224, Easthaven, "Easthaven",
                          STYLE.GYPSY, 1, 0, SKILL.MOSTLY_LUCK))
    registerGame(GameInfo(33, Westcliff, "Westcliff",
                          STYLE.KLONDIKE, 1, 0, SKILL.MOSTLY_LUCK))
    registerGame(GameInfo(225, Westhaven, "Westhaven",
                          STYLE.GYPSY, 1, 0, SKILL.BALANCED))
    registerGame(GameInfo(107, PasSeul, "Pas Seul",
                          STYLE.KLONDIKE, 1, 0, SKILL.BALANCED))
    registerGame(GameInfo(81, BlindAlleys, "Blind Alleys",
                          STYLE.KLONDIKE, 1, 1, SKILL.MOSTLY_LUCK))
    registerGame(GameInfo(215, Somerset, "Somerset",
                          STYLE.BELEAGUERED_CASTLE | STYLE.OPEN, 1, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(231, Canister, "Canister",
                          STYLE.BELEAGUERED_CASTLE | STYLE.OPEN, 1, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(229, AgnesSorel, "Agnes Sorel",
                          STYLE.GYPSY, 1, 0, SKILL.MOSTLY_LUCK))
    registerGame(GameInfo(4, EightTimesEight, "8 x 8",
                          STYLE.KLONDIKE, 2, -1, SKILL.BALANCED))
    registerGame(GameInfo(127, AchtmalAcht, "Eight Times Eight",
                          STYLE.KLONDIKE, 2, 2, SKILL.BALANCED,
                          altnames=("Achtmal Acht",) ))
    registerGame(GameInfo(133, Batsford, "Batsford",
                          STYLE.KLONDIKE, 2, 0, SKILL.BALANCED))
    registerGame(GameInfo(221, Stonewall, "Stonewall",
                          STYLE.RAGLAN, 1, 0, SKILL.MOSTLY_LUCK))
    registerGame(GameInfo(222, FlowerGarden, "Flower Garden",
                          STYLE.RAGLAN | STYLE.OPEN, 1, 0, SKILL.MOSTLY_SKILL,
                          altnames=("The Bouquet", "The Garden",) ))
    registerGame(GameInfo(233, KingAlbert, "King Albert",
                          STYLE.RAGLAN | STYLE.OPEN, 1, 0, SKILL.MOSTLY_SKILL,
                          altnames=("Idiot's Delight",) ))
    registerGame(GameInfo(232, Raglan, "Raglan",
                          STYLE.RAGLAN | STYLE.OPEN, 1, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(223, Brigade, "Brigade",
                          STYLE.RAGLAN | STYLE.OPEN, 1, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(230, Jane, "Jane",
                          STYLE.RAGLAN, 1, 0, SKILL.BALANCED))
    registerGame(GameInfo(236, AgnesBernauer, "Agnes Bernauer",
                          STYLE.RAGLAN, 1, 0, SKILL.BALANCED))
    registerGame(GameInfo(263, Phoenix, "Phoenix",
                          STYLE.RAGLAN | STYLE.OPEN, 1, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(283, Jumbo, "Jumbo",
                          STYLE.KLONDIKE, 2, 1, SKILL.BALANCED))
    registerGame(GameInfo(333, OpenJumbo, "Open Jumbo",
                          STYLE.KLONDIKE, 2, 1, SKILL.BALANCED))
    registerGame(GameInfo(326, Lanes, "Lanes",
                          STYLE.KLONDIKE, 1, 1, SKILL.BALANCED))
    registerGame(GameInfo(327, ThirtySix, "Thirty Six",
                          STYLE.KLONDIKE, 1, 0, SKILL.BALANCED))
    registerGame(GameInfo(350, Q_C_, "Q.C.",
                          STYLE.KLONDIKE, 2, 1, SKILL.BALANCED))
    registerGame(GameInfo(361, NorthwestTerritory, "Northwest Territory",
                          STYLE.RAGLAN, 1, 0, SKILL.BALANCED))
    registerGame(GameInfo(362, Morehead, "Morehead",
                          STYLE.BELEAGUERED_CASTLE | STYLE.OPEN, 1, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(388, Senate, "Senate",
                          STYLE.RAGLAN, 2, 0, SKILL.BALANCED))
    registerGame(GameInfo(389, SenatePlus, "Senate +",
                          STYLE.RAGLAN, 2, 0, SKILL.BALANCED))
    registerGame(GameInfo(390, Arizona, "Arizona",
                          STYLE.RAGLAN | STYLE.OPEN, 1, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(407, AuntMary, "Aunt Mary",
                          STYLE.KLONDIKE, 1, 0, SKILL.BALANCED))
    registerGame(GameInfo(420, DoubleDot, "Double Dot",
                          STYLE.KLONDIKE, 1, 0, SKILL.BALANCED))
    registerGame(GameInfo(434, SevenDevils, "Seven Devils",
                          STYLE.RAGLAN, 2, 0, SKILL.MOSTLY_LUCK))
    registerGame(GameInfo(452, DoubleEasthaven, "Double Easthaven",
                          STYLE.GYPSY, 2, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(453, TripleEasthaven, "Triple Easthaven",
                          STYLE.GYPSY, 3, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(470, MovingLeft, "Moving Left",
                          STYLE.KLONDIKE, 2, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(471, Souter, "Souter",
                          STYLE.KLONDIKE, 2, 1, SKILL.BALANCED))
    registerGame(GameInfo(473, BigForty, "Big Forty",
                          STYLE.KLONDIKE, 1, -1, SKILL.BALANCED))
    registerGame(GameInfo(474, AliBaba, "Ali Baba",
                          STYLE.KLONDIKE, 1, -1, SKILL.BALANCED))
    registerGame(GameInfo(475, Cassim, "Cassim",
                          STYLE.KLONDIKE, 1, -1, SKILL.BALANCED))
    registerGame(GameInfo(479, Saratoga, "Saratoga",
                          STYLE.KLONDIKE, 1, -1, SKILL.BALANCED))
    registerGame(GameInfo(491, Whitehorse, "Whitehorse",
                          STYLE.KLONDIKE, 1, -1, SKILL.BALANCED))
    registerGame(GameInfo(518, Boost, "Boost",
                          STYLE.KLONDIKE | STYLE.ORIGINAL, 1, 2, SKILL.BALANCED))
    registerGame(GameInfo(522, ArticGarden, "Artic Garden",
                          STYLE.RAGLAN, 1, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(532, GoldRush, "Gold Rush",
                          STYLE.KLONDIKE, 1, 2, SKILL.BALANCED))
    registerGame(GameInfo(539, Usk, "Usk",
                          STYLE.KLONDIKE, 1, 1, SKILL.BALANCED))
    registerGame(GameInfo(541, BatsfordAgain, "Batsford Again",
                          STYLE.KLONDIKE, 2, 1, SKILL.BALANCED))
    registerGame(GameInfo(572, GoldMine, "Gold Mine",
                          STYLE.NUMERICA, 1, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(585, LuckyThirteen, "Lucky Thirteen",
                          STYLE.ONE_DECK_TYPE, 1, 0, SKILL.MOSTLY_LUCK))
    registerGame(GameInfo(586, LuckyPiles, "Lucky Piles",
                          STYLE.FAN_TYPE, 1, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(601, AmericanCanister, "American Canister",
                          STYLE.BELEAGUERED_CASTLE | STYLE.OPEN, 1, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(602, BritishCanister, "British Canister",
                          STYLE.BELEAGUERED_CASTLE | STYLE.OPEN, 1, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(607, Legion, "Legion",
                          STYLE.KLONDIKE, 1, 0, SKILL.BALANCED))
    registerGame(GameInfo(627, QueenVictoria, "Queen Victoria",
                          STYLE.RAGLAN | STYLE.OPEN, 1, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(630, BigBertha, "Big Bertha",
                          STYLE.RAGLAN | STYLE.OPEN, 2, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(633, Athena, "Athena",
                          STYLE.KLONDIKE, 1, -1, SKILL.BALANCED))
    registerGame(GameInfo(634, Chinaman, "Chinaman",
                          STYLE.KLONDIKE, 1, 1, SKILL.BALANCED))
    registerGame(GameInfo(651, EightByEight, "Eight by Eight",
                          STYLE.KLONDIKE, 2, 2, SKILL.BALANCED))
    registerGame(GameInfo(667, Kingsley, "Kingsley",
                          STYLE.KLONDIKE, 1, 0, SKILL.MOSTLY_LUCK))
    registerGame(GameInfo(669, Scarp, "Scarp",
                          STYLE.GYPSY | STYLE.ORIGINAL, 3, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(726, EightSages, "Eight Sages",
                          STYLE.KLONDIKE, 2, 1, SKILL.MOSTLY_LUCK))

    # registerGame(GameInfo(400, Labyrinth, "Labyrinth",
    #                       STYLE.ONE_DECK_TYPE, 1, 0))
    # registerGame(GameInfo(4000, Labyrinth, "Labyrinth",
    #                       STYLE.ONE_DECK_TYPE, 1, 0))


    registerGame(GameInfo(37, LarasGame, "Lara's Game",
                          STYLE.TWO_DECK_TYPE, 2, 0, SKILL.BALANCED,
                          altnames=("Thirteen Packs",) ))
    registerGame(GameInfo(13006, RelaxedLarasGame, "Lara's Game Relaxed", STYLE.TWO_DECK_TYPE, 2, 1, SKILL.BALANCED))
    registerGame(GameInfo(13007, DoubleLarasGame, "Lara's Game Doubled", STYLE.TWO_DECK_TYPE, 4, 2, SKILL.BALANCED))

    VARIABLE_REDEALS = None
    registerGame(GameInfo(17, Matriarchy, "Matriarchy",
                          STYLE.TWO_DECK_TYPE, 2, VARIABLE_REDEALS, SKILL.BALANCED))

    registerGame(GameInfo(53, Montana, "Montana",
                          STYLE.MONTANA | STYLE.OPEN, 1, 2, SKILL.MOSTLY_SKILL,
                          numcards=48, altnames="Gaps"))
    registerGame(GameInfo(116, Spaces, "Spaces",
                          STYLE.MONTANA | STYLE.OPEN, 1, 2, SKILL.MOSTLY_SKILL,
                          numcards=48))
    registerGame(GameInfo(63, BlueMoon, "Blue Moon",
                          STYLE.MONTANA | STYLE.OPEN, 1, 2, SKILL.MOSTLY_SKILL,
                          altnames=("Rangoon",) ))
    registerGame(GameInfo(117, RedMoon, "Red Moon",
                          STYLE.MONTANA | STYLE.OPEN, 1, 2, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(275, Galary, "Galary",
                          STYLE.MONTANA | STYLE.OPEN | STYLE.ORIGINAL, 1, 2, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(276, Moonlight, "Moonlight",
                          STYLE.MONTANA | STYLE.OPEN | STYLE.ORIGINAL, 1, 2, SKILL.MOSTLY_SKILL,
                          numcards=48))
    registerGame(GameInfo(380, Jungle, "Jungle",
                          STYLE.MONTANA | STYLE.OPEN, 1, 1, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(381, SpacesAndAces, "Spaces and Aces",
                          STYLE.MONTANA | STYLE.OPEN, 1, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(706, Paganini, "Paganini",
                          STYLE.MONTANA | STYLE.OPEN, 1, 1, SKILL.MOSTLY_SKILL,
                          ranks=(0, 5, 6, 7, 8, 9, 10, 11, 12),
                          altnames=('Long Trip',) ))
    registerGame(GameInfo(736, Spoilt, "Spoilt",
                          STYLE.MONTANA, 1, 0, SKILL.MOSTLY_LUCK,
                          ranks=(0, 6, 7, 8, 9, 10, 11, 12),
                          ))
    registerGame(GameInfo(759, DoubleMontana, "Double Montana",
                          STYLE.MONTANA | STYLE.OPEN, 2, 0, SKILL.MOSTLY_SKILL))


    registerGame(GameInfo(89, MonteCarlo, "Monte Carlo",
                          STYLE.PAIRING_TYPE, 1, 0, SKILL.MOSTLY_LUCK,
                          altnames=("Quilt",) ))
    registerGame(GameInfo(216, MonteCarlo2Decks, "Monte Carlo (2 decks)",
                          STYLE.PAIRING_TYPE, 2, 0, SKILL.MOSTLY_LUCK))
    registerGame(GameInfo(212, Weddings, "Weddings",
                          STYLE.PAIRING_TYPE, 1, 0, SKILL.MOSTLY_LUCK))
    registerGame(GameInfo(90, SimpleCarlo, "Simple Carlo",
                          STYLE.PAIRING_TYPE, 1, 0, SKILL.MOSTLY_LUCK))
    registerGame(GameInfo(91, SimplePairs, "Simple Pairs",
                          STYLE.PAIRING_TYPE, 1, 0, SKILL.LUCK,
                          altnames=("Jamestown",)))
    registerGame(GameInfo(92, Neighbour, "Neighbour",
                          STYLE.PAIRING_TYPE, 1, 0, SKILL.MOSTLY_LUCK))
    registerGame(GameInfo(96, Fourteen, "Fourteen",
                          STYLE.PAIRING_TYPE | STYLE.OPEN, 1, 0, SKILL.MOSTLY_LUCK))
    registerGame(GameInfo(235, Nestor, "Nestor",
                          STYLE.PAIRING_TYPE | STYLE.OPEN, 1, 0, SKILL.MOSTLY_LUCK))
    registerGame(GameInfo(152, DerLetzteMonarch, "The Last Monarch",
                          STYLE.ONE_DECK_TYPE | STYLE.OPEN, 1, 0, SKILL.MOSTLY_SKILL,
                          altnames=("Der letzte Monarch",) ))
    registerGame(GameInfo(328, TheWish, "The Wish",
                          STYLE.PAIRING_TYPE, 1, 0, SKILL.MOSTLY_LUCK,
                          ranks=(0, 6, 7, 8, 9, 10, 11, 12) ))
    registerGame(GameInfo(329, TheWishOpen, "The Wish (open)",
                          STYLE.PAIRING_TYPE | STYLE.OPEN | STYLE.ORIGINAL, 1, 0, SKILL.MOSTLY_SKILL,
                          ranks=(0, 6, 7, 8, 9, 10, 11, 12) ))
    registerGame(GameInfo(368, Vertical, "Vertical",
                          STYLE.PAIRING_TYPE | STYLE.OPEN, 1, 0, SKILL.MOSTLY_LUCK))
    registerGame(GameInfo(649, DoubletsII, "Doublets II",
                          STYLE.PAIRING_TYPE, 1, 0, SKILL.MOSTLY_LUCK))
    registerGame(GameInfo(663, TheLastMonarchII, "The Last Monarch II",
                          STYLE.TWO_DECK_TYPE | STYLE.ORIGINAL, 2, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(727, RightAndLeft, "Right and Left",
                          STYLE.PAIRING_TYPE, 2, -1, SKILL.LUCK))

    registerGame(GameInfo(167, DerKleineNapoleon, "Der kleine Napoleon",
                          STYLE.NAPOLEON | STYLE.OPEN, 1, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(168, DerFreieNapoleon, "Der freie Napoleon",
                          STYLE.NAPOLEON | STYLE.OPEN, 1, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(169, Napoleon, "Napoleon",
                          STYLE.NAPOLEON | STYLE.OPEN, 1, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(170, FreeNapoleon, "Free Napoleon",
                          STYLE.NAPOLEON | STYLE.OPEN, 1, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(536, Master, "Master",
                          STYLE.NAPOLEON | STYLE.OPEN, 1, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(537, TheLittleCorporal, "The Little Corporal",
                          STYLE.NAPOLEON | STYLE.OPEN, 1, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(538, Bonaparte, "Bonaparte",
                          STYLE.NAPOLEON | STYLE.OPEN | STYLE.ORIGINAL, 1, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(705, BusyCards, "Busy Cards",
                          STYLE.NAPOLEON | STYLE.OPEN | STYLE.ORIGINAL, 2, 0, SKILL.MOSTLY_SKILL))

    registerGame(GameInfo(318, Needle, "Needle",
                          STYLE.FREECELL | STYLE.OPEN, 1, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(319, Haystack, "Haystack",
                          STYLE.FREECELL | STYLE.OPEN, 1, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(367, Pitchfork, "Pitchfork",
                          STYLE.FREECELL | STYLE.OPEN, 1, 0, SKILL.MOSTLY_SKILL))

    registerGame(GameInfo(257, Numerica, "Numerica",
                          STYLE.NUMERICA | STYLE.CONTRIB, 1, 0, SKILL.BALANCED,
                          altnames=("Sir Tommy",) ))
    registerGame(GameInfo(171, LadyBetty, "Lady Betty",
                          STYLE.NUMERICA, 1, 0, SKILL.BALANCED))
    registerGame(GameInfo(355, Frog, "Frog",
                          STYLE.NUMERICA, 2, 0, SKILL.BALANCED))
    registerGame(GameInfo(356, Fly, "Fly",
                          STYLE.NUMERICA, 2, 0, SKILL.BALANCED,
                          rules_filename='frog.html'))
    registerGame(GameInfo(357, Gnat, "Gnat",
                          STYLE.NUMERICA, 1, 0, SKILL.BALANCED))
    registerGame(GameInfo(378, Gloaming, "Gloaming",
                          STYLE.NUMERICA | STYLE.OPEN | STYLE.ORIGINAL, 1, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(379, Chamberlain, "Chamberlain",
                          STYLE.NUMERICA | STYLE.OPEN | STYLE.ORIGINAL, 1, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(402, Toad, "Toad",
                          STYLE.NUMERICA, 2, 0, SKILL.BALANCED))
    registerGame(GameInfo(430, PussInTheCorner, "Puss in the Corner",
                          STYLE.NUMERICA, 1, 1, SKILL.BALANCED))
    registerGame(GameInfo(435, Shifting, "Shifting",
                          STYLE.NUMERICA, 1, 0, SKILL.BALANCED))
    registerGame(GameInfo(472, Strategerie, "Strategerie",
                          STYLE.NUMERICA, 1, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(558, Numerica2Decks, "Numerica (2 decks)",
                          STYLE.NUMERICA, 2, 0, SKILL.BALANCED))
    registerGame(GameInfo(589, LastChance, "Last Chance",
                          STYLE.NUMERICA, 1, 0, SKILL.BALANCED))
    registerGame(GameInfo(599, Assembly, "Assembly",
                          STYLE.NUMERICA, 1, 0, SKILL.BALANCED))
    registerGame(GameInfo(600, AnnoDomini, "Anno Domini",
                          STYLE.NUMERICA, 1, 2, SKILL.BALANCED))
    registerGame(GameInfo(613, Fanny, "Fanny",
                          STYLE.NUMERICA, 2, 0, SKILL.BALANCED))
    registerGame(GameInfo(641, CircleNine, "Circle Nine",
                          STYLE.NUMERICA, 1, 0, SKILL.BALANCED))
    registerGame(GameInfo(643, Measure, "Measure",
                          STYLE.NUMERICA | STYLE.ORIGINAL, 1, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(644, DoubleMeasure, "Double Measure",
                          STYLE.NUMERICA | STYLE.ORIGINAL, 2, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(754, Amphibian, "Amphibian",
                          STYLE.NUMERICA | STYLE.ORIGINAL, 2, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(760, Aglet, "Aglet",
                          STYLE.ONE_DECK_TYPE | STYLE.ORIGINAL, 1, 0, SKILL.MOSTLY_SKILL))

    registerGame(GameInfo(59, Osmosis, "Osmosis",
                          STYLE.ONE_DECK_TYPE, 1, -1, SKILL.MOSTLY_LUCK))
    registerGame(GameInfo(60, Peek, "Peek",
                          STYLE.ONE_DECK_TYPE, 1, -1, SKILL.MOSTLY_LUCK))
    registerGame(GameInfo(298, OpenPeek, "Open Peek",
                          STYLE.ONE_DECK_TYPE | STYLE.OPEN | STYLE.ORIGINAL, 1, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(370, Genesis, "Genesis",
                          STYLE.ONE_DECK_TYPE | STYLE.OPEN | STYLE.ORIGINAL, 1, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(371, GenesisPlus, "Genesis +",
                          STYLE.ONE_DECK_TYPE | STYLE.OPEN | STYLE.ORIGINAL, 1, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(409, Bridesmaids, "Bridesmaids",
                          STYLE.ONE_DECK_TYPE, 1, -1, SKILL.MOSTLY_LUCK))
    registerGame(GameInfo(715, OsmosisII, "Treasure Trove",
                          STYLE.ONE_DECK_TYPE, 1, -1, SKILL.MOSTLY_LUCK))
    registerGame(GameInfo(716, PeekII, "Peek II",
                          STYLE.ONE_DECK_TYPE, 1, -1, SKILL.MOSTLY_LUCK,
                          rules_filename='treasuretrove.html'))

    registerGame(GameInfo(428, Parallels, "Parallels",
                          STYLE.TWO_DECK_TYPE, 2, 0, SKILL.BALANCED))
    registerGame(GameInfo(615, BritishBlockade, "British Blockade",
                          STYLE.TWO_DECK_TYPE, 2, 0, SKILL.BALANCED))

    registerGame(GameInfo(153, PasDeDeux, "Pas de Deux",
                          STYLE.MONTANA | STYLE.SEPARATE_DECKS, 2, 1, SKILL.MOSTLY_SKILL))

    registerGame(GameInfo(7, PictureGallery, "Picture Gallery",
                          STYLE.TWO_DECK_TYPE, 2, 0, SKILL.BALANCED,
                          altnames=("Die Bildgallerie", "Mod-3") ))
    registerGame(GameInfo(397, GreatWheel, "Great Wheel",
                          STYLE.TWO_DECK_TYPE, 2, 0, SKILL.BALANCED,
                          ranks=range(12) # without Kings
                          ))
    registerGame(GameInfo(398, MountOlympus, "Mount Olympus",
                          STYLE.TWO_DECK_TYPE, 2, 0, SKILL.BALANCED))
    registerGame(GameInfo(399, Zeus, "Zeus",
                          STYLE.TWO_DECK_TYPE, 2, 0, SKILL.BALANCED))
    registerGame(GameInfo(546, RoyalParade, "Royal Parade",
                          STYLE.TWO_DECK_TYPE, 2, 0, SKILL.MOSTLY_SKILL,
                          rules_filename='virginiareel.html'))
    registerGame(GameInfo(547, VirginiaReel, "Virginia Reel",
                          STYLE.TWO_DECK_TYPE, 2, 0, SKILL.MOSTLY_SKILL))


    # registerGame(GameInfo(341, PileOn2Decks, "PileOn (2 decks)",
    #                        STYLE.TWO_DECK_TYPE | STYLE.OPEN,, 2, 0))


    # register the game
    registerGame(GameInfo(41, PileOn, "PileOn",
                          STYLE.ONE_DECK_TYPE | STYLE.OPEN, 1, 0, SKILL.MOSTLY_SKILL,
                          altnames=("Fifteen Puzzle",) ))
    registerGame(GameInfo(289, SmallPileOn, "Small PileOn",
                          STYLE.ONE_DECK_TYPE | STYLE.OPEN | STYLE.ORIGINAL, 1, 0, SKILL.MOSTLY_SKILL,
                          ranks=(0, 5, 6, 7, 8, 9, 10, 11, 12),
                          rules_filename = "pileon.html"))
    registerGame(GameInfo(554, Foursome, "Foursome",
                          STYLE.ONE_DECK_TYPE, 1, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(555, Quartets, "Quartets",
                          STYLE.ONE_DECK_TYPE | STYLE.OPEN | STYLE.ORIGINAL, 1, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(703, FourByFour, "Four by Four",
                          STYLE.ONE_DECK_TYPE, 1, 0, SKILL.BALANCED))
    registerGame(GameInfo(740, Footling, "Footling",
                          STYLE.FREECELL | STYLE.OPEN | STYLE.ORIGINAL, 1, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(741, DoubleFootling, "Double Footling",
                          STYLE.FREECELL | STYLE.OPEN | STYLE.ORIGINAL, 2, 0, SKILL.MOSTLY_SKILL))


    registerGame(GameInfo(287, PushPin, "Push Pin",
                          STYLE.ONE_DECK_TYPE, 1, 0, SKILL.MOSTLY_LUCK))
    registerGame(GameInfo(288, RoyalMarriage, "Royal Marriage",
                          STYLE.ONE_DECK_TYPE, 1, 0, SKILL.MOSTLY_LUCK))
    ## registerGame(GameInfo(303, Queens, "Queens",
    ##                       STYLE.ONE_DECK_TYPE | STYLE.OPEN, 1, 0))
    registerGame(GameInfo(656, Accordion, "Accordion",
                          STYLE.ONE_DECK_TYPE, 1, 0, SKILL.BALANCED,
                          altnames=('Idle Year', 'Methuselah', 'Tower of Babel') ))
    registerGame(GameInfo(38, Pyramid, "Pyramid",
                          STYLE.PAIRING_TYPE, 1, 2, SKILL.MOSTLY_LUCK))
    registerGame(GameInfo(193, RelaxedPyramid, "Relaxed Pyramid",
                          STYLE.PAIRING_TYPE | STYLE.RELAXED, 1, 2, SKILL.MOSTLY_LUCK,
                          altnames=(" Pyramid's Stones",) ))
    ##registerGame(GameInfo(44, Thirteen, "Thirteen",
    ##                      STYLE.PAIRING_TYPE, 1, 0))
    registerGame(GameInfo(592, Giza, "Giza",
                          STYLE.PAIRING_TYPE | STYLE.OPEN, 1, 0, SKILL.BALANCED))
    registerGame(GameInfo(593, Thirteens, "Thirteens",
                          STYLE.PAIRING_TYPE, 1, 0, SKILL.LUCK))
    registerGame(GameInfo(594, Elevens, "Elevens",
                          STYLE.PAIRING_TYPE, 1, 0, SKILL.LUCK))
    registerGame(GameInfo(595, ElevensToo, "Elevens Too",
                          STYLE.PAIRING_TYPE, 1, 0, SKILL.LUCK))
    registerGame(GameInfo(596, SuitElevens, "Suit Elevens",
                          STYLE.PAIRING_TYPE, 1, 0, SKILL.LUCK))
    registerGame(GameInfo(597, Fifteens, "Fifteens",
                          STYLE.PAIRING_TYPE, 1, 0, SKILL.MOSTLY_LUCK))
    registerGame(GameInfo(619, TripleAlliance, "Triple Alliance",
                          STYLE.PAIRING_TYPE, 1, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(655, Pharaohs, "Pharaohs",
                          STYLE.PAIRING_TYPE, 1, 0, SKILL.BALANCED))
    registerGame(GameInfo(657, Baroness, "Baroness",
                          STYLE.PAIRING_TYPE, 1, 0, SKILL.BALANCED,
                          altnames=('Five Piles',) ))
    registerGame(GameInfo(658, Apophis, "Apophis",
                          STYLE.PAIRING_TYPE, 1, 2, SKILL.MOSTLY_LUCK))
    registerGame(GameInfo(659, Cheops, "Cheops",
                          STYLE.PAIRING_TYPE, 1, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(674, Exit, "Exit",
                          STYLE.PAIRING_TYPE, 1, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(677, TwoPyramids, "Two Pyramids",
                          STYLE.PAIRING_TYPE | STYLE.ORIGINAL, 2, 2, SKILL.MOSTLY_LUCK))
    registerGame(GameInfo(681, KingTut, "King Tut",
                          STYLE.PAIRING_TYPE, 1, -1, SKILL.MOSTLY_LUCK))
    registerGame(GameInfo(699, DoublePyramid, "Double Pyramid",
                          STYLE.PAIRING_TYPE, 2, 2, SKILL.MOSTLY_LUCK))
    registerGame(GameInfo(700, Triangle, "Triangle",
                          STYLE.PAIRING_TYPE, 1, 2, SKILL.MOSTLY_LUCK))
    registerGame(GameInfo(701, UpAndDown, "Up and Down",
                          STYLE.PAIRING_TYPE | STYLE.ORIGINAL, 2, 2, SKILL.MOSTLY_LUCK))
    registerGame(GameInfo(735, Hurricane, "Hurricane",
                          STYLE.PAIRING_TYPE, 1, 0, SKILL.MOSTLY_LUCK))
    registerGame(GameInfo(54, RoyalCotillion, "Royal Cotillion",
                          STYLE.TWO_DECK_TYPE, 2, 0, SKILL.LUCK))
    registerGame(GameInfo(55, OddAndEven, "Odd and Even",
                          STYLE.TWO_DECK_TYPE, 2, 1, SKILL.LUCK))
    registerGame(GameInfo(143, Kingdom, "Kingdom",
                          STYLE.TWO_DECK_TYPE, 2, 0, SKILL.MOSTLY_LUCK))
    registerGame(GameInfo(234, Alhambra, "Alhambra",
                          STYLE.TWO_DECK_TYPE, 2, 2, SKILL.BALANCED))
    registerGame(GameInfo(97, Carpet, "Carpet",
                          STYLE.ONE_DECK_TYPE, 1, 0, SKILL.MOSTLY_LUCK))
    registerGame(GameInfo(391, BritishConstitution, "British Constitution",
                          STYLE.TWO_DECK_TYPE, 2, 0, SKILL.BALANCED,
                          ranks=range(11), # without Queens and Kings
                          altnames=("Constitution",) ))
    registerGame(GameInfo(392, NewBritishConstitution, "New British Constitution",
                          STYLE.TWO_DECK_TYPE | STYLE.ORIGINAL, 2, 0, SKILL.BALANCED,
                          ranks=range(11) # without Queens and Kings
                          ))
    registerGame(GameInfo(443, Twenty, "Twenty",
                          STYLE.TWO_DECK_TYPE, 2, 0, SKILL.BALANCED))
    registerGame(GameInfo(465, Granada, "Granada",
                          STYLE.TWO_DECK_TYPE, 2, 2, SKILL.BALANCED))
    registerGame(GameInfo(579, ThreePirates, "Three Pirates",
                          STYLE.TWO_DECK_TYPE, 2, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(608, Frames, "Frames",
                          STYLE.TWO_DECK_TYPE, 2, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(609, GrantsReinforcement, "Grant's Reinforcement",
                          STYLE.TWO_DECK_TYPE, 2, 2, SKILL.BALANCED))
    registerGame(GameInfo(638, RoyalRendezvous, "Royal Rendezvous",
                          STYLE.TWO_DECK_TYPE, 2, 0, SKILL.BALANCED))
    registerGame(GameInfo(639, ShadyLanes, "Shady Lanes",
                          STYLE.TWO_DECK_TYPE, 2, 0, SKILL.BALANCED))
    # registerGame(GameInfo(675, FourWinds, "Four Winds",
    #                        STYLE.ONE_DECK_TYPE, 1, 1, SKILL.BALANCED))
    registerGame(GameInfo(676, BoxingTheCompass, "Boxing the Compass",
                          STYLE.TWO_DECK_TYPE, 2, 1, SKILL.BALANCED))
    registerGame(GameInfo(693, Colonel, "Colonel",
                          STYLE.TWO_DECK_TYPE, 2, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(695, TheRedAndTheBlack, "The Red and the Black",
                          STYLE.TWO_DECK_TYPE, 2, 0, SKILL.BALANCED))
    registerGame(GameInfo(748, TwilightZone, "Twilight Zone",
                          STYLE.TWO_DECK_TYPE, 2, 1, SKILL.BALANCED))
    registerGame(GameInfo(752, Reserves, "Reserves",
                          STYLE.TWO_DECK_TYPE, 2, 2, SKILL.BALANCED))

    registerGame(GameInfo(93, RoyalEast, "Royal East",
                          STYLE.ONE_DECK_TYPE, 1, 0, SKILL.BALANCED))

    registerGame(GameInfo(201, Sanibel, "Sanibel",
                          STYLE.YUKON | STYLE.CONTRIB | STYLE.ORIGINAL, 2, 0, SKILL.MOSTLY_SKILL))

    registerGame(GameInfo(118, SiebenBisAs, "Sieben bis As",
                          STYLE.MONTANA | STYLE.OPEN, 1, 0, SKILL.MOSTLY_SKILL,
                          ranks=(0, 6, 7, 8, 9, 10, 11, 12)))
    registerGame(GameInfo(144, Maze, "Maze",
                          STYLE.MONTANA | STYLE.OPEN, 1, 0, SKILL.MOSTLY_SKILL,
                          numcards=48))

    registerGame(GameInfo(436, Simplex, "Simplex",
                          STYLE.ONE_DECK_TYPE, 1, 0, SKILL.MOSTLY_LUCK))
    registerGame(GameInfo(10, RelaxedSpider, "Relaxed Spider",
                          STYLE.SPIDER | STYLE.RELAXED, 2, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(11, Spider, "Spider",
                          STYLE.SPIDER, 2, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(49, BlackWidow, "Black Widow",
                          STYLE.SPIDER, 2, 0, SKILL.MOSTLY_SKILL,
                          altnames=("Scarab",) ))
    registerGame(GameInfo(14, GroundsForADivorce, "Grounds for a Divorce",
                          STYLE.SPIDER, 2, 0, SKILL.MOSTLY_SKILL,
                          altnames=('Scheidungsgrund',) ))
    registerGame(GameInfo(114, GrandmothersGame, "Grandmother's Game",
                          STYLE.SPIDER, 2, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(24, Spiderette, "Spiderette",
                          STYLE.SPIDER, 1, 0, SKILL.BALANCED))
    registerGame(GameInfo(47, BabySpiderette, "Baby Spiderette",
                          STYLE.SPIDER, 1, 0, SKILL.BALANCED))
    registerGame(GameInfo(48, WillOTheWisp, "Will o' the Wisp",
                          STYLE.SPIDER, 1, 0, SKILL.BALANCED))
    registerGame(GameInfo(50, SimpleSimon, "Simple Simon",
                          STYLE.SPIDER | STYLE.OPEN, 1, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(194, Rachel, "Rachel",
                          STYLE.SPIDER | STYLE.XORIGINAL, 1, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(29, Scorpion, "Scorpion",
                          STYLE.SPIDER, 1, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(185, Wasp, "Wasp",
                          STYLE.SPIDER, 1, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(220, RougeEtNoir, "Rouge et Noir",
                          STYLE.GYPSY, 2, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(269, Spider1Suit, "Spider (1 suit)",
                          STYLE.SPIDER, 2, 0, SKILL.MOSTLY_SKILL,
                          suits=(0, 0, 0, 0),
                          rules_filename="spider.html"))
    registerGame(GameInfo(270, Spider2Suits, "Spider (2 suits)",
                          STYLE.SPIDER, 2, 0, SKILL.MOSTLY_SKILL,
                          suits=(0, 0, 2, 2),
                          rules_filename="spider.html"))
    registerGame(GameInfo(305, ThreeBlindMice, "Three Blind Mice",
                          STYLE.SPIDER, 1, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(309, MrsMop, "Mrs. Mop",
                          STYLE.SPIDER | STYLE.OPEN, 2, 0, SKILL.SKILL))
    registerGame(GameInfo(341, Cicely, "Cicely",
                          STYLE.SPIDER, 2, 0, SKILL.BALANCED))
    registerGame(GameInfo(342, Trillium, "Trillium",
                          STYLE.SPIDER, 2, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(343, Lily, "Lily",
                          STYLE.SPIDER, 2, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(344, Chelicera, "Chelicera",
                          STYLE.SPIDER, 1, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(345, ScorpionHead, "Scorpion Head",
                          STYLE.SPIDER, 1, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(346, ScorpionTail, "Scorpion Tail",
                          STYLE.SPIDER, 1, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(359, SpiderWeb, "Spider Web",
                          STYLE.SPIDER, 1, 0, SKILL.BALANCED))
    registerGame(GameInfo(366, SimonJester, "Simon Jester",
                          STYLE.SPIDER | STYLE.OPEN, 2, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(382, Applegate, "Applegate",
                          STYLE.SPIDER, 1, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(384, BigSpider, "Big Spider",
                          STYLE.SPIDER, 3, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(401, GroundsForADivorce3Decks, "Big Divorce",
                          STYLE.SPIDER, 3, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(441, York, "York",
                          STYLE.SPIDER | STYLE.OPEN | STYLE.ORIGINAL, 2, 0, SKILL.SKILL))
    registerGame(GameInfo(444, BigYork, "Big York",
                          STYLE.SPIDER | STYLE.OPEN | STYLE.ORIGINAL, 3, 0, SKILL.SKILL))
    registerGame(GameInfo(445, BigSpider1Suit, "Big Spider (1 suit)",
                          STYLE.SPIDER, 3, 0, SKILL.MOSTLY_SKILL,
                          suits=(0, 0, 0, 0),
                          rules_filename="bigspider.html"))
    registerGame(GameInfo(446, BigSpider2Suits, "Big Spider (2 suits)",
                          STYLE.SPIDER, 3, 0, SKILL.MOSTLY_SKILL,
                          suits=(0, 0, 2, 2),
                          rules_filename="bigspider.html"))
    registerGame(GameInfo(449, Spider3x3, "Spider 3x3",
                          STYLE.SPIDER | STYLE.ORIGINAL, 3, 0, SKILL.MOSTLY_SKILL,
                          suits=(0, 1, 2),
                          rules_filename="bigspider.html"))
    registerGame(GameInfo(454, Spider4Decks, "Spider (4 decks)",
                          STYLE.SPIDER, 4, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(455, GroundsForADivorce4Decks, "Very Big Divorce",
                          STYLE.SPIDER, 4, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(458, Spidike, "Spidike",
                          STYLE.SPIDER, 1, 0, SKILL.BALANCED)) # GT_GYPSY ?
    registerGame(GameInfo(459, FredsSpider, "Fred's Spider",
                          STYLE.SPIDER, 2, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(460, FredsSpider3Decks, "Fred's Spider (3 decks)",
                          STYLE.SPIDER, 3, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(461, OpenSpider, "Open Spider",
                          STYLE.SPIDER, 2, 0, SKILL.MOSTLY_SKILL,
                          altnames=('Beetle',) ))
    registerGame(GameInfo(501, WakeRobin, "Wake-Robin",
                          STYLE.SPIDER | STYLE.ORIGINAL, 2, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(502, TripleWakeRobin, "Wake-Robin (3 decks)",
                          STYLE.SPIDER | STYLE.ORIGINAL, 3, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(511, DoubleScorpion, "Double Scorpion",
                          STYLE.SPIDER, 2, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(512, TripleScorpion, "Triple Scorpion",
                          STYLE.SPIDER, 3, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(543, FarmersWife, "Farmer's Wife",
                          STYLE.SPIDER, 1, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(544, HowTheyRun, "How They Run",
                          STYLE.SPIDER, 1, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(570, LongTail, "Long Tail",
                          STYLE.SPIDER, 1, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(571, ShortTail, "Short Tail",
                          STYLE.SPIDER | STYLE.ORIGINAL, 2, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(670, ChineseSpider, "Chinese Spider",
                          STYLE.SPIDER, 4, 0, SKILL.MOSTLY_SKILL,
                          suits=(0, 1, 2),))
    registerGame(GameInfo(671, Incompatibility, "Incompatibility",
                          STYLE.SPIDER, 2, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(672, ScorpionII, "Scorpion II",
                          STYLE.SPIDER, 1, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(680, Tarantula, "Tarantula",
                          STYLE.SPIDER, 2, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(685, FechtersGame, "Fechter's Game",
                          STYLE.SPIDER, 2, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(710, Bebop, "Bebop",
                          STYLE.TWO_DECK_TYPE | STYLE.ORIGINAL, 2, 0, SKILL.MOSTLY_SKILL))
    #registerGame(GameInfo(000, SimpleSimonII, "Simple Simon II",
    #                      STYLE.SPIDER | STYLE.OPEN, 1, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(711, TheJollyRoger, "The Jolly Roger",
                          STYLE.SPIDER | STYLE.ORIGINAL, 2, 0, SKILL.MOSTLY_SKILL))

    registerGame(GameInfo(302, StHelena, "St. Helena",
                          STYLE.TWO_DECK_TYPE, 2, 2, SKILL.BALANCED,
                          altnames=("Napoleon's Favorite",
                                    "Washington's Favorite")
                          ))
    registerGame(GameInfo(408, BoxKite, "Box Kite",
                          STYLE.TWO_DECK_TYPE, 2, 0, SKILL.BALANCED))
    registerGame(GameInfo(620, LesQuatreCoins, "Les Quatre Coins",
                          STYLE.TWO_DECK_TYPE, 2, 2, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(621, RegalFamily, "Regal Family",
                          STYLE.TWO_DECK_TYPE, 2, 0, SKILL.BALANCED))

    registerGame(GameInfo(330, Sultan, "Sultan",
                          STYLE.TWO_DECK_TYPE, 2, 2, SKILL.MOSTLY_LUCK,
                          altnames=("Sultan of Turkey",) ))
    registerGame(GameInfo(331, SultanPlus, "Sultan +",
                          STYLE.TWO_DECK_TYPE, 2, 2, SKILL.MOSTLY_LUCK))
    registerGame(GameInfo(354, Boudoir, "Boudoir",
                          STYLE.TWO_DECK_TYPE, 2, 2, SKILL.MOSTLY_LUCK))
    registerGame(GameInfo(410, CaptiveQueens, "Captive Queens",
                          STYLE.ONE_DECK_TYPE, 1, 2, SKILL.MOSTLY_LUCK,
                          altnames=("Quadrille",) ))
    registerGame(GameInfo(418, Contradance, "Contradance",
                          STYLE.TWO_DECK_TYPE, 2, 1, SKILL.LUCK,
                          altnames=("Cotillion",) ))
    registerGame(GameInfo(419, IdleAces, "Idle Aces",
                          STYLE.TWO_DECK_TYPE, 2, 2, SKILL.MOSTLY_LUCK))
    registerGame(GameInfo(423, LadyOfTheManor, "Lady of the Manor",
                          STYLE.TWO_DECK_TYPE, 2, 0, SKILL.MOSTLY_LUCK,
                          altnames=("Vassal", "La Chatelaine") ))
    registerGame(GameInfo(424, Matrimony, "Matrimony",
                          STYLE.TWO_DECK_TYPE, 2, 16, SKILL.MOSTLY_LUCK))
    registerGame(GameInfo(429, Patriarchs, "Patriarchs",
                          STYLE.TWO_DECK_TYPE, 2, 1, SKILL.MOSTLY_LUCK))
    registerGame(GameInfo(438, SixesAndSevens, "Sixes and Sevens",
                          STYLE.TWO_DECK_TYPE, 2, 0, SKILL.MOSTLY_LUCK))
    registerGame(GameInfo(477, CornerSuite, "Corner Suite",
                          STYLE.TWO_DECK_TYPE, 1, 0, SKILL.MOSTLY_LUCK))
    registerGame(GameInfo(559, Marshal, "Marshal",
                          STYLE.TWO_DECK_TYPE, 2, 0, SKILL.BALANCED))
    registerGame(GameInfo(565, RoyalAids, "Royal Aids",
                          STYLE.TWO_DECK_TYPE, 2, UNLIMITED_REDEALS, SKILL.BALANCED))
    registerGame(GameInfo(598, PicturePatience, "Picture Patience",
                          STYLE.TWO_DECK_TYPE, 2, 0, SKILL.MOSTLY_LUCK,
                          rules_filename="patriarchs.html"))
    registerGame(GameInfo(635, CircleEight, "Circle Eight",
                          STYLE.ONE_DECK_TYPE, 1, 1, SKILL.MOSTLY_LUCK))
    registerGame(GameInfo(646, Adela, "Adela",
                          STYLE.TWO_DECK_TYPE, 2, 0, SKILL.MOSTLY_LUCK))
    registerGame(GameInfo(660, Toni, "Toni",
                          STYLE.TWO_DECK_TYPE, 2, 2, SKILL.MOSTLY_LUCK))
    registerGame(GameInfo(691, Khedive, "Khedive",
                          STYLE.TWO_DECK_TYPE, 2, 0, SKILL.MOSTLY_LUCK))
    registerGame(GameInfo(729, TwoRings, "Two Rings",
                          STYLE.TWO_DECK_TYPE, 2, 1, SKILL.MOSTLY_LUCK))
    registerGame(GameInfo(730, Phalanx, "Phalanx",
                          STYLE.ONE_DECK_TYPE, 1, 0, SKILL.MOSTLY_LUCK))
    registerGame(GameInfo(742, Grandee, "Grandee",
                          STYLE.TWO_DECK_TYPE, 2, 0, SKILL.BALANCED))
    registerGame(GameInfo(743, Turncoats, "Turncoats",
                          STYLE.ONE_DECK_TYPE, 1, 0, SKILL.BALANCED))
    registerGame(GameInfo(744, Voracious, "Voracious",
                          STYLE.TWO_DECK_TYPE, 2, 0, SKILL.BALANCED))
    registerGame(GameInfo(745, DesertIsland, "Desert Island",
                          STYLE.TWO_DECK_TYPE | STYLE.ORIGINAL, 2, 0, SKILL.BALANCED))
    registerGame(GameInfo(761, CatherineTheGreat, "Catherine the Great",
                          STYLE.TWO_DECK_TYPE, 2, 0, SKILL.BALANCED))
    registerGame(GameInfo(334, TakeAway, "Take Away",
                          STYLE.ONE_DECK_TYPE | STYLE.OPEN, 1, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(335, FourStacks, "Four Stacks",
                          STYLE.ONE_DECK_TYPE | STYLE.OPEN, 1, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(654, Striptease, "Striptease",
                          STYLE.ONE_DECK_TYPE, 1, 0, SKILL.MOSTLY_SKILL))

    registerGame(GameInfo(135, Terrace, "Terrace",
                          STYLE.TERRACE, 2, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(136, GeneralsPatience, "General's Patience",
                          STYLE.TERRACE, 2, 0, SKILL.MOSTLY_LUCK))
    registerGame(GameInfo(137, BlondesAndBrunettes, "Blondes and Brunettes",
                          STYLE.TERRACE, 2, 0, SKILL.MOSTLY_LUCK))
    registerGame(GameInfo(138, FallingStar, "Falling Star",
                          STYLE.TERRACE, 2, 0, SKILL.MOSTLY_LUCK))
    registerGame(GameInfo(431, QueenOfItaly, "Queen of Italy",
                          STYLE.TERRACE, 2, 0, SKILL.BALANCED))
    registerGame(GameInfo(499, Signora, "Signora",
                          STYLE.TERRACE, 2, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(500, Madame, "Madame",
                          STYLE.TERRACE, 3, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(533, MamySusan, "Mamy Susan",
                          STYLE.TERRACE, 2, 0, SKILL.BALANCED))
    registerGame(GameInfo(582, Wood, "Wood",
                          STYLE.TERRACE, 2, 0, SKILL.BALANCED))
    registerGame(GameInfo(637, BastilleDay, "Bastille Day",
                          STYLE.TERRACE, 2, 0, SKILL.BALANCED))

    registerGame(GameInfo(22216, ThreePeaks, "Three Peaks",
                          STYLE.PAIRING_TYPE | STYLE.SCORE, 1, 0, SKILL.BALANCED,
                          altnames=("Tri Peaks",)
                          ))
    registerGame(GameInfo(22231, ThreePeaksNoScore, "Three Peaks Non-scoring",
                          STYLE.PAIRING_TYPE, 1, 0, SKILL.BALANCED))


    registerGame(GameInfo(303, Tournament, "Tournament",
                          STYLE.TWO_DECK_TYPE, 2, 2, SKILL.MOSTLY_LUCK))
    registerGame(GameInfo(304, LaNivernaise, "La Nivernaise",
                          STYLE.TWO_DECK_TYPE, 2, 2, SKILL.MOSTLY_LUCK,
                          altnames = ("Napoleon's Flank", ),))
    registerGame(GameInfo(386, KingsdownEights, "Kingsdown Eights",
                          STYLE.TWO_DECK_TYPE, 2, 0, SKILL.BALANCED))
    registerGame(GameInfo(645, Saxony, "Saxony",
                          STYLE.TWO_DECK_TYPE, 2, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(652, LadiesBattle, "Ladies Battle",
                          STYLE.ONE_DECK_TYPE, 1, 0, SKILL.MOSTLY_LUCK))




    registerGame(GameInfo(35, UnionSquare, "Union Square",
                          STYLE.TWO_DECK_TYPE, 2, 0, SKILL.MOSTLY_SKILL,
                          altnames=('British Square',),
                          ))
    registerGame(GameInfo(439, SolidSquare, "Solid Square",
                          STYLE.TWO_DECK_TYPE, 2, 0, SKILL.BALANCED))
    registerGame(GameInfo(738, Boomerang, "Boomerang",
                          STYLE.TWO_DECK_TYPE, 2, 0, SKILL.BALANCED,
                          ranks=(0, 6, 7, 8, 9, 10, 11, 12),
                          ))
    registerGame(GameInfo(314, WaveMotion, "Wave Motion",
                          STYLE.ONE_DECK_TYPE | STYLE.OPEN, 1, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(753, Flourish, "Flourish",
                          STYLE.ONE_DECK_TYPE | STYLE.OPEN | STYLE.ORIGINAL, 1, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(30, Windmill, "Windmill",
                          STYLE.TWO_DECK_TYPE, 2, 0, SKILL.MOSTLY_LUCK))
    registerGame(GameInfo(277, NapoleonsTomb, "Napoleon's Tomb",
                          STYLE.ONE_DECK_TYPE, 1, 0, SKILL.MOSTLY_LUCK))
    registerGame(GameInfo(417, Corners, "Corners",
                          STYLE.ONE_DECK_TYPE, 1, 2, SKILL.MOSTLY_LUCK,
                          rules_filename='fourseasons.html'))
    registerGame(GameInfo(437, Simplicity, "Simplicity",
                          STYLE.ONE_DECK_TYPE, 1, 0, SKILL.MOSTLY_LUCK,
                          rules_filename='fourseasons.html'))
    registerGame(GameInfo(483, Czarina, "Czarina",
                          STYLE.ONE_DECK_TYPE, 1, 0, SKILL.MOSTLY_LUCK,
                          rules_filename='fourseasons.html'))
    registerGame(GameInfo(484, FourSeasons, "Four Seasons",
                          STYLE.ONE_DECK_TYPE, 1, 0, SKILL.MOSTLY_LUCK,
                          altnames=('Corner Card', 'Vanishing Cross') ))
    registerGame(GameInfo(561, DutchSolitaire, "Dutch Solitaire",
                          STYLE.TWO_DECK_TYPE, 2, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(696, FlorentinePatience, "Florentine Patience",
                          STYLE.ONE_DECK_TYPE, 1, 1, SKILL.MOSTLY_LUCK))

    registerGame(GameInfo(19, Yukon, "Yukon",
                          STYLE.YUKON, 1, 0, SKILL.BALANCED))
    registerGame(GameInfo(20, RussianSolitaire, "Russian Solitaire",
                          STYLE.YUKON, 1, 0, SKILL.BALANCED))
    registerGame(GameInfo(27, Odessa, "Odessa",
                          STYLE.YUKON, 1, 0, SKILL.BALANCED))
    registerGame(GameInfo(278, Grandfather, "Grandfather",
                          STYLE.YUKON, 1, 2, SKILL.BALANCED))
    registerGame(GameInfo(186, Alaska, "Alaska",
                          STYLE.YUKON, 1, 0, SKILL.BALANCED))
    registerGame(GameInfo(187, ChineseDiscipline, "Chinese Discipline",
                          STYLE.YUKON | STYLE.XORIGINAL, 1, 0, SKILL.BALANCED))
    registerGame(GameInfo(188, ChineseSolitaire, "Chinese Solitaire",
                          STYLE.YUKON | STYLE.XORIGINAL, 1, 0, SKILL.BALANCED))
    registerGame(GameInfo(189, Queenie, "Queenie",
                          STYLE.YUKON | STYLE.XORIGINAL, 1, 0, SKILL.BALANCED))
    registerGame(GameInfo(190, Rushdike, "Rushdike",
                          STYLE.YUKON | STYLE.XORIGINAL, 1, 0, SKILL.BALANCED))
    registerGame(GameInfo(191, RussianPoint, "Russian Point",
                          STYLE.YUKON | STYLE.XORIGINAL, 1, 0, SKILL.BALANCED))
    registerGame(GameInfo(192, Abacus, "Abacus",
                          STYLE.YUKON | STYLE.XORIGINAL, 1, 0, SKILL.BALANCED))
    registerGame(GameInfo(271, DoubleYukon, "Double Yukon",
                          STYLE.YUKON, 2, 0, SKILL.BALANCED))
    registerGame(GameInfo(272, TripleYukon, "Triple Yukon",
                          STYLE.YUKON, 3, 0, SKILL.BALANCED))
    registerGame(GameInfo(284, TenAcross, "Ten Across",
                          STYLE.YUKON, 1, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(285, Panopticon, "Panopticon",
                          STYLE.YUKON | STYLE.ORIGINAL, 1, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(339, Moosehide, "Moosehide",
                          STYLE.YUKON, 1, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(387, Roslin, "Roslin",
                          STYLE.YUKON, 1, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(447, AustralianPatience, "Australian Patience",
                          STYLE.YUKON, 1, 0, SKILL.BALANCED))
    registerGame(GameInfo(450, RawPrawn, "Raw Prawn",
                          STYLE.YUKON, 1, 0, SKILL.BALANCED))
    registerGame(GameInfo(456, BimBom, "Bim Bom",
                          STYLE.YUKON | STYLE.ORIGINAL, 2, 0, SKILL.BALANCED))
    registerGame(GameInfo(466, DoubleRussianSolitaire, "Double Russian Solitaire",
                          STYLE.YUKON, 2, 0, SKILL.BALANCED))
    registerGame(GameInfo(488, TripleRussianSolitaire, "Triple Russian Solitaire",
                          STYLE.YUKON, 3, 0, SKILL.BALANCED))
    registerGame(GameInfo(492, Geoffrey, "Geoffrey",
                          STYLE.YUKON, 1, 0, SKILL.MOSTLY_SKILL))
    registerGame(GameInfo(525, Queensland, "Queensland",
                          STYLE.YUKON, 1, 0, SKILL.BALANCED))
    registerGame(GameInfo(526, OutbackPatience, "Outback Patience",
                          STYLE.YUKON, 1, 0, SKILL.BALANCED))
    registerGame(GameInfo(530, RussianSpider, "Russian Spider",
                          STYLE.SPIDER, 1, 0, SKILL.BALANCED,
                          altnames=('Ukrainian Solitaire',) ))
    registerGame(GameInfo(531, DoubleRussianSpider, "Double Russian Spider",
                          STYLE.SPIDER | STYLE.ORIGINAL, 2, 0, SKILL.BALANCED))
    registerGame(GameInfo(603, Brisbane, "Brisbane",
                          STYLE.SPIDER, 1, 0, SKILL.BALANCED))
    registerGame(GameInfo(707, Hawaiian, "Hawaiian",
                          STYLE.TWO_DECK_TYPE | STYLE.ORIGINAL, 2, 0, SKILL.BALANCED))
    registerGame(GameInfo(732, Wave, "Wave",
                          STYLE.TWO_DECK_TYPE | STYLE.ORIGINAL, 2, 0, SKILL.BALANCED))
    registerGame(GameInfo(467, Zodiac, "Zodiac",
                          STYLE.TWO_DECK_TYPE, 2, -1, SKILL.BALANCED))
    registerGame(GameInfo(722, TwelveSleepingMaids, "Twelve Sleeping Maids",
                          STYLE.TWO_DECK_TYPE, 2, 2, SKILL.BALANCED))

    def r_shisen(id, gameclass, name, rules_filename="shisensho.html"):
        decks, ranks, trumps = comp_cardset(gameclass.NCARDS)
        gi = GameInfo(id, gameclass, name,
                      STYLE.SHISEN_SHO, 4*decks, 0, SKILL.MOSTLY_SKILL,
                      category=CATEGORY.MAHJONGG, short_name=name,
                      suits=range(3), ranks=range(ranks), trumps=range(trumps),
                      numcards=gameclass.NCARDS)
        gi.ncards = gameclass.NCARDS
        gi.rules_filename = rules_filename
        registerGame(gi)
        return gi

    #r_shisen(11001, Shisen_14x6, "Shisen-Sho 14x6")
    r_shisen(11001, Shisen_14x6, "Shisen-Sho 14x6")
    r_shisen(11002, Shisen_18x8, "Shisen-Sho 18x8")
    r_shisen(11003, Shisen_24x12, "Shisen-Sho 24x12")
    r_shisen(11004, Shisen_14x6_NoGravity, "Shisen-Sho (No Gravity) 14x6")
    r_shisen(11005, Shisen_18x8_NoGravity, "Shisen-Sho (No Gravity) 18x8")
    r_shisen(11006, Shisen_24x12_NoGravity, "Shisen-Sho (No Gravity) 24x12")
    r_shisen(11011, NotShisen_14x6, "Not Shisen-Sho 14x6", "notshisensho.html")
    r_shisen(11012, NotShisen_18x8, "Not Shisen-Sho 18x8", "notshisensho.html")
    r_shisen(11013, NotShisen_24x12, "Not Shisen-Sho 24x12", "notshisensho.html")

    del r_shisen

    registerGame(GameInfo(124, TowerOfHanoy, "Tower of Hanoy",
                          STYLE.PUZZLE_TYPE, 1, 0, SKILL.SKILL,
                          suits=(2,), ranks=range(9)))
    registerGame(GameInfo(207, HanoiPuzzle4, "Hanoi Puzzle 4",
                          STYLE.PUZZLE_TYPE, 1, 0, SKILL.SKILL,
                          suits=(2,), ranks=range(4),
                          rules_filename="hanoipuzzle.html"))
    registerGame(GameInfo(208, HanoiPuzzle5, "Hanoi Puzzle 5",
                          STYLE.PUZZLE_TYPE, 1, 0, SKILL.SKILL,
                          suits=(2,), ranks=range(5),
                          rules_filename="hanoipuzzle.html"))
    registerGame(GameInfo(209, HanoiPuzzle6, "Hanoi Puzzle 6",
                          STYLE.PUZZLE_TYPE, 1, 0, SKILL.SKILL,
                          suits=(2,), ranks=range(6),
                          rules_filename="hanoipuzzle.html"))

    registerGame(GameInfo(176, Memory24, "Memory 24",
                          STYLE.MEMORY | STYLE.SCORE, 2, 0, SKILL.SKILL,
                          suits=(0,2), ranks=(0,8,9,10,11,12)))
    registerGame(GameInfo(219, Memory30, "Memory 30",
                          STYLE.MEMORY | STYLE.SCORE, 2, 0, SKILL.SKILL,
                          suits=(0,2,3), ranks=(0,9,10,11,12)))
    registerGame(GameInfo(177, Memory40, "Memory 40",
                          STYLE.MEMORY | STYLE.SCORE, 2, 0, SKILL.SKILL,
                          suits=(0,2), ranks=(0,4,5,6,7,8,9,10,11,12)))
    registerGame(GameInfo(178, Concentration, "Concentration",
                          STYLE.MEMORY | STYLE.SCORE, 1, 0, SKILL.SKILL))

    def register(id, gameclass, name):
        ncards = 0
        for n in gameclass.ROWS:
            ncards += n
        ncards -= 1
        gi = GameInfo(id, gameclass, name,
                      STYLE.PUZZLE_TYPE, 1, 0, SKILL.SKILL,
                      category=CATEGORY.TRUMP_ONLY,
                      suits=(), ranks=(), trumps=range(ncards),
                      numcards=ncards,
                      rules_filename = "pegged.html")
        registerGame(gi)
        return gi

    register(180, Pegged, "Pegged")
    register(181, PeggedCross1, "Pegged Cross 1")
    register(182, PeggedCross2, "Pegged Cross 2")
    register(183, Pegged6x6, "Pegged 6x6")
    register(184, Pegged7x7, "Pegged 7x7")
    register(210, PeggedTriangle1, "Pegged Triangle 1")
    register(211, PeggedTriangle2, "Pegged Triangle 2")

    registerGame(GameInfo(139, PokerSquare, "Poker Square",
                          STYLE.POKER_TYPE | STYLE.SCORE, 1, 0, SKILL.MOSTLY_SKILL,
                          numcards=25))
    registerGame(GameInfo(140, PokerShuffle, "Poker Shuffle",
                          STYLE.POKER_TYPE | STYLE.SCORE | STYLE.OPEN, 1, 0, SKILL.MOSTLY_SKILL,
                          numcards=25))

    def r(id, gameclass, name, game_type, decks, redeals, skill_level):
        game_type = game_type | STYLE.TAROCK | STYLE.CONTRIB | STYLE.ORIGINAL
        gi = GameInfo(id, gameclass, name, game_type, decks, redeals, skill_level,
                      ranks=range(14), trumps=range(22))
        registerGame(gi)
        return gi

    r(157, WheelOfFortune, "Wheel of Fortune", STYLE.TAROCK, 1, 0, SKILL.BALANCED)
    r(158, ImperialTrumps, "Imperial Trumps", STYLE.TAROCK, 1, -1, SKILL.BALANCED)
    r(159, Pagat, "Pagat", STYLE.TAROCK | STYLE.OPEN, 1, 0, SKILL.MOSTLY_SKILL)
    r(160, Skiz, "Skiz", STYLE.TAROCK | STYLE.OPEN, 1, 0, SKILL.MOSTLY_SKILL)
    r(161, FifteenPlus, "Fifteen plus", STYLE.TAROCK, 1, 0, SKILL.BALANCED)
    r(162, Excuse, "Excuse", STYLE.TAROCK | STYLE.OPEN, 1, 0, SKILL.BALANCED)
    r(163, Grasshopper, "Grasshopper", STYLE.TAROCK, 1, 1, SKILL.MOSTLY_SKILL)
    r(164, DoubleGrasshopper, "Double Grasshopper", STYLE.TAROCK, 2, 1, SKILL.MOSTLY_SKILL)
    r(179, Ponytail, "Ponytail", STYLE.TAROCK, 2, 2, SKILL.MOSTLY_SKILL)
    r(202, Cavalier, "Cavalier", STYLE.TAROCK, 1, 0, SKILL.MOSTLY_SKILL)
    r(203, FiveAces, "Five Aces", STYLE.TAROCK, 1, 0, SKILL.MOSTLY_SKILL)
    r(204, Wicked, "Wicked", STYLE.TAROCK | STYLE.OPEN, 1, -1, SKILL.BALANCED)
    r(205, Nasty, "Nasty", STYLE.TAROCK | STYLE.OPEN, 1, -1, SKILL.BALANCED)

    del r

    def r(id, gameclass, name, game_type, decks, redeals, skill_level):
        game_type = game_type | STYLE.DASHAVATARA_GANJIFA
        gi = GameInfo(id, gameclass, name, game_type, decks, redeals, skill_level,
                      suits=range(10), ranks=range(12))
        registerGame(gi)
        return gi

    r(15406, Matsya, "Matsya", STYLE.DASHAVATARA_GANJIFA, 1, 0, SKILL.BALANCED)
    r(15407, Kurma, "Kurma", STYLE.DASHAVATARA_GANJIFA, 1, -1, SKILL.BALANCED)
    r(15408, Varaha, "Varaha", STYLE.DASHAVATARA_GANJIFA, 1, -1, SKILL.BALANCED)
    r(15409, Narasimha, "Narasimha", STYLE.DASHAVATARA_GANJIFA, 1, 0, SKILL.BALANCED)
    r(15410, Vamana, "Vamana", STYLE.DASHAVATARA_GANJIFA, 1, -1, SKILL.BALANCED)
    r(15411, Parashurama, "Parashurama", STYLE.DASHAVATARA_GANJIFA, 1, 1, SKILL.BALANCED)
    r(15412, TenAvatars, "Ten Avatars", STYLE.DASHAVATARA_GANJIFA, 1, 0, SKILL.MOSTLY_SKILL)
    r(15413, DashavataraCircles, "Dashavatara Circles", STYLE.DASHAVATARA_GANJIFA, 1, 0, SKILL.MOSTLY_SKILL)
    r(15414, Balarama, "Balarama", STYLE.DASHAVATARA_GANJIFA, 1, 0, SKILL.MOSTLY_SKILL)
    r(15415, Hayagriva, "Hayagriva", STYLE.DASHAVATARA_GANJIFA, 1, 0, SKILL.MOSTLY_SKILL)
    r(15416, Shanka, "Shanka", STYLE.DASHAVATARA_GANJIFA, 1, 0, SKILL.MOSTLY_SKILL)
    r(15417, Journey, "Journey to Cuddapah", STYLE.DASHAVATARA_GANJIFA, 1, 2, SKILL.BALANCED)
    r(15418, LongJourney, "Long Journey to Cuddapah", STYLE.DASHAVATARA_GANJIFA, 2, 2, SKILL.BALANCED)
    r(15419, Surukh, "Surukh", STYLE.DASHAVATARA_GANJIFA, 1, 0, SKILL.BALANCED)
    r(15420, AppachansWaterfall, "Appachan's Waterfall", STYLE.DASHAVATARA_GANJIFA, 1, 0, SKILL.MOSTLY_SKILL)
    r(15421, Hiranyaksha, 'Hiranyaksha', STYLE.DASHAVATARA_GANJIFA, 1, 0, SKILL.MOSTLY_SKILL)
    r(15422, Dashavatara, 'Dashavatara', STYLE.DASHAVATARA_GANJIFA, 1, 0, SKILL.BALANCED)

    del r

    def r(id, gameclass, name, game_type, decks, redeals, skill_level):
        game_type = game_type | STYLE.HANAFUDA
        gi = GameInfo(id, gameclass, name, game_type, decks, redeals, skill_level,
                      suits=range(12), ranks=range(4))
        registerGame(gi)
        return gi

    r(12345, Oonsoo, "Oonsoo", STYLE.HANAFUDA, 1, 0, SKILL.MOSTLY_SKILL)
    r(12346, MatsuKiri, "MatsuKiri", STYLE.HANAFUDA | STYLE.OPEN, 1, 0, SKILL.MOSTLY_SKILL)
    r(12372, MatsuKiriStrict, 'MatsuKiri Strict', STYLE.HANAFUDA | STYLE.OPEN, 1, 0, SKILL.MOSTLY_SKILL)
    r(12347, Gaji, "Gaji", STYLE.HANAFUDA | STYLE.OPEN, 1, 0, SKILL.MOSTLY_SKILL)
    r(12348, FlowerClock, "Flower Clock", STYLE.HANAFUDA | STYLE.OPEN, 1, 0, SKILL.MOSTLY_SKILL)
    r(12349, Pagoda, "Pagoda", STYLE.HANAFUDA, 2, 0, SKILL.BALANCED)
    r(12350, Samuri, "Samuri", STYLE.HANAFUDA, 1, 0, SKILL.BALANCED)
    r(12351, GreatWall, "Great Wall", STYLE.HANAFUDA, 4, 0, SKILL.MOSTLY_SKILL)
    r(12352, FourWinds, "Hanafuda Four Winds", STYLE.HANAFUDA, 1, 1, SKILL.MOSTLY_SKILL)
    r(12353, Sumo, "Sumo", STYLE.HANAFUDA, 1, 0, SKILL.MOSTLY_SKILL)
    r(12354, BigSumo, "Big Sumo", STYLE.HANAFUDA, 2, 0, SKILL.MOSTLY_SKILL)
    r(12355, LittleEasy, "Little Easy", STYLE.HANAFUDA, 1, -1, SKILL.BALANCED)
    r(12356, BigEasy, "Big Easy", STYLE.HANAFUDA, 2, -1, SKILL.BALANCED)
    r(12357, EasySupreme, "Easy Supreme", STYLE.HANAFUDA, 4, -1, SKILL.BALANCED)
    r(12358, JustForFun, "Just For Fun", STYLE.HANAFUDA, 1, 0, SKILL.MOSTLY_SKILL)
    r(12359, Firecracker, "Firecracker", STYLE.HANAFUDA, 1, 0, SKILL.BALANCED)
    r(12360, EasyX1, "Easy x One", STYLE.HANAFUDA, 1, 1, SKILL.BALANCED)
    r(12361, Relax, "Relax", STYLE.HANAFUDA, 1, 1, SKILL.BALANCED)
    r(12362, DoubleSamuri, "Double Samuri", STYLE.HANAFUDA, 2, 0, SKILL.BALANCED)
    r(12363, SuperSamuri, "Super Samuri", STYLE.HANAFUDA, 4, 0, SKILL.BALANCED)
    r(12364, DoubleYourFun, "Double Your Fun", STYLE.HANAFUDA, 2, 0, SKILL.MOSTLY_SKILL)
    r(12365, CherryBomb, "Cherry Bomb", STYLE.HANAFUDA, 2, 0, SKILL.BALANCED)
    r(12366, OonsooToo, "Oonsoo Too", STYLE.HANAFUDA, 1, 0, SKILL.MOSTLY_SKILL)
    r(12367, OonsooStrict, "Oonsoo Strict", STYLE.HANAFUDA, 1, 0, SKILL.MOSTLY_SKILL)
    r(12368, OonsooOpen, "Oonsoo Open", STYLE.HANAFUDA, 1, 0, SKILL.MOSTLY_SKILL)
    r(12379, OonsooTimesTwo, "Oonsoo Times Two", STYLE.HANAFUDA, 2, 0, SKILL.MOSTLY_SKILL)

    del r

    def r(id, gameclass, name, game_type, decks, redeals, skill_level):
        game_type = game_type | STYLE.HANAFUDA
        gi = GameInfo(id, gameclass, name, game_type, decks, redeals, skill_level,
                      suits=range(12), ranks=range(4))
        registerGame(gi)
        return gi

    r(12369, Paulownia, 'Paulownia', STYLE.HANAFUDA, 1, -1, SKILL.BALANCED)
    r(12370, LesserQueue, 'Lesser Queue', STYLE.HANAFUDA, 2, 2, SKILL.BALANCED)
    r(12371, GreaterQueue, 'Greater Queue', STYLE.HANAFUDA, 4, 2, SKILL.BALANCED)
    r(12373, JapaneseGarden, 'Japanese Garden', STYLE.HANAFUDA | STYLE.OPEN, 1, 0, SKILL.MOSTLY_SKILL)
    r(12374, JapaneseGardenII, 'Japanese Garden II', STYLE.HANAFUDA | STYLE.OPEN, 1, 0, SKILL.MOSTLY_SKILL)
    r(12375, SixSages, 'Six Sages', STYLE.HANAFUDA | STYLE.OPEN, 1, 0, SKILL.MOSTLY_SKILL)
    r(12376, SixTengus, 'Six Tengus', STYLE.HANAFUDA | STYLE.OPEN, 1, 0, SKILL.MOSTLY_SKILL)
    r(12377, JapaneseGardenIII, 'Japanese Garden III', STYLE.HANAFUDA | STYLE.OPEN, 1, 0, SKILL.MOSTLY_SKILL)
    r(12378, HanafudaFourSeasons, 'Hanafuda Four Seasons', STYLE.HANAFUDA | STYLE.OPEN, 1, 0, SKILL.MOSTLY_SKILL)
    r(12380, Eularia, 'Eularia', STYLE.HANAFUDA, 1, -1, SKILL.BALANCED)
    r(12381, Peony, 'Peony', STYLE.HANAFUDA, 1, -1, SKILL.BALANCED)
    r(12382, Iris, 'Iris', STYLE.HANAFUDA, 1, 0, SKILL.BALANCED)
    r(12383, Pine, 'Pine', STYLE.HANAFUDA, 1, 0, SKILL.BALANCED)
    r(12384, Wisteria, 'Wisteria', STYLE.HANAFUDA, 1, 0, SKILL.MOSTLY_SKILL)
    r(12385, FlowerArrangement, 'Flower Arrangement', STYLE.HANAFUDA, 2, 0, SKILL.BALANCED)

    del r

    def r(id, gameclass, name, game_type, decks, redeals, skill_level):
        game_type = game_type | STYLE.HEXADECK
        gi = GameInfo(id, gameclass, name, game_type, decks, redeals, skill_level,
                      suits=range(4), ranks=range(16), trumps=range(4))
        registerGame(gi)
        return gi

    r(165, BitsNBytes, 'Bits n Bytes', STYLE.HEXADECK, 1, 1, SKILL.BALANCED)
    r(166, HexAKlon, 'Hex A Klon', STYLE.HEXADECK, 1, -1, SKILL.BALANCED)
    r(16666, KlondikePlus16, 'Klondike Plus 16', STYLE.HEXADECK, 1, 1, SKILL.BALANCED)
    r(16667, HexAKlonByThrees, 'Hex A Klon by Threes', STYLE.HEXADECK, 1, -1, SKILL.BALANCED)
    r(16668, KingOnlyHexAKlon, 'King Only Hex A Klon', STYLE.HEXADECK, 1, -1, SKILL.BALANCED)
    r(16669, TheFamiliar, 'The Familiar', STYLE.HEXADECK, 1, 1, SKILL.BALANCED)
    r(16670, TwoFamiliars, 'Two Familiars', STYLE.HEXADECK, 2, 1, SKILL.BALANCED)
    r(16671, TenByEight, '10 x 8', STYLE.HEXADECK, 2, -1, SKILL.BALANCED)
    r(16672, Drawbridge, 'Drawbridge', STYLE.HEXADECK, 1, 1, SKILL.BALANCED)
    r(16673, DoubleDrawbridge, 'Double Drawbridge', STYLE.HEXADECK, 2, 1, SKILL.BALANCED)
    r(16674, HiddenPassages, 'Hidden Passages', STYLE.HEXADECK, 1, 1, SKILL.MOSTLY_LUCK)
    r(16675, CluitjarsLair, 'Cluitjar\'s Lair', STYLE.HEXADECK, 1, 0, SKILL.BALANCED)
    r(16676, MerlinsMeander, 'Merlin\'s Meander', STYLE.HEXADECK, 2, 2, SKILL.BALANCED)
    r(16677, MagesGame, 'Mage\'s Game', STYLE.HEXADECK, 1, 0, SKILL.BALANCED)
    r(16678, Convolution, 'Convolution', STYLE.HEXADECK, 2, 0, SKILL.MOSTLY_SKILL)
    r(16679, Labyrinth, 'Hex Labyrinth', STYLE.HEXADECK, 2, 0, SKILL.MOSTLY_SKILL)
    r(16680, Snakestone, 'Snakestone', STYLE.HEXADECK, 2, 0, SKILL.MOSTLY_SKILL)

    del r

    registerGame(GameInfo(13001, KatrinasGame, "Katrina's Game",
                          STYLE.TAROCK, 2, 1, SKILL.BALANCED,
                          ranks = range(14), trumps = range(22)))
    registerGame(GameInfo(13002, BridgetsGame, "Bridget's Game",
                          STYLE.HEXADECK, 2, 1, SKILL.BALANCED,
                          ranks = range(16), trumps = range(4)))
    registerGame(GameInfo(13003, FatimehsGame, "Fatimeh's Game",
                          STYLE.MUGHAL_GANJIFA, 1, 2, SKILL.BALANCED,
                          suits = range(8), ranks = range(12)))
    registerGame(GameInfo(13004, KalisGame, "Kali's Game",
                          STYLE.DASHAVATARA_GANJIFA, 1, 2, SKILL.BALANCED,
                          suits = range(10), ranks = range(12)))
    registerGame(GameInfo(13005, DojoujisGame, "Dojouji's Game",
                          STYLE.HANAFUDA, 2, 0, SKILL.BALANCED,
                          suits = range(12), ranks = range(4)))
    registerGame(GameInfo(13008, RelaxedKatrinasGame, "Katrina's Game Relaxed",
                          STYLE.TAROCK, 2, 1, SKILL.BALANCED,
                          ranks = range(14), trumps = range(22)))
    registerGame(GameInfo(13009, DoubleKatrinasGame, "Katrina's Game Doubled",
                          STYLE.TAROCK, 4, 2, SKILL.BALANCED,
                          ranks = range(14), trumps = range(22)))
    registerGame(GameInfo(13010, DoubleBridgetsGame, "Bridget's Game Doubled",
                          STYLE.HEXADECK, 4, 2, SKILL.BALANCED,
                          ranks = range(16), trumps = range(4)))
    registerGame(GameInfo(13011, RelaxedKalisGame, "Kali's Game Relaxed",
                          STYLE.DASHAVATARA_GANJIFA, 1, 2, SKILL.BALANCED,
                          suits = range(10), ranks = range(12)))
    registerGame(GameInfo(13012, DoubleKalisGame, "Kali's Game Doubled",
                          STYLE.DASHAVATARA_GANJIFA, 2, 3, SKILL.BALANCED,
                          suits = range(10), ranks = range(12)))
    registerGame(GameInfo(13013, RelaxedFatimehsGame, "Fatimeh's Game Relaxed",
                          STYLE.MUGHAL_GANJIFA, 1, 2, SKILL.BALANCED,
                          suits = range(8), ranks = range(12)))
    registerGame(GameInfo(13014, DoubleDojoujisGame, "Dojouji's Game Doubled",
                          STYLE.HANAFUDA, 4, 0, SKILL.BALANCED,
                          suits = range(12), ranks = range(4)))

    def register(id, gameclass, short_name):
        name = short_name
        ncards = int(name[:2]) * int(name[:2])
        gi = GameInfo(id, gameclass, name,
                    STYLE.MATRIX, 1, 0, SKILL.SKILL,
                    category=CATEGORY.TRUMP_ONLY, short_name=short_name,
                    suits=(), ranks=(), trumps=range(ncards),
                    numcards=ncards)
        gi.ncards = ncards
        gi.rules_filename = "matrix.html"
        registerGame(gi)
        return gi

    register(22223, Matrix3, " 3x3 Matrix")
    register(22224, Matrix4, " 4x4 Matrix")
    register(22225, Matrix5, " 5x5 Matrix")
    register(22226, Matrix6, " 6x6 Matrix")
    register(22227, Matrix7, " 7x7 Matrix")
    register(22228, Matrix8, " 8x8 Matrix")
    register(22229, Matrix9, " 9x9 Matrix")
    register(22230, Matrix10, "10x10 Matrix")
    register(22240, Matrix20, "20x20 Matrix")

    def r(id, gameclass, name, game_type, decks, redeals, skill_level):
        game_type = game_type | STYLE.MUGHAL_GANJIFA
        gi = GameInfo(id, gameclass, name, game_type, decks, redeals, skill_level,
                        suits=range(8), ranks=range(12))
        registerGame(gi)
        return gi

    r(14401, MughalCircles, 'Mughal Circles', STYLE.MUGHAL_GANJIFA, 1, 0, SKILL.MOSTLY_SKILL)
    r(14402, Ghulam, 'Ghulam', STYLE.MUGHAL_GANJIFA, 1, 0, SKILL.MOSTLY_SKILL)
    r(14403, Shamsher, 'Shamsher', STYLE.MUGHAL_GANJIFA, 1, 0, SKILL.MOSTLY_SKILL)
    r(14404, EightLegions, 'Eight Legions', STYLE.MUGHAL_GANJIFA, 1, 0, SKILL.MOSTLY_SKILL)
    r(14405, Ashrafi, 'Ashrafi', STYLE.MUGHAL_GANJIFA, 1, 0, SKILL.MOSTLY_SKILL)
    r(14406, Tipati, 'Tipati', STYLE.MUGHAL_GANJIFA, 1, 0, SKILL.BALANCED)
    r(14407, Ashwapati, 'Ashwapati', STYLE.MUGHAL_GANJIFA, 1, -1, SKILL.BALANCED)
    r(14408, Gajapati, 'Gajapati', STYLE.MUGHAL_GANJIFA, 1, -1, SKILL.BALANCED)
    r(14409, Narpati, 'Narpati', STYLE.MUGHAL_GANJIFA, 1, 0, SKILL.BALANCED)
    r(14410, Garhpati, 'Garhpati', STYLE.MUGHAL_GANJIFA, 1, -1, SKILL.BALANCED)
    r(14411, Dhanpati, 'Dhanpati', STYLE.MUGHAL_GANJIFA, 1, 1, SKILL.BALANCED)
    r(14412, AkbarsTriumph, 'Akbar\'s Triumph', STYLE.MUGHAL_GANJIFA, 1, 2, SKILL.BALANCED)
    r(14413, AkbarsConquest, 'Akbar\'s Conquest', STYLE.MUGHAL_GANJIFA, 2, 2, SKILL.BALANCED)
    r(16000, Vajra, 'Vajra', STYLE.MUGHAL_GANJIFA, 1, 0, SKILL.MOSTLY_SKILL)
    r(16001, Danda, 'Danda', STYLE.MUGHAL_GANJIFA, 1, 0, SKILL.MOSTLY_SKILL)
    r(16002, Khadga, 'Khadga', STYLE.MUGHAL_GANJIFA, 1, 0, SKILL.MOSTLY_SKILL)
    r(16003, Makara, 'Makara', STYLE.MUGHAL_GANJIFA, 1, 0, SKILL.MOSTLY_SKILL)
    r(16004, AshtaDikapala, 'Ashta Dikapala', STYLE.MUGHAL_GANJIFA, 1, 0, SKILL.BALANCED)

    del r

    def r(id, gameclass, name, game_type, decks, redeals, skill_level):
        game_type = game_type | STYLE.TAROCK | STYLE.CONTRIB | STYLE.ORIGINAL
        gi = GameInfo(id, gameclass, name, game_type, decks, redeals, skill_level,
                      ranks=range(14), trumps=range(22))
        registerGame(gi)
        return gi

    r(13163, Cockroach, 'Cockroach', STYLE.TAROCK, 1, 0, SKILL.MOSTLY_SKILL)
    r(13164, DoubleCockroach, 'Double Cockroach', STYLE.TAROCK, 2, 0, SKILL.MOSTLY_SKILL)
    r(13165, Corkscrew, 'Corkscrew', STYLE.TAROCK, 2, 0, SKILL.MOSTLY_SKILL)
    r(13166, Serpent, 'Serpent', STYLE.TAROCK, 2, 0, SKILL.MOSTLY_SKILL)
    r(13167, Rambling, 'Rambling', STYLE.TAROCK, 2, 0, SKILL.MOSTLY_SKILL)
    r(22232, LeGrandeTeton, 'Le Grande Teton', STYLE.TAROCK, 1, 0, SKILL.BALANCED)

    del r



def registerPegged():
    def register(id, gameclass, name):
        ncards = 0
        for n in gameclass.ROWS:
            ncards += n
        ncards -= 1
        gi = GameInfo(id, gameclass, name,
                      STYLE.PUZZLE_TYPE, 1, 0, SKILL.SKILL,
                      category=CATEGORY.TRUMP_ONLY,
                      suits=(), ranks=(), trumps=range(ncards),
                      numcards=ncards,
                      rules_filename="pegged.html")
        registerGame(gi)
        return gi

    register(180, Pegged, "Pegged")
    register(181, PeggedCross1, "Pegged Cross 1")
    register(182, PeggedCross2, "Pegged Cross 2")
    register(183, Pegged6x6, "Pegged 6x6")
    register(184, Pegged7x7, "Pegged 7x7")
    register(210, PeggedTriangle1, "Pegged Triangle 1")
    register(211, PeggedTriangle2, "Pegged Triangle 2")


def registerMatrix():
    def register(id, gameclass, short_name):
        name = short_name
        ncards = int(name[:2]) * int(name[:2])
        gi = GameInfo(id, gameclass, name,
                      STYLE.MATRIX, 1, 0, SKILL.SKILL,
                      category=CATEGORY.TRUMP_ONLY, short_name=short_name,
                      suits=(), ranks=(), trumps=range(ncards),
                      numcards=ncards)
        gi.ncards = ncards
        gi.rules_filename = "matrix.html"
        registerGame(gi)
        return gi

    register(22223, Matrix3, " 3x3 Matrix")
    register(22224, Matrix4, " 4x4 Matrix")
    register(22225, Matrix5, " 5x5 Matrix")
    register(22226, Matrix6, " 6x6 Matrix")
    register(22227, Matrix7, " 7x7 Matrix")
    register(22228, Matrix8, " 8x8 Matrix")
    register(22229, Matrix9, " 9x9 Matrix")
    register(22230, Matrix10, "10x10 Matrix")
    register(22240, Matrix20, "20x20 Matrix")