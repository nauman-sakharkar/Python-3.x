def lcs(X, Y):
	m, n = len(X), len(Y)
	L = [[0 for x in range(n+1)] for x in range(m+1)]
	for i in range(m+1): 
		for j in range(n+1): 
			if i == 0 or j == 0: 
				L[i][j] = 0
			elif X[i-1] == Y[j-1]: 
				L[i][j] = L[i-1][j-1] + 1
			else: 
				L[i][j] = max(L[i-1][j], L[i][j-1])
	lcs = ""
	while m > 0 and n > 0:
		if X[m-1] == Y[n-1]:
			lcs = X[m-1] + lcs
			m -= 1 
			n -= 1
		elif L[m-1][n] > L[m][n-1]:
			m -= 1 
		else:
			n -= 1
	return lcs

X = "ABCDE"
Y = "ACDEB"
print("LCS of",X,"and",Y,":",lcs(X,Y))
