(function () {
  'use strict';

  angular.module('teoria').directive('teoriaListaDeArtigos', ['listaDeArtigos.html', teoriaListaDeArtigos]);

  function teoriaListaDeArtigos(template) {
    return {
      restrict: 'E',
      replace: true,
      scope: {},
      templateUrl: template,
      controllerAs: 'vm',
      controller: ['Artigo', controlador]
    }

    function controlador(Artigo) {
      var self = this;
      self.carregarArtigos = carregarArtigos;

      self.$onInit = function () {
        carregarArtigos({});
      }

      function carregarArtigos(parâmetros) {
        Artigo.consulta(parâmetros, sucesso);

        function sucesso(artigos) {
          self.artigos = artigos;
        }
      }
    }
  }

})();
