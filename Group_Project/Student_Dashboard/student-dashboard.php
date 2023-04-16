<?php
$servername = "localhost";
$username = "root";
$password = "";
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

// Fetch current semester registration
$registration_sql = "SELECT c.course_code, c.course_name, p.first_name, p.last_name, sec.start_time, sec.end_time, sec.room_number, sec.section_number 
                     FROM student_current_semester_registration sr 
                     JOIN sections sec ON sr.section_id = sec.section_id 
                     JOIN courses c ON sec.course_id = c.course_id 
                     JOIN professors p ON sec.professor_id = p.professor_id 
                     WHERE sr.student_id = $student_id";
$registration_result = $conn->query($registration_sql);

// Close connection
$conn->close();
?>

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Student Dashboard</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-KyZXEAg3QhqLMpG8r+Knujsl5/EnJ6t97JpKcDp8UBU8rcijKKZn5PDCgCfzaE5Jp" crossorigin="anonymous">
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-s7UvuurdJxDAp8KjDO7aA7mD3Tm6bcdeq6q3+6QPAfIU2QviD9Rl9jTFs/3rZJf" crossorigin="anonymous"></script>
</head>
<body>
  <div class="container">
    <h1 class="my-4">Student Dashboard</h1>
    
    <h2>Personal Information</h2>
    <table class="table table-striped">
      <tbody>
        <tr>
          <th>Name</th>
          <td><?php echo $student["first_name"] . " " . $student["last_name"]; ?></td>
        </tr>
        <tr>
          <th>Email</th>
          <td><?php echo $student["email"]; ?></td>
        </tr>
        <tr>
          <th>Major</th>
          <td><?php echo $student["major_name"]; ?></td>
        </tr>
        <tr>
          <th>Honors Program</th>
          <td><?php echo $student["program_name"] ? $student["program_name"] : "Not Enrolled"; ?></td>
        </tr>
        <tr>
          <th>GPA</th>
          <td><?php echo $student["gpa"]; ?></td>
        </tr>
        <tr>
          <th>Credits Taken</th>
          <td><?php echo $student["credits_taken"]; ?></td>
        </tr>
        <tr>
          <th>Classification</th>
          <td><?php echo $student["classification"]; ?></td>
        </tr>
      </tbody>
    </table>

    <h2>Current Semester Registration</h2>
    <table class="table table-striped">
      <thead>
        <tr>
          <th>Course Code</th>
          <th>Course Name</th>
          <th>Professor</th>
          <th>Section Number</th>
          <th>Schedule</th>
          <th>Room Number</th>
        </tr>
      </thead>
      <tbody>
        <?php while ($row = $registration_result->fetch_assoc()): ?>
        <tr>
          <td><?php echo $row["course_code"]; ?></td>
          <td><?php echo $row["course_name"]; ?></td>
          <td><?php echo $row["first_name"] . " " . $row["last_name"]; ?></td>
          <td><?php echo $row["section_number"]; ?></td>
          <td><?php echo date("g:i A", strtotime($row["start_time"])) . " - " . date("g:i A", strtotime($row["end_time"])); ?></td>
          <td><?php echo $row["room_number"]; ?></td>
        </tr>
        <?php endwhile; ?>
      </tbody>
    </table>

    <div class="my-3">
      <a href="student_transcript.php" class="btn btn-primary">View Transcript</a>
    </div>
  </div>
</body>
</html>

