import inflect

p = inflect.engine()

# Convert numbers to word form
print(p.number_to_words(4))   # Output: 'four'
print(p.number_to_words(123)) # Output: 'one hundred and twenty-three'

