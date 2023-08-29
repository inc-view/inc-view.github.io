// Função para atualizar o número em um elemento HTML
function updateNumber(elementId, number) {
    const element = document.getElementById(elementId);
    if (element) {
        element.textContent = number;
    }
}

// Exemplo de uso para atualizar os números (substitua os números de exemplo pelos números desejados)
updateNumber('applicationsNumber', "R$"+2.8 + "M"); // Atualiza "Applications" para 3000
updateNumber('shortlistedNumber', "COMPLETO"); // Atualiza "Shortlisted" para 6000
updateNumber('peopleNumber', "+R$"+ 1.5 + "M"); // Atualiza "People" para 4500


var chart    = document.getElementById('chart').getContext('2d'),
    gradient = chart.createLinearGradient(0, 0, 0, 450);

gradient.addColorStop(0, 'rgba(0, 199, 214, 0.32)');
gradient.addColorStop(0.3, 'rgba(0, 199, 214, 0.1)');
gradient.addColorStop(1, 'rgba(0, 199, 214, 0)');


var data  = {
    labels: [ 'Janeiro', 'Fevereiro', 'Marco', 'Abril', 'Maio', 'Junho', 'Julho','Agosto','Setembro','Outubro', 'Novembro','Deezembro' ],
    datasets: [{
			label: 'Applications',
			backgroundColor: gradient,
			pointBackgroundColor: '#00c7d6',
			borderWidth: 1,
			borderColor: '#0e1a2f',
			data: [5000, 6000, 8000, 10000, 9500, 13000,14600,16400,13000,17000,18500,20500]
    }]
};

var options = {
	responsive: true,
	maintainAspectRatio: true,
	animation: {
		easing: 'easeInOutQuad',
		duration: 520
	},
	scales: {
		yAxes: [{
      ticks: {
        fontColor: '#5e6a81'
      },
			gridLines: {
				color: 'rgba(200, 200, 200, 0.08)',
				lineWidth: 1
			}
		}],
    xAxes:[{
      ticks: {
        fontColor: '#5e6a81'
      }
    }]
	},
	elements: {
		line: {
			tension: 0.4
		}
	},
	legend: {
		display: false
	},
	point: {
		backgroundColor: '#00c7d6'
	},
	tooltips: {
		titleFontFamily: 'Poppins',
		backgroundColor: 'rgba(0,0,0,0.4)',
		titleFontColor: 'white',
		caretSize: 5,
		cornerRadius: 2,
		xPadding: 10,
		yPadding: 10
	}
};

var chartInstance = new Chart(chart, {
    type: 'line',
    data: data,
		options: options
});

// document.querySelector('.open-right-area').addEventListener('click', function () {
//     document.querySelector('.app-right').classList.add('show');
// });

// document.querySelector('.close-right').addEventListener('click', function () {
//     document.querySelector('.app-right').classList.remove('show');
// });

// document.querySelector('.menu-button').addEventListener('click', function () {
//     document.querySelector('.app-left').classList.add('show');
// });

// document.querySelector('.close-menu').addEventListener('click', function () {
//     document.querySelector('.app-left').classList.remove('show');
// });


// status

function setStatusColor(id) {
	const statusElement = document.getElementById("status");
	const resultadoElement = document.getElementById("resultado-status");
	switch (id) {
	  case "entregue":
		statusElement.style.background = "green";
		resultadoElement.textContent = "Online";
		resultadoElement.style.color = "white";   
		break;
	  case "em_analise":
		statusElement.style.background = "yellow";
		resultadoElement.textContent = "Em Análise";
		resultadoElement.style.color = "white";
		break;
	  case "processamento":
		statusElement.style.background = "red";
		resultadoElement.textContent = "Offline";
		resultadoElement.style.color = "white";
	
		break;
	  default:
		statusElement.style.background = "gray";
		resultadoElement.textContent = "Desconhecido";
		resultadoElement.style.color = "white";
	}
  }
  
  // Defina o ID do status desejado aqui
  const statusId = "entregue"; // Pode ser "entregue", "em_analise" ou "processamento"
  setStatusColor(statusId);

  // Status_usuario

  function setStatusColor(id) {
	const statusElement = document.getElementById("Status_usuario");
	const resultadoElement = document.getElementById("result-status");
	switch (id) {
	  case "Alerta":
		statusElement.style.background = "green";
		resultadoElement.textContent = "Online";
		resultadoElement.style.color = "white";   
		break;
	  case "Normal":
		statusElement.style.background = "red";
		resultadoElement.textContent = "Em Análise";
		resultadoElement.style.color = "white";
		break;
	  default:
	}
  }