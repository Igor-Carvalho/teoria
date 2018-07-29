Vue.directive('fadeOut', {
  inserted: function (el) {
    $(el).delay(800).fadeOut('slow');
  }
});
