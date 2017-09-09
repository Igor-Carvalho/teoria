(function () {
  'use strict';

  angular.module('teoria').directive('caixaBusca', ['caixaBusca.html', caixaBusca]);

  function caixaBusca(template) {
    return {
      restrict: 'E',
      templateUrl: template,
      scope: {},
      bindToController: {
        abrir: '='
      },
      controllerAs: 'vm',
      controller: controller
    }

    function controller() {
      var self = this;
    }
  }
})();
