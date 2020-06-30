<template>
  <div class="card" v-if="show">
      <!-- {{ this.paper._source.peer_reviewed }}
      {{ this.paper._source.is_covid }} -->
      <h1 class="card-title">{{ paper._source.title }}</h1>
      <h2 class="card-subtitle">{{ paper._source.authors }}</h2>
      <div class="content">
          <p>
            {{ paper._source.excerpt }}
          </p>
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
    name: 'Card',
    props:{
        paper:{
            type: Object,
            required: true
        }
    },
    computed:{
        finalUrl(){
            let url = this.paper._source.url
            let semicolonIndex = url.indexOf(";")
            return url.slice(0, semicolonIndex)
        },
        filters(){
            return this.$store.getters.filters
        },
        show(){
            console.log("State of show changed")

            let peerReviewed = this.paper._source.peer_reviewed
            let onlyCovid = this.paper._source.is_covid

            if(
                (this.filters.peerReviewed == true && peerReviewed == "False") ||
                (this.filters.onlyCovid == true && onlyCovid == "False")
            ) return false
            else {
                return true
            }
        }
    }
}
</script>

<style lang="scss">
//Variables
$dark: #282a2c;
$lightdark: lighten($dark, 5);
$white: whitesmoke;
$border-radius: 20px;

$primary: #9161cf;

.card{
    background-color: $lightdark;
    padding: 2em;
    border-radius: $border-radius;
    margin-bottom: 1em;

    .card-title{
        font-size: 1.5em;
        margin-bottom: 0.25em;
    }
    .card-subtitle{
        font-size: 1em;
        color: $primary;
    }
    .content{
        margin-top: 1em;
    }
    .card-footer{
        margin-top: 1.5em;
        display: flex;
        justify-content: space-between;
        align-items: center;

        .button{
            border-radius: $border-radius;
            padding: 0.8em 1.5em;
            background: $primary;
            border: none;
            font-weight: bold;
            cursor: pointer;

            &:focus{
                outline: none !important;
            }
        }

        .date{
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
</style>