module.exports = {
    publicPath: process.env.NODE_ENV === 'production' ? '/static/dist/' : 'http://127.0.0.1:8080',
    outputDir: '../mysite/static/dist',
    indexPath: '../../templates/base-vue.html', // relative to outputDir!

    chainWebpack: config => {
        config.devServer
            .public('http://127.0.0.1:8080')
            .hotOnly(true)
            .headers({"Access-Control-Allow-Origin": "*"})
            .writeToDisk(filePath => filePath.endsWith('index.html'));
    }