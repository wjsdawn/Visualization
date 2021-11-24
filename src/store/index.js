import { createStore } from 'vuex'

export default createStore({
  state: {
    time:{}
  },
  mutations: {
    ChangeTime(state,msg){
      state.time['start'] = msg.start
      state.time['end'] = msg.end
    }

  },
  actions: {
  },
  modules: {
  }
})
