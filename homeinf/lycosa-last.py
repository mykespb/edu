#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2026
# 2026-04-28 2026-04-28 1.0
# lycosa.py

# ~ Проанализировать список из 221 вида тарантулов и определить,
# ~ сколько названий видов заканчивается на какую букву.

specia = """
Lycosa abnormis
Lycosa accurata
Lycosa adusta
Lycosa affinis
Lycosa anclata
Lycosa apacha
Lycosa approximata
Lycosa aragogi
Lycosa arambagensis
Lycosa ariadnae
Lycosa articulata
Lycosa artigasi
Lycosa asiatica
Lycosa aurea
Lycosa auroguttata
Lycosa australicola
Lycosa australis
Lycosa balaramai
Lycosa barnesi
Lycosa baulnyi
Lycosa bedeli
Lycosa beihaiensis
Lycosa bezzii
Lycosa bhatnagari
Lycosa biolleyi
Lycosa bistriata
Lycosa boninensis
Lycosa bonneti
Lycosa brunnea
Lycosa caenosa
Lycosa canescens
Lycosa capensis
Lycosa carbonelli
Lycosa carmichaeli
Lycosa cerrofloresiana
Lycosa chaperi
Lycosa choudhuryi
Lycosa cingara
Lycosa clarissa
Lycosa coelestis
Lycosa connexa
Lycosa contestata
Lycosa corallina
Lycosa coreana
Lycosa cowlei
Lycosa cretacea
Lycosa dacica
Lycosa danjiangensis
Lycosa dilatata
Lycosa dimota
Lycosa discolor
Lycosa elysae
Lycosa emuncta
Lycosa erjianensis
Lycosa erythrognatha
Lycosa eutypa
Lycosa falconensis
Lycosa fasciiventris
Lycosa fernandezi
Lycosa ferriculosa
Lycosa formosana
Lycosa frigens
Lycosa fuscana
Lycosa futilis
Lycosa geotubalis
Lycosa gibsoni
Lycosa gigantea
Lycosa gilberta
Lycosa gobiensis
Lycosa godeffroyi
Lycosa goliathus
Lycosa grahami
Lycosa guayaquiliana
Lycosa hickmani
Lycosa hildegardae
Lycosa hispanica
Lycosa horrida
Lycosa howarthi
Lycosa illicita
Lycosa immanis
Lycosa impavida
Lycosa implacida
Lycosa indagatrix
Lycosa indomita
Lycosa infesta
Lycosa injusta
Lycosa innocua
Lycosa inornata
Lycosa insulana
Lycosa insularis
Lycosa intermedialis
Lycosa interstitialis
Lycosa inviolata
Lycosa iranii
Lycosa ishikariana
Lycosa isolata
Lycosa jagadalpurensis
Lycosa kempi
Lycosa koyuga
Lycosa labialis
Lycosa labialisoides
Lycosa laeta
Lycosa lambai
Lycosa langei
Lycosa lativulva
Lycosa lebakensis
Lycosa leuckarti
Lycosa leucogastra
Lycosa leucophaeoides
Lycosa leucophthalma
Lycosa leucotaeniata
Lycosa liliputana
Lycosa longivulva
Lycosa mackenziei
Lycosa maculata
Lycosa madagascariensis
Lycosa madani
Lycosa magallanica
Lycosa magnifica
Lycosa mahabaleshwarensis
Lycosa masteri
Lycosa matusitai
Lycosa maya
Lycosa mexicana
Lycosa minae
Lycosa molyneuxi
Lycosa mordax
Lycosa moulmeinensis
Lycosa mukana
Lycosa munieri
Lycosa muntea
Lycosa musgravei
Lycosa niceforoi
Lycosa nigricans
Lycosa nigromarmorata
Lycosa nigropunctata
Lycosa nigrotaeniata
Lycosa nigrotibialis
Lycosa nilotica
Lycosa nordenskjoldi
Lycosa oculata
Lycosa ovalata
Lycosa pachana
Lycosa palliata
Lycosa pampeana
Lycosa paranensis
Lycosa parvipudens
Lycosa patagonica
Lycosa pavlovi
Lycosa perkinsi
Lycosa perspicua
Lycosa philadelphiana
Lycosa phipsoni
Lycosa pia
Lycosa pictipes
Lycosa pictula
Lycosa pintoi
Lycosa piochardi
Lycosa poliostoma
Lycosa poonaensis
Lycosa porteri
Lycosa praegrandis
Lycosa praestans
Lycosa proletarioides
Lycosa prolifica
Lycosa pulchella
Lycosa punctiventralis
Lycosa quadrimaculata
Lycosa rimicola
Lycosa ringens
Lycosa rostrata
Lycosa rufisterna
Lycosa russea
Lycosa sabulosa
Lycosa salifodina
Lycosa salvadorensis
Lycosa separata
Lycosa septembris
Lycosa sericovittata
Lycosa serranoa
Lycosa shahapuraensis
Lycosa shaktae
Lycosa shansia
Lycosa shillongensis
Lycosa signata
Lycosa signiventris
Lycosa sigridae
Lycosa similis
Lycosa singoriensis — Южнорусский тарантул
Lycosa sochoi
Lycosa storeniformis
Lycosa subfusca
Lycosa suboculata
Lycosa suzukii
Lycosa sylvatica
Lycosa tarantula — Апулийский тарантул
Lycosa tarantuloides
Lycosa tasmanicola
Lycosa teranganicola
Lycosa terrestris
Lycosa tetrophthalma
Lycosa thoracica
Lycosa thorelli
Lycosa tista
Lycosa transversa
Lycosa trichopus
Lycosa tula
Lycosa u-album
Lycosa vachoni
Lycosa vellutina
Lycosa ventralis
Lycosa vittata
Lycosa wadaiensis
Lycosa wangi
Lycosa woonda
Lycosa wroughtoni
Lycosa wulsini
Lycosa yalkara
Lycosa yerburyi
Lycosa yizhangensis
Lycosa yunnanensis
"""

from collections import Counter

cnt = Counter()

for species in specia.strip().split("\n"):
    letter = species.split()[1][-1]
    cnt[letter] += 1

print(cnt)

for k, v in cnt.items():
    print(f"ending: {k} => {v} word(s)")

# ~ Counter({'a': 106, 's': 56, 'i': 49, 'e': 6, 'x': 2, 'r': 1, 'm': 1})
# ~ ending: s => 56 word(s)
# ~ ending: a => 106 word(s)
# ~ ending: i => 49 word(s)
# ~ ending: e => 6 word(s)
# ~ ending: r => 1 word(s)
# ~ ending: x => 2 word(s)
# ~ ending: m => 1 word(s)
