import streamlit as st
import speedtest as sp

st.balloons()
st.title("Internet test website")

def speed_test():
    test = sp.Speedtest()

    down_speed = test.download()
    down_speed = round(down_speed / 10**6, 2)
    st.write(f"Download speed is {down_speed} Mbps")

    up_speed = test.upload()
    up_speed = round(up_speed / 10**6, 2)
    st.write(f"Upload speed is {up_speed} Mbps")

    ping = test.results.ping
    st.write(f"Ping is {ping} ms")

if st.button("Run speed test"):
    speed_test()

