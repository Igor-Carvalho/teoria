Vue.use(Contatos)
Vue.use(Inscritos)
Vue.use(VeeValidate)
Vue.use(VToaster, {timeout: 2000})

axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'
