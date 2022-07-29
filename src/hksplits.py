from typing import Any
from hkmem import HKmem
import hkenums

G = hkenums.Gamestate
H = hkenums.HeroTransitionState
menuing_scene_names = {"Menu_Title", "Quit_To_Menu", "PermaDeath"}

previous_values: dict[str, Any] = {}
def check_increased_by(mem: HKmem, variable: str, amount: int):
    """Returns whether mem.playerdata(variable) has increased by _amount_
       compared to last check"""
    current_val = mem.playerdata(variable)
    try:
        ret = current_val - previous_values[variable] == amount
    except KeyError:
        ret = False  # first time running this function for `variable`
    previous_values[variable] = current_val
    return ret

def check_increased(mem: HKmem, variable: str):
    """Returns whether mem: HKmem.playerdata(variable) has increas: stred
       compared to last check"""
    current_val = mem.playerdata(variable)
    try:
        ret = current_val > previous_values[variable]
    except KeyError:
        ret = False  # first time runnnig this function for `variable`
    previous_values[variable] = current_val
    return ret

def check_toggled_false(mem: HKmem, variable: str):
    """Checks if variable has toggled from True to False since last update"""
    current_val = mem.playerdata(variable)
    try:
        ret = previous_values[variable] and not current_val
    except KeyError:
        ret = False  # first time runnnig this function for `variable`
    previous_values[variable] = current_val
    return ret


def should_split_transition(next_scene: str, scene_name: str):
    if next_scene != scene_name:  # and not store.SplitThisTransition
        return not (
            scene_name == ""
            or next_scene == ""
            or scene_name in menuing_scene_names
            or next_scene in menuing_scene_names
        )
    return False


