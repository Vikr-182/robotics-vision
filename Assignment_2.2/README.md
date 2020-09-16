# Assignment 2

## File Structure

```
- Assignment_2.1
    - tools
        - main.py
        - constants.py
        - imports.py
        - individual.py
        - utils.py
- Assignment_2.2
    - tools
        - grid.py
        - constants.py
        - imports.py
        - individual.py
        - utils.py
        - png
            - 00000.png
            - 00001.png
            ..
            - 00076.png
- data (created)
    - dataset (created)
        - 01
            - 00000.bin
            - 00001.bin
            ..
            - 00076.bin
        - 01.txt
```

## Setup for Data

You need to MANUALLY ADD THE DATASET FOLDER INSIDE THE FOLDER NAMED "DATA". This was done since GitHub didn't allow pushing of the files.

```
$: git clone https://github.com/Mobile-Robotics-IIITH-2020/assignment-2-12_panzer-blow
$: cd assignment-2-12_panzer-blow/data
$: cp -r /path-to-dataset-folder/dataset ./
```

## Assignment 2.1

To run this assignment, please run the following commands - 

```
$: git clone https://github.com/Mobile-Robotics-IIITH-2020/assignment-2-12_panzer-blow
$: cd assignment-2-12_panzer-blow/Assignment_2.1/tools
$: python3 main.py
```

## Assignment 2.2

### 1. For getting indivdiual scans
```
$: git clone https://github.com/Mobile-Robotics-IIITH-2020/assignment-2-12_panzer-blow
$: cd assignment-2-12_panzer-blow/Assignment_2.2/tools
$: python3 individual.py

```

### 2. For getting scans of 5,10 and 15.
```
$: git clone https://github.com/Mobile-Robotics-IIITH-2020/assignment-2-12_panzer-blow
$: cd assignment-2-12_panzer-blow/Assignment_2.2/tools
$: python3 grid.py
```

