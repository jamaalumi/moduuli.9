import random

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

    def kiihdyta(self, muutos):

        self.nopeus += muutos
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif self.nopeus < 0:
            self.nopeus = 0

    def kulje(self, tunnit):

        self.matka += self.nopeus * tunnit



autot = []
for i in range(1, 11):
    rekisteritunnus = f"ABC-{i}"
    huippunopeus = random.randint(100, 200)
    autot.append(Auto(rekisteritunnus, huippunopeus))

kilpailu_kaynnissa = True
while kilpailu_kaynnissa:
    for auto in autot:
        nopeuden_muutos = random.randint(-10, 15)
        auto.kiihdyta(nopeuden_muutos)

        auto.kulje(1)

        if auto.matka >= 10000:
            kilpailu_kaynnissa = False
            break

print(f"{'Rekisteritunnus':<15}{'Huippunopeus (km/h)':<20}{'Nopeus (km/h)':<15}{'Kuljettu matka (km)':<20}")
for auto in autot:
    print(f"{auto.rekisteritunnus:<15}{auto.huippunopeus:<20}{auto.nopeus:<15}{auto.matka:<20.1f}")

