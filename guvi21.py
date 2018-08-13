def arithmetic_progression():
	input = raw_input().split()
	if not len(input) == 3:
		return arithmetic_progression()

	n = float(input[0])
	a = float(input[1])
	a = float(input[2])

	s = ( ( a * 2 ) + ( ( n - 1 ) * d ) ) * ( n / 2 )
	print( 'sum to n terms of given AP series: ' +str(s))

arithmetic_progression()
