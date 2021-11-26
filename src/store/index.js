import { createStore } from 'vuex'

export default createStore({
  state: {
    map_status:0,
    time:{
      start:0,
      end:8
    }
  },
  mutations: {
    ChangeTime(state,msg){
      state.time['start'] = msg.start
      state.time['end'] = msg.end
    },
    ChangeMapStatue(state,msg){
      state.map_status = msg
    }

  },
  actions: {
  },
  modules: {
  }
})
