#!/usr/bin/env python3.9
# Mikhail Kolodin 2021-08-04 2021-08-06 3.1

# solving Collatz problem... showing it :)
# https://ru.wikipedia.org/wiki/%D0%93%D0%B8%D0%BF%D0%BE%D1%82%D0%B5%D0%B7%D0%B0_%D0%9A%D0%BE%D0%BB%D0%BB%D0%B0%D1%82%D1%86%D0%B0
# https://www.popmech.ru/science/510082-10-slozhneyshih-matematicheskih-zadach-kotorye-ostayutsya-nereshennymi/
# https://www.youtube.com/watch?v=094y1Z2wpJg The Simplest Math Problem No One Can Solve
#    8 312 054 просмотра30 июл. 2021 г
# I tested it up to 1 million
# make good graph

LIM = 20

done = {}

def ext(i, j):
    if i in done:
        done[i] |= {j}
    else:
        done[i] = {j}

def test(i, j):
    global done
    if i in done:
        if j:
            ext(i, j)
        return
    if j:
        ext(i, j)
    if i % 2:
        test(3*i+1, i)
    else:
        test(i//2, i)

def main():
    for i in range(1, LIM+1):
        test(i, 0)

def digr():
    print("digraph G {")
    for k, v in done.items():
        for e in v:
            print(f"{e} -> {k};")
    print("}")


main()
# ~ print(done)
digr()


# ~ 1 (0), 4 (1), 2 (4), 1 (2), 4 (1), done.
# ~ 2 (0), done.
# ~ 3 (0), 10 (3), 5 (10), 16 (5), 8 (16), 4 (8), done.
# ~ 4 (0), done.
# ~ 5 (0), done.
# ~ 6 (0), 3 (6), 10 (3), done.
# ~ 7 (0), 22 (7), 11 (22), 34 (11), 17 (34), 52 (17), 26 (52), 13 (26), 40 (13), 20 (40), 10 (20), done.
# ~ 8 (0), done.
# ~ 9 (0), 28 (9), 14 (28), 7 (14), 22 (7), done.
# ~ 10 (0), done.
# ~ 11 (0), done.
# ~ 12 (0), 6 (12), 3 (6), done.
# ~ 13 (0), done.
# ~ 14 (0), done.
# ~ 15 (0), 46 (15), 23 (46), 70 (23), 35 (70), 106 (35), 53 (106), 160 (53), 80 (160), 40 (80), done.
# ~ 16 (0), done.
# ~ 17 (0), done.
# ~ 18 (0), 9 (18), 28 (9), done.
# ~ 19 (0), 58 (19), 29 (58), 88 (29), 44 (88), 22 (44), done.
# ~ 20 (0), done.
# ~ 21 (0), 64 (21), 32 (64), 16 (32), done.
# ~ 22 (0), done.
# ~ 23 (0), done.
# ~ 24 (0), 12 (24), 6 (12), done.
# ~ 25 (0), 76 (25), 38 (76), 19 (38), 58 (19), done.
# ~ 26 (0), done.
# ~ 27 (0), 82 (27), 41 (82), 124 (41), 62 (124), 31 (62), 94 (31), 47 (94), 142 (47), 71 (142), 214 (71), 107 (214), 322 (107), 161 (322), 484 (161), 242 (484), 121 (242), 364 (121), 182 (364), 91 (182), 274 (91), 137 (274), 412 (137), 206 (412), 103 (206), 310 (103), 155 (310), 466 (155), 233 (466), 700 (233), 350 (700), 175 (350), 526 (175), 263 (526), 790 (263), 395 (790), 1186 (395), 593 (1186), 1780 (593), 890 (1780), 445 (890), 1336 (445), 668 (1336), 334 (668), 167 (334), 502 (167), 251 (502), 754 (251), 377 (754), 1132 (377), 566 (1132), 283 (566), 850 (283), 425 (850), 1276 (425), 638 (1276), 319 (638), 958 (319), 479 (958), 1438 (479), 719 (1438), 2158 (719), 1079 (2158), 3238 (1079), 1619 (3238), 4858 (1619), 2429 (4858), 7288 (2429), 3644 (7288), 1822 (3644), 911 (1822), 2734 (911), 1367 (2734), 4102 (1367), 2051 (4102), 6154 (2051), 3077 (6154), 9232 (3077), 4616 (9232), 2308 (4616), 1154 (2308), 577 (1154), 1732 (577), 866 (1732), 433 (866), 1300 (433), 650 (1300), 325 (650), 976 (325), 488 (976), 244 (488), 122 (244), 61 (122), 184 (61), 92 (184), 46 (92), done.
# ~ 28 (0), done.
# ~ 29 (0), done.
# ~ 30 (0), 15 (30), 46 (15), done.
# ~ 31 (0), done.
# ~ 32 (0), done.
# ~ 33 (0), 100 (33), 50 (100), 25 (50), 76 (25), done.
# ~ 34 (0), done.
# ~ 35 (0), done.
# ~ 36 (0), 18 (36), 9 (18), done.
# ~ 37 (0), 112 (37), 56 (112), 28 (56), done.
# ~ 38 (0), done.
# ~ 39 (0), 118 (39), 59 (118), 178 (59), 89 (178), 268 (89), 134 (268), 67 (134), 202 (67), 101 (202), 304 (101), 152 (304), 76 (152), done.
# ~ 40 (0), done.
# ~ 41 (0), done.
# ~ 42 (0), 21 (42), 64 (21), done.
# ~ 43 (0), 130 (43), 65 (130), 196 (65), 98 (196), 49 (98), 148 (49), 74 (148), 37 (74), 112 (37), done.
# ~ 44 (0), done.
# ~ 45 (0), 136 (45), 68 (136), 34 (68), done.
# ~ 46 (0), done.
# ~ 47 (0), done.
# ~ 48 (0), 24 (48), 12 (24), done.
# ~ 49 (0), done.
# ~ 50 (0), done.
# ~ 51 (0), 154 (51), 77 (154), 232 (77), 116 (232), 58 (116), done.
# ~ 52 (0), done.
# ~ 53 (0), done.
# ~ 54 (0), 27 (54), 82 (27), done.
# ~ 55 (0), 166 (55), 83 (166), 250 (83), 125 (250), 376 (125), 188 (376), 94 (188), done.
# ~ 56 (0), done.
# ~ 57 (0), 172 (57), 86 (172), 43 (86), 130 (43), done.
# ~ 58 (0), done.
# ~ 59 (0), done.
# ~ 60 (0), 30 (60), 15 (30), done.
# ~ 61 (0), done.
# ~ 62 (0), done.
# ~ 63 (0), 190 (63), 95 (190), 286 (95), 143 (286), 430 (143), 215 (430), 646 (215), 323 (646), 970 (323), 485 (970), 1456 (485), 728 (1456), 364 (728), done.
# ~ 64 (0), done.
# ~ 65 (0), done.
# ~ 66 (0), 33 (66), 100 (33), done.
# ~ 67 (0), done.
# ~ 68 (0), done.
# ~ 69 (0), 208 (69), 104 (208), 52 (104), done.
# ~ 70 (0), done.
# ~ 71 (0), done.
# ~ 72 (0), 36 (72), 18 (36), done.
# ~ 73 (0), 220 (73), 110 (220), 55 (110), 166 (55), done.
# ~ 74 (0), done.
# ~ 75 (0), 226 (75), 113 (226), 340 (113), 170 (340), 85 (170), 256 (85), 128 (256), 64 (128), done.
# ~ 76 (0), done.
# ~ 77 (0), done.
# ~ 78 (0), 39 (78), 118 (39), done.
# ~ 79 (0), 238 (79), 119 (238), 358 (119), 179 (358), 538 (179), 269 (538), 808 (269), 404 (808), 202 (404), done.
# ~ 80 (0), done.
# ~ 81 (0), 244 (81), done.
# ~ 82 (0), done.
# ~ 83 (0), done.
# ~ 84 (0), 42 (84), 21 (42), done.
# ~ 85 (0), done.
# ~ 86 (0), done.
# ~ 87 (0), 262 (87), 131 (262), 394 (131), 197 (394), 592 (197), 296 (592), 148 (296), done.
# ~ 88 (0), done.
# ~ 89 (0), done.
# ~ 90 (0), 45 (90), 136 (45), done.
# ~ 91 (0), done.
# ~ 92 (0), done.
# ~ 93 (0), 280 (93), 140 (280), 70 (140), done.
# ~ 94 (0), done.
# ~ 95 (0), done.
# ~ 96 (0), 48 (96), 24 (48), done.
# ~ 97 (0), 292 (97), 146 (292), 73 (146), 220 (73), done.
# ~ 98 (0), done.
# ~ 99 (0), 298 (99), 149 (298), 448 (149), 224 (448), 112 (224), done.
# ~ 100 (0), done.

# ~ [(1, 2), (2, 4), (3, 6), (4, 1), (5, 10), (6, 12), (7, 14), (8, 16),
# ~ (9, 18), (10, 3), (11, 22), (12, 24), (13, 26), (14, 28), (15, 30),
# ~ (16, 5), (17, 34), (18, 36), (19, 38), (20, 40), (21, 42), (22, 7),
# ~ (23, 46), (24, 48), (25, 50), (26, 52), (27, 54), (28, 9), (29, 58),
# ~ (30, 60), (31, 62), (32, 64), (33, 66), (34, 11), (35, 70), (36, 72),
# ~ (37, 74), (38, 76), (39, 78), (40, 13), (41, 82), (42, 84), (43, 86),
# ~ (44, 88), (45, 90), (46, 15), (47, 94), (48, 96), (49, 98), (50, 100),
# ~ (52, 17), (53, 106), (55, 110), (56, 112), (58, 19), (59, 118), (61,
# ~ 122), (62, 124), (64, 21), (65, 130), (67, 134), (68, 136), (70, 23),
# ~ (71, 142), (73, 146), (74, 148), (76, 25), (77, 154), (80, 160), (82,
# ~ 27), (83, 166), (85, 170), (86, 172), (88, 29), (89, 178), (91, 182),
# ~ (92, 184), (94, 31), (95, 190), (98, 196), (100, 33), (101, 202), (103,
# ~ 206), (104, 208), (106, 35), (107, 214), (110, 220), (112, 37), (113,
# ~ 226), (116, 232), (118, 39), (119, 238), (121, 242), (122, 244), (124,
# ~ 41), (125, 250), (128, 256), (130, 43), (131, 262), (134, 268), (136,
# ~ 45), (137, 274), (140, 280), (142, 47), (143, 286), (146, 292), (148,
# ~ 49), (149, 298), (152, 304), (154, 51), (155, 310), (160, 53), (161,
# ~ 322), (166, 55), (167, 334), (170, 340), (172, 57), (175, 350), (178,
# ~ 59), (179, 358), (182, 364), (184, 61), (188, 376), (190, 63), (196,
# ~ 65), (197, 394), (202, 67), (206, 412), (208, 69), (214, 71), (215,
# ~ 430), (220, 73), (224, 448), (226, 75), (232, 77), (233, 466), (238,
# ~ 79), (242, 484), (244, 488), (250, 83), (251, 502), (256, 85), (262,
# ~ 87), (263, 526), (268, 89), (269, 538), (274, 91), (280, 93), (283,
# ~ 566), (286, 95), (292, 97), (296, 592), (298, 99), (304, 101), (310,
# ~ 103), (319, 638), (322, 107), (323, 646), (325, 650), (334, 668), (340,
# ~ 113), (350, 700), (358, 119), (364, 121), (376, 125), (377, 754), (394,
# ~ 131), (395, 790), (404, 808), (412, 137), (425, 850), (430, 143), (433,
# ~ 866), (445, 890), (448, 149), (466, 155), (479, 958), (484, 161), (485,
# ~ 970), (488, 976), (502, 167), (526, 175), (538, 179), (566, 1132),
# ~ (577, 1154), (592, 197), (593, 1186), (638, 1276), (646, 215), (650,
# ~ 1300), (668, 1336), (700, 233), (719, 1438), (728, 1456), (754, 251),
# ~ (790, 263), (808, 269), (850, 283), (866, 1732), (890, 1780), (911,
# ~ 1822), (958, 319), (970, 323), (976, 325), (1079, 2158), (1132, 377),
# ~ (1154, 2308), (1186, 395), (1276, 425), (1300, 433), (1336, 445),
# ~ (1367, 2734), (1438, 479), (1456, 485), (1619, 3238), (1732, 577),
# ~ (1780, 593), (1822, 3644), (2051, 4102), (2158, 719), (2308, 4616),
# ~ (2429, 4858), (2734, 911), (3077, 6154), (3238, 1079), (3644, 7288),
# ~ (4102, 1367), (4616, 9232), (4858, 1619), (6154, 2051), (7288, 2429),
# ~ (9232, 3077)]

