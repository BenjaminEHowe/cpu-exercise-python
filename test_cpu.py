import unittest
import cpu

class TestCPU(unittest.TestCase):
    def test_execute(self):
        try:
            cpu.execute()
        except SystemExit:
            pass
        self.assertEqual(cpu.pc, 4478)
        self.assertEqual(cpu.getStatement(cpu.pc), 'goto 7760')

if __name__ == '__main__':
    unittest.main()
