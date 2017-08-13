(function () {
  'use strict';

  angular.module('teoria').component('teoriaListaDeArtigos', {
    templateUrl: ['listaDeArtigos.html', function(template) { return template; }],
    controllerAs: 'vm',
    controller: controller
  });

  function controller() {
    var self = this;
    self.$onInit = function () {
      self.artigos = [
        {
          "título": "Migrate to Hugo from Jekyll",
          "autor": "Igor Oak",
          "created": "2017-04-04",
          "conteúdo": "Move static content to static Jekyll has a rule that any directory not starting with _ will be copied as-is to the _site output. Hugo keeps all static content under static. You should therefore move it all there. With Jekyll, something that looked like you’ll want any files that should reside at the root (such as CNAME) to be moved to static."
        },
        {
          "título": "Migrate to Hugo from Jekyll",
          "autor": "Igor Oak",
          "created": "2017-04-04",
          "conteúdo": "Move static content to static Jekyll has a rule that any directory not starting with _ will be copied as-is to the _site output. Hugo keeps all static content under static. You should therefore move it all there. With Jekyll, something that looked like you’ll want any files that should reside at the root (such as CNAME) to be moved to static."
        },
        {
          "título": "Migrate to Hugo from Jekyll",
          "autor": "Igor Oak",
          "created": "2017-04-04",
          "conteúdo": "Move static content to static Jekyll has a rule that any directory not starting with _ will be copied as-is to the _site output. Hugo keeps all static content under static. You should therefore move it all there. With Jekyll, something that looked like you’ll want any files that should reside at the root (such as CNAME) to be moved to static."
        },
        {
          "título": "Migrate to Hugo from Jekyll",
          "autor": "Igor Oak",
          "created": "2017-04-04",
          "conteúdo": "Move static content to static Jekyll has a rule that any directory not starting with _ will be copied as-is to the _site output. Hugo keeps all static content under static. You should therefore move it all there. With Jekyll, something that looked like you’ll want any files that should reside at the root (such as CNAME) to be moved to static."
        }
      ]
    }
  }
})();
