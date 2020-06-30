<template>
  <div class="sidebar">
      <div class="box">
        <span class="closeIcon" @click="$emit('close')">
            <img src="@/assets/Images/close-white-18dp.svg" alt="Close Sidebar">
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
        </div>
      </div>
  </div>
</template>

<script>
export default {
    name: 'Sidebar',
    computed:{
        filters(){
            return this.$store.getters.filters
        }
    },
    methods:{
        updatePeerReviewed(){
            this.filters.peerReviewed = !this.filters.peerReviewed
            this.updateFilterState()
        },
        updateOnlyCovid(){
            this.filters.onlyCovid = !this.filters.onlyCovid
            this.updateFilterState()
        },
        updateFilterState(){
            this.$store.dispatch('updateFilterState', this.filters)
        }
    }
}
</script>

<style lang="scss" scoped>

//Variables
$dark: #282a2c;
$lightdark: lighten($dark, 5);
$white: whitesmoke;
$border-radius: 20px;

$primary: #9161cf;

.sidebar{
    position: fixed;
    left: 0;
    top: 0;
    height: 100vh;
    width: 100%;
    background-color: darken($dark, 2);

    color: $white;
    overflow-y: hidden;

    .box{
        margin: 2em;
        padding: 1em;
        display: flex;
        flex-direction: column;

        .closeIcon{
            width: fit-content;
            img{
                width: 2em;
            }
        }
    }
}

.filters{
    display: flex;
    flex-direction: column;

    .filter{
        padding: 0.5em 0;

        display: flex;
        justify-content: space-between;
        align-items: center;
    }
}
</style>