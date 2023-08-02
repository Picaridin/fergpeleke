'''
BaseSorter is the abstract interface for sorting algorithms, and will raise errors if called.
'''

class BaseSorter:
	'''
	BaseSorter provides an abstract interface for sorting algorithms.
	Functions are NOT implemented, and will log errors if called.
	'''

	def __init__(self, inputList):
	  '''
	  Abstract function representing a sort operation on a List of integers.
	  Duplicate entries are allowed in the input, and will be handled properly.
	  
	  Args:
	  	my_list: List[int] of integers, to be sorted in-place.
	  
	  Returns:
	  	None
	  	Li
	  '''
		self.inputList = inputList

  '''
  Abstract function representing a sort operation on a List of integers.
  Duplicate entries are allowed in the input, and will be handled properly.
  
  Args:
  	my_list: List[int] of integers, to be sorted in-place.
  
  Returns:
  	None
  	'''
	def sort(self, inputList):
		raise Exception("BaseSorter.sort() cannot be called directly!!!!!")


	'''
	Abstract function representing a validation of whether or not the given list
	is sorted. Empty lists are considered sorted, and ordering of duplicates is
	irrelevant. The input list will NOT be modified by this function.
	
	Args:
	  my_list: List[int] of integers, to be validated as sorted or not.
	
	Returns:
	  bool: True if my_list is sorted, False if my_list is not sorted.
	  No
	'''
	def isSorted(self, inputList):
		if self.inputList == sorted(self.inputList):
			return True
		return False