(function () {
  'use strict';

  angular.module('teoria').component('teoriaArtigo', {
    templateUrl: ['artigo.html', function (template) { return template; }],
    bindings: {
      artigo: '='
    },
    controllerAs: 'vm',
    controller: controller
  });

  function controller() {
    var self = this;
  }
})();
