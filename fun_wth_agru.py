# def generate_report(student):
#     name=student["name"]
#     marks=student["marks"]
#     total=0
#     count=0
#     highest_subject=""
#     highest_marks=0
#     status="Pass"
#     for subject in marks:
#         mark=marks[subject]
#         total=total+mark
#         count=count+1
#         if mark>highest_marks:
#             highest_marks=mark
#             highest_subject=subject
#         if mark<35:
#             status="Fail"
#     average=total/count
#     if average>=90:
#         grade="A"
#     elif average>=80:
#         grade="B"
#     elif average>=70:
#         grade="C"
#     elif average>=60:
#         grade="D"
#     else:
#         grade="F"
#     print("Name:",name)
#     print("Total Marks:",total)
#     print("Average:",round(average,2))
#     print("Highest Subject:",highest_subject)
#     print("Grade:",grade)
#     print("Status:",status)
# generate_report({"name":"Rahul","marks":{"Math":85,"Science":72,"English":90})