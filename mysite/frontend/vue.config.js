const BundleTracker = require('webpack-bundle-tracker')
const DEPLOYMENT_PATH = '/static/dist/'

module.exports = {
    publicPath: process.env.NODE_ENV === 'production' ? DEPLOYMENT_PATH : 'http://localhost:8000/',
    outputDir: '../static/dist',

    devServer: {
        host: 'localhost',
        port: '8000',
        headers: {
            'Access-Control-Allow-Origin': '*',
        },
    },

    configureWebpack: {
        plugins: [
            new BundleTracker({ path: __dirname, filename: 'webpack-stats.json' }),
        ],
    },

    pluginOptions: {
      vuetify: {
			// https://github.com/vuetifyjs/vuetify-loader/tree/next/packages/vuetify-loader
		}
    }
}
