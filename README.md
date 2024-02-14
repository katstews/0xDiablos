# 0xDiablos
I remember coming across the challenge a month ago and instantly giving up because I had zero clue what any write ups meant. I had all the solutions right in front of me and yet I still could not understand it. I've done one buffer overflow (BFO) challenge, and that was it. The challenge compared to this was much much easier. This challenge was a two step process. 

## First challenge
First thing you want to do is run the program, and I did. But uh oh, I own a m1, so booooooo can't run it. I also dont want to deal with installing an emulator, so i'll take a different route for this challenge. <br> 

First thing, we boot up gdb to just take a quick look at what were looking at. We want to know what were working with. CANARY is disabled, good, the program isn't made to detect BFO. NX is disabled, meaning you **can** execute or insert some shellcode into your BFO. PIE is disabled, great, address are **NOT** randomized meaning we can target specific functions. RELRO is partial, meaning an attacker has the potential to exploit delayed resolution process (during full RELRO memory addresses of functions are resolved during program startup and are made READ ONLY). Thing we need to know is "Are the addresses static" and "Can we perform anything"? Yes and yes. Sweet, lets start decompiling.  
<img width="369" alt="Screenshot 2023-11-22 at 1 36 53 PM" src="https://github.com/katstews/0xDiablos/assets/112781868/755e6c97-97f1-42f7-a029-a0e0f4665a58">
<br>
Ok lets start anaylzing the code. I booted up Cutter and BAM we see a Vuln() function. Now huge quick refresher, the stack "grows" to lower memory. So any new values added will be essentially (EBP - X). Right so your EBP and RET will all be in the higher range of addresses. As so: <br>
![image](https://github.com/katstews/0xDiablos/assets/112781868/3c8c41be-69b2-48b8-a2a5-4dbee14bfc0c)

![image](https://github.com/katstews/0xDiablos/assets/112781868/7476a6bd-67f7-439d-a3e6-302b263011f2)
