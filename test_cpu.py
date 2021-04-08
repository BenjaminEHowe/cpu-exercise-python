import unittest
import cpu

class TestCPU(unittest.TestCase):
    def test_execute(self):
        cpu.execute()
        self.assertEqual(cpu.accumulator, 756216.3057730488)

if __name__ == '__main__':
    unittest.main()
