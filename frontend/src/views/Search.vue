<template>
  <div>
    <div class="navbar">
      <span class="icon" @click="sidebarOpen = !sidebarOpen">
        <img src="@/assets/Images/menu-white-18dp.svg" alt="Menu" />
      </span>
      <form @submit.prevent="search()" class="navSearch">
        <input
          type="text"
          placeholder="Search"
          :style="(error) ? 'color:crimson' : 'color:white'"
          name="searchString"
          id="searchString"
          v-model="searchString"
          required
        />
      </form>
    </div>

    <transition name="slide">
      <Sidebar v-show="sidebarOpen" @close="sidebarOpen = false" />
    </transition>

    <div class="two-grid">
      <div class="left-container">
        <div class="chart">
          <h1>Chart</h1>
          <Chart
            :chartData="{
          labels: ['x', 'y'],
          datasets: datasets
        }"
          />
        </div>
      </div>

      <div class="container">
        <!-- <h3>{{ $store.getters.count }}</h3> -->

        <h3>{{ (!papers.length && !loading) ? "No results" : "" }}</h3>
        <SkeletonCards v-if="loading" />
        <div v-else>
          <paginate
            v-if="papers.length"
            :page-count="2"
            v-model="page"
            :click-handler="paginateCallback"
            :prev-text="'<span class=\'side-btn prev-btn\'>Prev</span>'"
            :next-text="'<span class=\'side-btn next-btn\'>Next</span>'"
            :container-class="'pagination-container'"
            :page-class="'page-item'"
          ></paginate>

          <div class="cards">
            <Card
              v-for="paper in finalPapers"
              :paper="paper"
              :key="paper._source.id + paper._source.title"

              :datasets="datasets"
            />
          </div>

          <paginate
            v-if="papers.length"
            :page-count="2"
            v-model="page"
            :click-handler="paginateCallback"
            :prev-text="'<span class=\'side-btn prev-btn\'>Prev</span>'"
            :next-text="'<span class=\'side-btn next-btn\'>Next</span>'"
            :container-class="'pagination-container'"
            :page-class="'page-item'"
          ></paginate>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Card from "@/components/Card";
import SkeletonCards from "@/components/SkeletonCards";
import Sidebar from "@/components/Sidebar";
import Chart from "@/components/Chart.vue";

import axios from "axios";

export default {
  name: "Search",
  components: {
    Card,
    SkeletonCards,
    Sidebar,
    Chart,
  },
  data: () => ({
    page: 1,
    searchString: "",
    papers: [],
    finalPapers: [],
    error: false,
    loading: false,
    sidebarOpen: false,
  }),
  computed: {
    datasets() {
      let datasets = [
        {
          label: "Drug testing",
          backgroundColor: "white",
          data: [],
        },
        {
          label: "Covid Outbreak",
          backgroundColor: "#e9f74d",
          data: [],
        },
        {
          label: "Detection",
          backgroundColor: "#36c954",
          data: [],
        },
        {
          label: "Treatments",
          backgroundColor: "#517fc9",
          data: [],
        },
        {
          label: "Genetic Studies",
          backgroundColor: "purple",
          data: [],
        },
        {
          label: "Transmission",
          backgroundColor: "#d13737",
          data: [],
        },
        {
          label: "Crisis Management",
          backgroundColor: "teal",
          data: [],
        },
        {
          label: "Immunity Studies",
          backgroundColor: "orange",
          data: [],
        },
      ];

      this.papers.forEach((paper) => {
        datasets[paper._source.cluster].data.push({
          x: paper._source.x1,
          y: paper._source.x2,
        });
      });

      return datasets;
    },
  },
  watch: {
    $route: "callAPI",
  },
  methods: {
    search() {
      if (
        this.searchString.toLowerCase() == this.$route.query.q.toLowerCase()
      ) {
        this.error = true;
        setTimeout(() => {
          this.error = false;
        }, 1000);
      } else {
        this.$router.push({
          path: "/search",
          query: {
            q: this.searchString,
          },
        });
      }
    },

    paginateCallback(pageNum) {
      if (pageNum == 1) {
        this.finalPapers = this.papers.slice(0, this.papers.length / 2);
      } else if (pageNum == 2) {
        //Don't know why but papers.length - 1 gives a result less and papers.length is perfect.
        //Indexing in slice hmm
        this.finalPapers = this.papers.slice(
          this.papers.length / 2,
          this.papers.length
        );
      }
    },

    callAPI() {
      this.searchString = this.$route.query.q;
      let url = this.$store.state.getURL + this.searchString;

      this.loading = true;

      axios.get(url).then((response) => {
        this.papers = response.data.data.hits.hits;

        //Reset pagination
        this.paginateCallback(1);
        this.page = 1;

        this.loading = false;

        console.log(this.papers);
        // this.buildChart(this.papers);
      });
    },

    // buildChart(papers) {
    //   this.dataForChart = [];
    //   papers.forEach((paper) => {
    //     this.dataForChart.push({
    //       x: paper._source.x1,
    //       y: paper._source.x2,
    //     });
    //   });
    // },
  },
  mounted() {
    if (this.$route.query.q == "" || this.$route.query.q == null)
      this.$route.push("/");
    else this.callAPI();
  },
};
</script>

