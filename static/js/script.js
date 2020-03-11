
Chart.defaults.global.defaultFontFamily = 'Itim';
Chart.defaults.global.defaultFontSize = 18;

let charts = document.getElementById('Charts').getContext('2d');
let charts_week = document.getElementById('Charts_week').getContext('2d');
let charts_month = document.getElementById('Charts_month').getContext('2d');
let charts_year = document.getElementById('Charts_year').getContext('2d');


let date = document.getElementById('date').innerHTML;
let count = document.getElementById('count').innerHTML;

let listed_start_to_end = [];
let start_week = document.getElementById('start_week').innerHTML;
let total = document.getElementById('total').innerHTML;
let end_week = document.getElementById('end_week').innerHTML;
let result = document.getElementById('result').innerHTML;

let s_w = start_week.split(' ');
let s_e = end_week.split(' ');

let s_w_w = s_w[1][0] + '' + s_w[1][1];
let s_e_e = s_e[1][0] + '' + s_e[1][1];

let listed_start_to_end_month = [];
let count_month = document.getElementById('count_month').innerHTML;

let listed_start_to_end_year = [];
let count_year = document.getElementById('count_year').innerHTML;

for (let i= Number(s_w_w); i<Number(s_e_e); i++){
    listed_start_to_end.push(s_w[0]+'-' + i + '-' + s_w[2]);
}

for (let i= Number(s_w_w); i<Number(s_w_w)+30; i++){
    if (i > 30){
        listed_start_to_end_month.push(s_w[0]+'-' + (i-30) + '-' + (Number(s_w[2]) + 1));
    }else{
        listed_start_to_end_month.push(s_w[0]+'-' + i + '-' + s_w[2]);
    }
}


let color = [];





for (let i=0;i<10;i++){
    color.push('rgba(255,' + Math.floor(Math.random() * 150) + ',' + Math.floor(Math.random() * 150) + ',' + '0.5)');
}


let show_day = new Chart(charts, {
    type: 'bar',
    data: {
        labels: [date],
        datasets: [{
            barPercentage: 1.0,
            label: 'จำนวนการขายสินค้าทั้งหมดใน 1 วัน',
            data: [count],
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
        labels: listed_start_to_end,
        datasets: [{
            barPercentage: 1.0,
            label: 'ค่าเฉลี่ยการขายสินค้าทั้งหมด',
            data: [result, result/2],
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
        labels: listed_start_to_end_month,
        datasets: [{
            barPercentage: 1.0,
            label: 'ค่าเฉลี่ยการขายสินค้าทั้งหมด',
            data: [count_month, count_month/2],
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
    type: 'line',
    data: {
        labels: [
            'Jan',
            'Fed', 
            'Mar',
            'Apr',
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
            label: 'ค่าเฉลี่ยการขายสินค้าทั้งหมด',
            data: [count_year/2],
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