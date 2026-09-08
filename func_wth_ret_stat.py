def process_student_results(
    student_id,
    student_name,
    subject_marks,
    attendance_percentage,
    assignment_score,
    extracurricular_points,
):
    total_marks = 0
    failed_subjects = []

    for subject, marks in subject_marks.items():
        total_marks += marks
        if marks < 35:
            failed_subjects.append(subject)

    num_subjects = len(subject_marks)
    raw_average = total_marks / num_subjects if num_subjects > 0 else 0

    assignment_contribution = assignment_score * 0.10
    final_score = raw_average + assignment_contribution + extracurricular_points

    if attendance_percentage < 75:
        final_score -= 5
        attendance_status = "Shortage of Attendance"
    else:
        attendance_status = "Good Attendance"

    if final_score >= 90:
        grade = "A+"
    elif final_score >= 80:
        grade = "A"
    elif final_score >= 70:
        grade = "B"
    elif final_score >= 60:
        grade = "C"
    elif final_score >= 50:
        grade = "D"
    else:
        grade = "Fail"

    overall_result = "Fail" if len(failed_subjects) > 0 or grade == "Fail" else "Pass"

    return {
        "student_id": student_id,
        "student_name": student_name,
        "total_marks": total_marks,
        "average": round(final_score, 2),
        "grade": grade,
        "attendance_status": attendance_status,
        "failed_subjects": failed_subjects,
        "result": overall_result,
    }


def display_student_report(report):
    print(f"Student ID: {report['student_id']}\n")
    print(f"Student Name: {report['student_name']}")
    print(f"Total Marks: {report['total_marks']}")
    print(f"Average: {report['average']}")
    print(f"Grade: {report['grade']}")
    print(f"Attendance Status: {report['attendance_status']}")
    print(f"Failed Subjects: {report['failed_subjects']}")
    print(f"Result: {report['result']}")


sample_marks = {
    "Math": 95,
    "Science": 88,
    "English": 76,
    "Computer": 92,
    "Physics": 34,
}

student_report = process_student_results(
    student_id=1001,
    student_name="Alex",
    subject_marks=sample_marks,
    attendance_percentage=82,
    assignment_score=18,
    extracurricular_points=3,
)

display_student_report(student_report)