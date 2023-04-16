<?php
require_once 'db_connection.php';
require_once 'course_registration_functions.php';

$student_id = 1; // Replace with the actual student ID (e.g., from a session variable)
$section_id = intval($_GET['section_id']);

$registration_status = register_student_for_course($conn, $student_id, $section_id);
$message = $registration_status ? 'Registration successful.' : 'Error registering for the course.';


header("Location: index.php?message=" . urlencode($message));
?>
