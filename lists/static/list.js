if (typeof require === 'function') {
  var $ = require('./jquery-3.4.1.min')
}

function initialize() {
  $('input[name="text"]').on('keypress', () => {
    $('.has-error').hide()
  })
}

if (typeof module === 'object' && module.exports) {
  module.exports = initialize
}
