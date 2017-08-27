(function () {
  'use strict';

  angular.module('teoria').component('inscriçãoForm', {
    templateUrl: ['inscriçãoForm.html', function (template) { return template; }],
    controllerAs: 'vm',
    controller: ['InscriçãoServiço', controller]
  });

  function controller(InscriçãoServiço) {
    var self = this;
    self.$onInit = function () {
      self.dados = {};
    }

    self.inscrever = inscrever;

    function inscrever() {
      self.mensagem = 'Aguarde um momento...';
      self.promessa = InscriçãoServiço.inscrever(self.dados);
      self.promessa.then(sucesso, erro);

      function sucesso(resposta) {
        if (resposta.data.ativo) {
          self.mensagem = 'Esse email já está cadastrado e ativo em nossa base de dados.';
        } else {
          self.mensagem = 'Um email foi enviado contendo o link de ativação para sua inscrição. Obrigado!';
        }
        self.dados = {};
      }

      function erro(resposta) {
        self.mensagem = 'Infelizmente um erro aconteceu em nosso servidor.';
      }
    }
  }
})();
