(function () {
  'use strict';

  angular.module('teoria').directive('contatoForm', ['contatoForm.html', contatoForm]);

  function contatoForm(contatoFormTemplate) {
    return {
      restrict: 'E',
      templateUrl: contatoFormTemplate,
      scope: {},
      controllerAs: 'vm',
      controller: ['ContatoServiço', 'toastr', controlador]
    }

    function controlador(ContatoServiço, toastr) {
      var self = this;
      self.enviarEmail = enviarEmail;

      self.$onInit = function () {
        self.dados = {};
      }

      function enviarEmail() {
        self.promise = ContatoServiço.enviarEmail(self.dados);
        self.promise.then(sucesso, erro);

        function sucesso() {
          toastr.success('Sua mensagem foi enviada com sucesso. Muito obrigado!');
          self.dados = {};
        }

        function erro(resposta) {
          self.erros = resposta.data;
        }
      }
    }
  }
})();
