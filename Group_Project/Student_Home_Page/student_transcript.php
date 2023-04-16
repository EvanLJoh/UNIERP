<?php
require_once 'session_helper.php';

if (!check_session()) {
  header('Location: student-login.html');
  exit();
} else {
  // Continue with the script
}





$servername = "localhost";
$username = "root";
$password = "root";
$dbname = "UNIERPv3";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}

// Replace the value with the actual student ID.
$student_id = 1;

// Fetch student information
$student_sql = "SELECT s.*, m.major_name, hp.program_name FROM students s 
                LEFT JOIN majors m ON s.major_id = m.major_id 
                LEFT JOIN honors_programs hp ON s.honors_program_id = hp.program_id 
                WHERE s.student_id = $student_id";
$student_result = $conn->query($student_sql);
$student = $student_result->fetch_assoc();

// Fetch student transcript
$transcript_sql = "SELECT t.*, c.course_code, c.course_name FROM student_transcript t
                   JOIN courses c ON t.course_id = c.course_id
                   WHERE t.student_id = $student_id
                   ORDER BY t.year ASC, t.semester ASC";
$transcript_result = $conn->query($transcript_sql);

// Close connection
$conn->close();
?>

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Student Transcript</title>
  <link href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">

</head>
<body>
  <div class="container">
    <h1 class="my-4">Student Transcript</h1>
    
    <h2><?php echo $student["first_name"] . " " . $student["last_name"]; ?></h2>
    <p><?php echo $student["email"]; ?></p>
    <p><?php echo $student["major_name"]; ?></p>
    
    <table class="table table-striped">
      <thead>
        <tr>
          <th>Year</th>
          <th>Semester</th>
          <th>Course Code</th>
          <th>Course Name</th>
          <th>Grade</th>
          <th>Credits Earned</th>
        </tr>
      </thead>
      <tbody>
        <?php while ($row = $transcript_result->fetch_assoc()): ?>
        <tr>
          <td><?php echo $row["year"]; ?></td>
          <td><?php echo $row["semester"]; ?></td>
          <td><?php echo $row["course_code"]; ?></td>
          <td><?php echo $row["course_name"]; ?></td>
          <td><?php echo $row["grade"]; ?></td>
          <td><?php echo $row["credits_earned"]; ?></td>
        </tr>
        <?php endwhile; ?>
      </tbody>
    </table>

    <div class="my-3">
      <a href="student_transcript.php" class="btn btn-primary">View Transcript</a>
      <a href="student-home.php" class="btn btn-secondary">Back to Home</a>
    </div>
  </div>
</body>
</html>
