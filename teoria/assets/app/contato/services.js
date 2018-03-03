Vue.prototype.sendEmail = function (dados) {
  return Vue.http.post('/contatos/enviar/email/contato/', dados);
}
