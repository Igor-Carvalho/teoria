Vue.component('contatoForm', resolve => {
  axios.get('/public/app/contato/componentes/contatoForm.html').then(response => {
    resolve({
      template: response.data,
      delimiters: ['[[', ']]'],
      data: function () {
        return {
          dados: {nome:'', email:'', website:'', local:'', assunto:'', mensagem:''}
        }
      },
      methods: {
        enviarEmail() {
          this.$validator.validate().then(semErros => {
            if (semErros) {
              this.Contatos.sendEmail(this.dados).then(response => {
                this.$toaster.success('Email enviado com sucesso!')
                this.dados = {nome:'', email:'', website:'', local:'', assunto:'', mensagem:''}
                this.$validator.reset()
              })
            } else {
              this.$toaster.error('Preencha os campos do formulário')
            }
          })
        }
      }
    })
  })
})
