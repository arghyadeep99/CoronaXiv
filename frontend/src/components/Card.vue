<template>
  <div class="card" v-if="show">
    <!-- {{ this.paper._source.peer_reviewed }}
    {{ this.paper._source.is_covid }}-->
    <div
      class="cluster-name"
      :style="'background-color: ' + datasets[paper._source.cluster].backgroundColor"
    >{{ paper._source.cluster_name }}</div>
    <h1 class="card-title">{{ paper._source.title }}</h1>
    <h2 class="card-subtitle">{{ paper._source.authors }}</h2>
    <div class="content">
      <p>{{ paper._source.excerpt }}</p>
    </div>
    <div class="keywords">
      <span class="keyword" v-for="keyword in keywords" :key="keyword">{{keyword}}</span>
    </div>
    <div class="card-footer">
      <a :href="finalUrl" target="_blank">
        <button class="button">Visit</button>
      </a>
      <span class="date">{{ paper._source.publish_time }}</span>
    </div>
  </div>
</template>

<script>
export default {
  name: "Card",
  props: {
    paper: {
      type: Object,
      required: true,
    },
    datasets: {
      type: Array,
      required: false,
    },
  },
  computed: {
    keywords() {
      let keywords = this.paper._source.keywords;
      keywords = keywords
        .slice(0, -1)
        .slice(1, -1)
        .replace(/'/g, "")
        .split(",");

      return keywords;
    },
    finalUrl() {
      let url = this.paper._source.url;
      let semicolonIndex = url.indexOf(";");
      return url.slice(0, semicolonIndex);
    },
    filters() {
      return this.$store.getters.filters;
    },
    show() {
      console.log("State of show changed");

      let peerReviewed = this.paper._source.peer_reviewed;
      let onlyCovid = this.paper._source.is_covid;
      let date = new Date(this.paper._source.publish_time);

      let show = true;

      if (this.filters.peerReviewed && peerReviewed == "False") show = false;
      else if (this.filters.onlyCovid && onlyCovid == "False") show = false;
      else if(this.filters.dateRange != null){
        let start = new Date(this.filters.dateRange.start)
        let end = new Date(this.filters.dateRange.end)
        
        console.log(start.getTime() + " " + end.getTime())
        console.log(date.getTime())

        if(date.getTime() > end.getTime() || date.getTime() < start.getTime()) show = false;
      }

      return show;

      // if (
      //   (this.filters.peerReviewed == true && peerReviewed == "False") ||
      //   (this.filters.onlyCovid == true && onlyCovid == "False")
      // )
      //   return false;
      // else {
      //   return true;
      // }
    },
  },
};
</script>

<style lang="scss">
//Variables
$dark: #282a2c;
$lightdark: lighten($dark, 5);
$white: whitesmoke;
$border-radius: 20px;

$primary: #9161cf;

.card {
  background-color: $lightdark;
  padding: 2em;
  border-radius: $border-radius;
  margin-bottom: 1em;

  .cluster-name {
    width: fit-content;
    padding: 0.5em 1em;
    margin-bottom: 1em;
    color: $dark;
    font-size: 0.8em;
    font-weight: bold;
    border-radius: $border-radius;
  }
  .card-title {
    font-size: 1.6em;
    margin-bottom: 0.25em;
  }
  .card-subtitle {
    font-size: 1em;
    color: $primary;
  }
  .content {
    margin-top: 1em;
  }
  .keywords {
    margin-top: 1em;
    display: flex;
    align-items: center;
    flex-wrap: wrap;
    .keyword {
      margin: 0.5em 0.2em 0;
      color: $dark;
      font-weight: bold;
      font-size: 0.9em;
      background-color: $primary;
      padding: 0.1em 0.5em;
      border-radius: $border-radius;
    }
  }
  .card-footer {
    margin-top: 1.5em;
    display: flex;
    justify-content: space-between;
    align-items: center;

    .button {
      border-radius: $border-radius;
      padding: 0.8em 1.5em;
      background: $primary;
      border: none;
      font-weight: bold;
      cursor: pointer;

      &:focus {
        outline: none !important;
      }
    }

    .date {
      color: lighten($primary, 10);
      font-weight: bold;
    }
  }
}

//Horizontal Scrolling for Mobile. Decided not to implement it
// @media only screen and (max-width: 768px){
//     .card{
//         display: inline-block;
//         width: 50vw;
//         margin-right: 1em;

//         height: 100%;

//         // white-space: pre-line;
//         // .content{
//         //     width: 80%;
//         // }

//         flex: auto 0 0;
//     }
// }

@media only screen and (min-width: 768px) {
  .card {
    padding: 2em 3em;
  }
}
</style>