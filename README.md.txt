# HPRNG Hardware-Entropic Pseudorandom Number Generator

<h2>Why?</h2>
In my initial journey, the idea was "simple": to find ways to "bypass" Python's time library to avoid generating random numbers based on system time. In other words, I aimed to prevent the use of randomness sources provided by the operating system, opting instead for the system time, which is easier to manipulate on a PC. Following this, I began analyzing os.urandom(). However, as I delved into the intricacies of computational randomness, I stumbled upon something called "HRNG" (Hardware Random Number Generator). When I realized it was already daytime, I was finishing assembling a ball of aluminum foil to capture electrical noise.


<h2>Operation</h2>

The program operates as a pseudo-random number generator that incorporates data from various external sources to add greater unpredictability. In an attempt to enhance unpredictability, I gathered information from sensors such as a Light Dependent Resistor (LDR), a microphone, and an electric noise receiver. These readings, combined with factors such as system time and process ID, form the basis of the generation process. I included electrical, luminous, and microphone noise, process ID, and the current timestamp using a Mersenne twister reconstruction (Credits in the code).

<h2>My beautiful sensors</h2>
![script](https://github.com/Gutierre0x80/HPRNG/img/Hardware.jpeg)
[Yes, I used a ball of aluminum foil as an electric noise receiver.]

<h2>Output</h2>
![script](https://github.com/Gutierre0x80/HPRNG/img/out.jpeg)

This project may have some errors; if you'd like to help me improve, feel free to reach out to me on Discord.
My discord: gutierre0x80
_______________________________________________________________________________________________________________