<style lang="scss">
//Variables
$dark: #282a2c;
$lightdark: lighten($dark, 5);
$white: whitesmoke;
$border-radius: 20px;

.navbar {
  display: flex;
  justify-content: space-evenly;
  align-items: center;

  padding: 1em;

  .icon {
    width: 20%;
    display: flex;
    justify-content: center;
    align-items: center;

    img {
      width: 2em;
    }
  }

  .navSearch {
    width: 70%;
    margin-right: 2em;
    height: 2.8em;

    input {
      background-color: $lightdark;
      color: $white;
      border: none;
      height: 100%;
      width: 100%;
      padding: 0 1em;
      font-weight: bold;

      &:focus {
        outline: none !important;
      }
    }
  }
}

.container {
  color: $white;
  margin: 1em 2em;
}

.left-container {
  margin: 2em 3em 3em;
  color: $white;
}

.pagination-container {
  margin: 1em 2em;
  width: calc(100% - 4em);

  display: flex;
  align-items: center;
  justify-content: center;

  list-style-type: none;

  li a {
    &:focus {
      outline: none;
    }
  }
}
.page-item {
  padding: 1em 1.5em;
  background-color: $lightdark;
}
.page-item.active {
  background-color: lighten($lightdark, 5);
}
.side-btn {
  padding: 1em 1.5em;
  background-color: darken($lightdark, 1);
}
.prev-btn {
  border-top-left-radius: $border-radius;
  border-bottom-left-radius: $border-radius;
}
.next-btn {
  border-top-right-radius: $border-radius;
  border-bottom-right-radius: $border-radius;
}

//Sidebar transition
.slide-enter-active,
.slide-leave-active {
  transition: all 0.4s ease-in-out;
}
.slide-enter,
.slide-leave-to {
  transform: translateX(-100%) scaleX(0);
}

//Horizontal Scrolling for Mobile. Decided not to implement it
// @media only screen and (max-width: 768px){
//   body{
//     font-size: 12px;
//   }
//   .cards{
//     // overflow-x: scroll;
//     // overflow-y: hidden;
//     // white-space: nowrap;

//     display: flex;
//     flex-wrap: nowrap;
//     overflow-x: auto;

//     //For iOS
//     -webkit-overflow-scrolling: touch;
//   }
// }

@media only screen and (min-width: 768px) {
  .navbar {
    display: flex;
    justify-content: start;
    .icon {
      cursor: pointer;
      width: fit-content;
      margin: 0 2em;
    }
    .navSearch {
      width: 100%;
    }
  }

  .two-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
  }

  .chart {
    position: fixed;
    width: 35vw;
  }
}
</style>