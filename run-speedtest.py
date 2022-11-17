# Python program to test internet speed

import speedtest


st = speedtest.Speedtest()

expected_down = 400
expected_up = 10

print("Running Test......")
down = st.download()
up = st.upload()

print ("Down")
print(str(round(down, 2)) + " byte/sec")
print(str(round(down/1000000, 2)) + " Mb/sec")

print ('--------')
print ("Up")
print(str(round(up, 2)) + " byte/sec")
print(str(round(up/1000000, 2)) + " Mb/sec")