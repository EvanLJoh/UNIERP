<?php
header('Content-Type: application/json');

$servername = "localhost";
$username = "root";
$password = "root";
$dbname = "UNIERPv3";

mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);

$conn = new mysqli($servername, $username, $password, $dbname);

if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}

$sql = "SELECT c.course_code, c.course_name, c.credits, COALESCE(GROUP_CONCAT(pr.course_name SEPARATOR ', '), 'None') AS prerequisites, COALESCE(m.major_name, 'None') AS major_name, c.major_only
        FROM courses c
        LEFT JOIN course_prerequisites cp ON c.course_id = cp.course_id
        LEFT JOIN courses pr ON cp.prerequisite_id = pr.course_id
        LEFT JOIN major_requirements mr ON c.course_id = mr.course_id
        LEFT JOIN majors m ON mr.major_id = m.major_id
        GROUP BY c.course_id";

$result = $conn->query($sql);

$courses = array();

if ($result->num_rows > 0) {
  while ($row = $result->fetch_assoc()) {
    $courses[] = $row;
  }
} 

$conn->close();

echo json_encode($courses);
?>

