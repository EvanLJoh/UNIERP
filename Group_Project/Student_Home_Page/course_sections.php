

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Course Sections</title>
  <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
</head>
<body>
  <h1>Course Sections</h1>
  <input type="text" id="course-code" placeholder="Enter course code">
  <button id="search-btn">Search</button>
  <div id="sections-container"></div>

  <script>
    $("#search-btn").on("click", function() {
      let courseCode = $("#course-code").val();
      if (courseCode) {
        $.getJSON("fetch_sections.php?course_code=" + encodeURIComponent(courseCode), function(sections) {
          displaySections(sections);
        });
      }
    });

    function displaySections(sections) {
      $("#sections-container").empty();

      if (sections.length > 0) {
        // Create table
        let table = $("<table></table>");
        table.attr("border", "1");

        // Create table header
        let thead = $("<thead></thead>");
        let headerRow = $("<tr></tr>");
        headerRow.append("<th>Section Number</th>");
        headerRow.append("<th>Semester</th>");
        headerRow.append("<th>Year</th>");
        headerRow.append("<th>Start Time</th>");
        headerRow.append("<th>End Time</th>");
        headerRow.append("<th>Capacity</th>");
        headerRow.append("<th>Days of Week</th>");
        headerRow.append("<th>Professor</th>");
        headerRow.append("<th>Room Number</th>");
        headerRow.append("<th>Building</th>");
        thead.append(headerRow);

        // Create table body
        let tbody = $("<tbody></tbody>");
        for (let i = 0; i < sections.length; i++) {
          let row = $("<tr></tr>");
          row.append("<td>" + sections[i].section_number + "</td>");
          row.append("<td>" + sections[i].semester + "</td>");
          row.append("<td>" + sections[i].year + "</td>");
          row.append("<td>" + sections[i].start_time + "</td>");
          row.append("<td>" + sections[i].end_time + "</td>");
          row.append("<td>" + sections[i].capacity + "</td>");
          row.append("<td>" + sections[i].days_of_week + "</td>");
          row.append("<td>" + sections[i].first_name + " " + sections[i].last_name + "</td>");
          row.append("<td>" + sections[i].room_number + "</td>");
          row.append("<td>" + sections[i].building + "</td>");
          tbody.append(row);
          }

          // Add table header and body to table
          table.append(thead);
          table.append(tbody);

          // Add table to sections container
          $("#sections-container").append(table);
        } else {
          $("#sections-container").append("<p>No sections found for the entered course code.</p>");
        }
      }

      </script>
</body>
</html>
