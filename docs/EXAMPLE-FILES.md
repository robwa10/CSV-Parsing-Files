# Example Files  
All example files begin with ex.  
For example *ex_occurrence.py*

[README.md](../README.md) contains overview documentation.  
[MODULES.md](/docs/MODULES.md) contains documentation for all modules.  
EXAMPLE-FILES.md contains documentation for files demonstrating module functionality.

### ex_occurrence.py  
##### File input types  
CSV  
##### Functionality  
Reads and parses CSV.  
Counts the occurrences of all data in a specified column.
##### Output  
Prints the results in the terminal.

#### Modules Used  
parse_csv.py  
pull.py  
items.py

#### Usage
```
> python3 ex_occurence.py
> Please input a file. > ./sample_data/csv_files/one.csv
> Which column contains the data you would like counted? e.g.[1,2,3...] > 1

// ["5304: '5.7.1'", "2799: '550'", "1326: '4.2.2'", "199: '5.1.1'", "125: '4.1.0'", "125: '552'", "122: '5.2.1'", "1: 'status'"]
```
