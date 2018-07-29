window.Contatos = {
  install(Vue, options) {
    Vue.prototype.Contatos = {
      sendEmail (dados) {
        return axios.post('/contatos/enviar/email/contato/', dados);
      }
    }
  }
}
