from abstractClasses import Tiere


class Hund(Tiere.Tier):
    def laufen(self):
        print("laufen")


einTier = Tiere.Tier()
einTier.laufen()
