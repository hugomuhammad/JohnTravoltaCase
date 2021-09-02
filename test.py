#Muhammad Hugo Athallah Hardy
#11190910000035

import unittest
import JohnTravolta

class Testcode(unittest.TestCase):

    def test_calc1(self):
        self.assertEqual(JohnTravolta.bisa_tabung(52,600000),'Bisa menabung sebanyak: 270000.0')
    
    def test_calc2(self):
        self.assertEqual(JohnTravolta.bisa_tabung(40,200000),'Bisa menabung sebanyak: 400000')
    
    def test_calc3(self):
        self.assertEqual(JohnTravolta.bisa_tabung(32,300000),'Bisa menabung sebanyak: 180000')
    
    def test_calc4(self):
        self.assertEqual(JohnTravolta.bisa_tabung(16,280000),'cari tambahan')
    
    def test_calc5(self):
        self.assertEqual(JohnTravolta.bisa_tabung(0,0),'tidak bisa menabung')

if __name__ == '__main__':
    unittest.main()