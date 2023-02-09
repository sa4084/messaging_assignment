import { createStore } from 'vuex'

export default createStore({
  state: {
    isAuthenticated: false,
    token: "",
    isLoading: false,
    sent: [],
    inbox: [],
    email: '',
    prev: 0
  },
  getters: {
  },
  mutations: {
    initializeMessenger(state) {
      if (localStorage.getItem('token')) {
        state.token = localStorage.getItem('token')
        state.isAuthenticated = true
        state.email = localStorage.getItem('email')
      } else {
        state.token = ''
        state.isAuthenticated = false
        state.email = ''
      }
    },
    setSent(state, sent) {
      // console.log(sent)
      state.sent = sent
    },
    setEmail(state, email) {
      // console.log(sent)
      state.email = email
    },
    setInbox(state, inbox) {
      state.inbox = inbox
    },
    setprev(state, prev) {
      state.prev = prev
    },
    removeEmail(state) {
      // state.token = ''
      // state.isAuthenticated = false
      state.email = ''
    },
    setIsLoading(state, status) {
      state.isLoading = status
    },
    setToken(state, token) {
      state.token = token
      state.isAuthenticated = true
    },
    removeToken(state) {
      state.token = ''
      state.isAuthenticated = false
    },
  },
  actions: {
  },
  modules: {
  }
})
