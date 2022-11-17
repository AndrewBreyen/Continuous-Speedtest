# Python program to test internet speed

import speedtest


st = speedtest.Speedtest()

down = st.download()
print(str(round(down, 2)) + " bytes/sec")