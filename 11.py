Your_expenses={"Hotel":3000, "Food":1000, "Transportation":500, "Attractions":300, "Miscellaneous":200 }
Partner_expenses={"Hotel":2000, "Food":1200, "Transportation":600, "Attractions":500, "Miscellaneous":150}
Your_total="5,000"
Partner_total="4,650"

print("Your total expenses:",Your_total)
print("Partner's total expenses:",Partner_total)

if Your_total > Partner_total:
    print("You spent more money overall.")
elif Partner_total >Your_total:
    print("Your partner spent more money overall.")
else:
    print("You both spent the same amount")

max_diff=0
diff_category=""
for category in Your_expenses:
    diff=abs(Your_expenses[category]-Partner_expenses[category])
    if diff > max_diff:
        max_diff =diff
        diff_category = category

print("Category with significant differences:",diff_category)
print("Difference:", max_diff)
