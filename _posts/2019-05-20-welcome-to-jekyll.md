---
layout: post
---
he
<svg></svg>
hu
<div id="text"></div>
<script>
    var vWidth = 300;
    var vHeight = 300;
    var vRadius = Math.min(vWidth, vHeight) / 2;
    var vColor = d3.scaleOrdinal(d3.schemeCategory20b);
    var vData = {
        'id': 'TOPICS', 'children': [{
            'id': 'Topic A',
            'children': [{'id': 'Sub A1', 'size': 4}, {'id': 'Sub A2', 'size': 4}]
        }, {
            'id': 'Topic B',
            'children': [{'id': 'Sub B1', 'size': 3}, {'id': 'Sub B2', 'size': 3},
                {'id': 'Sub B3', 'size': 3}]
        }, {
            'id': 'Topic C',
            'children': [{'id': 'Sub C1', 'size': 4}, {'id': 'Sub C2', 'size': 4}]
        }]};

    // Prepare our physical space
    var g = d3.select('svg')
        .attr('width', vWidth).attr('height', vHeight)
        .append('g')
        .attr('transform', 'translate(' + vWidth / 2 + ',' + vHeight / 2 + ')');

    // Declare d3 layout
    var vLayout = d3.partition().size([2 * Math.PI, vRadius]);
    var vArc = d3.arc()
        .startAngle(function (d) { return d.x0; })
        .endAngle(function (d) { return d.x1; })
        .innerRadius(function (d) { return d.y0; })
        .outerRadius(function (d) { return d.y1; });

    // Layout + Data
    var vRoot = d3.hierarchy(vData).sum(function (d) { return d.size });
    var vNodes = vRoot.descendants();
    vLayout(vRoot);
    var vSlices = g.selectAll('path').data(vNodes).enter().append('path');

    // Draw on screen
    vSlices.filter(function(d) { return d.parent; })
        .attr('d', vArc)
        .style('stroke', '#fff')
        .style('fill', function (d) {
            return vColor((d.children ? d : d.parent).data.id); });
</script>
