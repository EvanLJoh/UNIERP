<?php
require_once 'session_helper.php';

if (!check_session()) {
  header('Location: student-login.html');
  exit();
} else {
  // Continue with the script
}

ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);



?>


<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/css/bootstrap.min.css" rel="stylesheet">
  <style>
    body {
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .bg-primary-gradient {
      background: linear-gradient(90deg, rgba(0, 123, 255, 1) 0%, rgba(9, 34, 121, 1) 100%);
    }
    .card {
      transition: all .2s ease-in-out;
    }
    .card:hover {
      transform: scale(1.05);
    }
  </style>
  <title>Student Dashboard - University Registration System</title>
</head>
<body>
  <header class="bg-primary-gradient text-white text-center py-4">
    <h1>University Registration System</h1>
  </header>
  <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
    <div class="container">
      <ul class="navbar-nav">
        <li class="nav-item"><a href="#" class="nav-link">Home</a></li>
        <li class="nav-item"><a href="#" class="nav-link">Courses</a></li>
        <li class="nav-item"><a href="#" class="nav-link">Profile</a></li>
        <li class="nav-item"><a href="logout.php" class="nav-link">Logout</a></li>
      </ul>
    </div>
  </nav>
  <main class="container my-4">
   <h2 class="mb-4">Welcome, <?= $_SESSION['student_name'] ?>!</h2>
    <section class="row g-4">
      <div class="col-md-6 col-lg-3 mb-4">
        <div class="card">
          <div class="card-body">
            <h3 class="card-title">Student Dashboard</h3>
            <p class="card-text">View your personal information, major, honors program, GPA, and classification.</p>
            <a href="student-dashboard.php" class="btn btn-primary">Go to Dashboard</a>
          </div>
        </div>
      </div>

      <div class="col-md-6 col-lg-3 mb-4">
        <div class="card">
          <div class="card-body">
            <h3 class="card-title">Course Catalog</h3>
            <p class="card-text">Browse and search for available courses, prerequisites, and major requirements.</p>
            <a href="course-catalog.php" class="btn btn-primary">Go to Course Catalog</a>
          </div>
        </div>
      </div>
      
      <div class="col-md-6 col-lg-3 mb-4">
        <div class="card">
          <div class="card-body">
            <h3 class="card-title">Course Registration</h3>
            <p class="card-text"> Register for courses and check for registration restrictions.</p>
            <a href="course-registration.php" class="btn btn-primary">Course Registration</a>
          </div>
        </div>
      </div>
      
      <div class="col-md-6 col-lg-3 mb-4">
        <div class="card">
          <div class="card-body">
            <h3 class="card-title">Grade Report</h3>
            <p class="card-text">View your grades and academic performance summary for each semester.</p>
            <a href="#" class="btn btn-primary">View Grades</a>
          </div>
        </div>
      </div>
      
    </section>
  </main>
  <footer class="text-center py-3">
    <p>&copy; 2023 University ERP. All rights reserved.</p>
  </footer>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>

