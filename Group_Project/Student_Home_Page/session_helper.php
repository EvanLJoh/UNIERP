<?php
session_start();

function check_session() {
  return isset($_SESSION['student_id']);
}
?>
