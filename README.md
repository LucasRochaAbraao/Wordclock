# Wordclock
This repo contains a wordclock project, from design to code.

Currently the script works on a terminal, printing the time as natural language (in Pt-br). There are no dependencies, download `wordclock.py` and run it with python3. It works on mac, linux and windows. The other file, `wordclock_raspberrypi.py` is currently being developed to interact with an individually addressable LED strip, lighting up the LEDs that make up the words to display the current time.

The esp8266 project was put on hold, as the memory available on that board is really low, so for this prototype I'll stick with python and a raspberry pi. Once I get an MVP of this product I might try a different programming languange such as c++ or Rust to get the same result with a much lower memory footprint, lowering the cost of production by using the esp8266.