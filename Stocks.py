#!/usr/bin/env python3

import sys

def parse():
	arglen = len(sys.argv)
	stock = ""
	if arglen == 1:
		print(input("Please enter a stock name: "))
	else:
		print("Stock = ",sys.argv[1])
		stock = sys.argv[1] 

parse()
