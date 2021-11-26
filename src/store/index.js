import { createStore } from 'vuex'

export default createStore({
  state: {
    dd:0,
    time:{
      start:0,
      end:8
    }
  },
  mutations: {
    ChangeTime(state,msg){
      state.time['start'] = msg.start
      state.time['end'] = msg.end
      state.dd = state.dd + 1
    }

  },
  actions: {
  },
  modules: {
  }
})
