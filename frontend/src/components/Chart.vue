<script>
import { Scatter, mixins } from "vue-chartjs";

const { reactiveProp } = mixins;

export default {
  extends: Scatter,
  // props: ["chartData"],
  mixins: [reactiveProp],
  data() {
    return {
      options: {
        scales: {
          xAxes: [
            {
              type: "linear",
              position: "bottom",
            },
          ],
        },
      },
    };
  },
  mounted() {
    this.renderChart(this.chartData, this.options);
  },
};
</script>

<style>
</style>