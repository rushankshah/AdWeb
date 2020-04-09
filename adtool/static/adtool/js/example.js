// ads.forEach(element => {
//     document.getElementById('example').innerHTML += "<h2>" + element.fields.name + "</h2>" + "<h2>" + element.fields.clicks + "</h2>";
// });

var data = []

ads.forEach(element => {
    data.push({ label: element.fields.name, y: element.fields.clicks });
});

window.onload = function () {

    var chart = new CanvasJS.Chart("chartContainer", {
        theme: "light1", // "light2", "dark1", "dark2"
        animationEnabled: false, // change to true		
        title: {
            text: "Basic Column Chart"
        },
        data: [
            {
                // Change type to "bar", "area", "spline", "pie",etc.
                type: "column",
                dataPoints: data

            }
        ]
    });
    chart.render();

}
