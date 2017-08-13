(function () {
  'use strict';

  angular.module('teoria').component('teoriaEtiquetas', {
    template: '<span class="teoria-etiqueta" ng-repeat="etiqueta in vm.etiquetas">[[ etiqueta.nome ]]</span>',
    bindings: {
      etiquetas: '='
    },
    controllerAs: 'vm',
    controller: function () { var self = this; }
  });
})();
