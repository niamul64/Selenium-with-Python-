import unittest
import main


class MainTest(unittest.TestCase):

    def test1_send_data(self):
        found1 = main.send_data(self)
        given_name = 'MK Saadi'
        self.assertEqual(found1[0], given_name)

    def test2_send_data(self):
        found2 = main.send_data(self)
        given_mail = "mksaadi@gmail.com"
        self.assertEqual(found2[1], given_mail)

    def test3_send_data(self):
        given_current_add = "Farmgate"
        found3 = main.send_data(self)
        self.assertEqual(found3[2], given_current_add)

    def test4_send_data(self):
        given_perm_add = "Lalmatia"
        found4 = main.send_data(self)
        self.assertEqual(found4[3], given_perm_add)


if __name__ == '__main__':
    unittest.main()
