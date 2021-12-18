/*
 * @Author: your name
 * @Date: 2021-12-16 14:38:56
 * @LastEditTime: 2021-12-18 14:54:47
 * @LastEditors: your name
 * @Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
 * @FilePath: \Visualization\src\store\index.js
 */
import { createStore } from 'vuex'

export default createStore({
  state: {
    map_status:0,
    time:{
      start:7,
      end:8
    },
    page:1,
    pauseFlag:false,
    timeFlag:0,
    reqdata:0,
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
