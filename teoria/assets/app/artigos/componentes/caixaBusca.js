Vue.component('caixaBusca', {
  props: ['abrir'],
  methods: {
    fechar() {
      this.$emit('fechar');
    }
  },
  template: `<div class="header-search open-search" :class="{'open': abrir}">
<div class="container">
  <div class="row">
    <div class="col-sm-8 col-sm-offset-2 col-xs-10 col-xs-offset-1">
      <div class="navbar-search">
        <form class="search-global" action="/artigos/">
          <input type="text" placeholder="Termos de busca"
              autocomplete="off" name="busca" value="" class="search-global-input"/>
          <button class="search-global-btn"><i class="icon-magnifier"></i></button>
          <div class="search-global-note">Digite o que você está procurando</div>
        </form>
      </div>
    </div>
  </div>
</div>
<button type="button" class="search-close close" @click="fechar()"><i class="fa fa-times"></i></button>
</div>`
});
