(function () {
  'use strict';

  angular.module('teoria').directive('caixaBusca', ['caixaBusca.html', caixaBusca]);

  function caixaBusca(templateUrl) {
    return {
      restrict: 'E',
      templateUrl: templateUrl,
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
