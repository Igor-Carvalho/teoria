Vue.directive('fadeOut', {
  inserted (el) {
    $(el).delay(800).fadeOut('slow');
  }
});
