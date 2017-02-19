from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import sys


def main():
	try:
		#get string score
		fuzz.ratio("ACME Factory", "ACME Factory Inc.")

		fuzz.partial_ratio("ACME Factory", "ACME Factory Inc.")
		fuzz.ratio('Barack Obama', 'Barack H. Obama')# 89
		fuzz.partial_ratio('Barack Obama', 'Barack H. Obama')# 75
		fuzz.ratio('Barack H Obama', 'Barack H. Obama')# 97
		fuzz.partial_ratio('Barack H Obama', 'Barack H. Obama')# 92
		fuzz.ratio('Donald J Trump', 'Donald J. Trump')# 97
		print(fuzz.partial_ratio('Donald J Trump', 'Donald J. Trump'))# 92		

		query = 'Barack Obama'
		choices = ['Barack H Obama', 'Barack H. Obama', 'B. Obama']
		# Get a list of matches ordered by score, default limit to 5
		process.extract(query, choices)
		# [('Barack H Obama', 95), ('Barack H. Obama', 95), ('B. Obama', 85)]
		 
		# If we want only the top one
		print(process.extractOne(query, choices)) # ('Barack H Obama', 95)
	except:
		e = sys_exc.info()
		print(e)
		sys.exit(1)

if __name__ == "__main__":
	main()