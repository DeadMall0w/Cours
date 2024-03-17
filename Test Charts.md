
```dataviewjs
const labels = ['One', 'Two', 'Three'];
const data = [1, 2, 3];

const chartData = {  
    type: 'bar',
    data: {
        labels: labels,
        datasets: [{
            label: 'Numbers',
            data: data
        }]
    }
}

window.renderChart(chartData, this.container);
```

```chart
type: line
labels: [label1, label2, label3, label4]
series:
	- title: Title X
	  data: [2,3,4,5]
	- title: Title Y
	  data: [5,4,3,2]
	- title: Title Z
	  data: [3,5,2,4]
```

```chart
type: line 
labels: [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
series: 
	- title: Fonction Quadratique 
	  data: [100, 81, 64, 49, 36, 25, 16, 9, 4, 1, 0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```
