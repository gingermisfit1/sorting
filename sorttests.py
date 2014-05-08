import sorting
import unittest

class TestSequenceFunctions(unittest.TestCase):

    def test1(self):
        ''' given a list, swap element 1 for the next element'''
        inlist = [4,3,2,1]
        outlist = [4,2,3,1]
        assert (sorting.swap(inlist,1)==outlist) #test 1 fails, swap does not work as expected.

    def test2(self):
        '''Test 2 checks that the bubble sort can sort a list of 4 items reversed.
        '''
        inlist = [4,3,2,1]
        outlist = [1,2,3,4]
        assert (sorting.bsort(inlist)==outlist) #test 2 fails - list not sorted by bubble sort
        
    def test3(self):
        '''given a list, sort items into sorted and unsorted elements using current minimum'''
        inlist = [4,8,23,15,94,178]
        assert (sorting.ssort(inlist)==outlist) #test 3 fails - list not sorted by selection sort

if __name__ == '__main__':
    unittest.main()
