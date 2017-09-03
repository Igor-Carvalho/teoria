(function () {
  'use strict';

  angular.module('teoria').factory('ContatoServiço', ['$http', 'emailDeContatoURL', ContatoServiço]);

  function ContatoServiço($http, emailDeContatoURL) {
    return {
      enviarEmail: enviarEmail
    }

    function enviarEmail(dados) {
      return $http.post(emailDeContatoURL, dados);
    }
  }
})();
