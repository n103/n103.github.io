---
layout: post
---
d
<div id='myDiv'>
<!-- Plotly chart will be drawn inside this DIV -->
</div>
<script> src="{{base}}/assets/tod.js </script>
<script>

        
        var log = {
            x: data['source'],
            y: data['target'],
            text: data['text'],

            mode: 'markers',
            marker: {
                size: data['valueLog'],
                color: data['color']
            }
        };

        var config = [log];

        var layout = {
            title: 'Todeszahlen Deutschland 2019',
            showlegend: false,
            height: 1800,
            //width: 1400,
            autosize: true,
            margin: {
                l: 310
            }

        };

        Plotly.newPlot('myDiv', config, layout);

</script>
{% comment %}
Might you have an include in your theme? Why not try it here!
{% include my-themes-great-include.html %}
{% endcomment %}

No laudem altera adolescens has, volumus lucilius eum no. Eam ei nulla audiam efficiantur. Suas affert per no, ei tale nibh sea. Sea ne magna harum, in denique scriptorem sea, cetero alienum tibique ei eos. Labores persequeris referrentur eos ei.
