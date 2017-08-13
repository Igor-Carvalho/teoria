(function () {
  'use strict';

  var app = angular.module('teoria');

  app.config([
    '$stateProvider',
    '$urlRouterProvider',
    stateConfig
  ]);

  app.run(['$rootScope', '$state', run]);

  function run($rootScope, $state) {
    $rootScope.$state = $state;
  }

  function stateConfig($stateProvider,
                       $urlRouterProvider) {
  
    $urlRouterProvider.otherwise('/artigos');

    $stateProvider.state('artigos', {
      url: '/artigos',
      template: '<teoria-lista-de-artigos></teoria-lista-de-artigos>'
    });

    $stateProvider.state('artigos.detalhe', {
      url: '/:id',
      template: '<teoria-artigo artigo="vm.artigo"></teoria-artigo>',
      resolve: {
        artigo: ['Artigo', '$stateParams', function (Artigo, $stateParams) {
          return new Artigo({id: $stateParams.id}).$get();
        }]
      },
      controllerAs: 'vm',
      controller: ['artigo', function (artigo) {
        var self = this;
        self.$onInit = function () {
          self.artigo = artigo;
        }
      }]
    });
  }
})();
