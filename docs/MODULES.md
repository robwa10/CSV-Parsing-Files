# Functions  

[README.md](../README.md) contains overview documentation.  
__MODULES.md__ contains documentation for all modules.  
[EXAMPLE-FILES.md](/docs/EXAMPLE-FILES.md) contains documentation for files demonstrating module functionality.

## Table of Contents  
[Maths](https://github.com/robwa10/Parse-and-Analyze/blob/master/docs/MODULES.md#maths)  
* [compound_interest](https://github.com/robwa10/Parse-and-Analyze/blob/master/docs/MODULES.md#compound_interestinvestment-rate-time)
* [items](https://github.com/robwa10/Parse-and-Analyze/blob/master/docs/MODULES.md#itemsa_list-n1000)

[Parsing](https://github.com/robwa10/Parse-and-Analyze/blob/master/docs/MODULES.md#parsing)  
* [parse_csv](https://github.com/robwa10/Parse-and-Analyze/blob/master/docs/MODULES.md#parse_csva_file-sn-d)  
* [pull](https://github.com/robwa10/Parse-and-Analyze/blob/master/docs/MODULES.md#pulla_list-n)

[Validation](https://github.com/robwa10/Parse-and-Analyze/blob/master/docs/MODULES.md#validation)  
* [validate_choice](https://github.com/robwa10/Parse-and-Analyze/blob/master/docs/MODULES.md#validate_choicechoices)


## Maths  

### `compound_interest(investment, rate, time)`  

#### Arguments
- param1 *(int)* investment: The amount of original investment.
- param2 *(int)* rate: Interest rate in whole number. i.e. 2% = 2.
- param3 *(int)* time: Length of investment. Used to exponentially raise total. Assumes interest is applied for every whole integer in param.  

#### Returns  
- Integer: Does not round or format the returned value.  

#### Example  
```
>>>print(compound_interest(10, 3, 5))
11.592740743000002
```

### `items(a_list, n=1000)`  
Counts the instances of each item in a list using `Counter`.  

#### Arguments  
- a_list *(list)*: The list to count.  
- dict=False [optional] *(boolean)*: Boolean to return list (default) or dictionary. Must be passed if an integer is passed as third param.  
- n=1000 [optional] *(int)*: Integer to limit data returned. Default is 1000.  


#### Returns  
- *(List)* [default]: Returns a list. Each item in the list is `[occurrence total: 'value']`.
- *(Dictionary)* [optional]: Returns a dictionary. Key, value pairs are `{occurrence total: 'value'}`.

#### Example  
```
data = [a, v, a, f, d, b, d, f, d, b, d, a, f, a, a]
results = items(data)
limit_results = items(data, 3)
dict_limit_results = items(data, True, 3)

print(results)
print(limit_results)
print(dict_limit_results)
// ["5: 'a'","4: 'd'", "3: 'f'", "2: 'b'",  "1: 'v'"]
// ["5: 'a'","4: 'd'", "3: 'f'"]
// {5: 'a', 4: 'd', 3: 'f'}
```

## Parsing

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

### `pull(a_list, column)`  
Pass in data from `parsed_csv()` and a column index. Creates a list with data from index. Catches empty columns.

#### Arguments  
- a_list *(list)*: A list of lists.
- column *(int)*: index of a column in CSV.

#### Returns  
- *(List)*: Returns a list.  

#### Example  
```
parsed_data = parse_csv('data.csv')  
email = pull(parsed_data, 2)

print(email)
// [jsmith@email.com, jane@email.com]
```
## Validation

### `validate_choice(choices=[])`  
Presents the user with a selection of choices and validates their input. Defaults to Yes or No selection if called with no argument.

#### Arguments
- choices [optional] *(list)*: List of choices for user to select from. Defaults to Yes/No if called with no param.

#### Returns
- *(string)*: Returns validated input as a lowercase string.  

#### Example
```
my_choices = ['Bob', 'Susie', '3', '4']
print(validate_choice(my_choices))

// Please choose one.
// Bob
// Susie
// 3
// 4
// > Bob
// bob
```  
