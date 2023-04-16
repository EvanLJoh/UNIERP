<?php
header("Content-Type: application/json");
require_once("db_connection.php");

if (isset($_GET["course_code"])) {
    $course_code = $_GET["course_code"];
    
    $sql = "SELECT s.section_number, s.semester, s.year, s.start_time, s.end_time, s.capacity, s.days_of_week,
            p.first_name, p.last_name, s.room_number, s.building
            FROM sections s
            JOIN professors p ON s.professor_id = p.professor_id
            JOIN courses c ON s.course_id = c.course_id
            WHERE c.course_code = ?";
    
    $stmt = $conn->prepare($sql);
    $stmt->bind_param("s", $course_code);
    $stmt->execute();
    $result = $stmt->get_result();
    
    if ($result->num_rows > 0) {
        $sections = [];
        while ($row = $result->fetch_assoc()) {
            $sections[] = $row;
        }
        echo json_encode($sections);
    } else {
        echo json_encode([]);
    }
    
    $stmt->close();
} else {
    http_response_code(400);
    echo json_encode(["error" => "Invalid request. Course Code is missing."]);
}

$conn->close();
?>
