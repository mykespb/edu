# tests fot lists

# Дана строка с именами.
# Имена могут повторяться и идти в произвольном порядке.
# Распечатать все имена в алфавитном порядке по 1 разу.

s = """Olivia Isabelle Isabelle Ava Amelia Ellie Emily Jessica Isla Isabella Poppy Albert Austin Mia Chloe Scarlett Sophie Lily Ruby Evie Grace Ella Sophia Chloe Scarlett Freya Isabelle Phoebe Alice Ellie Bethany Maryam Heidi Paige Faith Rose Ivy Florence Hurriet Maddison Zoe Samuel Jack Joseph Harry Alfie Isabelle Jacob Thomas Charlie Ellie Albert Chloe Scarlett Austin Oscar James William Joshua George Ethan Noah Archie Henry Leo Chloe Scarlett John Oliver David Ryan Dexter Connor Isabelle Albert Austin Stanley Ellie Theodore Owen Caleb"""

# ~ names = []
# ~ for name in s.split():
    # ~ if name not in names:
        # ~ names.append(name)
# ~ names.sort()
# ~ for name in names:
    # ~ print(name, end=", ")

# ~ print(*(sorted(set(s.split()))), sep=", ")

def cap(stroka):
    """capitalize"""
    return stroka[0].upper() + stroka[1:].lower() if stroka else ""

print(*(sorted(cap(q[::-1]) for q in s.split())))

# ~ Acissej Aihpos Ailema Aim Aivilo Alle Allebasi Alsi Auhsoj Ava Ayerf Belac Bocaj Divad Ebeohp Ecarg Ecila Ecnerolf Egiap Egroeg Eifla Eihcra Eihpos Eille Eille Eille Eille Eilrahc Eive Ellebasi Ellebasi Ellebasi Ellebasi Ellebasi Eolhc Eolhc Eolhc Eolhc Eoz Erodoeht Esor Haon Hpesoj Htiaf Idieh Kcaj Leumas Mailliw Mayram Nahte Nayr Newo Nhoj Nitsua Nitsua Nitsua Nosiddam Oel Racso Retxed Revilo Ronnoc Samoht Semaj Teirruh Trebla Trebla Trebla Ttelracs Ttelracs Ttelracs Ttelracs Ybur Yelnats Ylil Ylime Ynahteb Yppop Yrneh Yrrah Yvi
