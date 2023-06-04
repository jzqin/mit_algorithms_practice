import unittest
from satisfying_booking     import satisfying_booking

verbose = True

tests = (
    (
        ((2, 19), (17, 18), (12, 25), (5, 15), (9, 11)),
        ((1, 2, 5), (2, 5, 9), (3, 9, 11), (2, 11, 12), (3, 12, 15), (2, 15, 17), (3, 17, 18), (2, 18, 19), (1, 19, 25)),
    ),
    (
        ((7, 20), (35, 44), (71, 80), (72, 89), (2, 77), (7, 78), (23, 26), (36, 44), (44, 86), (27, 100)),
        ((1, 2, 7), (3, 7, 20), (2, 20, 23), (3, 23, 26), (2, 26, 27), (3, 27, 35), (4, 35, 36), (5, 36, 44), (4, 44, 71), (5, 71, 72), (6, 72, 77), (5, 77, 78), (4, 78, 80), (3, 80, 86), (2, 86, 89), (1, 89, 100)),
    ),
    (
        ((32, 89), (112, 390), (163, 247), (50, 75), (107, 385), (62, 276), (82, 312), (18, 104), (136, 351), (72, 170), (151, 356), (104, 175), (65, 161), (215, 345), (60, 179), (182, 269), (101, 212), (159, 278), (73, 144), (216, 242)),
        ((1, 18, 32), (2, 32, 50), (3, 50, 60), (4, 60, 62), (5, 62, 65), (6, 65, 72), (7, 72, 73), (8, 73, 75), (7, 75, 82), (8, 82, 89), (7, 89, 101), (8, 101, 107), (9, 107, 112), (10, 112, 136), (11, 136, 144), (10, 144, 151), (11, 151, 159), (12, 159, 161), (11, 161, 163), (12, 163, 170), (11, 170, 175), (10, 175, 179), (9, 179, 182), (10, 182, 212), (9, 212, 215), (10, 215, 216), (11, 216, 242), (10, 242, 247), (9, 247, 269), (8, 269, 276), (7, 276, 278), (6, 278, 312), (5, 312, 345), (4, 345, 351), (3, 351, 356), (2, 356, 385), (1, 385, 390)),
    ),
    (
        ((273, 395), (127, 623), (102, 618), (141, 191), (458, 899), (379, 398), (16, 815), (738, 843), (297, 572), (87, 343), (206, 788), (213, 651), (679, 797), (222, 255), (62, 829), (109, 166), (366, 617), (128, 476), (122, 425), (339, 703), (107, 347), (213, 419), (259, 407), (150, 249), (127, 594), (587, 813), (85, 759), (242, 303), (174, 579), (125, 158)),
        ((1, 16, 62), (2, 62, 85), (3, 85, 87), (4, 87, 102), (5, 102, 107), (6, 107, 109), (7, 109, 122), (8, 122, 125), (9, 125, 127), (11, 127, 128), (12, 128, 141), (13, 141, 150), (14, 150, 158), (13, 158, 166), (12, 166, 174), (13, 174, 191), (12, 191, 206), (13, 206, 213), (15, 213, 222), (16, 222, 242), (17, 242, 249), (16, 249, 255), (15, 255, 259), (16, 259, 273), (17, 273, 297), (18, 297, 303), (17, 303, 339), (18, 339, 343), (17, 343, 347), (16, 347, 366), (17, 366, 379), (18, 379, 395), (17, 395, 398), (16, 398, 407), (15, 407, 419), (14, 419, 425), (13, 425, 458), (14, 458, 476), (13, 476, 572), (12, 572, 579), (11, 579, 587), (12, 587, 594), (11, 594, 617), (10, 617, 618), (9, 618, 623), (8, 623, 651), (7, 651, 679), (8, 679, 703), (7, 703, 738), (8, 738, 759), (7, 759, 788), (6, 788, 797), (5, 797, 813), (4, 813, 815), (3, 815, 829), (2, 829, 843), (1, 843, 899)),
    ),
    (
        ((214, 1957), (839, 1997), (465, 2371), (154, 1369), (950, 1804), (565, 1715), (1128, 1816), (58, 1421), (620, 1623), (948, 1606), (1034, 2105), (323, 2320), (1874, 2171), (335, 537), (969, 2083), (1072, 2355), (285, 1975), (127, 137), (257, 1122), (479, 2317), (1192, 1325), (106, 1858), (442, 649), (339, 2483), (587, 2469), (566, 1022), (1246, 1753), (708, 2197), (367, 1190), (110, 1899), (545, 1745), (1280, 1375), (1313, 2323), (703, 1248), (142, 1869), (265, 1247), (670, 1395), (362, 1942), (321, 2455), (548, 897), (553, 605), (880, 2305), (1519, 1800), (1536, 1852), (797, 2450), (496, 2491), (348, 1444), (1083, 1315), (396, 1071), (143, 1757)),
        ((1, 58, 106), (2, 106, 110), (3, 110, 127), (4, 127, 137), (3, 137, 142), (4, 142, 143), (5, 143, 154), (6, 154, 214), (7, 214, 257), (8, 257, 265), (9, 265, 285), (10, 285, 321), (11, 321, 323), (12, 323, 335), (13, 335, 339), (14, 339, 348), (15, 348, 362), (16, 362, 367), (17, 367, 396), (18, 396, 442), (19, 442, 465), (20, 465, 479), (21, 479, 496), (22, 496, 537), (21, 537, 545), (22, 545, 548), (23, 548, 553), (24, 553, 565), (25, 565, 566), (26, 566, 587), (27, 587, 605), (26, 605, 620), (27, 620, 649), (26, 649, 670), (27, 670, 703), (28, 703, 708), (29, 708, 797), (30, 797, 839), (31, 839, 880), (32, 880, 897), (31, 897, 948), (32, 948, 950), (33, 950, 969), (34, 969, 1022), (33, 1022, 1034), (34, 1034, 1071), (33, 1071, 1072), (34, 1072, 1083), (35, 1083, 1122), (34, 1122, 1128), (35, 1128, 1190), (34, 1190, 1192), (35, 1192, 1246), (36, 1246, 1247), (35, 1247, 1248), (34, 1248, 1280), (35, 1280, 1313), (36, 1313, 1315), (35, 1315, 1325), (34, 1325, 1369), (33, 1369, 1375), (32, 1375, 1395), (31, 1395, 1421), (30, 1421, 1444), (29, 1444, 1519), (30, 1519, 1536), (31, 1536, 1606), (30, 1606, 1623), (29, 1623, 1715), (28, 1715, 1745), (27, 1745, 1753), (26, 1753, 1757), (25, 1757, 1800), (24, 1800, 1804), (23, 1804, 1816), (22, 1816, 1852), (21, 1852, 1858), (20, 1858, 1869), (19, 1869, 1874), (20, 1874, 1899), (19, 1899, 1942), (18, 1942, 1957), (17, 1957, 1975), (16, 1975, 1997), (15, 1997, 2083), (14, 2083, 2105), (13, 2105, 2171), (12, 2171, 2197), (11, 2197, 2305), (10, 2305, 2317), (9, 2317, 2320), (8, 2320, 2323), (7, 2323, 2355), (6, 2355, 2371), (5, 2371, 2450), (4, 2450, 2455), (3, 2455, 2469), (2, 2469, 2483), (1, 2483, 2491)),
    ),
)

def check(test):
    R, staff_sol = test
    student_sol = satisfying_booking(R)
    n1 = len(staff_sol)
    n2 = len(student_sol)
    if n1 != n2: return False
    for i in range(n1):
        b1, b2 = staff_sol[i], student_sol[i]
        if len(b1) != 3 or len(b2) != 3:  
            return False
        for j in range(3):
            if b1[j] != b2[j]:  return False
    return True

class TestCases(unittest.TestCase):
    def test_01(self): self.assertTrue(check(tests[ 0]))
    def test_02(self): self.assertTrue(check(tests[ 1]))
    def test_03(self): self.assertTrue(check(tests[ 2]))
    def test_04(self): self.assertTrue(check(tests[ 3]))
    def test_05(self): self.assertTrue(check(tests[ 4]))

if __name__ == '__main__':
   res = unittest.main(verbosity = 3, exit = False)
