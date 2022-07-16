function Asciiplot(x1,y1,x2,y2) {
	// Initialise the size of the plot on the graph and the contents of the graph.
	var plotsize = 20;
	var plotgraph = "";

	// Initialise the counters and variables.
	var county;
	var countx;
	var l;
	var HasDrawnOne = 0;
	// The coefficient.
	var m;
	m = (y2 - y1)/(x2 - x1);
	// The y intercept.
	var c;
	c = y1 - m*x1;
	// Loop for the size of the plotsize and create the graph.
	// This could also alternatively be done by specifying an array containing strings of numbers. The end result will involve converting back from the array into text, so may as well do it directly.
	for(county = 0; county < plotsize; county++) {
		for(countx = 0; countx < plotsize; countx++) {

			if(((countx == x1) && (county == y1)) || ((countx == x2) && (county == y2))) {
				plotgraph += "O";
			} else if (
				// Work out if we're in the linear regression between the two points. Checks for if countx has exceeded the threshold of the limits of rounding to ensure that at least one * is drawn per line, otherwise there can be disconnections with the line in ASCII art for really steep regressions.
				((Math.round(m*countx + c) == county)
				 || ( countx > ((county - c)/m)))
				 && (countx <= Math.max(x1,x2) && countx >= Math.min(x1,x2))
				 && (county <= Math.max(y1,y2) && county >= Math.min(y1,y2))
				 && (HasDrawnOne == 0)
			)
			{
				plotgraph += "*";
				HasDrawnOne = 1;
			} else {
				plotgraph += "-";
			}
		}
		plotgraph += "<br />";
		HasDrawnOne = 0;
	}

	return plotgraph;
}
