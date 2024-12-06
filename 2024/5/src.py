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

middle_sums = 0
for pages in pages_to_produce:
    is_valid_ordering = True
    for i in range(len(pages) - 1):
        if (pages[i], pages[i + 1]) not in ordering_rules:
            is_valid_ordering = False
            break
    if is_valid_ordering:
        middle_sums += pages[len(pages) // 2]

print(middle_sums)
