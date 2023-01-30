module.exports = {
    publicPath: process.env.NODE_ENV === 'production' ? '/static/dist/' : 'http://127.0.0.1:8080',
    outputDir: '../mysite/static/dist',

    // relative to outputDir!
    indexPath: '../../templates/base-vue.html',

    devServer: {
            host: '127.0.0.1',
            port: '8080',
            headers: {
            'Access-Control-Allow-Origin': '*',
        },

            devMiddleware: {
                      writeToDisk: true,
                    },
    },

    pluginOptions: {
      vuetify: {
   // https://github.com/vuetifyjs/vuetify-loader/tree/next/packages/vuetify-loader
  }
    }
}