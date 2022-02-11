def print_report_information(file_name):
    the_file = open(file_name)
    for line in the_file:
        # import pdb; pdb.set_trace()
        line = line.rstrip()
        words = line.split('|')

        melon = words[0]
        count = words[1]
        amount = words[2]

        print(f"Delivered {count} {melon}s for total of ${amount}")
    the_file.close()



print("Day 1")
print_report_information('um-deliveries-day-1.txt')
print("Day 2")
print_report_information('um-deliveries-day-2.txt')
print("Day 3")
print_report_information('um-deliveries-day-3.txt')