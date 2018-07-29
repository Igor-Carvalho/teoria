Vue.use(Contatos)
Vue.use(Inscritos)
Vue.use(VeeValidate)
Vue.use(VToaster, {timeout: 2000})

axios.defaults.headers.common['xsrfCookieName'] = 'csrftoken'
axios.defaults.headers.common['xsrfHeaderName'] = 'X-CSRFToken'
