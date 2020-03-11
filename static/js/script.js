
Chart.defaults.global.defaultFontFamily = 'Itim';
Chart.defaults.global.defaultFontSize = 18;

let charts = document.getElementById('Charts').getContext('2d');
let charts_week = document.getElementById('Charts_week').getContext('2d');
let charts_month = document.getElementById('Charts_month').getContext('2d');
let charts_year = document.getElementById('Charts_year').getContext('2d');

let product_name = [];
let product_total = [];
let date = new Date();
let loop = document.getElementById('total_product').innerHTML;

let color = [];

for (let travel = 1; travel <= loop; travel++) {
    product_name.push(document.getElementById('' + travel).innerHTML);
    product_total.push(document.getElementById('t' + travel).innerHTML);

}

for (let i=0;i<loop;i++){
    color.push('rgba(255,' + Math.floor(Math.random() * 100) + ',' + Math.floor(Math.random() * 100) + ',' + '0.5)');
}
console.log(color);

let show_day = new Chart(charts, {
    type: 'bar',
    data: {
        labels: product_name,
        datasets: [{
            barPercentage: 1.0,
            label: 'สินค้าที่นิยมซื้อมากที่สุด',
            data: product_total,
            backgroundColor: color,
            borderWidth: 4,
            borderColor: '#777',
            hoverBorderWidth: 3,
            hoverBorderWidth: '#000',

        }],
    },
    options: {
        title: {
            display: true,
            text: 'Chart of Day',
            fontSize: 32
        },
        legend: {
            position: 'right',
            labels: {
                fontColor: '#000',
                fontSize: 20
            }
        },
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true,
                    stepSize: 1
                }
            }]
        }
    }
});


let show_week = new Chart(charts_week, {
    type: 'bar',
    data: {
        labels: product_name,
        datasets: [{
            barPercentage: 1.0,
            label: 'สินค้าที่นิยมซื้อมากที่สุด',
            data: product_total,
            backgroundColor: color,
            borderWidth: 4,
            borderColor: '#777',
            hoverBorderWidth: 3,
            hoverBorderWidth: '#000',

        }],
    },
    options: {
        title: {
            display: true,
            text: 'Chart of Week',
            fontSize: 32
        },
        legend: {
            position: 'right',
            labels: {
                fontColor: '#000',
                fontSize: 20
            }
        },
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true,
                    stepSize: 1
                }
            }]
        }
    }
});


let show_month = new Chart(charts_month, {
    type: 'line',
    data: {
        labels: [
            'Jan',
            'Feb',
            'Mar',
            'April',
            'May',
            'Jun',
            'Jul',
            'Aug',
            'Sep',
            'Oct',
            'Nov',
            'Dec'
        ],
        datasets: [{
            barPercentage: 1.0,
            label: 'สินค้าที่นิยมซื้อมากที่สุด',
            data: product_total,
            backgroundColor: color,
            borderWidth: 4,
            borderColor: '#777',
            hoverBorderWidth: 3,
            hoverBorderWidth: '#000',

        }],
    },
    options: {
        title: {
            display: true,
            text: 'Chart of Month',
            fontSize: 32
        },
        legend: {
            position: 'right',
            labels: {
                fontColor: '#000',
                fontSize: 20
            }
        },
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true,
                    stepSize: 1
                }
            }]
        }
    }
});


let show_year = new Chart(charts_year, {
    type: 'bar',
    data: {
        labels: product_name,
        datasets: [{
            barPercentage: 1.0,
            label: 'สินค้าที่นิยมซื้อมากที่สุด',
            data: product_total,
            backgroundColor: color,
            borderWidth: 4,
            borderColor: '#777',
            hoverBorderWidth: 3,
            hoverBorderWidth: '#000',

        }],
    },
    options: {
        title: {
            display: true,
            text: 'Chart of Year',
            fontSize: 32
        },
        legend: {
            position: 'right',
            labels: {
                fontColor: '#000',
                fontSize: 20
            }
        },
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true,
                    stepSize: 1
                }
            }]
        }
    }
});