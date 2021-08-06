#!/usr/bin/env python3.9
# Mikhail Kolodin 2021-08-04 1.1

# solving Collatz problem... showing it :)
# https://ru.wikipedia.org/wiki/%D0%93%D0%B8%D0%BF%D0%BE%D1%82%D0%B5%D0%B7%D0%B0_%D0%9A%D0%BE%D0%BB%D0%BB%D0%B0%D1%82%D1%86%D0%B0
# https://www.popmech.ru/science/510082-10-slozhneyshih-matematicheskih-zadach-kotorye-ostayutsya-nereshennymi/

LIM = 1_000

done = set()

def test(i):
    global done
    print(i, end=", ")
    if i in done:
        print("done.")
        return
    if i % 2:
        done.add(i)
        test(3*i+1)
    else:
        done.add(i)
        test(i//2)

def main():
    for i in range(1, LIM+1):
        test(i)

main()

# ~ 1, 4, 2, 1, done.
# ~ 2, done.
# ~ 3, 10, 5, 16, 8, 4, done.
# ~ 4, done.
# ~ 5, done.
# ~ 6, 3, done.
# ~ 7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, done.
# ~ 8, done.
# ~ 9, 28, 14, 7, done.
# ~ 10, done.
# ~ 11, done.
# ~ 12, 6, done.
# ~ 13, done.
# ~ 14, done.
# ~ 15, 46, 23, 70, 35, 106, 53, 160, 80, 40, done.
# ~ 16, done.
# ~ 17, done.
# ~ 18, 9, done.
# ~ 19, 58, 29, 88, 44, 22, done.
# ~ 20, done.
# ~ 21, 64, 32, 16, done.
# ~ 22, done.
# ~ 23, done.
# ~ 24, 12, done.
# ~ 25, 76, 38, 19, done.
# ~ 26, done.
# ~ 27, 82, 41, 124, 62, 31, 94, 47, 142, 71, 214, 107, 322, 161, 484, 242, 121, 364, 182, 91, 274, 137, 412, 206, 103, 310, 155, 466, 233, 700, 350, 175, 526, 263, 790, 395, 1186, 593, 1780, 890, 445, 1336, 668, 334, 167, 502, 251, 754, 377, 1132, 566, 283, 850, 425, 1276, 638, 319, 958, 479, 1438, 719, 2158, 1079, 3238, 1619, 4858, 2429, 7288, 3644, 1822, 911, 2734, 1367, 4102, 2051, 6154, 3077, 9232, 4616, 2308, 1154, 577, 1732, 866, 433, 1300, 650, 325, 976, 488, 244, 122, 61, 184, 92, 46, done.
# ~ 28, done.
# ~ 29, done.
# ~ 30, 15, done.
# ~ 31, done.
# ~ 32, done.
# ~ 33, 100, 50, 25, done.
# ~ 34, done.
# ~ 35, done.
# ~ 36, 18, done.
# ~ 37, 112, 56, 28, done.
# ~ 38, done.
# ~ 39, 118, 59, 178, 89, 268, 134, 67, 202, 101, 304, 152, 76, done.
# ~ 40, done.
# ~ 41, done.
# ~ 42, 21, done.
# ~ 43, 130, 65, 196, 98, 49, 148, 74, 37, done.
# ~ 44, done.
# ~ 45, 136, 68, 34, done.
# ~ 46, done.
# ~ 47, done.
# ~ 48, 24, done.
# ~ 49, done.
# ~ 50, done.
# ~ 51, 154, 77, 232, 116, 58, done.
# ~ 52, done.
# ~ 53, done.
# ~ 54, 27, done.
# ~ 55, 166, 83, 250, 125, 376, 188, 94, done.
# ~ 56, done.
# ~ 57, 172, 86, 43, done.
# ~ 58, done.
# ~ 59, done.
# ~ 60, 30, done.
# ~ 61, done.
# ~ 62, done.
# ~ 63, 190, 95, 286, 143, 430, 215, 646, 323, 970, 485, 1456, 728, 364, done.
# ~ 64, done.
# ~ 65, done.
# ~ 66, 33, done.
# ~ 67, done.
# ~ 68, done.
# ~ 69, 208, 104, 52, done.
# ~ 70, done.
# ~ 71, done.
# ~ 72, 36, done.
# ~ 73, 220, 110, 55, done.
# ~ 74, done.
# ~ 75, 226, 113, 340, 170, 85, 256, 128, 64, done.
# ~ 76, done.
# ~ 77, done.
# ~ 78, 39, done.
# ~ 79, 238, 119, 358, 179, 538, 269, 808, 404, 202, done.
# ~ 80, done.
# ~ 81, 244, done.
# ~ 82, done.
# ~ 83, done.
# ~ 84, 42, done.
# ~ 85, done.
# ~ 86, done.
# ~ 87, 262, 131, 394, 197, 592, 296, 148, done.
# ~ 88, done.
# ~ 89, done.
# ~ 90, 45, done.
# ~ 91, done.
# ~ 92, done.
# ~ 93, 280, 140, 70, done.
# ~ 94, done.
# ~ 95, done.
# ~ 96, 48, done.
# ~ 97, 292, 146, 73, done.
# ~ 98, done.
# ~ 99, 298, 149, 448, 224, 112, done.
# ~ 100, done.
# ~ 101, done.
# ~ 102, 51, done.
# ~ 103, done.
# ~ 104, done.
# ~ 105, 316, 158, 79, done.
# ~ 106, done.
# ~ 107, done.
# ~ 108, 54, done.
# ~ 109, 328, 164, 82, done.
# ~ 110, done.
# ~ 111, 334, done.
# ~ 112, done.
# ~ 113, done.
# ~ 114, 57, done.
# ~ 115, 346, 173, 520, 260, 130, done.
# ~ 116, done.
# ~ 117, 352, 176, 88, done.
# ~ 118, done.
# ~ 119, done.
# ~ 120, 60, done.
# ~ 121, done.
# ~ 122, done.
# ~ 123, 370, 185, 556, 278, 139, 418, 209, 628, 314, 157, 472, 236, 118, done.
# ~ 124, done.
# ~ 125, done.
# ~ 126, 63, done.
# ~ 127, 382, 191, 574, 287, 862, 431, 1294, 647, 1942, 971, 2914, 1457, 4372, 2186, 1093, 3280, 1640, 820, 410, 205, 616, 308, 154, done.
# ~ 128, done.
# ~ 129, 388, 194, 97, done.
# ~ 130, done.
# ~ 131, done.
# ~ 132, 66, done.
# ~ 133, 400, 200, 100, done.
# ~ 134, done.
# ~ 135, 406, 203, 610, 305, 916, 458, 229, 688, 344, 172, done.
# ~ 136, done.
# ~ 137, done.
# ~ 138, 69, done.
# ~ 139, done.
# ~ 140, done.
# ~ 141, 424, 212, 106, done.
# ~ 142, done.
# ~ 143, done.
# ~ 144, 72, done.
# ~ 145, 436, 218, 109, done.
# ~ 146, done.
# ~ 147, 442, 221, 664, 332, 166, done.
# ~ 148, done.
# ~ 149, done.
# ~ 150, 75, done.
# ~ 151, 454, 227, 682, 341, 1024, 512, 256, done.
# ~ 152, done.
# ~ 153, 460, 230, 115, done.
# ~ 154, done.
# ~ 155, done.
# ~ 156, 78, done.
# ~ 157, done.
# ~ 158, done.
# ~ 159, 478, 239, 718, 359, 1078, 539, 1618, 809, 2428, 1214, 607, 1822, done.
# ~ 160, done.
# ~ 161, done.
# ~ 162, 81, done.
# ~ 163, 490, 245, 736, 368, 184, done.
# ~ 164, done.
# ~ 165, 496, 248, 124, done.
# ~ 166, done.
# ~ 167, done.
# ~ 168, 84, done.
# ~ 169, 508, 254, 127, done.
# ~ 170, done.
# ~ 171, 514, 257, 772, 386, 193, 580, 290, 145, done.
# ~ 172, done.
# ~ 173, done.
# ~ 174, 87, done.
# ~ 175, done.
# ~ 176, done.
# ~ 177, 532, 266, 133, done.
# ~ 178, done.
# ~ 179, done.
# ~ 180, 90, done.
# ~ 181, 544, 272, 136, done.
# ~ 182, done.
# ~ 183, 550, 275, 826, 413, 1240, 620, 310, done.
# ~ 184, done.
# ~ 185, done.
# ~ 186, 93, done.
# ~ 187, 562, 281, 844, 422, 211, 634, 317, 952, 476, 238, done.
# ~ 188, done.
# ~ 189, 568, 284, 142, done.
# ~ 190, done.
# ~ 191, done.
# ~ 192, 96, done.
# ~ 193, done.
# ~ 194, done.
# ~ 195, 586, 293, 880, 440, 220, done.
# ~ 196, done.
# ~ 197, done.
# ~ 198, 99, done.
# ~ 199, 598, 299, 898, 449, 1348, 674, 337, 1012, 506, 253, 760, 380, 190, done.
# ~ 200, done.

