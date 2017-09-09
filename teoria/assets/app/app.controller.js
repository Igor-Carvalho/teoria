(function () {
  'use strict';

  angular.module('teoria').controller('mainCtrl', mainCtrl);

  function mainCtrl() {
    var self = this;
    
    self.$onInit = function () {
      self.abrir = false;
    }
  }
})();
