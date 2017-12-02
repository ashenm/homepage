/**
 * Homepage
 * Homepage of Ashen Gunaratne
 *
 * Ashen Gunaratne
 * mail@ashenm.ml
 *
 */

const compression = require('compression');
const nunjucks = require('nunjucks');
const express = require('express');
const router = require('./router');
const app = express();

nunjucks.configure('views', {
  autoescape: true,
  trimBlocks: true,
  lstripBlocks: true,
  express: app
});

app.set('view engine', 'njk');

app.use(compression());
app.use(express.static('public'));
app.use(router);

app.listen(process.env.PORT || 8080);
