<?php
// process_registration.php

// Include your database connection file
require_once 'db_connection.php';

header('Content-Type: application/json');
$input_data = json_decode(file_get_contents('php://input'), true);

// Extract variables from input_data
$student_id = $input_data['student_id'];
$course_id = $input_data['course_id'];
$section_id = $input_data['section_id'];
$semester_credits = $input_data['semester_credits'];

// Prepare and execute the stored procedure
try {
    $stmt = $conn->prepare("CALL RegisterStudentForClass(?, ?, ?, ?)");
    $stmt->bind_param("iiii", $student_id, $course_id, $section_id, $semester_credits);
    $result = $stmt->execute();

    if ($result) {
        $response = array("status" => "success", "message" => "Successfully registered for the class.");
    } else {
        $response = array("status" => "error", "message" => $conn->error);
    }
} catch (Exception $e) {
    $response = array("status" => "error", "message" => $e->getMessage());
}

// Close the statement and connection
$stmt->close();
$conn->close();

echo json_encode($response);
?>
