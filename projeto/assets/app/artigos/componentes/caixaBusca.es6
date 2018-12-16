Vue.component('caixaBusca', resolve => {
  axios.get('/public/app/artigos/componentes/caixaBusca.html').then(response => {
    resolve({
      template: response.data,
      props: ['abrir'],
      methods: {
        fechar () {
          this.$emit('fechar');
        }
      },
      watch: {
        abrir () {
          if (this.abrir) {
            setTimeout(() => this.$refs.inputBusca.focus(), 500)
          }
        }
      }
    })
  })
});
