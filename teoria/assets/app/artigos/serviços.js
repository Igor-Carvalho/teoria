(function () {
  'use strict';

  angular.module('teoria').factory('Artigo', ['$resource', 'artigosURL', ArtigoResource]);

  function ArtigoResource($resource, artigosURL) {
    var baseURL = artigosURL;

    var Artigo = $resource(baseURL + ':id/', {id: '@id'}, {
      consulta: {
        method: 'GET',
        isArray: false,
        transformResponse: function (resposta) {
          var json_resposta = angular.fromJson(resposta);

          var artigos = [];
          angular.forEach(json_resposta.results, function (artigo) {
            artigos.push(new Artigo(artigo));
          });
          json_resposta.results = artigos;

          return json_resposta;
        }
      }
    });

    return Artigo;
  }
})();
