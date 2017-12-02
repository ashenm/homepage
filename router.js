/**
 * Express Router
 * Route handler for Homepage
 *
 * Ashen Gunaratne
 * mail@ashenm.ml
 *
 */

const loader = require('./custom-router');
const express = require('express');
const router = express.Router();
const path = require('path');
const fs = require('fs'); 

// custom route handler
const delegate = new loader(path.join(__dirname, '.data', 'routes.txt'));

// parse resume data
const resume = JSON.parse(fs.readFileSync(path.join(__dirname, '.data', 'resume.json'), 'utf8'));

// webroot
router.get('/', (request, response) => response.render('index'));

// resume
router.get('/resume', (request, response) => {
  if (!request.query.dl) {
    response.render('resume', {resume: resume});
  } else {
    response.set('Content-Disposition', 'attachment; filename="resume-ashenm.pdf"');
    response.sendFile(path.join(__dirname, '.cache', 'resume.pdf'));
  }
});

// redirect matching custom routes
router.use((request, response, next) => {
  const target = delegate.route(request.path);
  target ? response.redirect(301, target) : next();
});

// resourse not found
router.use((request, response, next) => response.status(404).render('404'));

module.exports = router;
