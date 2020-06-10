def greedy_cover(universal,subsets):
	elements_set = set([el for subset in subsets for el in subset])
	if elements_set!=universal:
		return lsit()
	cover_set = set()
	covered_set = []
	while cover_set!=universal:
		max_subset = max(subsets, key=lambda s: len(s-cover_set))
		cover_set = cover_set | max_subset
		covered_set.append(max_subset)
	return covered_set

universal = set(range(1, 11))
subsets = [set([1, 2, 3, 8, 9, 10]),
    set([1, 2, 3, 4, 5]),
    set([4, 5, 7]),
    set([5, 6, 7]),
    set([6, 7, 8, 9, 10])]
print("Universal set:",universal)
print("Subsets:",subsets)
print("Cover set:",greedy_cover(universal,subsets))
