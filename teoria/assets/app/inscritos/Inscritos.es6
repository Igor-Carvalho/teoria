window.Inscritos = {
  install(Vue, options) {
    Vue.prototype.Inscritos = {
      enroll (dados) {
        return axios.post('/api/v1/inscritos/', dados)
      }
    }
  }
}
