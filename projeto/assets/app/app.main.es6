new Vue({
  el: '#app',
  data() {
    return {
      abrir: false
    }
  },
  methods: {
    fechar() {
      this.abrir = false;
    }
  }
});
