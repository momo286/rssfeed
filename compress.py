import zlib

a="Depuis deux mois, des centaines de migrants, majoritairement iraniens, ont tenté de traverser la Manche sur des canots pneumatiques pour rejoindre l’Angleterre, poussant le ministre de l’intérieufghdfgldfgkd,fkg ,dfkgn, dkfngjd nfgj ndjfngjdnfgjdnfgjdfngr britannique, Sajid Javid, à déclarer un « incident majeur » et à rentrer précipitamment de ses vacances dimanche 30 décembre. Après un échange téléphonique avec son homologue français, Christophe Castener, il a annoncé un renforcement de la surveillance des plages et de la mer. Les Britanniques vont notamment financer des drones et des caméras pour surveiller la dizaine de points d’embarquement qui a été identifiée en France"

b=a.encode()
c = zlib.compress(b, 9)
print(len(b))
print(len(c))
