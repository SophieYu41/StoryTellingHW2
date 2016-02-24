var ws = new WebSocket("ws://localhost:8080");

//function draw
// Get message from websocket and parse data, add new data to the graph and send alert if it
// triggers the condition that Trump has surpassed Clinton
ws.onmessage = function draw(msg) {
  data = msg.data;
  console.log(data);
  obj = JSON.parse(data);
  if(data) {
    time = obj['time'];
    rate_trump = obj['rate_trump'];
    rate_clinton = obj['rate_clinton'];  
    addData(time, rate_trump, true);
    addData(time, rate_clinton, false);
    if(rate_trump > rate_clinton) {
      send_alert(time, rate_trump-rate_clinton);
    }
  }
};

// Defind data point and layout for the graph
var data_x_trump = [];
var data_y_trump = [];
var data_x_clinton = [];
var data_y_clinton = [];

var layout = {
  xaxis: {
    title: 'time'
  },
  yaxis: {
    title: 'number'
  },
  margin: {
    t: 0
  },
  hovermode: 'closest'
};

// Append new data point on the graph. Set maximum 10 data points
//on the graph
function addData(x, y, isTrump) {
  if(isTrump) {
    data_x_trump.push(x);
    data_y_trump.push(y);
    if(data_x_trump.length > 10) {
      data_x_trump.shift();
      data_y_trump.shift();    
    }
  } else {
    data_x_clinton.push(x);
    data_y_clinton.push(y);
    if(data_x_clinton.length > 10) {
      data_x_clinton.shift();
      data_y_clinton.shift();    
    }
    console.log(data_x_clinton);
    console.log(data_y_clinton);
  }
  redraw();
}

// redraw function to refresh the graph
function redraw() {
  console.log("redraw");
  var data = [
    {
      x: data_x_trump,
      y: data_y_trump,
      name: 'Trump'
    },
    {
      x: data_x_clinton,
      y: data_y_clinton,
      name: 'Clinton'
    }
  ];
  Plotly.newPlot('graph', data, layout);
}

// If the rate triggers the alert, we prepend a message to the message queue
function send_alert(time, diff) {
  $('.messageBox').show(); 
    setTimeout(function() {
        $('.messageBox').hide();
    }, 2000);
  $('#alert').prepend('<li>' + '@ ' + time + ', Hillary Clinton is surpassed by Donald Trump by ' + diff + '</li>')
}
