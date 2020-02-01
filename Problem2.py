# The cover price of a book is $25, but bookstores get a 10% discount. Shipping costs $2
# for the first five copies and 2.75 cents for all rest of copies. Write a Python program to
# show what is the total wholesale cost for 40 copies display the result.

print('Cover Price of the Book before discount in Dollar: 25')
cp = 25
dp = cp - float(cp) * (10/100)
print('Discounted Cover Price in Dollar: ', dp)
tcs = 40
print('Total number of copies to be sold: ', tcs)
sc = 5 * 2 + 35 * (2.75/100)
print('Total Cost of Shipping ', sc)
tc = dp * 40 + sc
print('Total Cost including shipping ', tc)
