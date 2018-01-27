# Imported modules
import parse as p


f = input("Please input a file. > ")
cell = int(
    input(
    "Which column contains the data you would like counted? e.g.[1,2,3...] > ")
    ) - 1

parsed = p.parse_csv(f)
data = p.pull(parsed, cell)
print(p.items(data))
