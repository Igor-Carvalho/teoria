(function () {
  'use strict';

  angular.module('teoria').directive('teoriaArtigo', ['artigo.html', teoriaArtigo]);

  function teoriaArtigo(template) {
    return {
      retrict: 'E',
      replace: true,
      scope: {},
      templateUrl: template,
      bindToController: {
        artigo: '='
      },
      controllerAs: 'vm',
      controller: controlador
    }

    function controlador() {
      var self = this;
    }
  }
})();
