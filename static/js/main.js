var currentSortCol = "";
var isAscending = true;

function submitQuery() {
    var query = document.getElementById("query").value;
    var resultDiv = document.getElementById("result");

    resultDiv.innerHTML = "";
    currentSortCol = "";
    isAscending = true;

    if (query.trim() === "") {
        resultDiv.innerHTML = "<p>Please enter the query.</p>";
        return;
    }

    fetch("/search_startup?q=" + encodeURIComponent(query))
        .then(response => response.json())
        .then(data => {
            resultDiv.innerHTML = "<h2>Search Results:</h2>" + "<p>Click the Column Tabs to sort the data entries</p>" + jsonToTable(data.result);

            document.getElementById("resetButton").style.display = "block";
            resultDiv.classList.add("table-view");
            resultDiv.dataset.json = JSON.stringify(data.result);
        })
        .catch(error => {
            resultDiv.innerHTML = "<p>Error: " + error.message + "</p>";
        });
}

function resetForm() {
    document.getElementById("query").value = "";
    document.getElementById("result").innerHTML = "";
    document.getElementById("result").classList.remove("table-view");
    document.getElementById("resetButton").style.display = "none";
}

function jsonToTable(json) {
    if (!json || json.length === 0) {
        return "<p>No results found.</p>";
    }

    var keys = Object.keys(json[0]);

    var table = "<table border='1'><tr>";
    for (var i = 0; i < keys.length; i++) {
        table += "<th onclick=\"sortTable('" + keys[i] + "')\">" + keys[i].toUpperCase();
        table += "<span class=\"arrow\">" + (keys[i] === currentSortCol ? (isAscending ? "↑" : "↓") : "") + "</span>";
        table += "</th>";
    }
    table += "</tr>";

    json.sort(function(a, b) {
        var colA = a[currentSortCol];
        var colB = b[currentSortCol];
        var comparison = 0;

        if (colA > colB) {
            comparison = 1;
        } else if (colA < colB) {
            comparison = -1;
        }

        return isAscending ? comparison : -comparison;
    });

    for (var j = 0; j < json.length; j++) {
        table += "<tr>";
        for (var k = 0; k < keys.length; k++) {
            table += "<td>" + json[j][keys[k]] + "</td>";
        }
        table += "</tr>";
    }

    table += "</table>";
    return table;
}

function handleKeyPress(event) {
    if (event.keyCode === 13) {
        event.preventDefault();
        submitQuery();
    }
}

function sortTable(column) {
    if (column === currentSortCol) {
        isAscending = !isAscending;
    } else {
        currentSortCol = column;
        isAscending = true;
    }

    var resultDiv = document.getElementById("result");
    resultDiv.innerHTML = "<h2>Search Results:</h2>" + "<p>Click the Column Tabs to sort the data entries</p>" + jsonToTable(JSON.parse(resultDiv.dataset.json));
}