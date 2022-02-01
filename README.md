# Mercedes AMG Petronas F1 Team Technical Interview Solution

This is my solution for the Mercedes AMG Petronas F1 team technical interview which was implemented using Python. This README provides a breif file structure out line and then a report of my , including any assumptions I made and my findings. **A [user manual (MANUAL.md)](manual.md) is also provided which describes how to run the system and unit tests.**

## File Structure
* [USERMANUAL.md](USERMANUAL.md) - describes how to run the system and unit tests
* **[src/](src) - contains all the code for the project**
* [src/main.py](src/main.py) - the program which implements the task
* [src/test.py](src/test.py) - test cases which test the function within main.py
* [src/inputs](src/inputs) - contains all the input file which are read into main.py
* [src/outputs](src/output) - stores the output of the main.py program

## Report

I chose Python to write this program.

In the functions when peforming calculations on the arrays I decided to use iteration (for loops) t

Assumptions:
- I assumed the channels.txt and parameters.txt could not be changed and therefore I imported them into the program using string manipulation in order to extract the required data. 
- I assumed that the format of channels.txt and parameters.txt was the same format the output file had to be.
- I assumed as the data provided in channels.txt was rounded to 15 decimel places I also made all the other channels and metrics calculated to be rounded to 15 decimel places
