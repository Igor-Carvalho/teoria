(function () {
  'use strict';

  angular.module('teoria').factory('Artigo', ['$resource', '$sce', 'artigosURL', ArtigoResource]);

  function ArtigoResource($resource, $sce, artigosURL) {
    var Artigo = $resource(artigosURL + ':id/', {id: '@id'}, {
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
      },
      get: {
        method: 'GET',
        isArray: false,
        transformResponse: function (resposta) {
          var artigo = angular.fromJson(resposta);
          artigo['conteúdo'] = $sce.trustAsHtml(artigo['conteúdo']);
          return artigo;
        }
      }
    });

    return Artigo;
  }
})();
