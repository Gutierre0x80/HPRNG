import time
import os
import serial

(w, n, m, r) = (32, 624, 397, 31)
a = 0x9908B0DF
(u, d) = (11, 0xFFFFFFFF)
(s, b) = (7, 0x9D2C5680)
(t, c) = (15, 0xEFC60000)
l = 18
f = 1812433253

MT = [0 for _ in range(n)]
index = n + 1
lower_mask = 0x7FFFFFFF
upper_mask = 0x80000000

def mt_seed(seed):
    global index
    index = n
    MT[0] = seed
    for i in range(1, n):
        temp = f * (MT[i-1] ^ (MT[i-1] >> (w-2))) + i
        MT[i] = temp & 0xFFFFFFFF

def extract_number(serial_port):
    global index
    if index >= n:
        twist()
        index = 0

    noise_value = int(read_serial_data(serial_port))
    ldr_value = int(read_serial_data(serial_port))
    mic_value = int(read_serial_data(serial_port))
    current_millis = current_time_millis()
    pid = get_pid()

    y = MT[index] ^ ldr_value ^ mic_value ^ noise_value ^ current_millis ^ pid
    y = y ^ ((y >> u) & d)
    y = y ^ ((y << s) & b)
    y = y ^ ((y << t) & c)
    y = y ^ (y >> l)

    index += 1
    return y & 0xFFFFFFFF, ldr_value, mic_value, noise_value, pid, current_millis

def twist():
    for i in range(n):
        x = (MT[i] & upper_mask) + (MT[(i + 1) % n] & lower_mask)
        xA = x >> 1
        if x % 2 != 0:
            xA = xA ^ a
        MT[i] = MT[(i + m) % n] ^ xA

def current_time_millis():
    return round(time.time() * 1000)

def get_pid():
    return os.getpid()

def read_serial_data(serial_port):
    try:
        data = serial_port.readline().decode('latin-1').strip()
        return int(data)
    except ValueError:
        print("Error converting data to integer. Default value used.")
        return 0

def main():
    serial_port = serial.Serial('COM5', 9600, timeout=1)
    time.sleep(2)

    while True:
        random_number, ldr_value, mic_value, noise_value, pid, current_millis = extract_number(serial_port)
        print(f"Random: {random_number} | LDR: {ldr_value} | Mic: {mic_value} | Noise: {noise_value} | PID: {pid} | Time: {current_millis}")
        time.sleep(1)

if __name__ == '__main__':
    main()


# Credits for Mersenne Twister rebuild: https://github.com/yinengy/Mersenne-Twister-in-Python