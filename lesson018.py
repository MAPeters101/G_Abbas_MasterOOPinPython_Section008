class Pakistan:
    def language(self):
        print("Urdu")

class Punjab(Pakistan):
    def language(self):
        super().language()

class KPK(Pakistan):
    def language(self):
        print("Pasto")

pakistan = Pakistan()
pakistan.language()

punjab = Punjab()
punjab.language()

kpk = KPK()
kpk.language()
