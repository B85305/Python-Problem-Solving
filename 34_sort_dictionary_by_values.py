
marks = {
    "Amit": 85,
    "Bhakti": 95,
    "Riya": 75,
    "Neha": 90
}

sorted_marks = dict(
    sorted(marks.items(), key=lambda item: item[1])
)

print("Sorted Dictionary:", sorted_marks)
