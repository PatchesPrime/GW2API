import unittest
from GW2API import AccountAPI
from GW2API import descriptions
from .secrets import APIKEY


class TestAccountAPI(unittest.TestCase):
    def getAccount(self):
        return(AccountAPI(APIKEY))

    def test_getWallet(self):
        api = self.getAccount()

        # Just verify stuff is in it.
        self.assertTrue(len(api.getWallet()) > 5)

        # Verify data.
        for unit in api.wallet:
            self.assertTrue('name' in unit.keys())
            self.assertTrue('icon' in unit.keys())
            self.assertTrue('description' in unit.keys())

    def test_getRecipes(self):
        api = self.getAccount()

        # Verify populated.
        self.assertTrue(len(api.getRecipes()) > 50)

        # Verify some information.
        self.assertTrue(api.recipes[0].id == 842)
        self.assertTrue(api.recipes[0].time == 5000)

    def test_getTitles(self):
        api = self.getAccount()

        self.assertTrue(len(api.getTitles()) > 5)
        self.assertTrue(api.titles[0].name == 'Been there. Done that.')

    def test_getBank(self):
        api = self.getAccount()

        self.assertTrue(len(api.getBank()) > 5)

        for unit in api.bank:
            self.assertTrue(isinstance(unit['object'], descriptions.Item))

    def test_getAchievements(self):
        api = self.getAccount()

        self.assertTrue(len(api.getAchievements()) > 5)
        self.assertTrue(api.achievements[0]['object'].name == 'Centaur Slayer')

        for unit in api.achievements:
            self.assertTrue(
                isinstance(unit['object'], descriptions.Achievement)
            )

    def test_getMaterials(self):
        api = self.getAccount()

        self.assertTrue(len(api.getMaterials()) > 5)
        self.assertTrue(api.materials[0]['object'].name == 'Carrot')

        for unit in api.materials:
            self.assertTrue(
                isinstance(unit['object'], descriptions.Item)
            )

    def test_getOutfits(self):
        api = self.getAccount()

        self.assertTrue(len(api.getOutfits()) > 2)
        self.assertTrue(api.outfits[0].name == 'Hexed Outfit')

        for unit in api.outfits:
            self.assertTrue(
                isinstance(unit, descriptions.Outfit)
            )

    def test_getMasteries(self):
        api = self.getAccount()

        self.assertTrue(len(api.getMasteries()) > 5)
        self.assertTrue(api.masteries[0]['object'].name == 'Exalted Lore')

        for unit in api.masteries:
            self.assertTrue(
                isinstance(unit['object'], descriptions.Mastery)
            )

    def test_getInventory(self):
        api = self.getAccount()

        # No len because I only have one slot..Might change.
        api.getInventory()
        self.assertTrue(api.inventory[0]['object'].name == 'Royal Terrace Pass')

        for unit in api.inventory:
            self.assertTrue(
                isinstance(unit['object'], descriptions.Item)
            )

    def test_getTradeHistory(self):
        api = self.getAccount()

        # Yep.
        self.assertTrue(all(k in api.getTradeHistory() for k in ('buying', 'selling', 'bought')))

        # Double yep.
        self.assertTrue(all(k in dir(api) for k in ('buying', 'selling', 'bought')))

    def test_getCharacters(self):
        api = self.getAccount()

        self.assertTrue(len(api.getCharacters()) > 3)

        for unit in api.characters:
            self.assertTrue(isinstance(unit, descriptions.Character))

    def test_getDyes(self):
        api = self.getAccount()

        self.assertTrue(len(api.getDyes()) > 100)  # I have a lot of dyes.

        for unit in api.dyes:
            self.assertTrue(isinstance(unit, descriptions.Dye))

        self.assertTrue(api.dyes[0].name == 'Chalk')

    def test_getSkins(self):
        api = self.getAccount()

        self.assertTrue(len(api.getSkins()) > 100)

        for unit in api.skins:
            self.assertTrue(isinstance(unit, descriptions.Skin))

        self.assertTrue(api.skins[0].name == 'Chainmail Leggings')

    def test_getTraits(self):
        api = self.getAccount()

        # Call it once for speed.
        build = api.getTraits('Necromancer Patches')

        # Today on ugly, we have this.
        for unit in build.values():
            for area in unit:
                self.assertTrue(
                    isinstance(area['line'], descriptions.Specialization)
                )
                for trait in area['traits']:
                    self.assertTrue(
                        isinstance(trait, descriptions.Trait)
                    )

    def test_getMatchResults(self):
        api = self.getAccount()

        results = api.getMatchResults('all')

        for match in results:
            self.assertTrue(
                isinstance(match, descriptions.PVPMatch)
            )

    def test_getPVPStats(self):
        api = self.getAccount()

        strings = ('pvp_rank', 'pvp_wins', 'pvp_losses',
                   'pvp_desertions', 'pvp_byes', 'pvp_forfeits',
                   'pvp_professions', 'pvp_ranked', 'pvp_unranked')

        # This just assigns attributes.
        api.getPVPStats()

        # Dirty check.
        self.assertTrue(
            all(k in dir(api) for k in strings)
        )

    def test_getGuildRanks(self):
        api = self.getAccount()

        # NULL represent?
        guild = api.getGuildRanks('A4AF6C09-452F-44EE-BD3E-704FB5C371FB')

        # If this is here, it's the right thing.
        self.assertTrue(guild[0]['id'] == 'Grand Poobah')

    def test_getGuildMembers(self):
        api = self.getAccount()

        members = api.getGuildMembers('A4AF6C09-452F-44EE-BD3E-704FB5C371FB')

        # Am I there?
        self.assertTrue(members[0]['name'] == 'Patches.7584')