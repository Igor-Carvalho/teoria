(function () {
  'use strict';

  var app = angular.module('teoria');

  app.config([
    '$stateProvider',
    '$urlRouterProvider',
    stateConfig
  ]);

  function stateConfig($stateProvider,
                       $urlRouterProvider) {
  
    $urlRouterProvider.otherwise('/home');

    $stateProvider.state('home', {
      url: '/home',
      template: '<h4>Home here</h4>'
    });
  }
})();
