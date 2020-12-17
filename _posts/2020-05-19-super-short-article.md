---
layout: post
title: "Some articles are just so short that we have to make the footer stick"
categories: misc
---
  
<p>
  <label for="nRadius" 
         style="display: inline-block; width: 240px; text-align: right">
         radius = <span id="nRadius-value">…</span>
  </label>
  <input type="range" min="1" max="150" id="nRadius">
</p>

<script>

var width = 600;
var height = 300;
 
var holder = d3.select("body")
      .append("svg")
      .attr("width", width)    
      .attr("height", height); 

// draw the circle
holder.append("circle")
  .attr("cx", 300)
  .attr("cy", 150) 
  .style("fill", "none")   
  .style("stroke", "blue") 
  .attr("r", 120);

// when the input range changes update the circle 
d3.select("#nRadius").on("input", function() {
  update(+this.value);
});

// Initial starting radius of the circle 
update(120);

// update the elements
function update(nRadius) {

  // adjust the text on the range slider
  d3.select("#nRadius-value").text(nRadius);
  d3.select("#nRadius").property("value", nRadius);

  // update the circle radius
  holder.selectAll("circle") 
    .attr("r", nRadius);
}

</script>