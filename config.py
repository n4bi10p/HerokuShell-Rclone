import os

w = open('config.json', 'w+')
w.write('{')
w.write('\n')
w.write('    "authToken": "'+os.getenv('1932305135:AAGi_e3nJVgOyQDTA-0ED5hXiMZ5TJX28_8')+'",')
w.write('\n')
w.write('    "owner": '+os.getenv('773182035'))
w.write('\n')
w.write('}')
