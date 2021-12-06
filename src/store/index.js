import { createStore } from 'vuex'

export default createStore({
  state: {
    map_status:0,
    time:{
      start:7,
      end:8
    },
    timeFlag:0,
    timeJson:{

    },
    pieFlag:0
  },
  mutations: {
    ChangeTime(state,msg){
      state.time['start'] = msg.start
      state.time['end'] = msg.end
      state.timeFlag = state.timeFlag + 1
      console.log(state.timeFlag)
    },
    ChangeMapStatue(state,msg){
      state.map_status = msg
    },
    ChangeTimeJson(state,msg){
      for(let key in state.timeJson){
        delete state.timeJson[key]
      }
      for(let key in msg){
        state.timeJson[key] = msg[key]
      }
    },
    ChangePieFlag(state,msg){
      state.pieFlag = state.pieFlag + 1
    },
  },
  actions: {
  },
  modules: {
  }
})
