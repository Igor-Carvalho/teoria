Vue.use(VueResource);
Vue.use(VeeValidate);
Vue.use(VToaster, {timeout: 2000});

Vue.http.headers.common['xsrfCookieName'] = 'csrftoken';
Vue.http.headers.common['xsrfHeaderName'] = 'X-CSRFToken';
