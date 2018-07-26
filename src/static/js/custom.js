jQuery(document).ready(function(){
    /*---- Display recipients ----*/
    $('#recipients_list').DataTable( {
        "ajax": "/recipient/json/1",
        "columns": [
            { "data": "id" },
            { "data": "user_name"},
            { "data": "name" },
            { "data": "email" },
            { "data": "state",  "mRender": function (data) { return data == 1? 'active' : 'not active'; }},
            { "data": "last_send_date" },
            { "data": null,
              "bSortable": false,
              "mRender": function (data) { return "<a href='edit/" + data.id + "'>" + "Edit" + "</a>"; }
            },
            { "data": null,
              "bSortable": false,
              "mRender": function (data) { return "<a href='delete/" + data.id + "' onclick='return confirm(\"Are you sure you want to delete?\");'>" + "Delete" + "</a>"; }
            }
        ],
    } );

    if (window.location.pathname == '/reports/' + campaign_id) {
        /*----- Pie chart -----*/
        $.ajax({
            url: "/reports/json/form-filled/"+campaign_id,
            dataType: 'json',
            success: function(results){
                var labels = [], data = [];
                results.forEach(function(result){
                    labels.push(result.label);
                    data.push(result.items);
                });
                drawChart("PieChart", "pie",  labels, data, true);
            }
        })
        /*----- Bar chart -----*/
        $.ajax({
            url: "/reports/json/form-filled-month/"+campaign_id,
            dataType: 'json',
            success: function(results){
                var labels = [], data = [];
                results.forEach(function(result){
                    labels.push(result.label);
                    data.push(result.items);
                });
                drawChart("BarChart", "bar",  labels, data, false);
            }
        })

        function drawChart(id, type, labels, data, display_legend){
            var pie = document.getElementById(id).getContext('2d');
            var PieChart = new Chart(pie, {
                type: type,
                data: {
                    labels: labels,
                    datasets: [{
                        data: data,
                        backgroundColor: [
                            'rgba(54, 162, 235, 0.2)',
                            'rgba(255, 99, 132, 0.2)',
                        ],
                        borderColor: [
                            'rgba(54, 162, 235, 1)',
                            'rgba(255,99,132,1)',
                        ],
                        borderWidth: 1
                    }]
                },
                options: {
                    legend: {
                        display: display_legend
                    },
                    scales: {
                        yAxes: [{
                            ticks: {
                                beginAtZero:true
                            }
                        }]
                    }
                }
            });
        }
    }
});