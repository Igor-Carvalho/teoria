(function () {
  'use strict';

  angular.module('teoria').directive('fadeOut', fadeOut);

  function fadeOut() {
    return {
      restrict: 'A',
      link: function (scope, element, attrs) {
        element.delay(800).fadeOut('slow');
      }
    }
  }
})();
