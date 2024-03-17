
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

```chart
type: line
labels: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]    
series:
  - title: x+10
    data: [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60]
```


```chart
type: line
labels: [2, 3, 4, 5, 6, 7, 8, 9, 10]
series:
  - title: Random
    data: [0.19556915236024186, 0.5440015513914206, 0.7515191933875971, 0.5664808083687602, 0.9521597883888201, 0.1609172202365169, 0.040543510007465144, 0.2841346844280448, 0.6774593060331356]
```

```chart
type: line
labels: [1,2,3,4]
series:
  - title: test
    data: [4,3,2,1]
tension: 1
width: 100%
labelColors: false
fill: false
beginAtZero: false
bestFit: false
bestFitTitle: undefined
bestFitNumber: 0
```
