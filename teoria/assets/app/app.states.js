(function () {
  'use strict';

  var app = angular.module('teoria');

  app.config([
    '$stateProvider',
    '$urlRouterProvider',
    stateConfig
  ]);

  app.run(['$rootScope', run]);

  function run($rootScope) {
  }

  function stateConfig($stateProvider,
                       $urlRouterProvider) {
  
    $urlRouterProvider.otherwise('/artigos');

    $stateProvider.state('artigos', {
      url: '/artigos',
      template: '<teoria-lista-de-artigos></teoria-lista-de-artigos>'
    });
  }
})();
