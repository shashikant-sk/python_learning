# Check whether a given key already exists in a dictionary

 #original 
d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
def is_key_present(x):
  if x in d:
      print('Key is present in the dictionary')
  else:
      print('Key is not present in the dictionary')
is_key_present(5)
is_key_present(9)

# ----------------------------------------
 
#  modfied
def key_in_dict(d, key):
  return (key in d) 
students = {
  'Theodore': 19,
  'Roxanne': 22,
  'Mathew': 21,
  'Betty': 20
}
print("\nOriginal dictionary elements:")
print(students)
print(key_in_dict(students, 'Roxanne'))
print(key_in_dict(students, 'Gina'))