gladeessence = 0
def autosplit(splitname: str, mem: HKmem, scene_name: str, next_scene: str, gamestate: int) -> bool:
    """Returns whether the goal for the given split has been met."""
    global gladeessence
    if scene_name == "RestingGrounds_08" and check_increased_by(mem, "dreamOrbs", 1):
        gladeessence += 1
    match splitname:
        case "Abyss":
            return mem.playerdata("visitedAbyss")
        case "AbyssShriek":
            return mem.playerdata("screamLevel") == 2
        case "Aluba":
            return mem.playerdata("killedLazyFlyer")
        case "AncestralMound":
            return next_scene == "Crossroads_ShamanTemple" and next_scene != scene_name
        case "AspidHunter":
            return mem.playerdata("killsSpitter") == 17
        case "BaldurShell":
            return mem.playerdata("gotCharm_5")
        case "BeastsDenTrapBench":
            return mem.playerdata("spiderCapture")
        case "BlackKnight":
            return mem.playerdata("killedBlackKnight")
        case "BrettaRescued":
            return mem.playerdata("brettaRescued")
        case "BrummFlame":
            return mem.playerdata("gotBrummsFlame")
        case "BrokenVessel":
            return mem.playerdata("killedInfectedKnight")
        case "BroodingMawlek":
            return mem.playerdata("killedMawlek")
        case "CityOfTears":
            return mem.playerdata("visitedRuins")
        case "Collector":
            return mem.playerdata("collectorDefeated")
        case "TransCollector":
            return mem.playerdata("collectorDefeated") and scene_name == "Ruins2_11" and next_scene != scene_name
        case "Colosseum":
            return mem.playerdata("seenColosseumTitle")
        case "ColosseumBronze":
            return mem.playerdata("colosseumBronzeCompleted")
        case "ColosseumGold":
            return mem.playerdata("colosseumGoldCompleted")
        case "ColosseumSilver":
            return mem.playerdata("colosseumSilverCompleted")
        case "CrossroadsStation":
            return mem.playerdata("openedCrossroads")
        case "CrystalGuardian1":
            return mem.playerdata("defeatedMegaBeamMiner")
        case "CrystalGuardian2":
            return mem.playerdata("killsMegaBeamMiner") == 0
        case "CrystalHeart":
            return mem.playerdata("hasSuperDash")
        case "CrystalPeak":
            return mem.playerdata("visitedMines")
        case "CycloneSlash":
            return mem.playerdata("hasCyclone")
        case "Dashmaster":
            return mem.playerdata("gotCharm_31")
        case "DashSlash":
            return mem.playerdata("hasUpwardSlash")
        case "DeepFocus":
            return mem.playerdata("gotCharm_34")
        case "Deepnest":
            return mem.playerdata("visitedDeepnest")
        case "DeepnestSpa":
            return mem.playerdata("visitedDeepnestSpa")
        case "DeepnestStation":
            return mem.playerdata("openedDeepnest")
        case "DefendersCrest":
            return mem.playerdata("gotCharm_10")
        case "DescendingDark":
            return mem.playerdata("quakeLevel") == 2
        case "DesolateDive":
            return mem.playerdata("quakeLevel") == 1
        case "Dirtmouth":
            return mem.playerdata("visitedDirtmouth")
        case "Dreamer1":
            return mem.playerdata("guardiansDefeated") == 1
        case "Dreamer2":
            return mem.playerdata("guardiansDefeated") == 2
        case "Dreamer3":
            return mem.playerdata("guardiansDefeated") == 3
        case "DreamNail":
            return mem.playerdata("hasDreamNail")
        case "DreamNail2":
            return mem.playerdata("dreamNailUpgraded")
        case "DreamGate":
            return mem.playerdata("hasDreamGate")
        case "Dreamshield":
            return mem.playerdata("gotCharm_38")
        case "DreamWielder":
            return mem.playerdata("gotCharm_30")
        case "DungDefender":
            return mem.playerdata("killedDungDefender")
        case "ElderbugFlower":
            return mem.playerdata("elderbugGaveFlower")
        case "ElderHu":
            return mem.playerdata("killedGhostHu")
        case "ElegantKey":
            return mem.playerdata("hasWhiteKey")
        case "EternalOrdealAchieved":
            return mem.playerdata("ordealAchieved")
        case "EternalOrdealUnlocked":
            return mem.playerdata("zoteStatueWallBroken")
        case "FailedKnight":
            return mem.playerdata("falseKnightDreamDefeated")
        case "FalseKnight":
            return mem.playerdata("killedFalseKnight")
        case "Flukemarm":
            return mem.playerdata("killedFlukeMother")
        case "Flukenest":
            return mem.playerdata("gotCharm_11")
        case "FogCanyon":
            return mem.playerdata("visitedFogCanyon")
        case "ForgottenCrossroads":
            return mem.playerdata("visitedCrossroads")
        case "FragileGreed":
            return mem.playerdata("gotCharm_24")
        case "FragileHeart":
            return mem.playerdata("gotCharm_23")
        case "FragileStrength":
            return mem.playerdata("gotCharm_25")
        case "FungalWastes":
            return mem.playerdata("visitedFungus")
        case "FuryOfTheFallen":
            return mem.playerdata("gotCharm_6")
        case "Galien":
            return mem.playerdata("killedGhostGalien")
        case "GatheringSwarm":
            return mem.playerdata("gotCharm_1")
        case "GlowingWomb":
            return mem.playerdata("gotCharm_22")
        case "Godhome":
            return mem.playerdata("visitedGodhome")
        case "GodTamer":
            return mem.playerdata("killedLobsterLancer")
        case "GodTuner":
            return mem.playerdata("hasGodfinder")
        case "Gorb":
            return mem.playerdata("killedGhostAladar")
        case "GorgeousHusk":
            return mem.playerdata("killedGorgeousHusk")
        case "GreatSlash":
            return mem.playerdata("hasDashSlash")
        case "Greenpath":
            return mem.playerdata("visitedGreenpath")
        case "GreenpathStation":
            return mem.playerdata("openedGreenpath")
        case "Grimmchild":
            return mem.playerdata("gotCharm_40")
        case "Grimmchild2":
            return mem.playerdata("grimmChildLevel") == 2
        case "Grimmchild3":
            return mem.playerdata("grimmChildLevel") == 3
        case "Grimmchild4":
            return mem.playerdata("grimmChildLevel") == 4
        case "GrubberflysElegy":
            return mem.playerdata("gotCharm_35")
        case "Grubsong":
            return mem.playerdata("gotCharm_3")
        case "GreatHopper":
            return mem.playerdata("killedGiantHopper")
        case "GreyPrince":
            return mem.playerdata("killedGreyPrince")
        case "GruzMother":
            return mem.playerdata("killedBigFly")
        case "HeavyBlow":
            return mem.playerdata("gotCharm_15")
        case "Hegemol":
            return mem.playerdata("maskBrokenHegemol")
        case "HegemolDreamer":
            return mem.playerdata("hegemolDefeated")
        case "HiddenStationStation":
            return mem.playerdata("openedHiddenStation")
        case "Hive":
            return mem.playerdata("visitedHive")
        case "Hiveblood":
            return mem.playerdata("gotCharm_29")
        case "HollowKnightDreamnail":
            return next_scene == "Dream_Final_Boss"
        case "HollowKnightBoss":
            return mem.playerdata("killedHollowKnight")
        case "RadianceBoss":
            return mem.playerdata("killedFinalBoss")
        case "Hornet1":
            return mem.playerdata("killedHornet")
        case "Hornet2":
            return mem.playerdata("hornetOutskirtsDefeated")
        case "HowlingWraiths":
            return mem.playerdata("screamLevel") == 1
        case "HuntersMark":
            return mem.playerdata("killedHunterMark")
        case "HuskMiner":
            return check_increased_by(mem, "killsZombieMiner", -1)
        case "InfectedCrossroads":
            return mem.playerdata("crossroadsInfected") and mem.playerdata("visitedCrossroads")
        case "IsmasTear":
            return mem.playerdata("hasAcidArmour")
        case "JonisBlessing":
            return mem.playerdata("gotCharm_27")
        case "KingdomsEdge":
            return mem.playerdata("visitedOutskirts")
        case "KingsBrand":
            return mem.playerdata("hasKingsBrand")
        case "Kingsoul":
            return mem.playerdata("charmCost_36") == 5 and mem.playerdata("royalCharmState") == 3
        case "KingsStationStation":
            return mem.playerdata("openedRuins2")
        case "Lemm1":
            return mem.playerdata("metRelicDealer")
        case "Lemm2":
            return mem.playerdata("metRelicDealerShop")
        case "LifebloodCore":
            return mem.playerdata("gotCharm_9")
        case "LifebloodHeart":
            return mem.playerdata("gotCharm_8")
        case "LittleFool":
            return mem.playerdata("littleFoolMet")
        case "Longnail":
            return mem.playerdata("gotCharm_18")
        case "LostKin":
            return mem.playerdata("infectedKnightDreamDefeated")
        case "LoveKey":
            return mem.playerdata("hasLoveKey")
        case "LumaflyLantern":
            return mem.playerdata("hasLantern")
        case "Lurien":
            return mem.playerdata("maskBrokenLurien")
        case "LurienDreamer":
            return mem.playerdata("lurienDefeated")
        case "MantisClaw":
            return mem.playerdata("hasWalljump")
        case "MantisLords":
            return mem.playerdata("defeatedMantisLords")
        case "MarkOfPride":
            return mem.playerdata("gotCharm_13")
        case "Markoth":
            return mem.playerdata("killedGhostMarkoth")
        case "Marmu":
            return mem.playerdata("killedGhostMarmu")
        case "MaskFragment1":
            return mem.playerdata("maxHealthBase") == 5 and mem.playerdata("heartPieces") == 1
        case "MaskFragment2":
            return mem.playerdata("maxHealthBase") == 5 and mem.playerdata("heartPieces") == 2
        case "MaskFragment3":
            return mem.playerdata("maxHealthBase") == 5 and mem.playerdata("heartPieces") == 3
        case "Mask1":
            return mem.playerdata("maxHealthBase") == 6
        case "MaskFragment5":
            mask_shards = mem.playerdata("heartPieces")
            return mask_shards == 5 or (mem.playerdata("maxHealthBase") == 6 and mask_shards == 1)
        case "MaskFragment6":
            mask_shards = mem.playerdata("heartPieces")
            return mask_shards == 6 or (mem.playerdata("maxHealthBase") == 6 and mask_shards == 2)
        case "MaskFragment7":
            mask_shards = mem.playerdata("heartPieces")
            return mask_shards == 7 or (mem.playerdata("maxHealthBase") == 6 and mask_shards == 3)
        case "Mask2":
            return mem.playerdata("maxHealthBase") == 7
        case "MaskFragment9":
            mask_shards = mem.playerdata("heartPieces")
            return mask_shards == 9 or (mem.playerdata("maxHealthBase") == 7 and mask_shards == 1)
        case "MaskFragment10":
            mask_shards = mem.playerdata("heartPieces")
            return mask_shards == 10 or (mem.playerdata("maxHealthBase") == 7 and mask_shards == 2)
        case "MaskFragment11":
            mask_shards = mem.playerdata("heartPieces")
            return mask_shards == 11 or (mem.playerdata("maxHealthBase") == 7 and mask_shards == 3)
        case "Mask3":
            return mem.playerdata("maxHealthBase") == 8
        case "MaskFragment13":
            mask_shards = mem.playerdata("heartPieces")
            return mask_shards == 13 or (mem.playerdata("maxHealthBase") == 8 and mask_shards == 1)
        case "MaskFragment14":
            mask_shards = mem.playerdata("heartPieces")
            return mask_shards == 14 or (mem.playerdata("maxHealthBase") == 8 and mask_shards == 2)
        case "MaskFragment15":
            mask_shards = mem.playerdata("heartPieces")
            return mask_shards == 15 or (mem.playerdata("maxHealthBase") == 8 and mask_shards == 3)
        case "Mask4":
            return mem.playerdata("maxHealthBase") == 9
        case "MatoOroNailBros":
            return mem.playerdata("killedNailBros")
        case "MegaMossCharger":
            return mem.playerdata("megaMossChargerDefeated")
        case "MenderBug":
            return mem.playerdata("killedMenderBug")
        case "MonarchWings":
            return mem.playerdata("hasDoubleJump")
        case "Monomon":
            return mem.playerdata("maskBrokenMonomon")
        case "MonomonDreamer":
            return mem.playerdata("monomonDefeated")
        case "MossKnight":
            return mem.playerdata("killedMossKnight")
        case "MothwingCloak":
            return mem.playerdata("hasDash")
        case "MrMushroom1":
            return mem.playerdata("mrMushroomState") == 2
        case "MrMushroom2":
            return mem.playerdata("mrMushroomState") == 3
        case "MrMushroom3":
            return mem.playerdata("mrMushroomState") == 4
        case "MrMushroom4":
            return mem.playerdata("mrMushroomState") == 5
        case "MrMushroom5":
            return mem.playerdata("mrMushroomState") == 6
        case "MrMushroom6":
            return mem.playerdata("mrMushroomState") == 7
        case "MrMushroom7":
            return mem.playerdata("mrMushroomState") == 8
        case "MushroomBrawler":
            return mem.playerdata("killsMushroomBrawler") == 6
        case "NailmastersGlory":
            return mem.playerdata("gotCharm_26")
        case "NailUpgrade1":
            return mem.playerdata("nailSmithUpgrades") == 1
        case "NailUpgrade2":
            return mem.playerdata("nailSmithUpgrades") == 2
        case "NailUpgrade3":
            return mem.playerdata("nailSmithUpgrades") == 3
        case "NailUpgrade4":
            return mem.playerdata("nailSmithUpgrades") == 4
        case "NightmareKingGrimm":
            return mem.playerdata("killedNightmareGrimm")
        case "NightmareLantern":
            return mem.playerdata("nightmareLanternLit")
        case "NightmareLanternDestroyed":
            return mem.playerdata("destroyedNightmareLantern")
        case "NoEyes":
            return mem.playerdata("killedGhostNoEyes")
        case "Nosk":
            return mem.playerdata("killedMimicSpider")
        case "NotchFogCanyon":
            return mem.playerdata("notchFogCanyon")
        case "NotchSalubra1":
            return mem.playerdata("salubraNotch1")
        case "NotchSalubra2":
            return mem.playerdata("salubraNotch2")
        case "NotchSalubra3":
            return mem.playerdata("salubraNotch3")
        case "NotchSalubra4":
            return mem.playerdata("salubraNotch4")
        case "NotchShrumalOgres":
            return mem.playerdata("notchShroomOgres")
        case "PaleLurkerKey":
            return mem.playerdata("gotLurkerKey")
        case "PaleOre":
            return mem.playerdata("ore") > 0
        case "Pantheon1":
            return mem.playerdata("bossDoorStateTier1")
        case "Pantheon2":
            return mem.playerdata("bossDoorStateTier2")
        case "Pantheon3":
            return mem.playerdata("bossDoorStateTier3")
        case "Pantheon4":
            return mem.playerdata("bossDoorStateTier4")
        case "Pantheon5":
            return mem.playerdata("bossDoorStateTier5")
        case "PathOfPain":
            return mem.playerdata("newDataBindingSeal")
        case "PureVessel":
            return mem.playerdata("killedHollowKnightPrime")
        case "QueensGardens":
            return mem.playerdata("visitedRoyalGardens")
        case "QueensGardensStation":
            return mem.playerdata("openedRoyalGardens")
        case "QueensStationStation":
            return mem.playerdata("openedFungalWastes")
        case "QuickSlash":
            return mem.playerdata("gotCharm_32")
        case "QuickFocus":
            return mem.playerdata("gotCharm_7")
        case "RestingGrounds":
            return mem.playerdata("visitedRestingGrounds")
        case "RestingGroundsStation":
            return mem.playerdata("openedRestingGrounds")
        case "RoyalWaterways":
            return mem.playerdata("visitedWaterways")
        case "SalubrasBlessing":
            return mem.playerdata("salubraBlessing")
        case "SeerDeparts":
            return mem.playerdata("mothDeparted")
        case "ShadeCloak":
            return mem.playerdata("hasShadowDash")
        case "ShadeSoul":
            return mem.playerdata("fireballLevel") == 2
        case "ShamanStone":
            return mem.playerdata("gotCharm_19")
        case "ShapeOfUnn":
            return mem.playerdata("gotCharm_28")
        case "SharpShadow":
            return mem.playerdata("gotCharm_16")
        case "SheoPaintmaster":
            return mem.playerdata("killedPaintmaster")
        case "SimpleKey":
            return mem.playerdata("simpleKeys") > 0
        case "SlyKey":
            return mem.playerdata("hasSlykey")
        case "SlyNailsage":
            return mem.playerdata("killedNailsage")
        case "SoulCatcher":
            return mem.playerdata("gotCharm_20")
        case "SoulEater":
            return mem.playerdata("gotCharm_21")
        case "SoulMaster":
            return mem.playerdata("killedMageLord")
        case "SoulTyrant":
            return mem.playerdata("mageLordDreamDefeated")
        case "SpellTwister":
            return mem.playerdata("gotCharm_33")
        case "SporeShroom":
            return mem.playerdata("gotCharm_17")
        case "SpiritGladeOpen":
            return mem.playerdata("gladeDoorOpened")
        case "Sprintmaster":
            return mem.playerdata("gotCharm_37")
        case "StalwartShell":
            return mem.playerdata("gotCharm_4")
        case "StagnestStation":
            return (next_scene == "Cliffs_03" and mem.playerdata("travelling")
                    and mem.playerdata("openedStagNest"))
        case "SteadyBody":
            return mem.playerdata("gotCharm_14")
        case "StoreroomsStation":
            return mem.playerdata("openedRuins1")
        case "TeachersArchive":
            return scene_name == "Fungus3_archive"
        case "ThornsOfAgony":
            return mem.playerdata("gotCharm_12")
        case "TraitorLord":
            return mem.playerdata("killedTraitorLord")
        case "TramPass":
            return mem.playerdata("hasTramPass")
        case "TroupeMasterGrimm":
            return mem.playerdata("killedGrimm")
        case "UnbreakableGreed":
            return mem.playerdata("fragileGreed_unbreakable")
        case "UnbreakableHeart":
            return mem.playerdata("fragileHealth_unbreakable")
        case "UnbreakableStrength":
            return mem.playerdata("fragileStrength_unbreakable")
        case "UnchainedHollowKnight":
            return mem.playerdata("unchainedHollowKnight")
        case "Uumuu":
            return mem.playerdata("killedMegaJellyfish")
        case "VengefulSpirit":
            return mem.playerdata("fireballLevel") == 1
        case "TransVS":
            return mem.playerdata("fireballLevel") == 1 and next_scene != scene_name
        case "VesselFragment1":
            return mem.playerdata("MPReserveMax") == 0 and mem.playerdata("vesselFragments") == 1
        case "VesselFragment2":
            return mem.playerdata("MPReserveMax") == 0 and mem.playerdata("vesselFragments") == 2
        case "Vessel1":
            return mem.playerdata("MPReserveMax") == 33
        case "VesselFragment4":
            fragments = mem.playerdata("vesselFragments")
            return fragments == 4 or (mem.playerdata("MPReserveMax") == 33 and fragments == 1)
        case "VesselFragment5":
            return fragments == 5 or (mem.playerdata("MPReserveMax") == 33 and fragments == 2)
        case "Vessel2":
            return mem.playerdata("MPReserveMax") == 66
        case "VesselFragment7":
            fragments = mem.playerdata("vesselFragments")
            return fragments == 7 or (mem.playerdata("MPReserveMax") == 66 and fragments == 1)
        case "VesselFragment8":
            fragments = mem.playerdata("vesselFragments")
            return fragments == 8 or (mem.playerdata("MPReserveMax") == 66 and fragments == 2)
        case "Vessel3":
            return mem.playerdata("MPReserveMax") == 99
        case "VoidHeart":
            return mem.playerdata("gotShadeCharm")
        case "WatcherChandelier":
            return mem.playerdata("watcherChandelier")
        case "WaywardCompass":
            return mem.playerdata("gotCharm_2")
        case "Weaversong":
            return mem.playerdata("gotCharm_39")
        case "WhiteDefender":
            return mem.playerdata("killedWhiteDefender")
        case "WhitePalace":
            return mem.playerdata("visitedWhitePalace")
        case "Xero":
            return mem.playerdata("killedGhostXero")
        case "Zote1":
            return mem.playerdata("zoteRescuedBuzzer")
        case "Zote2":
            return mem.playerdata("zoteRescuedDeepnest")
        case "ZoteKilled":
            return mem.playerdata("killedZote")
        case "Flame1":
            return mem.playerdata("flamesCollected") == 1
        case "Flame2":
            return mem.playerdata("flamesCollected") == 2
        case "Flame3":
            return mem.playerdata("flamesCollected") == 3
        case "HiveKnight":
            return mem.playerdata("killedHiveKnight")
        case "Ore1":
            return mem.total_pale_ore_found() == 1
        case "Ore2":
            return mem.total_pale_ore_found() == 2
        case "Ore3":
            return mem.total_pale_ore_found() == 3
        case "Ore4":
            return mem.total_pale_ore_found() == 4
        case "Ore5":
            return mem.total_pale_ore_found() == 5
        case "Ore6":
            return mem.total_pale_ore_found() == 6
        case "Grub1":
            return mem.playerdata("grubsCollected") == 1
        case "Grub2":
            return mem.playerdata("grubsCollected") == 2
        case "Grub3":
            return mem.playerdata("grubsCollected") == 3
        case "Grub4":
            return mem.playerdata("grubsCollected") == 4
        case "Grub5":
            return mem.playerdata("grubsCollected") == 5
        case "Grub6":
            return mem.playerdata("grubsCollected") == 6
        case "Grub7":
            return mem.playerdata("grubsCollected") == 7
        case "Grub8":
            return mem.playerdata("grubsCollected") == 8
        case "Grub9":
            return mem.playerdata("grubsCollected") == 9
        case "Grub10":
            return mem.playerdata("grubsCollected") == 10
        case "Grub11":
            return mem.playerdata("grubsCollected") == 11
        case "Grub12":
            return mem.playerdata("grubsCollected") == 12
        case "Grub13":
            return mem.playerdata("grubsCollected") == 13
        case "Grub14":
            return mem.playerdata("grubsCollected") == 14
        case "Grub15":
            return mem.playerdata("grubsCollected") == 15
        case "Grub16":
            return mem.playerdata("grubsCollected") == 16
        case "Grub17":
            return mem.playerdata("grubsCollected") == 17
        case "Grub18":
            return mem.playerdata("grubsCollected") == 18
        case "Grub19":
            return mem.playerdata("grubsCollected") == 19
        case "Grub20":
            return mem.playerdata("grubsCollected") == 20
        case "Grub21":
            return mem.playerdata("grubsCollected") == 21
        case "Grub22":
            return mem.playerdata("grubsCollected") == 22
        case "Grub23":
            return mem.playerdata("grubsCollected") == 23
        case "Grub24":
            return mem.playerdata("grubsCollected") == 24
        case "Grub25":
            return mem.playerdata("grubsCollected") == 25
        case "Grub26":
            return mem.playerdata("grubsCollected") == 26
        case "Grub27":
            return mem.playerdata("grubsCollected") == 27
        case "Grub28":
            return mem.playerdata("grubsCollected") == 28
        case "Grub29":
            return mem.playerdata("grubsCollected") == 29
        case "Grub30":
            return mem.playerdata("grubsCollected") == 30
        case "Grub31":
            return mem.playerdata("grubsCollected") == 31
        case "Grub32":
            return mem.playerdata("grubsCollected") == 32
        case "Grub33":
            return mem.playerdata("grubsCollected") == 33
        case "Grub34":
            return mem.playerdata("grubsCollected") == 34
        case "Grub35":
            return mem.playerdata("grubsCollected") == 35
        case "Grub36":
            return mem.playerdata("grubsCollected") == 36
        case "Grub37":
            return mem.playerdata("grubsCollected") == 37
        case "Grub38":
            return mem.playerdata("grubsCollected") == 38
        case "Grub39":
            return mem.playerdata("grubsCollected") == 39
        case "Grub40":
            return mem.playerdata("grubsCollected") == 40
        case "Grub41":
            return mem.playerdata("grubsCollected") == 41
        case "Grub42":
            return mem.playerdata("grubsCollected") == 42
        case "Grub43":
            return mem.playerdata("grubsCollected") == 43
        case "Grub44":
            return mem.playerdata("grubsCollected") == 44
        case "Grub45":
            return mem.playerdata("grubsCollected") == 45
        case "Grub46":
            return mem.playerdata("grubsCollected") == 46
        case "GrubBasinDive":
            return check_increased_by(mem, "grubsCollected", 1) and scene_name == "Abyss_17"
        case "GrubBasinWings":
            return check_increased_by(mem, "grubsCollected", 1) and scene_name == "Abyss_19"
        case "GrubCityBelowLoveTower":
            return check_increased_by(mem, "grubsCollected", 1) and scene_name == "Ruins2_07"
        case "GrubCityBelowSanctum":
            return check_increased_by(mem, "grubsCollected", 1) and scene_name == "Ruins1_05"
        case "GrubCityCollector":
            return check_increased_by(mem, "grubsCollected", 1) and scene_name == "Ruins2_11"
        case "GrubCityCollectorAll":
            return "Ruins2_11" in mem.playerdata("scenesGrubRescued")
        case "GrubCityGuardHouse":
            return check_increased_by(mem, "grubsCollected", 1) and scene_name == "Ruins_House_01"
        case "GrubCitySanctum":
            return check_increased_by(mem, "grubsCollected", 1) and scene_name == "Ruins1_32"
        case "GrubCitySpire":
            return check_increased_by(mem, "grubsCollected", 1) and scene_name == "Ruins2_03"
        case "GrubCliffsBaldurShell":
            return check_increased_by(mem, "grubsCollected", 1) and scene_name == "Fungus1_28"
        case "GrubCrossroadsAcid":
            return check_increased_by(mem, "grubsCollected", 1) and scene_name == "Crossroads_35"
        case "GrubCrossroadsGuarded":
            return check_increased_by(mem, "grubsCollected", 1) and scene_name == "Crossroads_48"
        case "GrubCrossroadsSpikes":
            return check_increased_by(mem, "grubsCollected", 1) and scene_name == "Crossroads_31"
        case "GrubCrossroadsVengefly":
            return check_increased_by(mem, "grubsCollected", 1) and scene_name == "Crossroads_05"
        case "GrubCrossroadsWall":
            return check_increased_by(mem, "grubsCollected", 1) and scene_name == "Crossroads_03"
        case "GrubCrystalPeaksBottomLever":
            return check_increased_by(mem, "grubsCollected", 1) and scene_name == "Mines_04"
        case "GrubCrystalPeaksCrown":
            return check_increased_by(mem, "grubsCollected", 1) and scene_name == "Mines_24"
        case "GrubCrystalPeaksCrushers":
            return check_increased_by(mem, "grubsCollected", 1) and scene_name == "Mines_19"
        case "GrubCrystalPeaksCrystalHeart":
            return check_increased_by(mem, "grubsCollected", 1) and scene_name == "Mines_31"
        case "GrubCrystalPeaksMimics":
            return check_increased_by(mem, "grubsCollected", 1) and scene_name == "Mines_16"
        case "GrubCrystalPeaksMound":
            return check_increased_by(mem, "grubsCollected", 1) and scene_name == "Mines_35"
        case "GrubCrystalPeaksSpikes":
            return check_increased_by(mem, "grubsCollected", 1) and scene_name == "Mines_03"
        case "GrubDeepnestBeastsDen":
            return check_increased_by(mem, "grubsCollected", 1) and scene_name == "Deepnest_Spider_Town"
        case "GrubDeepnestDark":
            return check_increased_by(mem, "grubsCollected", 1) and scene_name == "Deepnest_39"
        case "GrubDeepnestMimics":
            return check_increased_by(mem, "grubsCollected", 1) and scene_name == "Deepnest_36"
        case "GrubDeepnestNosk":
            return check_increased_by(mem, "grubsCollected", 1) and scene_name == "Deepnest_31"
        case "GrubDeepnestSpikes":
            return check_increased_by(mem, "grubsCollected", 1) and scene_name == "Deepnest_03"
        case "GrubFogCanyonArchives":
            return check_increased_by(mem, "grubsCollected", 1) and scene_name == "Fungus3_47"
        case "GrubFungalBouncy":
            return check_increased_by(mem, "grubsCollected", 1) and scene_name == "Fungus2_18"
        case "GrubFungalSporeShroom":
            return check_increased_by(mem, "grubsCollected", 1) and scene_name == "Fungus2_20"
        case "GrubGreenpathCornifer":
            return check_increased_by(mem, "grubsCollected", 1) and scene_name == "Fungus1_06"
        case "GrubGreenpathHunter":
            return check_increased_by(mem, "grubsCollected", 1) and scene_name == "Fungus1_07"
        case "GrubGreenpathMossKnight":
            return check_increased_by(mem, "grubsCollected", 1) and scene_name == "Fungus1_21"
        case "GrubGreenpathVesselFragment":
            return check_increased_by(mem, "grubsCollected", 1) and scene_name == "Fungus1_13"
        case "GrubHiveExternal":
            return check_increased_by(mem, "grubsCollected", 1) and scene_name == "Hive_03"
        case "GrubHiveInternal":
            return check_increased_by(mem, "grubsCollected", 1) and scene_name == "Hive_04"
        case "GrubKingdomsEdgeCenter":
            return check_increased_by(mem, "grubsCollected", 1) and scene_name == "Deepnest_East_11"
        case "GrubKingdomsEdgeOro":
            return check_increased_by(mem, "grubsCollected", 1) and scene_name == "Deepnest_East_14"
        case "GrubQueensGardensBelowStag":
            return check_increased_by(mem, "grubsCollected", 1) and scene_name == "Fungus3_10"
        case "GrubQueensGardensUpper":
            return check_increased_by(mem, "grubsCollected", 1) and scene_name == "Fungus3_22"
        case "GrubQueensGardensWhiteLady":
            return check_increased_by(mem, "grubsCollected", 1) and scene_name == "Fungus3_48"
        case "GrubRestingGroundsCrypts":
            return check_increased_by(mem, "grubsCollected", 1) and scene_name == "RestingGrounds_10"
        case "GrubWaterwaysCenter":
            return check_increased_by(mem, "grubsCollected", 1) and scene_name == "Waterways_04"
        case "GrubWaterwaysHwurmps":
            return check_increased_by(mem, "grubsCollected", 1) and scene_name == "Waterways_14"
        case "GrubWaterwaysIsma":
            return check_increased_by(mem, "grubsCollected", 1) and scene_name == "Waterways_13"
        case "Mimic1":
            return mem.playerdata("killsGrubMimic") == 4
        case "Mimic2":
            return mem.playerdata("killsGrubMimic") == 3
        case "Mimic3":
            return mem.playerdata("killsGrubMimic") == 2
        case "Mimic4":
            return mem.playerdata("killsGrubMimic") == 1
        case "Mimic5":
            return mem.playerdata("killsGrubMimic") == 0
        case "TreeCity":
            return "Ruins1_17" in mem.playerdata("scenesEncounteredDreamPlantC")
        case "TreeCliffs":
            return "Cliffs_01" in mem.playerdata("scenesEncounteredDreamPlantC")
        case "TreeCrossroads":
            return "Crossroads_07" in mem.playerdata("scenesEncounteredDreamPlantC")
        case "TreeDeepnest":
            return "Deepnest_39" in mem.playerdata("scenesEncounteredDreamPlantC")
        case "TreeGlade":
            return "RestingGrounds_08" in mem.playerdata("scenesEncounteredDreamPlantC")
        case "TreeGreenpath":
            return "Fungus1_13" in mem.playerdata("scenesEncounteredDreamPlantC")
        case "TreeHive":
            return "Hive_02" in mem.playerdata("scenesEncounteredDreamPlantC")
        case "TreeKingdomsEdge":
            return "Deepnest_East_07" in mem.playerdata("scenesEncounteredDreamPlantC")
        case "TreeLegEater":
            return "Fungus2_33" in mem.playerdata("scenesEncounteredDreamPlantC")
        case "TreeMantisVillage":
            return "Fungus2_17" in mem.playerdata("scenesEncounteredDreamPlantC")
        case "TreeMound":
            return "Crossroads_ShamanTemple" in mem.playerdata("scenesEncounteredDreamPlantC")
        case "TreePeak":
            return "Mines_23" in mem.playerdata("scenesEncounteredDreamPlantC")
        case "TreeQueensGardens":
            return "Fungus3_11" in mem.playerdata("scenesEncounteredDreamPlantC")
        case "TreeRestingGrounds":
            return "RestingGrounds_05" in mem.playerdata("scenesEncounteredDreamPlantC")
        case "TreeWaterways":
            return "Abyss_01" in mem.playerdata("scenesEncounteredDreamPlantC")
        case "Essence100":
            return mem.playerdata("dreamOrbs") >= 100
        case "Essence200":
            return mem.playerdata("dreamOrbs") >= 200
        case "Essence300":
            return mem.playerdata("dreamOrbs") >= 300
        case "Essence400":
            return mem.playerdata("dreamOrbs") >= 400
        case "Essence500":
            return mem.playerdata("dreamOrbs") >= 500
        case "Essence600":
            return mem.playerdata("dreamOrbs") >= 600
        case "Essence700":
            return mem.playerdata("dreamOrbs") >= 700
        case "Essence800":
            return mem.playerdata("dreamOrbs") >= 800
        case "Essence900":
            return mem.playerdata("dreamOrbs") >= 900
        case "Essence1000":
            return mem.playerdata("dreamOrbs") >= 1000
        case "Essence1100":
            return mem.playerdata("dreamOrbs") >= 1100
        case "Essence1200":
            return mem.playerdata("dreamOrbs") >= 1200
        case "Essence1300":
            return mem.playerdata("dreamOrbs") >= 1300
        case "Essence1400":
            return mem.playerdata("dreamOrbs") >= 1400
        case "Essence1500":
            return mem.playerdata("dreamOrbs") >= 1500
        case "Essence1600":
            return mem.playerdata("dreamOrbs") >= 1600
        case "Essence1700":
            return mem.playerdata("dreamOrbs") >= 1700
        case "Essence1800":
            return mem.playerdata("dreamOrbs") >= 1800
        case "Essence1900":
            return mem.playerdata("dreamOrbs") >= 1900
        case "Essence2000":
            return mem.playerdata("dreamOrbs") >= 2000
        case "Essence2100":
            return mem.playerdata("dreamOrbs") >= 2100
        case "Essence2200":
            return mem.playerdata("dreamOrbs") >= 2200
        case "Essence2300":
            return mem.playerdata("dreamOrbs") >= 2300
        case "Essence2400":
            return mem.playerdata("dreamOrbs") >= 2400
        case "KingsPass":
            return scene_name == "Tutorial_01" and next_scene == "Town"
        case "KingsPassEnterFromTown":
            return scene_name == "Town" and next_scene == "Tutorial_01"
        case "BlueLake":
            return scene_name != "Crossroads_50" and next_scene == "Crossroads_50"
        case "CatacombsEntry":
            return scene_name != "RestingGrounds_10" and next_scene == "RestingGrounds_10"
        case "VengeflyKingP":
            return scene_name == "GG_Vengefly" and next_scene == "GG_Gruz_Mother"
        case "GruzMotherP":
            return scene_name == "GG_Gruz_Mother" and next_scene == "GG_False_Knight"
        case "FalseKnightP":
            return scene_name == "GG_False_Knight" and next_scene == "GG_Mega_Moss_Charger"
        case "MassiveMossChargerP":
            return scene_name == "GG_Mega_Moss_Charger" and next_scene == "GG_Hornet_1"
        case "Hornet1P":
            return scene_name == "GG_Hornet_1" and next_scene in {"GG_Spa", "GG_Engine"}
        case "GorbP":
            return scene_name == "GG_Ghost_Gorb" and next_scene == "GG_Dung_Defender"
        case "DungDefenderP":
            return scene_name == "GG_Dung_Defender" and next_scene == "GG_Mage_Knight"
        case "SoulWarriorP":
            return scene_name == "GG_Mage_Knight" and next_scene == "GG_Brooding_Mawlek"
        case "BroodingMawlekP":
            return scene_name == "GG_Brooding_Mawlek" and next_scene in {"GG_Engine", "GG_Nailmasters"}
        case "OroMatoNailBrosP":
            return scene_name == "GG_Nailmasters" and next_scene in {"GG_End_Sequence", "GG_Spa"}
        case "XeroP":
            return scene_name == "GG_Ghost_Xero" and next_scene == "GG_Crystal_Guardian"
        case "CrystalGuardianP":
            return scene_name == "GG_Crystal_Guardian" and next_scene == "GG_Soul_Master"
        case "SoulMasterP":
            return scene_name == "GG_Soul_Master" and next_scene == "GG_Oblobbles"
        case "OblobblesP":
            return scene_name == "GG_Oblobbles" and next_scene == "GG_Mantis_Lords"
        case "MantisLordsP":
            return scene_name == "GG_Mantis_Lords" and next_scene == "GG_Spa"
        case "MarmuP":
            return scene_name == "GG_Ghost_Marmu" and next_scene in {"GG_Nosk", "GG_Flukemarm"}
        case "NoskP":
            return scene_name == "GG_Nosk" and next_scene == "GG_Flukemarm"
        case "FlukemarmP":
            return scene_name == "GG_Flukemarm" and next_scene == "GG_Broken_Vessel"
        case "BrokenVesselP":
            return scene_name == "GG_Broken_Vessel" and next_scene in {"GG_Engine", "GG_Ghost_Galien"}
        case "SheoPaintmasterP":
            return scene_name == "GG_Painter" and next_scene in {"GG_End_Sequence", "GG_Spa"}
        case "HiveKnightP":
            return scene_name == "GG_Hive_Knight" and next_scene == "GG_Ghost_Hu"
        case "ElderHuP":
            return scene_name == "GG_Ghost_Hu" and next_scene == "GG_Collector"
        case "CollectorP":
            return scene_name == "GG_Collector" and next_scene == "GG_God_Tamer"
        case "GodTamerP":
            return scene_name == "GG_God_Tamer" and next_scene == "GG_Grimm"
        case "TroupeMasterGrimmP":
            return scene_name == "GG_Grimm" and next_scene == "GG_Spa"
        case "GalienP":
            return scene_name == "GG_Ghost_Galien" and next_scene in {"GG_Grey_Prince_Zote", "GG_Painter", "GG_Uumuu"}
        case "GreyPrinceZoteP":
            return scene_name == "GG_Grey_Prince_Zote" and next_scene in {"GG_Uumuu", "GG_Failed_Champion"}
        case "UumuuP":
            return scene_name == "GG_Uumuu" and next_scene in {"GG_Hornet_2", "GG_Nosk_Hornet"}
        case "Hornet2P":
            return scene_name == "GG_Hornet_2" and next_scene in {"GG_Engine", "GG_Spa"}
        case "SlyP":
            return scene_name == "GG_Sly" and next_scene in {"GG_End_Sequence", "GG_Hornet_2"}
        case "EnragedGuardianP":
            return scene_name == "GG_Crystal_Guardian_2" and next_scene == "GG_Lost_Kin"
        case "LostKinP":
            return scene_name == "GG_Lost_Kin" and next_scene == "GG_Ghost_No_Eyes"
        case "NoEyesP":
            return scene_name == "GG_Ghost_No_Eyes" and next_scene == "GG_Traitor_Lord"
        case "TraitorLordP":
            return scene_name == "GG_Traitor_Lord" and next_scene == "GG_White_Defender"
        case "WhiteDefenderP":
            return scene_name == "GG_White_Defender" and next_scene == "GG_Spa"
        case "FailedChampionP":
            return scene_name == "GG_Failed_Champion" and next_scene in {"GG_Ghost_Markoth", "GG_Grimm_Nightmare"}
        case "MarkothP":
            return scene_name == "GG_Ghost_Markoth" and next_scene in {"GG_Watcher_Knights", "GG_Grey_Prince_Zote", "GG_Failed_Champion"}
        case "WatcherKnightsP":
            return scene_name == "GG_Watcher_Knights" and next_scene in {"GG_Soul_Tyrant", "GG_Uumuu"}
        case "SoulTyrantP":
            return scene_name == "GG_Soul_Tyrant" and next_scene in {"GG_Engine_Prime", "GG_Ghost_Markoth"}
        case "PureVesselP":
            return scene_name == "GG_Hollow_Knight" and next_scene in {"GG_End_Sequence", "GG_Radiance", "GG_Door_5_Finale"}
        case "NoskHornetP":
            return scene_name == "GG_Nosk_Hornet" and next_scene == "GG_Sly"
        case "NightmareKingGrimmP":
            return scene_name == "GG_Grimm_Nightmare" and next_scene == "GG_Spa"
        case "WhitePalaceOrb1":
            return mem.playerdata("whitePalaceOrb_1")
        case "WhitePalaceOrb2":
            return mem.playerdata("whitePalaceOrb_2")
        case "WhitePalaceOrb3":
            return mem.playerdata("whitePalaceOrb_3")
        case "WhitePalaceSecretRoom":
            return mem.playerdata("whitePalaceSecretRoomVisited")
        case "WhitePalaceLeftEntry":
            return next_scene == "White_Palace_04" and next_scene != scene_name
        case "WhitePalaceLeftWingMid":
            return scene_name == "White_Palace_04" and next_scene == "White_Palace_14"
        case "WhitePalaceRightEntry":
            return next_scene == "White_Palace_15" and next_scene != scene_name
        case "WhitePalaceRightClimb":
            return scene_name == "White_Palace_05" and next_scene == "White_Palace_16"
        case "WhitePalaceRightSqueeze":
            return scene_name == "White_Palace_16" and next_scene == "White_Palace_05"
        case "WhitePalaceRightDone":
            return scene_name == "White_Palace_05" and next_scene == "White_Palace_15"
        case "WhitePalaceTopEntry":
            return scene_name == "White_Palace_03_hub" and next_scene == "White_Palace_06"
        case "WhitePalaceTopClimb":
            return scene_name == "White_Palace_06" and next_scene == "White_Palace_07"
        case "WhitePalaceTopLeverRoom":
            return scene_name == "White_Palace_07" and next_scene == "White_Palace_12"
        case "WhitePalaceTopLastPlats":
            return scene_name == "White_Palace_12" and next_scene == "White_Palace_13"
        case "WhitePalaceThroneRoom":
            return scene_name == "White_Palace_13" and next_scene == "White_Palace_09"
        case "WhitePalaceAtrium":
            return next_scene == "White_Palace_03_hub" and next_scene != scene_name
        case "PathOfPainEntry":
            return next_scene == "White_Palace_18" and scene_name == "White_Palace_06"
        case "PathOfPainTransition1":
            return next_scene == "White_Palace_17" and scene_name == "White_Palace_18"
        case "PathOfPainTransition2":
            return next_scene == "White_Palace_19" and scene_name == "White_Palace_17"
        case "PathOfPainTransition3":
            return next_scene == "White_Palace_20" and scene_name == "White_Palace_19"
        case "WhiteFragmentLeft":
            return mem.playerdata("gotQueenFragment")
        case "WhiteFragmentRight":
            return mem.playerdata("gotKingFragment")
        case "BenchAny":
            return mem.playerdata("atBench")
        case "BenchCrossroadsStag":
            return mem.playerdata("atBench") and scene_name == "Crossroads_47"
        case "BenchGreenpathStag":
            return mem.playerdata("atBench") and scene_name == "Fungus1_16_alt"
        case "BenchQueensStation":
            return mem.playerdata("atBench") and scene_name == "Fungus2_02"
        case "BenchStorerooms":
            return mem.playerdata("atBench") and scene_name == "Ruins1_29"
        case "BenchKingsStation":
            return mem.playerdata("atBench") and scene_name == "Ruins2_08"
        case "BenchHiddenStation":
            return mem.playerdata("atBench") and scene_name == "Abyss_22"
        case "BenchRGStag":
            return mem.playerdata("atBench") and scene_name == "RestingGrounds_09"
        case "BenchQGStag":
            return mem.playerdata("atBench") and scene_name == "Fungus3_40"
        case "TollBenchQG":
            return mem.playerdata("tollBenchQueensGardens")
        case "TollBenchCity":
            return mem.playerdata("tollBenchCity")
        case "TollBenchBasin":
            return mem.playerdata("tollBenchAbyss")
        case "CityGateOpen":
            return mem.playerdata("openedCityGate")
        case "CityGateAndMantisLords":
            return mem.playerdata("openedCityGate") and mem.playerdata("defeatedMantisLords")
        case "NailsmithKilled":
            return mem.playerdata("nailsmithKilled")
        case "NailsmithChoice":
            return mem.playerdata("nailsmithKilled")
        case "TramDeepnest":
            return mem.playerdata("openedTramLower")
        case "WaterwaysManhole":
            return mem.playerdata("openedWaterwaysManhole")
        case "NotchGrimm":
            return mem.playerdata("gotGrimmNotch")
        case "SlyRescued":
            return mem.playerdata("slyRescued")
        case "FlowerQuest":
            return mem.playerdata("xunFlowerGiven")
        case "CityKey":
            return mem.playerdata("hasCityKey")
        case "CanOvercharm":
            return mem.playerdata("canOvercharm")
        case "MetGreyMourner":
            return mem.playerdata("metXun")
        case "GreyMournerSeerAscended":
            return mem.playerdata("metXun") and mem.playerdata("mothDeparted")
        case "HasDelicateFlower":
            return mem.playerdata("hasXunFlower")
        case "killedSanctumWarrior":
            return mem.playerdata("killedMageKnight")
        case "killedSoulTwister":
            return mem.playerdata("killedMage")
        case "EnterNKG":
            return scene_name == "Grimm_Main_Tent" and next_scene == "Grimm_Nightmare"
        case "EnterGreenpath":
            return scene_name != "Fungus1_01" and next_scene == "Fungus1_01"
        case "EnterGreenpathWithOvercharm":
            return (scene_name != "Fungus1_01"
                    and next_scene == "Fungus1_01"
                    and mem.playerdata("canOvercharm"))
        case "EnterSanctum":
            return scene_name != "Ruins1_23" and next_scene == "Ruins1_23"
        case "EnterSanctumWithShadeSoul":
            return (scene_name != "Ruins1_23"
                    and next_scene == "Ruins1_23"
                    and mem.playerdata("fireballLevel") == 2)
        case "EnterAnyDream":
            return next_scene.startswith("Dream_") and next_scene != scene_name
        case "EnterGodhome":
            return next_scene == "GG_Atrium" and next_scene != scene_name
        case "DgateKingdomsEdgeAcid":
            return (mem.playerdata("dreamGateScene") == "Deepnest_East_04"
                    and 27.0 < mem.playerdata("dreamGateX") < 29.0
                    and 07.0 < mem.playerdata("dreamGateY") < 9.0)
        case "FailedChampionEssence":
            return mem.playerdata("falseKnightOrbsCollected")
        case "SoulTyrantEssence":
            return mem.playerdata("mageLordOrbsCollected")
        case "LostKinEssence":
            return mem.playerdata("infectedKnightOrbsCollected")
        case "WhiteDefenderEssence":
            return mem.playerdata("whiteDefenderOrbsCollected")
        case "GreyPrinceEssence":
            return mem.playerdata("greyPrinceOrbsCollected")
        case "PreGrimmShop":
            return (mem.playerdata("hasLantern")
                    and mem.playerdata("maxHealthBase") == 6
                    and (mem.playerdata("vesselFragments") == 4 or (mem.playerdata("MPReserveMax") == 33 and mem.playerdata("vesselFragments") == 2)))
        case "PreGrimmShopTrans":
            return (mem.playerdata("hasLantern")
                    and mem.playerdata("maxHealthBase") == 6
                    and (mem.playerdata("vesselFragments") == 4 or (mem.playerdata("MPReserveMax") == 33 and mem.playerdata("vesselFragments") == 2))
                    and scene_name != "Room_shop")
        case "ElderHuEssence":
            return mem.playerdata("elderHuDefeated") == 2
        case "GalienEssence":
            return mem.playerdata("galienDefeated") == 2
        case "GorbEssence":
            return mem.playerdata("aladarSlugDefeated") == 2
        case "MarmuEssence":
            return mem.playerdata("mumCaterpillarDefeated") == 2
        case "NoEyesEssence":
            return mem.playerdata("noEyesDefeated") == 2
        case "XeroEssence":
            return mem.playerdata("xeroDefeated") == 2
        case "MarkothEssence":
            return mem.playerdata("markothDefeated") == 2
        case "DungDefenderIdol":
            return check_increased(mem, "trinket3") and scene_name == "Waterways_15"
        case "WaterwaysEntry":
            return next_scene == "Waterways_01" and next_scene != scene_name
        case "FogCanyonEntry":
            return next_scene == "Fungus3_26" and next_scene != scene_name
        case "FungalWastesEntry":
            return next_scene != scene_name and next_scene in {
                "Fungus2_06",   # Room outside Leg Eater
                "Fungus2_03",   # From Queens' Station
                "Fungus2_23",   # Bretta from Waterways
                "Fungus2_20",   # Spore Shroom room, from QG
            }
        case "SoulMasterEncountered":
            return mem.playerdata("mageLordEncountered")
        case "CrystalMoundExit":
            return scene_name == "Mines_35" and next_scene != scene_name
        case "CrystalPeakEntry":
            return next_scene in {"Mines_02", "Mines_10"} and next_scene != scene_name
        case "QueensGardensEntry":
            return next_scene in {"Fungus3_34", "Deepnest_43"} and next_scene != scene_name
        case "BasinEntry":
            return next_scene == "Abyss_04" and next_scene != scene_name
        case "HiveEntry":
            return next_scene == "Hive_01" and next_scene != scene_name
        case "KingdomsEdgeEntry":
            return next_scene == "Deepnest_East_03" and next_scene != scene_name
        case "KingdomsEdgeOvercharmedEntry":
            return (next_scene == "Deepnest_East_03" and
                    next_scene != scene_name and
                    mem.playerdata("overcharmed"))
        case "AllCharmNotchesLemm2CP":
            return (mem.playerdata("soldTrinket1") == 1 and
                    mem.playerdata("soldTrinket2") == 6 and
                    mem.playerdata("soldTrinket3") == 4)
        case "HappyCouplePlayerDataEvent":
            return mem.playerdata("nailsmithConvoArt")
        case "GodhomeBench":
            return scene_name == "GG_Spa" and scene_name != next_scene  # and not store.SplitThisTransition
        case "GodhomeLoreRoom":
            return (scene_name in {"GG_Engine", "GG_Unn", "GG_Wyrm"}
                    and scene_name != next_scene)  # and not store.SplitThisTransition)
        case "Menu":
            return scene_name == "Menu_Title"
        case "MenuClaw":
            return mem.playerdata("hasWalljump")
        case "MenuGorgeousHusk":
            return mem.playerdata("killedGorgeousHusk")
        case "TransClaw":
            return mem.playerdata("hasWalljump") and next_scene != scene_name
        case "TransGorgeousHusk":
            return mem.playerdata("killedGorgeousHusk") and next_scene != scene_name
        case "TransDescendingDark":
            return mem.playerdata("quakeLevel") == 2 and next_scene != scene_name
        case "TransTear":
            return mem.playerdata("hasAcidArmour") and next_scene != scene_name
        case "TransTearWithGrub":
            return (mem.playerdata("hasAcidArmour")
                    and "Waterways_13" in mem.playerdata("scenesGrubRescued")
                    and next_scene != scene_name)
        case "PlayerDeath":
            return mem.playerdata("health") == 0
        case "ShadeKilled":
            return check_toggled_false(mem, "soulLimited")
        case "SlyShopFinished":
            return ((mem.playerdata("vesselFragments") == 8
                     or (mem.playerdata("MPReserveMax") == 66 and mem.playerdata("vesselFragments") == 2))
                    and scene_name != "Room_shop"
                    and mem.playerdata("gotCharm_37"))
        case "ElegantKeyShoptimised":
            return mem.playerdata("maxHealthBase") == 5 and mem.playerdata("heartPieces") == 1 and mem.playerdata("hasWhiteKey")
        case "CorniferAtHome":
            return mem.playerdata("corniferAtHome") and scene_name == "Town" and next_scene == "Room_mapper"
        case "AllSeals":
            return mem.playerdata("trinket2") + mem.playerdata("soldTrinket2") == 17
        case "AllEggs":
            return mem.playerdata("rancidEggs") + mem.playerdata("jinnEggsSold") == 21
        case "SlySimpleKey":
            return mem.playerdata("slySimpleKey")
        case "AllBreakables":
            return (mem.playerdata("brokenCharm_23") and
                    mem.playerdata("brokenCharm_24") and
                    mem.playerdata("brokenCharm_25"))
        case "AllUnbreakables":
            return (mem.playerdata("fragileGreed_unbreakable") and
                    mem.playerdata("fragileHealth_unbreakable") and
                    mem.playerdata("fragileStrength_unbreakable"))
        case "MetEmilitia":
            return mem.playerdata("metEmilitia")
        case "SavedCloth":
            return mem.playerdata("savedCloth")
        case "MineLiftOpened":
            return mem.playerdata("mineLiftOpened")
        case "mapDirtmouth":
            return mem.playerdata("mapDirtmouth")
        case "mapCrossroads":
            return mem.playerdata("mapCrossroads")
        case "mapGreenpath":
            return mem.playerdata("mapGreenpath")
        case "mapFogCanyon":
            return mem.playerdata("mapFogCanyon")
        case "mapRoyalGardens":
            return mem.playerdata("mapRoyalGardens")
        case "mapFungalWastes":
            return mem.playerdata("mapFungalWastes")
        case "mapCity":
            return mem.playerdata("mapCity")
        case "mapWaterways":
            return mem.playerdata("mapWaterways")
        case "mapMines":
            return mem.playerdata("mapMines")
        case "mapDeepnest":
            return mem.playerdata("mapDeepnest")
        case "mapCliffs":
            return mem.playerdata("mapCliffs")
        case "mapOutskirts":
            return mem.playerdata("mapOutskirts")
        case "mapRestingGrounds":
            return mem.playerdata("mapRestingGrounds")
        case "mapAbyss":
            return mem.playerdata("mapAbyss")
        case "givenGodseekerFlower":
            return mem.playerdata("givenGodseekerFlower")
        case "givenOroFlower":
            return mem.playerdata("givenOroFlower")
        case "givenWhiteLadyFlower":
            return mem.playerdata("givenWhiteLadyFlower")
        case "givenEmilitiaFlower":
            return mem.playerdata("givenEmilitiaFlower")
        case "KilledOblobbles":
            return mem.playerdata("killsOblobble") == 1
        case "WhitePalaceEntry":
            return next_scene == "White_Palace_11" and next_scene != scene_name
        case "ManualSplit":
            return False
        case "AnyTransition":
            return should_split_transition(next_scene, scene_name)
        case "TransitionAfterSaveState":
            if should_split_transition(next_scene, scene_name):
                return not (next_scene in {"Room_Mender_House", "Room_Sly_Storeroom"} or
                            scene_name in {"Room_Mender_House", "Room_Sly_Storeroom"})
        case "RandoWake":
            return (not mem.playerdata("disablePause")
                    and gamestate == G.PLAYING
                    and scene_name not in menuing_scene_names)
        case "RidingStag":
            return mem.playerdata("travelling")
        case "WhitePalaceLowerEntry":
            return next_scene == "White_Palace_01" and next_scene != scene_name
        case "WhitePalaceLowerOrb":
            return next_scene == "White_Palace_02" and next_scene != scene_name
        case "QueensGardensPostArenaTransition":
            return next_scene == "Fungus3_13" and next_scene != scene_name
        case "QueensGardensFrogsTrans":
            return next_scene == "Fungus1_23" and next_scene != scene_name
        case "Pantheon1to4Entry":
            return next_scene == "GG_Boss_Door_Entrance" and next_scene != scene_name
        case "Pantheon5Entry":
            return next_scene == "GG_Vengefly_V" and next_scene != scene_name
        case "OnObtainGhostMarissa":
            return check_increased_by(mem, "dreamOrbs", 1) and scene_name == "Ruins_Bathhouse"
        case "OnObtainGhostCaelifFera":
            return check_increased_by(mem, "dreamOrbs", 1) and scene_name == "Fungus1_24"
        case "OnObtainGhostPoggy":
            return check_increased_by(mem, "dreamOrbs", 1) and scene_name == "Ruins_Elevator"
        case "OnObtainGhostGravedigger":
            return check_increased_by(mem, "dreamOrbs", 1) and scene_name == "Town"
        case "OnObtainGhostJoni":
            return check_increased_by(mem, "dreamOrbs", 1) and scene_name == "Cliffs_05"
        case "OnObtainGhostCloth":
            return (check_increased_by(mem, "dreamOrbs", 1)
                    and scene_name == "Fungus3_23"
                    and mem.playerdata("killedTraitorLord"))
        case "OnObtainGhostVespa":
            return check_increased_by(mem, "dreamOrbs", 1) and scene_name == "Hive_05" and mem.playerdata("gotCharm_29")
        case "OnObtainGhostRevek":
            return (scene_name == "RestingGrounds_08"
                    and gladeessence == 19
                    or gladeessence == 18 and check_increased_by(mem, "dreamOrbs", 1))
        case "OnObtainWanderersJournal":
            return check_increased_by(mem, "trinket1", 1)
        case "OnObtainHallownestSeal":
            return check_increased_by(mem, "trinket2", 1)
        case "OnObtainKingsIdol":
            return check_increased_by(mem, "trinket3", 1)
        case "ArcaneEgg8":
            return mem.playerdata("trinket4") == 8
        case "OnObtainArcaneEgg":
            return check_increased_by(mem, "trinket4", 1)
        case "OnObtainRancidEgg":
            return check_increased_by(mem, "rancidEggs", 1)
        case "OnObtainMaskShard":
            return check_increased_by(mem, "maxHealthBase", 1) or (check_increased_by(mem, "heartPieces", 1) and mem.playerdata("heartPieces") < 4)
        case "OnObtainVesselFragment":
            return check_increased_by(mem, "MPReserveMax", 33) or (check_increased_by(mem, "vesselFragments", 1) and mem.playerdata("vesselFragments") < 3)
        case "OnObtainSimpleKey":
            return check_increased_by(mem, "simpleKeys", 1)
        case "OnUseSimpleKey":
            return check_increased_by(mem, "simpleKeys", -1)
        case "OnObtainGrub":
            return check_increased_by(mem, "grubsCollected", 1)
        case "OnObtainPaleOre":
            return check_increased_by(mem, "ore", 1)
        case "OnObtainWhiteFragment":
            return check_increased(mem, "royalCharmState")
        case "OnDefeatGPZ":
            return check_increased_by(mem, "greyPrinceDefeats", 1)
        case "OnDefeatWhiteDefender":
            return check_increased_by(mem, "whiteDefenderDefeats", 1)
        case "FlowerRewardGiven":
            return mem.playerdata("xunRewardGiven")
        case "ColosseumBronzeUnlocked":
            return mem.playerdata("colosseumBronzeOpened")
        case "ColosseumSilverUnlocked":
            return mem.playerdata("colosseumSilverOpened")
        case "ColosseumGoldUnlocked":
            return mem.playerdata("colosseumGoldOpened")
        case "ColosseumBronzeEntry":
            return scene_name == "Room_Colosseum_01" and next_scene == "Room_Colosseum_Bronze"
        case "ColosseumSilverEntry":
            return scene_name == "Room_Colosseum_01" and next_scene == "Room_Colosseum_Silver"
        case "ColosseumGoldEntry":
            return scene_name == "Room_Colosseum_01" and next_scene == "Room_Colosseum_Gold"
        case "ColosseumBronzeExit":
            return mem.playerdata("colosseumBronzeCompleted") and next_scene != "Room_Colosseum_Bronze" and next_scene != scene_name
        case "ColosseumSilverExit":
            return mem.playerdata("colosseumSilverCompleted") and next_scene != "Room_Colosseum_Silver" and next_scene != scene_name
        case "ColosseumGoldExit":
            return mem.playerdata("colosseumGoldCompleted") and next_scene != "Room_Colosseum_Gold" and next_scene != scene_name
        case "SoulTyrantEssenceWithSanctumGrub":
            return mem.playerdata("mageLordOrbsCollected") and "Ruins1_32" in mem.playerdata("scenesGrubRescued")
        case "EndingSplit":
            return next_scene in {"Cinematic_Ending", "GG_End_Sequence"}
        case "EnterHornet1":
            return next_scene == "Fungus1_04" and next_scene != scene_name
        case "EnterSoulMaster":
            return next_scene == "Ruins1_24" and next_scene != scene_name
        case "EnterHiveKnight":
            return next_scene == "Hive_05" and next_scene != scene_name
        case "EnterHornet2":
            return next_scene == "Deepnest_East_Hornet" and next_scene != scene_name
        case "EnterBroodingMawlek":
            return next_scene == "Crossroads_09" and next_scene != scene_name
        case "EnterTMG":
            return (next_scene == "Grimm_Main_Tent" and next_scene != scene_name
                    and mem.playerdata("grimmChildLevel") == 2
                    and mem.playerdata("flamesCollected") == 3)
        case "EnterLoveTower":
            return next_scene == "Ruins2_11" and next_scene != scene_name
        case "VengeflyKingTrans":
            return mem.playerdata("zoteRescuedBuzzer") and next_scene != scene_name
        case "MegaMossChargerTrans":
            return mem.playerdata("megaMossChargerDefeated") and next_scene != scene_name
        case "GladeIdol":
            return check_increased(mem, "trinket3") and scene_name == "RestingGrounds_08"
        case "AbyssDoor":
            return mem.playerdata("abyssGateOpened")
        case "AbyssLighthouse":
            return mem.playerdata("abyssLighthouse")
        case "LumaflyLanternTransition":
            return mem.playerdata("hasLantern") and scene_name != "Room_shop"
        case "PureSnail":
            return (check_increased_by(mem, "health", 1)
                    and mem.playerdata("equippedCharm_5")    # Baldur Shell
                    and mem.playerdata("equippedCharm_7")    # Quick Focus
                    and mem.playerdata("equippedCharm_17")   # Spore Shroom
                    and mem.playerdata("equippedCharm_28"))  # Shape of Unn
    raise Exception("Unknown split name")
