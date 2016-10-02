def map(arr, function):
  _map(0, arr, function)

def _map(index, array, function):
  if index == len(array):
    return
  array[index] = function(array[index])
  _map(index+1, array, function)