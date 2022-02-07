#  nested loops 
#  python allows loops to be nested in loops , Nested loops could be :


# for in for i      |  while in while 
# for var1 in seq1  | while condition(1) 
# for var2 in seq2  | while condition(2)
# statemnet(s)      | statemnet(s)          
# ---------------------------------------------------------------
# for in while         | while in for
# while condition(1)   | for var1 in seq1
# for var1 in seq1     | while condition
# statements(s)        | statements(s)
# -----------------------------------------------

x = [[ 1,2,3,4 ], ['a','b','c','c']]
for i in x:
    for j in i:
        print(j)
        
        # end ="" won't create a new line