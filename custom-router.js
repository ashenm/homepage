/**
 * Custom Router
 * Custom Route Handler
 *
 * Ashen Gunaratne
 * mail@ashenm.ml
 *
 */

const fs = require('fs');

class Router {

  constructor(file) {

    Object.defineProperties(this, {
      file: {
        value: file
      },
      routes: {
        writable: true,
        value: Router.forge(file)
      }
    });

    // watch for changes on file
    // and update routes accordingly
    this.watch();

  }

  /**
   * Returns the matching URL for
   * parameterised path else undefined
   */
  route(path) {
    return this.routes[path.toLowerCase()];
  }

  /**
   * Repopulate routes on file content change
   */
  watch() {
    fs.watch(this.file, (event, file) => {
      if (event === 'change')
        this.routes = Router.forge(this.file);
    })
  }

  /**
   * Returns a hash-map of routes
   * constructed from the parametrised file
   */
  static forge(file) {
    return fs.readFileSync(file, 'utf8').split(/\r\n|\r|\n/)
      .reduce((accumulator, route, index, routes) => {

        const sanitised = route.trim();
        const [path, location] = sanitised.split(' ');

        // ignore whitespace
        if (!sanitised)
          return accumulator;

        // ignore comments
        if (sanitised.startsWith('#'))
          return accumulator;

        accumulator[path] = location;
        return accumulator;

      }, {});
  }

}

module.exports = Router;
