<?php





function check_course_quota($conn, $section_id) {
  $sql = "CALL check_course_quota(?, @quota_reached)";
  $stmt = $conn->prepare($sql);
  $stmt->bind_param("i", $section_id);
  $stmt->execute();
  $result = $conn->query("SELECT @quota_reached AS quota_reached");
  $row = $result->fetch_assoc();
  return $row['quota_reached'];
}

function has_time_conflict($conn, $student_id, $section_id) {
  $sql = "CALL has_time_conflict(?, ?, @conflict)";
  $stmt = $conn->prepare($sql);
  $stmt->bind_param("ii", $student_id, $section_id);
  $stmt->execute();
  $result = $conn->query("SELECT @conflict AS conflict");
  $row = $result->fetch_assoc();
  return $row['conflict'];
}


function is_major_course_allowed($conn, $student_id, $course_id) {
  $sql = "CALL is_major_course_allowed(?, ?, @allowed)";
  $stmt = $conn->prepare($sql);
  $stmt->bind_param("ii", $student_id, $course_id);
  $stmt->execute();
  $result = $conn->query("SELECT @allowed AS allowed");
  $row = $result->fetch_assoc();
  return $row['allowed'];
}


function has_prerequisites($conn, $student_id, $course_id) {
  $sql = "CALL has_prerequisites(?, ?, @prerequisites_met)";
  $stmt = $conn->prepare($sql);
  $stmt->bind_param("ii", $student_id, $course_id);
  $stmt->execute();
  $result = $conn->query("SELECT @prerequisites_met AS prerequisites_met");
  $row = $result->fetch_assoc();
  return $row['prerequisites_met'];
}


function fetch_courses($conn) {
    $sql = "SELECT c.course_code, c.course_name, s.section_number AS sec, s.semester AS cmp, c.credits AS cred, s.days_of_week, s.start_time, s.end_time, s.capacity, CONCAT(p.first_name, ' ', p.last_name) AS professor_name, s.building, s.room_number, s.section_id
            FROM sections AS s
            JOIN courses AS c ON s.course_id = c.course_id
            JOIN professors AS p ON s.professor_id = p.professor_id";
  
    $result = $conn->query($sql);
  
    if ($result->num_rows > 0) {
      $courses = array();
  
      while ($row = $result->fetch_assoc()) {
        $courses[] = $row;
      }
  
      return $courses;
    } else {
      return false;
    }
  }


function register_student_for_course($conn, $student_id, $section_id) {
    $can_register = true;
  
    // Check course quotas
    if (!check_course_quota($conn, $section_id)) {
      $can_register = false;
    }
  
    // Resolve time conflicts
    if (has_time_conflict($conn, $student_id, $section_id)) {
      $can_register = false;
    }
  
    // Enforce major-only courses
    if (!is_major_course_allowed($conn, $student_id, $section_id)) {
      $can_register = false;
    }
  
    // Check for prerequisites
    if (!has_prerequisites($conn, $student_id, $section_id)) {
      $can_register = false;
    }
  
    // If all checks pass, register the student for the course
    if ($can_register) {
      $sql = "INSERT INTO student_current_semester_registration (student_id, section_id) VALUES (?, ?)";
      $stmt = $conn->prepare($sql);
      $stmt->bind_param("ii", $student_id, $section_id);
  
      if ($stmt->execute()) {
        return true;
      } else {
        return false;
      }
    } else {
      return false;
    }
  }



?>