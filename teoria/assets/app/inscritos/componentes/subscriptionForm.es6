Vue.component('subscriptionForm', {
  template: `<form id="mc-form" name="mcForm" novalidate>
<div class="subscribe-form margin-top-20">
  <input id="mc-email" name="email" type="email" placeholder="Endereço de Email" class="text-input"
      v-model="dados.email" v-validate.initial="'required|email'">
  <button class="submit-btn" type="submit" :disabled="errors.any()" @click.prevent="inscrever()">Inscrever</button>
</div>

<p>Inscreva-se no nosso boletim de notícias</p>
<label for="mc-email" class="mc-label">[[ mensagem ]]</label>
</form>`,
  delimiters: ['[[', ']]'],
  data: function () {
    return {
      dados: {},
      mensagem: ''
    }
  },
  methods: {
    inscrever() {
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
});
