// import "core.js";



let chart = am4core.create("chartdiv", am4charts.XYChart);

ads.forEach(element => {
    chart.data = chart.data + { "name": element.fields.name, "clicks": element.fields.clicks };
})

let categoryAxis = chart.xAxes.push(new am4charts.CategoryAxis());
categoryAxis.dataFields.category = "name";
categoryAxis.title.text = "Name of Ad";
let valueAxis = chart.yAxes.push(new am4charts.ValueAxis());
valueAxis.dataFields.category = "clicks";
valueAxis.title.text = "Number of clicks";

let series = chart.series.push(new am4charts.ColumnSeries());
series.name = "Number of clicks per ad";
series.columns.template.tooltipText = "Series: {name}\nCategory: {categoryX}\nValue: {valueY}";
series.columns.template.fill = am4core.color("#104547");
series.dataFields.valueY = "clicks";
series.dataFields.categoryX = "name";

chart.cursor = new am4charts.XYCursor();


// ads.forEach(element => {
//     document.getElementById('example').innerHTML += "<h2>" + element.fields.name + "</h2>" + "<h2>" + element.fields.clicks + "</h2>";
// });
// var names = [];
// var clicks = [];
// ads.forEach(element =>{
//     names.push(element.fields.name);
//     clicks.push(element.fields.clicks);
// }
// )
// console.log(names);
// console.log(clicks);
