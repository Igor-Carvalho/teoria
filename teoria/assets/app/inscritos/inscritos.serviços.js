(function () {
  'use strict';

  angular.module('teoria').factory('InscriçãoServiço', ['$http', 'inscriçãoURL', InscriçãoServiço]);

  function InscriçãoServiço($http, inscriçãoURL) {
    return {
      inscrever: function (dados) {
        return $http.post(inscriçãoURL, dados);
      }
    }
  }
})();
