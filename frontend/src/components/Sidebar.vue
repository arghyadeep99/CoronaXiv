<template>
  <div class="sidebar">
    <div class="box">
      <span class="closeIcon" @click="$emit('close')">
        <img src="@/assets/Images/close-white-18dp.svg" alt="Close Sidebar" />
      </span>

      <h1 style="margin: 1em 0">Filters</h1>

      <div class="filters">
        <div class="filter">
          <b>Peer reviewed:</b>
          <toggle-button
            :color="{
                        checked: '#9161cf',
                        unchecked: '#676768'
                    }"
            :value="filters.peerReviewed"
            :sync="true"
            :labels="{checked: 'Yes', unchecked: 'No'}"
            @change="updatePeerReviewed"
          />
        </div>

        <div class="filter">
          <b>Show only covid-19 papers:</b>
          <toggle-button
            :color="{
                        checked: '#9161cf',
                        unchecked: '#676768'
                    }"
            :value="filters.onlyCovid"
            :sync="true"
            :labels="{checked: 'Yes', unchecked: 'No'}"
            @change="updateOnlyCovid"
          />
        </div>

        <div style="padding: 0.5em 0">
          <div class="filter">
            <b>Date range:</b>
            <button class="button" @click="() => dateRange = null">Clear</button>
          </div>

          <!-- Somehow it doesn't work without this being called somewhere, so it's hidden -->
          <span hidden>{{ finalDateRange }}</span>

          <v-date-picker mode="range" color="purple" v-model="dateRange" is-dark is-inline />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Sidebar",
  data() {
    return {
      dateRange: this.$store.getters.filters.dateRange,
    };
  },
  computed: {
    filters() {
      return this.$store.getters.filters;
    },
    finalDateRange() {
      if (this.dateRange != null) {
        let final = {
          start: this.convertDate(this.dateRange.start),
          end: this.convertDate(this.dateRange.end),
        };
        this.$store.commit("updateDateRange", final);
        return final;
      } else {
        this.$store.commit("updateDateRange", null);
        return null;
      }
    },
  },
  methods: {
    updatePeerReviewed() {
      this.filters.peerReviewed = !this.filters.peerReviewed;
      this.updateFilterState();
    },
    updateOnlyCovid() {
      this.filters.onlyCovid = !this.filters.onlyCovid;
      this.updateFilterState();
    },
    updateFilterState() {
      this.$store.dispatch("updateFilterState", this.filters);
    },
    convertDate(date) {
      date = new Date(date)
      let day = date.getDate();
      if (day < 10) {
        day = "0" + day;
      }
      let month = date.getMonth() + 1;
      if (month < 10) {
        month = "0" + month;
      }
      let year = date.getFullYear();
      return year + "-" + month + "-" + day;
    },
  },
};
</script>

<style lang="scss" scoped>
//Variables
$dark: #282a2c;
$lightdark: lighten($dark, 5);
$white: whitesmoke;
$border-radius: 20px;

$primary: #9161cf;

.sidebar {
  position: fixed;
  left: 0;
  top: 0;
  height: 100vh;
  width: 100%;
  background-color: darken($dark, 2);
  z-index: 10;

  color: $white;
  overflow-y: hidden;

  .box {
    margin: 2em;
    padding: 1em;
    display: flex;
    flex-direction: column;

    .closeIcon {
      width: fit-content;
      img {
        width: 2em;
      }
    }
  }
}

.filters {
  display: flex;
  flex-direction: column;

  .filter {
    padding: 0.5em 0;

    display: flex;
    justify-content: space-between;
    align-items: center;
  }
}

.button {
  border-radius: $border-radius;
  padding: 0.5em 0.8em;
  background: $primary;
  border: none;
  font-weight: bold;
  cursor: pointer;

  &:focus {
    outline: none !important;
  }
}

@media only screen and (min-width: 768px) {
  .sidebar {
    width: 30%;

    .box {
      .closeIcon {
        cursor: pointer;
      }
    }
  }
}
</style>