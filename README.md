# HPRNG Hardware-Entropic Pseudorandom Number Generator

<h2>Why?</h2>
In my initial journey, the idea was "simple": to find ways to "force" Python's time library not to use the randomness sources provided by the operating system (I wanted the random_seed_urandom() function to fail). Thus, the library would use the random_seed_time_pid() function, which utilizes the current time and the PID. In other words, I sought to avoid using randomness sources provided by the operating system, as if the library used the system time, it would be easier to manipulate. With this, I could finally make all pseudorandom numbers "coincidentally" be the same without setting a seed. After that, I began to analyze os.urandom(). However, as I delved into the complexities of computational randomness, I came across something called "HRNG" (Hardware Random Number Generator). When I realized it was already daytime, I was finishing assembling a ball of aluminum foil to capture electrical noise.


<h2>Operation</h2>


The program operates as a pseudo-random number generator that incorporates data from some external sources to try to increase unpredictability. I collected information from sensors such as a Light Dependent Resistor (LDR), a microphone, and an electric noise receiver. These readings, combined with factors like system time and process ID, form the foundation of the generation process. I included electrical, luminous, and microphone noises, the process ID, and the current date/time stamp using a reconstruction of the Mersenne twister (Credits in the code).


<h2>My beautiful sensors</h2>
<img src="https://github.com/Gutierre0x80/HPRNG/raw/main/img/Hardware.jpeg" width="345">

[Yes, I used a ball of aluminum foil as an electric noise receiver.]

<h2>Output</h2>
<img src="https://github.com/Gutierre0x80/HPRNG/raw/main/img/out.jpg" width="345">


This project may have some errors; if you'd like to help me improve, feel free to reach out to me on Discord.

Edit: I wasn't able to finish this project. For various reasons, perhaps I didn't find it sufficiently relevant. But if you want to use my project for something useful, I would suggest collecting multiple samples of noise and using XOR to mix the bits, or something similar, it doesn't matter. I would also consider implementing Avalanche Noise using a Zener diode and some sources of jitter, like crystal oscillators.

My discord: gutierre0x80
_______________________________________________________________________________________________________________
