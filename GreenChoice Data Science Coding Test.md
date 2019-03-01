## Question 1

I wrote a function called SearchName to initiate the searching process regarding the input parent name.

```
# Build Graph
name = {
    'A' : ['B','I'],
    'B' : ['C', 'D'],
    'C' : [],
    'D' : ['G', 'E'],
    'E' : ['F'],
    'F' : ['I'],
    'I' : ['H'],
    'H' : ['G'],
    'G' : []
    }

# Define the searching function
def SearchName(name, parent, child):
    if parent not in child:
        child.append(parent)
        for n in name[parent]:
            SearchName(name, n, child)
    return child

# Call the function
parent = input("Pleas input the parent name: ")    
visited = SearchName(name,parent, [])
print(visited)
```
## Question 2




