# Python program to test internet speed continuously, every 30 minutes, and write results to a CSV file

import speedtest
import csv
from os.path import exists
from datetime import datetime

results_file = "results.csv"

################################
# CHECK IF RESULTS FILE EXISTS #
################################
if exists(results_file):
	print (results_file + ' exists, skipping...')
else:
	print (results_file + ' does not exist, creating...')
	with open(results_file, 'w', newline='') as csvfile:
		csvwriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
		csvwriter.writerow(['DateTime', 'Down', 'DownPercentOfExpected', 'Up', 'UpPercentOfExpected'])
		csvfile.close

st = speedtest.Speedtest()

expected_down_mbps = 400
expected_up_mbps = 10

########
# DOWN #
########
print("Running Test DOWN......")
down = st.download(threads=4)
down_bps = round(down, 2)
down_mbps = down_bps/1000000
down_percent_of_expected = round((down_mbps/expected_down_mbps)*100,2)

print ("Down:")
print(str(down_bps) + " bytes/sec")
print(str(down_mbps) + " Mb/sec")
print(str(down_percent_of_expected)+"% of expected")


######
# UP #
######
print("Running Test UP......")
up = st.upload(threads=4)
up_bps = round(up, 2)
up_mbps = up_bps/1000000
up_percent_of_expected = round((up_mbps/expected_up_mbps)*100,2)

print ("Up:")
print(str(up_bps) + " bytes/sec")
print(str(up_mbps) + " Mb/sec")
print(str(up_percent_of_expected)+"% of expected")


#########################
# WRITE RESULTS TO FILE #
#########################
with open(results_file,"a",newline="") as csvfile:
    # creating writer object
    csv_writer=csv.writer(csvfile)
    # appending data
    csv_writer.writerow([datetime.now(), down_mbps, down_percent_of_expected, up_mbps, up_percent_of_expected]) 