import csv

csvfile = open('cpc.csv', 'rb')
reader = csv.reader(csvfile)

#handle blank line
row = reader.next()








filenames = ['keywords-0k-to-2k','keywords-2k-to-4k',
'keywords-4k-to-6k','keywords-6k-to-8k','keywords-8k-to-10k',
'keywords-10k-to-12k','keywords-12k-to-14k','keywords-14k-to-16k',
'keywords-16k-to-18k','keywords-18k-to-20k']



for filename in filenames:
	file = open(filename, 'w')

	for i in range(0, 1999):
		row = reader.next()
		file.write(row[0] + "\n")

	row = reader.next()
	file.write(row[0])

	file.close()


