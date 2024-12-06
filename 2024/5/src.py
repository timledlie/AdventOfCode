from functools import cmp_to_key

with open("input.txt") as file:
    lines = file.read()

orderings_text, pages_text = lines.split("\n\n")

ordering_rules = set()
for ordering_text in orderings_text.split():
    a, b = ordering_text.split('|')
    ordering_rules.add((int(a), int(b)))

pages_to_produce = []
for page_text in pages_text.split():
    pages_to_produce.append([int(page) for page in page_text.split(',')])


# the ordering rules define a custom sort order for the pages
def custom_sort(a, b):
    return -1 if (a, b) in ordering_rules else 1


middle_sums = 0
for pages in pages_to_produce:
    for i in range(len(pages) - 1):
        if (pages[i], pages[i + 1]) not in ordering_rules:
            pages_sorted = sorted(pages, key=cmp_to_key(custom_sort))
            middle_sums += pages_sorted[len(pages_sorted) // 2]
            break

print(middle_sums)
