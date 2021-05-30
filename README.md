# marks.py  
Marks calculator. Basing on previous marks it calculates what mark you need to get in remaining assessments in order to get desired end mark.  

It can be used to calculate:  
* module mark  
* year mark  
* whole degree mark  

# How to use it
Supply marks achieved for past assessments by modifying `previous_marks` list in the [marks.py](./marks.py), and then run it with python. See [Usage examples](usage-examples) section. To get numerical value at given point of the graph the user can put mouse cursor over specific point and observe bottom-right corner of the window (where x/y coordinates are displayed).  

# Prerequisites
Python 3.7 (or later) with the following libraries:  
* matplotlib  
* numpy  
* tkinter  

These libraries can be installed by executing the following command:  
`python3 -m pip install matplotlib numpy tk`  

# Usage examples
3 examples below show how to modify the `previous_marks` list/section of the [marks.py](./marks.py) code. All examples assume that the student achieved 70% from every past assessment.  

### Calculating module mark
In example below it is assumed that the student completed 2 assessments so far, each being worth 20% of the whole module. Remaining 60% could be an exam or several smaller percentage assessments, it does not really matter.  

```python
previous_marks = [
    # Format: (mark, weight)

    (70, 20), # e.g. first assignment/test
    (70, 20)  # e.g. second assignment/test
    ]
```

This example would result in the following output:  
![IMAGE DIDNT SHOW](./images/example_1.png)  

The graph tells that even if the student received 100% in all remaining assessments, his mark end/total mark would be ~87%, if in all remaining assessments he got 30%, his end/total mark would be ~46%.  

### Calculating year mark
In example below it is assumed that the student has 8 modules.  

```python
M_WEIGHT = 100 / 8   # weight of a single module
previous_marks = [
    # Format: (mark, weight)

    # finished modules marks
    (70, M_WEIGHT), # Whole finished module
    (70, M_WEIGHT), # Another finished module

    # unfinished modules marks
    (70, M_WEIGHT * 0.2), # Assessment worth 20% of some unfinished module
    (70, M_WEIGHT * 0.15) # Assessment worth 15% of some unfinished module
    ]
```

The graph tells that even if the student received 100% in all remaining assessments, his mark end/total mark would be ~91%, if in all remaining assessments he got 30%, his end/total mark would be ~41%.  

This example would result in the following output:  
![IMAGE DIDNT SHOW](./images/example_2.png)  


### Calculating whole degree mark
In example below it is assumed that second year of a degree was worth 40%, 3rd year was worth 60% and that there were 8 modules in the 3rd year. It is also assumed that the 1st year doesn't count towards the overall degree mark.  

```python
SECOND_YEAR_WEIGHT = 40
M_WEIGHT = 60 / 8           # single module weight (in 3rd year)

previous_marks = [
    # Format: (mark, weight)

    # 2nd year overall mark
    (70,   SECOND_YEAR_WEIGHT), 

    # total module marks
    (70,   M_WEIGHT),       # Some module final mark
    (70,   M_WEIGHT),       # Another module final mark
    (70,   M_WEIGHT),       # And another module final mark

    # module marks with some assessments unmarked yet
    (70,  M_WEIGHT * 0.06), # Assessment worth 6%  of some unfinished module
    (70,  M_WEIGHT * 0.12), # Assessment worth 12% of some unfinished module
    (70,  M_WEIGHT * 0.12), # Assessment worth 12% of some unfinished module
    (70,  M_WEIGHT * 0.1),  # Assessment worth 10% of some unfinished module
    (70,  M_WEIGHT * 0.2),  # Assessment worth 20% of some unfinished module
    ] 
```

This example would result in the following output:  
![IMAGE DIDNT SHOW](./images/example_3.png)  

The graph tells that even if the student received 100% in all remaining assessments, his mark end/total mark would be ~79%, if in all remaining assessments he got 30%, his end/total mark would be ~56%.  


