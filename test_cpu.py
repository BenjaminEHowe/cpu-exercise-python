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
    
    def test_pow(self):
        self.assertEqual(cpu.calc('^ 2 5'), 32)

    def test_mod(self):
        self.assertEqual(cpu.calc('% 5 2'), 1)

if __name__ == '__main__':
    unittest.main()
