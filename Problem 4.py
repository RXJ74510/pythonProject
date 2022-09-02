it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print("length of the set it_companies ", len(it_companies))
it_companies.add('Twitter')
it_companies.update(['Sony', 'Samsung'])
print(it_companies)

print("removing Sony from it_companies")
it_companies.remove('Sony')
print('After removing sony: ', it_companies)

print('Both remove and discard will remove an element from the set.\
        Discard will not throw any error if the element  to be removed is not present in the set,\
        but remove() will throw an error')

a_and_b = A.union(B)
print(a_and_b)

a_intersect_b = A.intersection(B)

is_subset = A.issubset(B)
print('is A subset of B: ', is_subset)

is_disjoint = A.isdisjoint(B)
print('is A disjoint of B: ', is_disjoint)

join_a_with_b = A.union(B)
join_b_with_a = B.union(A)

sym_diff = A.symmetric_difference(B)
print('Symmetric difference between A and B is: ', sym_diff)

del A
del B
print('Deleted sets A and B')

ages_set = set(age)
print('ages list length: {0}, ages set length: {1}'.format(len(age), len(ages_set)))