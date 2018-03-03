Vue.component('subscriptionForm', {
  delimiters: ['[[', ']]'],
  data: function () {
    return {
      dados: {},
      mensagem: ''
    }
  },
  methods: {
    inscrever() {
      var self = this;
      self.mensagem = '';
      self.enroll(self.dados).then(sucesso, erro);

      function sucesso(inscrito) {
        if (inscrito.body.ativo) {
          self.mensagem = 'Esse email já está cadastrado em nossa base de dados';
        } else {
          self.mensagem = `Em email contendo informações para completar o registro foi enviado para ${ inscrito.body.email }`;
        }
      }

      function erro() {
        self.mensagem = 'Erro ao adicionar email';
      }
    }
  },
  template: `<form id="mc-form" name="mcForm" novalidate>
<div class="subscribe-form margin-top-20">
  <input id="mc-email" name="email" type="email" placeholder="Endereço de Email" class="text-input" v-model="dados.email" v-validate="'required|email'">
  <button class="submit-btn" type="submit" :disabled="errors.any()" @click.prevent="inscrever()">Inscrever</button>
</div>

<p>Inscreva-se no nosso boletim de notícias</p>
<label for="mc-email" class="mc-label">[[ mensagem ]]</label>
</form>`
});
