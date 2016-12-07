if __name__ == '__main__':
    import unittest
    from src.utilities import util

    # Bypass localization
    util.localize()

    import __builtin__
    __builtin__._ = lambda x: x

    from src.source.tests import klondike
    from src.source.tests import spider
    from src.source.tests import freecell
    from src.source.tests import hanoi

    def test_games():
        k_suite = unittest.TestLoader().loadTestsFromTestCase(klondike.KlondikeTest)
        sp_suite = unittest.TestLoader().loadTestsFromTestCase(spider.SpiderTest)
        fc_suite = unittest.TestLoader().loadTestsFromTestCase(freecell.FreeCellTest)
        hn_suite = unittest.TestLoader().loadTestsFromTestCase(hanoi.HanoiTest)
        unittest.TextTestRunner().run(k_suite)
        unittest.TextTestRunner().run(sp_suite)
        unittest.TextTestRunner().run(fc_suite)
        unittest.TextTestRunner().run(hn_suite)


    test_games()