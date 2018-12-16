Vue.component('subscriptionForm', resolve => {
  axios.get('/public/app/inscritos/componentes/subscriptionForm.html').then(response => {
    resolve({
      template: response.data,
      delimiters: ['[[', ']]'],
      data () {
        return {
          dados: {},
          mensagem: ''
        }
      },
      methods: {
        inscrever () {
          this.mensagem = ''
          this.Inscritos.enroll(this.dados).then(response => {
            if (response.data.ativo) {
              this.mensagem = 'Esse email já está cadastrado em nossa base de dados'
            } else {
              const m = `Em email contendo informações para completar o registro foi enviado para ${ response.data.email }`
              this.mensagem = m
            }
          }).catch(response => {
            this.mensagem = response.response.data.email[0];
          });
        }
      },
    })
  })
});
