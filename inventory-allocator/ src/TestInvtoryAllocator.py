from InventoryAllocator import InventoryAllocator as ia
import unittest


class TestSum(unittest.TestCase):
    # test case 0: input emply order or empty warehouses
    def test_0(self):
        # 0.0 empty order
        test0_0 = {'order': {},
                   'warehouses':  [{'name': 'owd', 'inventory': {'apple': 5}},
                                   {'name': 'dm', 'inventory': {'apple': 5, 'banana': 1}}],
                   'expected': []
                   }
        # 0.1 empty warehouses
        test0_1 = {'order': {'apple': 5, 'banana': 1},
                   'warehouses':  [],
                   'expected': []
                   }
        # 0.2 empty order and empty warehouses
        test0_2 = {'order': {},
                   'warehouses':  [],
                   'expected': []
                   }
        self.assertEqual(ia().inventory_allocator(test0_0['order'], test0_0['warehouses']),
                         test0_0['expected'], 'Test Failed in Case 0_0')
        self.assertEqual(ia().inventory_allocator(test0_1['order'], test0_1['warehouses']),
                         test0_1['expected'], 'Test Failed in Case 0_1')
        self.assertEqual(ia().inventory_allocator(test0_2['order'], test0_2['warehouses']),
                         test0_2['expected'], 'Test Failed in Case 0_2')

    # test case 1: orders can be supplied by only one waerehouse
    def test_1(self):
        # case 1_0: perfectly match!
        test1_0 = {'order': {'apple': 5, 'banana': 1},
                 'warehouses':  [{'name': 'owd', 'inventory': {'apple': 5, 'banana': 1}}],
                 'expected': [{'owd': {'apple': 5, 'banana': 1}}]
                 }
        
        # case 1_1: objects do not perfectly match, and some warehouses are not used.
        test1_1 = {'order': {'apple': 5, 'banana': 1},
                 'warehouses':  [{'name': 'owd', 'inventory': {'apple': 6, 'banana': 2}},
                                 {'name': 'dm', 'inventory': {'apple': 5, 'banana': 1}}],
                 'expected': [{'owd': {'apple': 5, 'banana': 1}}]
                 }

        self.assertEqual(ia().inventory_allocator(test1_0['order'], test1_0['warehouses']),
                         test1_0['expected'], 'Test Failed in Case 1_0')         
        self.assertEqual(ia().inventory_allocator(test1_1['order'], test1_1['warehouses']),
                         test1_1['expected'], 'Test Failed in Case 1_1')


    # test case 2: there are objects that need to be splitted to deliver from multiple warehouses
    def test_2(self):
        test2 = {'order': {'apple': 10, 'banana': 5, 'orange': 3},
                 'warehouses':  [{'name': 'owd', 'inventory': {'apple': 6, 'banana': 2}},
                                 {'name': 'dm', 'inventory': {'apple': 5, 'banana': 3}},
                                 {'name': 'fer', 'inventory': {'banana': 10, 'orange': 10}}],
                 'expected': [{'owd': {'apple': 6, 'banana': 2}}, {'dm': {'apple': 4, 'banana': 3}},
                              {'fer': {'orange': 3}}]
                 }

        self.assertEqual(ia().inventory_allocator(test2['order'], test2['warehouses']),
                         test2['expected'], 'Test Failed in Case 2')
        

    # test case 3: there are objects that cann't be supplied by all the inventories combined from all the warehouses
    def test_3(self):
        test3 = {'order': {'apple': 100, 'banana': 5, 'orange': 3},
                 'warehouses':  [{'name': 'owd', 'inventory': {'apple': 6, 'banana': 2}},
                                 {'name': 'dm', 'inventory': {'apple': 5, 'banana': 3}},
                                 {'name': 'fer', 'inventory': {'banana': 10, 'orange': 10}}],
                 'expected': []
                 }
        self.assertEqual(ia().inventory_allocator(test3['order'], test3['warehouses']),
                         test3['expected'], 'Test Failed in Case 2')


if __name__ == '__main__':
    unittest.main()
