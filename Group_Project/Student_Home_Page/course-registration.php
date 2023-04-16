<?php
require_once 'session_helper.php';

if (!check_session()) {
  header('Location: student-login.html');
  exit();
} else {
  // Continue with the script
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Student Registration</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet">
  <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.6/dist/umd/popper.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.min.js"></script>
</head>
<body>
  <div class="container">
    <h1 class="text-center mt-5">Registration</h1>
    <div class="row">
      <div class="col-lg-6 offset-lg-3">
        <form id="registrationForm">
          <div class="mb-3">
            <label for="studentID" class="form-label">Student ID</label>
            <input type="number" class="form-control" id="studentID" name="student_id" required>
          </div>
          <div class="mb-3">
            <label for="courseID" class="form-label">Course ID</label>
            <input type="number" class="form-control" id="courseID" name="course_id" required>
          </div>
          <div class="mb-3">
            <label for="sectionID" class="form-label">Section ID</label>
            <input type="number" class="form-control" id="sectionID" name="section_id" required>
          </div>
          <div class="mb-3">
            <label for="semesterCredits" class="form-label">Semester Credits</label>
            <input type="number" class="form-control" id="semesterCredits" name="semester_credits" required>
          </div>
          <div class="d-grid">
            <button type="submit" class="btn btn-primary">Register</button>
            <div class="my-3">
            <a href="student_transcript.php" class="btn btn-primary">View Transcript</a>
            <a href="student-home.php" class="btn btn-secondary">Back to Home</a>
            </div>
          </div>
        </form>
      </div>
    </div>
  </div>

  <script>
    document.getElementById("registrationForm").addEventListener("submit", async function (event) {
      event.preventDefault();
      const formData = new FormData(event.target);
      const studentID = formData.get("student_id");
      const courseID = formData.get("course_id");
      const sectionID = formData.get("section_id");
      const semesterCredits = formData.get("semester_credits");

      const response = await fetch("process_registration.php", {
        method: "POST",
        body: JSON.stringify({
          student_id: studentID,
          course_id: courseID,
          section_id: sectionID,
          semester_credits: semesterCredits
        }),
        headers: {
          "Content-Type": "application/json"
        }
      });

      const jsonResponse = await response.json();

      if (jsonResponse.status === "success") {
        alert("Successfully registered for the class.");
      } else {
        alert(`Registration failed: ${jsonResponse.message}`);
      }
    });
  </script>
</body>
</html>
