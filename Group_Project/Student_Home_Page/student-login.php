<?php
ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);

session_start();

if (isset($_POST['login'])) {
    $student_id = $_POST['student-id'];
    $registration_pin = $_POST['registration-pin'];

    $servername = "localhost";
    $username = "root";
    $password = "root";
    $dbname = "UNIERPv3";

    try {
        $conn = new mysqli($servername, $username, $password, $dbname);

        if ($conn->connect_error) {
            throw new Exception("Connection failed: " . $conn->connect_error);
        }

        $sql = "SELECT student_id, CONCAT(first_name, ' ', last_name) as student_name FROM students WHERE student_id = ? AND registration_pin = ? LIMIT 0, 25";
        $stmt = $conn->prepare($sql);
        $stmt->bind_param("ii", $student_id, $registration_pin);
        $stmt->execute();
        $stmt->store_result();

        if ($stmt->num_rows > 0) {
            $stmt->bind_result($student_id, $student_name);
            $stmt->fetch();
            $_SESSION['student_id'] = $student_id;
            $_SESSION['student_name'] = $student_name; // Store the student's name in the session
            header("location: student-home.php");
        } else {
            echo "Invalid login credentials";
        }

        $stmt->close();
        $conn->close();
    } catch (Exception $e) {
        echo "Error: " . $e->getMessage();
    }
}
?>

