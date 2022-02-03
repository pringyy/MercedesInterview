# User Manual

This file gives instructions on how to run both the main program and the supporting test suite. If you have any issues while running this program please contact me on my email: pringle@live.co.uk

## How to Run Main Program

**Step 1**: You need to have Python 3.9+ installed onto your machine to ensure this application runs as intended (untested with older versions). Download the version and follow the installation guide for the Operating System you are using here: 
*  https://www.python.org/downloads/release/python-390/
  
**Step 2**: Once you have completed the setup above, navigate to the 'MercedesInterview/src' folder on your terminal or Python IDLE.

**Step 3**: To run the program you will need to run the following command:
```
python main.py
```
 You will then be prompted with the following:
```
Enter the name of the file which stores the channel X in src/inputs: 
```

**Step 4**: Enter 'channels.txt' in order to import the original file provided as this is stored in src/inputs:
```
Enter the name of the file which stores the channel X in src/inputs: channels.txt
```
You will then be prompted with the following:
```
Enter the name of the file which stores paramaters m and c in src/inputs:
```

**Step 5**: Enter 'parameters.txt' in order to import the original parameters file provided as this is also stored in src/inputs:
```
Enter the name of the file which stores paramaters m and c in src/inputs: parameters.txt
```

**Step 6**: Done! The output should be generated and exported to the src/outputs folder

**NOTE**: You can run any input for the parameters or X channel as long as they are in the same exact same format as the original files and are present in src/inputs. If the file names are different you would just change what file you type during step 4 and step 5.

## How to Run Test Suite
**Step 1**: Once Python is installed and you have navigated to 'MercedesInterview/src' in your console, run the following command to run the test suite:
```
python test.py
```





