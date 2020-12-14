<template>
  <div>
    <section>
      <div class="box">
        <h1 class="logo">CoronaXiv</h1>
        <div class="searchBox">
          <span class="material-icon">
            <img src="@/assets/Images/search-white-18dp.svg" alt="Search">
          </span>
          <form @submit.prevent="search()">
            <input type="text" placeholder="Search" v-model="searchString" @focus="footer = false" @blur="footer = true" required>
          </form>
        </div>
      </div>

      <!-- Removing footer on input focus for mobile devices -->
      <footer v-if="footer">
        CoronaXiv is an ElasticSearch-powered AI Search Engine that indexes the thousands of research papers that have piled up in response to the Corona Virus pandemic and illustrates various visualizations.
      </footer>
    </section>
  </div>
</template>

<script>
export default {
  name: 'Home',
  data: function(){
    return{
      searchString: '',
      footer: true
    }
  },
  methods:{
    search(){
      this.$router.push({
        path: '/search',
        query: {
          q: this.searchString
        }
      })
    }
  }
}
</script>

<style lang="scss">
@import '@/assets/style.scss'
</style>