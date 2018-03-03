Vue.component('contatoForm', {
  delimiters: ['[[', ']]'],
  data: function () {
    return {
      dados: {}
    }
  },
  methods: {
    enviarEmail() {
      var self = this;
      this.sendEmail(self.dados).then(sucesso);

      function sucesso() {
        self.$toaster.success('Email enviado com sucesso!');
        self.dados = {};
      }
    }
  },
  template: `<form name="contatoForm" novalidate>
  <div class="col-sm-6">
    <div class="form-group">
      <span v-show="errors.has('nome:required')" class="danger">Este campo é requerido</span>
      <input type="text" id="name" name="nome" class="form-control" placeholder="Seu nome (requerido)" v-model="dados.nome" v-validate.initial="'required'" autofocus>
    </div>
  </div>

  <div class="col-sm-6">
    <div class="form-group">
      <span v-show="errors.has('email:required')" class="danger">Este campo é requerido</span>
      <span v-show="errors.has('email:email')" class="danger">Email inválido</span>
      <input type="text" id="email" name="email" class="form-control" placeholder="Seu email (requerido)" v-model="dados.email" v-validate.initial="'required|email'">
    </div>
  </div>

  <div class="col-sm-6">
    <div class="form-group">
      <span v-show="errors.has('website')" class="danger">URL inválida</span>
      <input type="text" id="website" name="website" class="form-control" placeholder="Seu website (não esqueça o http://)" v-model="dados.website" v-validate="'url'">
    </div>
  </div>

  <div class="col-sm-6">
    <div class="form-group">
      <input type="text" id="address" class="form-control" placeholder="De onde você é?" v-model="dados.local">
    </div>
  </div>

  <div class="col-sm-12">
    <span v-show="errors.has('assunto:required')" class="danger">Este campo é requerido</span>
    <select id="assunto" name="assunto" class="form-group form-control" v-model="dados.assunto" v-validate.initial="'required'">
      <option value="" selected disabled>Assunto (requerido)</option>
      <option>Desenvolvimento de Software</option>
      <option>Conversa informal</option>
      <option>Outro</option>
    </select>
  </div>

  <div class="col-sm-12">
    <span v-show="errors.has('mensagem:required')" class="danger">Este campo é requerido</span>
    <div class="textarea-message form-group">
      <textarea id="mensagem" name="mensagem" class="textarea-message form-control"
          placeholder="Digite sua mensagem aqui  (requerido)" rows="8" v-model="dados.mensagem" v-validate.initial="'required'"></textarea>
    </div>
  </div>

  <div class="text-center">      
    <button type="submit" class="load-more-button" :disabled="errors.any()" @click.prevent="enviarEmail()">Enviar</button>
  </div>
</form>`
})