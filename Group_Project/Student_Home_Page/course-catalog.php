<?php
require_once 'session_helper.php';

if (!check_session()) {
  header('Location: student-login.html');
  exit();
} else {
  // Continue with the script
}
?>






<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Course Catalog</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/css/bootstrap.min.css" rel="stylesheet">
  <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/js/bootstrap.bundle.min.js"></script>
  <style>
    .search-container {
      margin-top: 2rem;
    }
  </style>
</head>
<body>
<div class="d-flex justify-content-between align-items-center my-3">
  <a href="student-home.php" class="btn btn-primary">Back to Student Home</a>
  <h1 class="text-center">Course Catalog</h1>
</div>

  <div class="container">
    <h1 class="text-center">Course Catalog</h1>
    <div class="search-container">
      <input type="text" id="search-input" class="form-control" placeholder="Search by course code, course name, or major">
    </div>
    <div class="table-responsive">
      <table class="table table-striped table-hover mt-4" id="courses-table">
        <thead>
          <tr>
            <th>Course Code</th>
            <th>Course Name</th>
            <th>Credits</th>
            <th>Prerequisites</th>
            <th>Major Only Course?</th>
          </tr>
        </thead>
        <tbody>
        </tbody>
      </table>
    </div>
  </div>

  <div id="sections-container"></div>
  <div class="modal fade" id="sections-modal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog modal-lg">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="exampleModalLabel">Available Sections</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
        <div class="table-responsive">
          <table class="table table-striped table-hover mt-4" id="sections-table">
            <thead>
              <tr>
                <th>Section Number</th>
                <th>Professor</th>
                <th>Semester</th>
                <th>Year</th>
                <th>Days</th>
                <th>Start Time</th>
                <th>End Time</th>
                <th>Room</th>
                <th>Capacity</th>
              </tr>
            </thead>
            <tbody>
            </tbody>
          </table>
        </div>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
      </div>
    </div>
  </div>
</div>

  <script>
    let coursesData = [];

    $(document).ready(function () {
      fetchCourses();
      
      $("#search-input").on("keyup", function () {
  const searchTerm = $(this).val().toLowerCase();
  if (searchTerm.length > 0) {
    const filteredCourses = coursesData.filter((course) => {
      const courseCode = course.course_code || "";
      const courseName = course.course_name || "";
      const majorRequirements = course.major_requirements || "";

      return (
        courseCode.toLowerCase().includes(searchTerm) ||
        courseName.toLowerCase().includes(searchTerm) ||
        majorRequirements.toLowerCase().includes(searchTerm)
      );
    });
    renderCourses(filteredCourses);
  } else {
    renderCourses(coursesData);
  }
});

  });
  function fetchCourses() {
  $.ajax({
    url: "fetch_courses.php",
    type: "GET",
    dataType: "json",
    success: function (data) {
      coursesData = data;
      renderCourses(data);
    },
    error: function (error) {
      console.log("Error fetching courses:", error);
    },
  });
}

function renderCourses(courses) {
  const tbody = $("#courses-table tbody");
  tbody.empty();

  courses.forEach((course) => {
    const tr = $("<tr>");
    tr.append(`<td>${course.course_code}</td>`);
    tr.append(`<td>${course.course_name}</td>`);
    tr.append(`<td>${course.credits}</td>`);
    tr.append(`<td>${course.prerequisites}</td>`);

    // Display "Major only course" when the major_only attribute is 1
    const majorInfo = course.major_only == 1 ? `${course.major_name} (Major only course)` : course.major_name;
    tr.append(`<td>${majorInfo}</td>`);

    tr.on("click", () => {
      fetchSections(course.course_code);
      $("#sections-modal").modal("show");
    });

    tbody.append(tr);
  });
}


function fetchSections(course_code) {
  $.ajax({
    url: "fetch_sections.php",
    type: "GET",
    data: { course_code: course_code },
    dataType: "json",
    success: function (data) {
      renderSections(data);
    },
    error: function (error) {
      console.log("Error fetching sections:", error);
    },
  });
}

function renderSections(sections) {
  const tbody = $("#sections-table tbody");
  tbody.empty();

  sections.forEach((section) => {
    const tr = $("<tr>");
    tr.append(`<td>${section.section_number}</td>`);
    tr.append(`<td>${section.first_name} ${section.last_name}</td>`);
    tr.append(`<td>${section.semester}</td>`);
    tr.append(`<td>${section.year}</td>`);
    tr.append(`<td>${section.days_of_week}</td>`); // Updated from 'days' to 'days_of_week'
    tr.append(`<td>${section.start_time}</td>`);
    tr.append(`<td>${section.end_time}</td>`);
    tr.append(`<td>${section.room_number}</td>`); // Updated from 'room' to 'room_number'
    tr.append(`<td>${section.capacity}</td>`);

    tbody.append(tr);
  });
}
</script>
</body>
</html>
