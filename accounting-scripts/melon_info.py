"""Print out all the melons in our inventory."""


from melons import melons


def print_melon(melons_name, melons_info_list):
    """Print each melon with corresponding attribute information."""
    sedless = melons_info_list[1]
    have_or_have_not = 'have'
    if sedless:
        have_or_have_not = 'do not have'
    print(f'{melons_name}s {have_or_have_not} seeds. It weights {melons_info_list[3]}, flesh color is {melons_info_list[2]}, rind color {melons_info_list[4]} and priced as ${melons_info_list[0]:.2f}')


for i in melons:
    print_melon(i, list(melons[i].values()))
