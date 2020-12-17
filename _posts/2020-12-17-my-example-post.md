---
layout: post
---
<script>
    src='https://cdn.plot.ly/plotly-latest.min.js'
        Plotly.d3.json('tod.json', function(fig) {

            var data = {
                type: "sankey",
                domain: {
                    x: [0, 1],
                    y: [0, 1]
                },
                orientation: "h",
                valueformat: ".0f",
                node: {
                    pad: 15,
                    thickness: 15,
                    line: {
                        color: "black",
                        width: 0.5
                    },
                    label: fig.data[0].node.label,
                    color: fig.data[0].node.color
                },

                link: {
                    source: fig.data[0].link.source,
                    target: fig.data[0].link.target,
                    value: fig.data[0].link.value,
                    label: fig.data[0].link.label
                }
            }

            var data = [data]

            var layout = {
                //width: 2000,
                height: 5500,
                autosize: true,
                font: {
                    size: 10
                }
            }

            Plotly.newPlot('myDiv', data, layout)
        });
</script>
{% comment %}
Might you have an include in your theme? Why not try it here!
{% include my-themes-great-include.html %}
{% endcomment %}

No laudem altera adolescens has, volumus lucilius eum no. Eam ei nulla audiam efficiantur. Suas affert per no, ei tale nibh sea. Sea ne magna harum, in denique scriptorem sea, cetero alienum tibique ei eos. Labores persequeris referrentur eos ei.
