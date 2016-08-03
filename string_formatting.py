formatter = '%r %r %r %r'
formatter1 = '%s %s %s %s'
print formatter
print formatter %(1, 2, 3, 4)
print formatter %("one", "two", "Three", "Four")
print formatter %(True, False, False, True)
print formatter %(formatter, formatter, formatter, formatter)
print formatter %(
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)

print formatter1 %(
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)   
