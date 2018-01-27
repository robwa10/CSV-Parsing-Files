# Functions  

[README.md](../README.md) contains overview documentation.  
__MODULES.md__ contains documentation for all modules.  
[EXAMPLE-FILES.md](/docs/EXAMPLE-FILES.md) contains documentation for files demonstrating module functionality.

## *Parsing*

### `parse_csv(a_file, s='\n', d=',')`  
Creates a list from data within each row of a CSV file and appends that list to a list.

#### Arguments
- a_file *(file)*: The CSV to be parsed.
- s [optional] *(string)* : The character that splits rows.
- d [optional] *(string)*: The character that splits data within each row.

#### Returns
- *(List of lists)*: Returns a list of lists.  

#### Example
```
parsed_data = parse_csv('data.csv')

print(parsed_data)
// [[John, Smith, jsmith@email.com], [Jane, Doe, jane@email.com]]
```  
___  

### `pull(a_list, n)`  
Pass in data from `parsed_csv()` and a column index. Creates a list with data from index. Catches empty columns.

#### Arguments  
- a_list *(list)*: A list of lists.
- n *(int)*: index of column in CSV.

#### Returns  
- *(List)*: Returns a list.  

#### Example  
```
parsed_data = parse_csv('data.csv')  
email = pull(parsed_data, 2)

print(email)
// [jsmith@email.com, jane@email.com]
```

## *Counting*  

### `items(a_list, n=1000)`  
Counts the instances of each item in a list using `Counter`.  

#### Arguments  
- a_list *(list)*: The list to count.
- n=1000 [optional] *(int)*: Integer to limit data returned. Default is 1000.
- x=False [optional] *(boolean)*: Boolean to return list or dictionary. List is default.

#### Returns  
- *(List)* [default]: Returns a list. Each item in the list is `[occurrence total: 'value']`.
- *(Dictionary)* [optional]: Returns a dictionary. Key, value pairs are `{occurrence total: 'value'}`.

#### Example  
```
data = [a, v, a, f, d, b, d, f, d, b, d, a, f, a, a]
results = items(data)
limit_results = items(data, 3)
limit_results = items(data, 3, True)

print(results)
print(limit_results)
// ["5: 'a'","4: 'd'", "3: 'f'", "2: 'b'",  "1: 'v'"]
// ["5: 'a'","4: 'd'", "3: 'f'"]
// {5: 'a', 4: 'd', 3: 'f'}
```
