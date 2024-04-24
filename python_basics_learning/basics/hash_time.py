from timeit import timeit, Timer

print('---------  CREATE LIST vs ITERATOR  --------\n')

def comp():
	[ x for x in range(10_000_000) ]         #    must wait until list is fully instantiated, also requires huge memory

def gen():
	( x for x in range(10_000_000) )         #   'ready-in-an-instant' irrespective of data size, requires tiny memory (  just enough for one entry )

comp_time = timeit(comp, number=100) 
print(f'LIST          10M, time = {comp_time:.6f}')

gen_time = timeit(gen, number=100)
print(f'ITERATOR 10M, time =  {gen_time:.6f}')


print('\n---------  SEARCH COMPARISON  --------\n')

# linear search
lst1 = [ x for x in range(10_000_000)]  

code1 = """
for i in lst1:
	if i == 2000000:
            print('GOTTCHA', 2000000)
            break
"""

code2 = """
for i in lst1:
	if i == 8000000:
            print('GOTTCHA', 8000000)
            break
"""
 
# linear search
list_2m = timeit(code1, setup='from __main__ import lst1', number=1)
print(f'LINEAR SEARCH 2M, time = {list_2m:.6f}\n')

list_8m = timeit(code2, setup='from __main__ import lst1', number=1) 
print(f'LINEAR SEARCH 8M, time = {list_8m:.6f}\n')


# hash search
d1 = { key : 1 for key in range(10_000_000)}

dict_2m = timeit('print(d1[2000000])', setup='from __main__ import d1', number=1)
print(f'HASH SEARCH 2M, {dict_2m:.6f}\n')

dict_8m = timeit('print(d1[8000000])', setup='from __main__ import d1', number=1)
print(f'HASH SEARCH 8M, {dict_8m:.6f}')


