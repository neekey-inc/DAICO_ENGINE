const pkg = require('./package')


module.exports = {
  mode: 'universal',

  head: {
    title: '【代行ENGINE】管理サイト',
    meta: [
      { charset: 'utf-8' },
      { name: 'keywords', content: '代行ENGINE' },
      { name: 'description', content: '【代行ENGINE】管理サイト' },
      { name: 'copyright', content: '©Neekey.inc 2019 allright reserved. 無断転載禁止' },
      { name: 'mobile-web-app-capable', content: 'yes' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }
    ]
  },

  loading: { color: '#fff' },

  css: [
    'element-ui/lib/theme-chalk/index.css',
    '@/assets/css/app.css',
  ],

  plugins: [
    '@/plugins/element-ui'
  ],

  modules: [
    '@nuxtjs/axios',
    // '@nuxtjs/google-analytics',
  ],

  build: {
    transpile: [/^element-ui/],
    extend(config, ctx) {
    }
  }
}
