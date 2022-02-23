"""Generate sales report showing total melons each salesperson sold."""

# initialize two lists
salespeople = []
melons_sold = []

# open txt file
f = open('sales-report.txt')
# for each line in the file
for line in f:
    # remove space at the end
    line = line.rstrip()
    # split by | and put it into a list
    entries = line.split('|')
    # select name of a person
    salesperson = entries[0]
    print('salesperson', salesperson)
    # and amount of melons
    melons = int(entries[2])

    # search for a seller's name in the list of salespeople
    # if it's there
    if salesperson in salespeople:
        # get index of a sale's person's name and save it in position
        position = salespeople.index(salesperson)

        # and add melon into list of sold melons in particular position
        melons_sold[position] += melons
    # if it's not there
    else:
        # add name of the sale's person into a list of sales people
        salespeople.append(salesperson)
        # add melons into a list of sold melons
        melons_sold.append(melons)

# generate report of how many melons are sols by a particular person
for i in range(len(salespeople)):
    print(f'{salespeople[i]} sold {melons_sold[i]} melons')
