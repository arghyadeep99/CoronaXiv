import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    getURL: "http://localhost:5000/?title=",
    filters:{
      peerReviewed: false,
      onlyCovid: false,
      dateRange: null
    },
    count: 0
  },
  getters:{
    filters(state){
      return state.filters
    },
    count(state){
      return state.count
    }
  },
  mutations: {
    updateFilterState(state, payload){
      state.filters = payload
    },
    updateDateRange(state, payload){
      state.filters.dateRange = payload
    },
    incrementCount(state){
      state.count = state.count + 1
    }
  },
  actions: {
    updateFilterState({ commit }, payload){
      commit('updateFilterState', payload)
    },
    incrementCount({ commit }){
      commit('incrementCount')
    }
  },
  modules: {
  }
})
