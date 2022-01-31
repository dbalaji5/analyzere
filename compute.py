import sys

class AnalyzeReProblem:

	def __init__(self, threshold, limit):
		self.threshold = threshold
		self.limit = limit
		#flag to verify if the limit has been reached yet.
		self.limitCrossed = False

	def computeRangeAdditions(self):

		"""
		computeRangeAdditions calculates the output from the input
		line of numbers based on threshold and limit.
		"""
		
		computeSum = float(0)

		# iterator to process the input lines.
		for line in sys.stdin:

			line = float(line)

			if self.limitCrossed:  
				print(0.0)
				continue

			#condition to verify if the value is less than threshold.
			if line <= threshold or line == 0.0: 
				print(0.0)
				continue

			# excess value after threshold is set as current value
			val = line - threshold

			tempSum = computeSum + val

			#condition to validate if limit has been reached with cumulative sum or current value.

			overLimit = ((tempSum > limit) or (line > limit)) 

			if overLimit:
				# if the limit is crossed, the current value is set as the remainder of cumulative sum and limit.
				val = limit - computeSum
				self.limitCrossed = True
			
			print(val)

			computeSum += val

		#last output to display the cumulative sum

		print(computeSum)

#first command line argument for threshold value

threshold = float(sys.argv[1])

#second command line argument for limit value

limit = float(sys.argv[2])

analyzeRe = AnalyzeReProblem(threshold, limit)

analyzeRe.computeRangeAdditions()