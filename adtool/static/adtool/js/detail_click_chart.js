const adclicks = [];
const hourlist = [];
const obj = {};



function fill_chart_lists() {
    // This function fills adclicks and hourlist with corresponding values
    click_log.forEach(click_data => {
        const d = time_calc(new Date(click_data.fields.click_date));
        const index_d = hourlist.indexOf(d)
        if (index_d===-1){
            hourlist.push(d);
            obj[hourlist[hourlist.length-1]] = 1
        }
        else{
            obj[d] += 1
        }
    });
    
    hourlist.forEach(key => {
        adclicks.push(obj[key]);
    });
    
    function time_calc(in_date) {
        return (in_date.getHours() > 12 ? in_date.getHours()-12 + "PM" : in_date.getHours() + "AM");
    }
}

fill_chart_lists()



const ctx = document.getElementById('detail-click-chart').getContext('2d');
const myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: hourlist,
        datasets: [{
            label: 'Clicks',
            data: adclicks,
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            yAxes: [{
                scaleLabel: {
                    display: true,
                    labelString: 'Clicks',
                },
                ticks: {
                    beginAtZero: true,
                    callback: function (value) { if (Number.isInteger(value)) { return value; } },
                    stepSize: 1
                }
            }],
            xAxes: [{
                scaleLabel: {
                    display: true,
                    labelString: 'Hours',
                },
            }]
        }
    }
});