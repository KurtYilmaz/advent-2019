import unittest, filecmp

from day2 import perform_operation


class PerformOperationTest(unittest.TestCase):
    def test_unsupported_opcode(self):
        self.assertEqual(perform_operation("0", "99", "12"), None)

    def test_addition_1_1(self):
        self.assertEqual(perform_operation("1", "1", "1"), 2)

    def test_addition_90_4(self):
        self.assertEqual(perform_operation("1", "90", "4"), 94)

    def test_multiplication_2_4(self):
        self.assertEqual(perform_operation("2", "2", "4"), 8)

    def test_multiplication_7_6(self):
        self.assertEqual(perform_operation("2", "7", "6"), 42)


from day2 import run_file


class RunFileTest(unittest.TestCase):
    def test_file_empty(self):
        run_file("test_files/test_empty_in.txt", "test_files/test_empty_out.txt")
        self.assertTrue(
            filecmp.cmp(
                "test_files/test_empty_out.txt", "test_files/test_empty_expected.txt"
            )
        )

    def test_file_1(self):
        run_file("test_files/test1_in.txt", "test_files/test1_out.txt")
        self.assertTrue(
            filecmp.cmp("test_files/test1_out.txt", "test_files/test1_expected.txt")
        )

    def test_file_2(self):
        run_file("test_files/test2_in.txt", "test_files/test2_out.txt")
        self.assertTrue(
            filecmp.cmp("test_files/test2_out.txt", "test_files/test2_expected.txt")
        )

    def test_file_3(self):
        run_file("test_files/test3_in.txt", "test_files/test3_out.txt")
        self.assertTrue(
            filecmp.cmp("test_files/test3_out.txt", "test_files/test3_expected.txt")
        )



if __name__ == "__main__":
    unittest.main()
