Vue.prototype.enroll = function (dados) {
  return Vue.http.post('/api/v1/inscritos/', dados);
}